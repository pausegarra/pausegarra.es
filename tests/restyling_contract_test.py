import hashlib
import json
import re
import subprocess
import sys
import unittest
from collections import Counter
from copy import deepcopy
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

from project_images_contract_test import assert_preserved_files, NEW_PAGE_PATHS

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
FIXTURE = ROOT / 'tests/fixtures/restyling-before.json'
SLUGS = ('monitoring', 'sendif', 'number-detection', 'translator',
         'survey-monkey-webhook-manager', 'volchik-cheburashka',
         'russian-cheatsheet', 'pullyt', 'ai-factory')
HOME_PATHS = ('en/index.html', 'es/index.html')
# The immutable pre-restyling fixture was captured in 2026. Only one token
# per home belongs to the dynamic copyright; other dates remain protected.
BASELINE_COPYRIGHT_YEAR = '2026'

class Element:
    def __init__(self, tag='', attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def all(self, tag=None):
        result = [self] if tag is None or self.tag == tag else []
        for child in self.children:
            if isinstance(child, Element):
                result.extend(child.all(tag))
        return result

    def text(self, raw=False):
        if not raw and self.tag in ('script', 'style', 'svg', 'noscript'):
            return ''
        return ' '.join(child.text(raw) if isinstance(child, Element) else child
                        for child in self.children)

class Document(HTMLParser):
    VOID = set('area base br col embed hr img input link meta param source track wbr'.split())

    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.root = Element()
        self.stack = [self.root]
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        node = Element(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_data(self, data):
        self.stack[-1].children.append(data)

def normal(text):
    return ' '.join(text.split())

def copyright_year(doc):
    years = [match.group(1) for footer in doc.all('footer')
             for paragraph in footer.all('p')
             if (match := re.match(r'^© (\d{4}) Pau Segarra\.', normal(paragraph.text())))]
    if len(years) != 1:
        raise AssertionError('se esperaba un año de copyright en el footer')
    return years[0]

def documents():
    return {p.relative_to(DIST).as_posix(): Document(p.read_text()).root
            for p in sorted(DIST.rglob('*.html'))}

def protected():
    paths = []
    for folder in ('src/lib', 'src/pages', 'src/content', 'public'):
        paths.extend(p for p in (ROOT / folder).rglob('*') if p.is_file())
    paths.extend(ROOT / name for name in (
        'src/content.config.ts', 'src/compoents/organisms/HomePage.astro',
        'src/compoents/molecules/LocaleRedirect.astro', 'astro.config.mjs',
        'tailwind.config.mjs', 'tsconfig.json', 'skills-lock.json', 'AGENTS.md'))
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}

def semantic(doc):
    body = doc.all('body')[0]
    # Astro's automatic root redirect omits optional html/head tags.
    head = next(iter(doc.all('head')), doc)
    meta = [n.attrs for n in head.all('meta') if n.attrs.get('name') != 'theme-color']
    links = [n.attrs for n in head.all('link') if n.attrs.get('rel') in
             ('canonical', 'alternate', 'icon', 'sitemap')]
    structured = [json.loads(n.text(raw=True)) for n in doc.all('script')
                  if n.attrs.get('type') == 'application/ld+json']
    return {
        'words': dict(Counter(re.findall(r'\w+|[^\w\s]', body.text()))),
        'hrefs': sorted(n.attrs['href'] for n in body.all('a') if 'href' in n.attrs),
        'images': sorted((n.attrs.get('src'), n.attrs.get('alt')) for n in body.all('img')),
        'title': normal(head.all('title')[0].text()),
        'lang': next(iter(doc.all('html')), doc).attrs.get('lang'),
        'meta': sorted(meta, key=lambda a: json.dumps(a, sort_keys=True)),
        'links': sorted(links, key=lambda a: json.dumps(a, sort_keys=True)),
        'structured': structured,
    }

def card_words(locale, slug):
    front = (ROOT / f'src/content/projects/{locale}/{slug}.md').read_text().split('---', 2)[1]
    values = []
    for field_name in ('title', 'shortDescription'):
        match = re.search(rf'^{field_name}: (.+)$', front, re.M)
        if not match:
            raise AssertionError(f'falta {field_name} en {locale}/{slug}')
        raw = match.group(1)
        values.append(json.loads(raw) if raw.startswith('"') else raw)
    for field_name in ('features', 'tech'):
        match = re.search(rf'^{field_name}:\n((?:  - [^\n]+\n?)+)', front, re.M)
        if not match:
            raise AssertionError(f'falta {field_name} en {locale}/{slug}')
        values.extend(line[4:] for line in match.group(1).splitlines())
    return Counter(re.findall(r'\w+|[^\w\s]', ' '.join(values)))

class Contract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = json.loads(FIXTURE.read_text())
        cls.docs = documents()
        if not cls.docs:
            raise AssertionError('dist vacío: ejecutar yarn build antes de los tests')

    def test_preservation(self):
        assert_preserved_files(protected(), self.baseline['protected'], allow_ai_factory=True)
        self.assertEqual(set(self.docs), set(self.baseline['pages']) | NEW_PAGE_PATHS)
        for path in self.baseline['pages']:
            doc = self.docs[path]
            with self.subTest(path=path):
                old, new = self.baseline['pages'][path], semantic(doc)
                old_words, new_words = Counter(old['words']), Counter(new['words'])
                old_hrefs = Counter(old['hrefs'])
                if path in HOME_PATHS:
                    self.assertGreater(old_words[BASELINE_COPYRIGHT_YEAR], 0)
                    old_words.subtract([BASELINE_COPYRIGHT_YEAR])
                    new_words.subtract([copyright_year(doc)])
                    locale = path.split('/')[0]
                    old_words.subtract(card_words(locale, 'pullyt'))
                    old_words.update(card_words(locale, 'ai-factory'))
                    old_hrefs.subtract([f'/{locale}/projects/pullyt/'])
                    old_hrefs.update([f'/{locale}/projects/ai-factory/'])
                self.assertFalse(old_words - new_words, 'contenido perdido')
                self.assertFalse(old_hrefs - Counter(new['hrefs']), 'enlace perdido')
                for key in ('title', 'lang', 'meta', 'links', 'structured'):
                    self.assertEqual(old[key], new[key], key)
                self.assertEqual([tuple(image) for image in old['images']], new['images'])

    def test_copyright_year(self):
        expected_year = str(datetime.now().year)
        for path in HOME_PATHS:
            with self.subTest(path=path):
                self.assertEqual(copyright_year(self.docs[path]), expected_year)

    def test_routes_and_accessibility(self):
        expected = {'index.html', 'projects/index.html'}
        expected.update(f'projects/{slug}/index.html' for slug in SLUGS)
        for locale in ('en', 'es'):
            expected.update((f'{locale}/index.html', f'{locale}/projects/index.html'))
            expected.update(f'{locale}/projects/{slug}/index.html' for slug in SLUGS)
        self.assertEqual(expected, set(self.docs))
        for path, doc in self.docs.items():
            with self.subTest(path=path):
                for image in doc.all('img'):
                    self.assertTrue(image.attrs.get('alt'))
                for anchor in doc.all('a'):
                    if anchor.attrs.get('target') == '_blank':
                        self.assertTrue({'noopener', 'noreferrer'} <= set(anchor.attrs.get('rel', '').split()))
                if path.startswith(('en/', 'es/')):
                    self.assertEqual(len(doc.all('h1')), 1)
                    self.assertEqual(len(doc.all('main')), 1)
                    self.assertEqual(doc.all('main')[0].attrs.get('id'), 'main-content')
                    self.assertTrue(any(a.attrs.get('href') == '#main-content' for a in doc.all('a')))
                for anchor in doc.all('a'):
                    href = anchor.attrs.get('href', '')
                    target = urlsplit(href)
                    if target.scheme or target.netloc:
                        continue
                    destination = (DIST / unquote(target.path).lstrip('/') if target.path.startswith('/')
                                   else DIST / path).resolve()
                    if target.path and not target.path.startswith('/'):
                        destination = ((DIST / path).parent / unquote(target.path)).resolve()
                    if destination.is_dir():
                        destination = destination / 'index.html'
                    elif not destination.is_file() and not destination.suffix:
                        destination = destination / 'index.html'
                    self.assertTrue(destination.is_file(), (path, href))
                    if target.fragment:
                        destination_doc = self.docs.get(destination.relative_to(DIST).as_posix())
                        if destination_doc:
                            self.assertIn(unquote(target.fragment),
                                          [n.attrs.get('id') for n in destination_doc.all()])

    def test_navigation(self):
        labels = {'en': ('Home', 'Projects', 'Contact'), 'es': ('Inicio', 'Proyectos', 'Contacto')}
        for path, doc in self.docs.items():
            if not path.startswith(('en/', 'es/')):
                continue
            with self.subTest(path=path):
                locale = path.split('/')[0]
                headers = doc.all('header')
                self.assertEqual(len(headers), 1, 'falta header compartido')
                navs = headers[0].all('nav')
                self.assertTrue(navs, 'falta navegación semántica')
                anchors = navs[0].all('a')
                destinations = (f'/{locale}/', f'/{locale}/projects/', f'/{locale}/#contact')
                for href, label in zip(destinations, labels[locale]):
                    matches = [a for a in anchors if a.attrs.get('href', '').rstrip('/') == href.rstrip('/')]
                    self.assertEqual(len(matches), 1, href)
                    self.assertEqual(normal(matches[0].text()), label)
                current = [a for a in anchors if a.attrs.get('aria-current') == 'page']
                self.assertEqual(len(current), 1)
                self.assertEqual(normal(current[0].text()), labels[locale][int('/projects/' in path)])
                options = [a for a in headers[0].all('a') if 'data-locale' in a.attrs]
                self.assertEqual({a.attrs['data-locale'] for a in options}, {'en', 'es'})
                route = path.split('/', 1)[1].removesuffix('index.html')
                for option in options:
                    self.assertEqual(option.attrs['href'].rstrip('/'),
                                     f"/{option.attrs['data-locale']}/{route}".rstrip('/'))

    def test_detail_structure(self):
        for locale in ('en', 'es'):
            for slug in SLUGS:
                path = f'{locale}/projects/{slug}/index.html'
                with self.subTest(path=path):
                    main = self.docs[path].all('main')[0]
                    breadcrumbs = [nav for nav in main.all('nav') if nav.all('ol')]
                    self.assertEqual(len(breadcrumbs), 1, 'falta breadcrumb navegable')
                    hrefs = {a.attrs.get('href', '').rstrip('/') for a in breadcrumbs[0].all('a')}
                    self.assertTrue({f'/{locale}', f'/{locale}/projects'} <= hrefs)
                    headings = {normal(h.text()) for h in main.all('h2')}
                    self.assertTrue(({'Technologies', 'Features'} if locale == 'en'
                                     else {'Tecnologías', 'Funciones'}) <= headings)

    def test_transition_contract(self):
        layout = (ROOT / 'src/layouts/Layout.astro').read_text()
        self.assertIn("import { ClientRouter } from 'astro:transitions'", layout)
        self.assertIn('<ClientRouter />', layout)
        sources = {
            'src/compoents/atoms/Title.astro': ['transition:name={transitionName}'],
            'src/compoents/molecules/Project.astro': [
                'project-title-${transitionKey}', 'project-description-${transitionKey}'],
            'src/compoents/organisms/ProjectDetailPage.astro': [
                'project-title-${locale}-${projectSlug}', 'project-description-${locale}-${projectSlug}'],
            'src/compoents/organisms/projects.astro': [
                'projects-title', 'projects-divider', '${locale}-${getProjectSlug(project.slug)}'],
            'src/compoents/organisms/ProjectsIndexPage.astro': [
                'projects-title', 'projects-divider', '${locale}-${getProjectSlug(project.slug)}'],
        }
        for path, markers in sources.items():
            text = (ROOT / path).read_text()
            for marker in markers:
                self.assertIn(marker, text, (path, marker))

class CopyrightRegression(unittest.TestCase):
    def case_for_year(self, year):
        case = Contract('test_preservation')
        case.baseline = json.loads(FIXTURE.read_text())
        case.docs = deepcopy(documents())
        # Simulate a build in another year, changing only the real footer.
        for path in HOME_PATHS:
            footer = case.docs[path].all('footer')[0]
            replacements = 0
            for paragraph in footer.all('p'):
                for index, child in enumerate(paragraph.children):
                    if isinstance(child, str):
                        paragraph.children[index], count = re.subn(
                            r'(©\s+)\d{4}', rf'\g<1>{year}', child)
                        replacements += count
            self.assertEqual(replacements, 1)
        return case

    def test_next_year_build_preserves_content(self):
        case = self.case_for_year(2027)
        case.test_preservation()
        with patch(__name__ + '.datetime') as clock:
            clock.now.return_value.year = 2027
            case.test_copyright_year()

    def test_year_outside_copyright_is_still_protected(self):
        case = self.case_for_year(2027)
        case.baseline['pages']['en/index.html']['words']['2026'] += 1
        paragraph = Element('p')
        paragraph.children = ['2026']
        body = case.docs['en/index.html'].all('body')[0]
        body.children.append(paragraph)
        case.test_preservation()
        body.children.remove(paragraph)
        with self.assertRaisesRegex(AssertionError, 'contenido perdido'):
            case.test_preservation()

    def test_stale_copyright_year_is_rejected(self):
        case = self.case_for_year(2026)
        with patch(__name__ + '.datetime') as clock:
            clock.now.return_value.year = 2027
            with self.assertRaises(AssertionError):
                case.test_copyright_year()

    def test_missing_copyright_year_is_rejected(self):
        case = self.case_for_year(2027)
        footer = case.docs['en/index.html'].all('footer')[0]
        for paragraph in footer.all('p'):
            paragraph.children = [child.replace('2027', '') if isinstance(child, str) else child
                                  for child in paragraph.children]
        with self.assertRaisesRegex(AssertionError, 'copyright'):
            case.test_copyright_year()

if __name__ == '__main__':
    if sys.argv[1:] == ['--capture']:
        subprocess.run(['git', 'diff', '--exit-code', '--', 'src', 'public',
                        'astro.config.mjs', 'tailwind.config.mjs', 'tsconfig.json'], cwd=ROOT, check=True)
        pages = documents()
        if len(pages) != 30:
            raise SystemExit(f'baseline esperaba 30 HTML; encontró {len(pages)}')
        FIXTURE.parent.mkdir(parents=True, exist_ok=True)
        payload = {'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
                   'protected': protected(), 'pages': {p: semantic(d) for p, d in pages.items()}}
        with FIXTURE.open('x') as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
    else:
        unittest.main()
