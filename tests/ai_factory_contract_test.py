import hashlib
import json
import re
import unittest
from pathlib import Path
from restyling_contract_test import Document, normal

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
REPO = 'https://github.com/pausegarra/ai-factory'
LEGACY = {'monitoring', 'sendif', 'number-detection', 'translator',
          'survey-monkey-webhook-manager', 'volchik-cheburashka',
          'russian-cheatsheet', 'pullyt'}
FEATURED = {'ai-factory', 'number-detection', 'russian-cheatsheet',
            'volchik-cheburashka'}
COPY = {
    'en': {
        'description': 'Local GitHub automation through visual workflows and CLI agents, built with Tauri 2, Rust and React.',
        'alt': 'Conceptual illustration of local GitHub automation with connected workflows and AI agents',
        'features': ['Local CLI agent execution', 'Visual workflow editing',
                     'Four GitHub triggers', 'GitHub tokens per account',
                     'Run history and persistent artifacts'],
        'language': 'English interface',
    },
    'es': {
        'description': 'Automatización local de GitHub mediante flujos visuales y agentes CLI, construida con Tauri 2, Rust y React.',
        'alt': 'Ilustración conceptual de automatización local de GitHub con flujos conectados y agentes de IA',
        'features': ['Ejecución local de agentes CLI', 'Edición visual de flujos',
                     'Cuatro disparadores de GitHub', 'Tokens de GitHub por cuenta',
                     'Historial y artefactos persistentes'],
        'language': 'interfaz en inglés',
    },
}
TECH = ['Tauri 2', 'Rust', 'React', 'React Flow', 'Tailwind CSS']


def parts(locale, slug):
    path = ROOT / f'src/content/projects/{locale}/{slug}.md'
    if not path.is_file():
        raise AssertionError(f'falta entrada localizada: {path}')
    return path.read_text().split('---', 2)[1:]


def field(front, name):
    match = re.search(rf'^{name}: (.+)$', front, re.M)
    if not match:
        raise AssertionError(f'falta {name}')
    raw = match.group(1)
    return json.loads(raw) if raw.startswith('"') else raw


def items(front, name):
    match = re.search(rf'^{name}:\n((?:  - [^\n]+\n?)+)', front, re.M)
    if not match:
        raise AssertionError(f'falta lista {name}')
    return [line[4:] for line in match.group(1).splitlines()]


def document(relative):
    path = DIST / relative
    if not path.is_file():
        raise AssertionError(f'falta {path}; ejecutar yarn build')
    return Document(path.read_text()).root


def card_slugs(doc, locale):
    # Project cards include a feature heading; contact cards also have an h3.
    anchors = [a for a in doc.all('a') if a.all('h3') and a.all('h4')]
    prefix = f'/{locale}/projects/'
    hrefs = [a.attrs.get('href', '') for a in anchors]
    if not all(href.startswith(prefix) for href in hrefs):
        raise AssertionError('tarjeta sin enlace a detalle de su locale')
    slugs = [href.removeprefix(prefix).strip('/') for href in hrefs]
    if len(slugs) != len(set(slugs)):
        raise AssertionError('tarjeta duplicada')
    return set(slugs)


class Sources(unittest.TestCase):
    def test_localized_entry_contract(self):
        bodies = []
        for locale, copy in COPY.items():
            with self.subTest(locale=locale):
                front, body = parts(locale, 'ai-factory')
                self.assertEqual(field(front, 'title'), 'AI Factory')
                self.assertEqual(field(front, 'shortDescription'), copy['description'])
                self.assertEqual(field(front, 'link'), REPO)
                self.assertEqual(field(front, 'featured'), 'true')
                self.assertEqual(items(front, 'tech'), TECH)
                self.assertEqual(items(front, 'features'), copy['features'])
                self.assertRegex(front, r'(?m)^  - title: GitHub$')
                self.assertIn(f'    url: {REPO}\n', front)
                self.assertRegex(front, r'(?m)^    className: ".+"$')
                self.assertEqual(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', body),
                                 [(copy['alt'], '/ai-factory.png')])
                self.assertIn(copy['language'], body)
                for term in ('GitHub', 'REST', 'tokens', 'Codex', 'OpenCode'):
                    self.assertIn(term, body)
                self.assertNotIn('```', body, 'el portfolio no es una guía de instalación')
                bodies.append(body)
        self.assertEqual(len(bodies), 2, "se requieren ambos cuerpos localizados")
        self.assertNotEqual(*bodies)

    def test_featured_swap_preserves_pullyt_and_other_sources(self):
        baseline = json.loads((ROOT / 'tests/fixtures/restyling-before.json').read_text())
        for locale in COPY:
            folder = ROOT / 'src/content/projects' / locale
            self.assertEqual({p.stem for p in folder.glob('*.md')}, LEGACY | {'ai-factory'})
            featured = {p.stem for p in folder.glob('*.md')
                        if re.search(r'^featured: true$', p.read_text(), re.M)}
            self.assertEqual(featured, FEATURED)
            relative = f'src/content/projects/{locale}/pullyt.md'
            current = (ROOT / relative).read_bytes()
            self.assertEqual(current.count(b'featured: false\n'), 1)
            restored = current.replace(b'featured: false\n', b'featured: true\n', 1)
            self.assertEqual(hashlib.sha256(restored).hexdigest(), baseline['protected'][relative])


class Built(unittest.TestCase):
    def test_home_replaces_pullyt_and_catalogue_keeps_both(self):
        for locale in COPY:
            with self.subTest(locale=locale):
                self.assertEqual(card_slugs(document(f'{locale}/index.html'), locale), FEATURED)
                self.assertEqual(card_slugs(document(f'{locale}/projects/index.html'), locale),
                                 LEGACY | {'ai-factory'})
                self.assertTrue((DIST / locale / 'projects/pullyt/index.html').is_file())

    def test_localized_details_image_link_and_metadata(self):
        for locale, copy in COPY.items():
            with self.subTest(locale=locale):
                doc = document(f'{locale}/projects/ai-factory/index.html')
                self.assertEqual(doc.all('html')[0].attrs.get('lang'), locale)
                self.assertEqual(normal(doc.all('h1')[0].text()), 'AI Factory')
                self.assertEqual(len(doc.all('main')), 1)
                self.assertEqual(normal(doc.all('title')[0].text()), 'AI Factory | Pau Segarra')
                descriptions = [n.attrs.get('content') for n in doc.all('meta')
                                if n.attrs.get('name') == 'description']
                self.assertEqual(descriptions, [copy['description']])
                canonical = [n.attrs['href'].rstrip('/') for n in doc.all('link')
                             if n.attrs.get('rel') == 'canonical']
                self.assertEqual(canonical, [f'https://pausegarra.com/{locale}/projects/ai-factory'])
                language_links = [a for a in doc.all('a') if 'data-locale' in a.attrs]
                self.assertEqual({a.attrs['data-locale'] for a in language_links}, set(COPY))
                for anchor in language_links:
                    self.assertEqual(anchor.attrs['href'].rstrip('/'),
                                     f"/{anchor.attrs['data-locale']}/projects/ai-factory")
                github = [a for a in doc.all('a') if a.attrs.get('href') == REPO]
                self.assertTrue(github)
                self.assertTrue(any('GitHub' in a.text() for a in github))
                for anchor in github:
                    self.assertEqual(anchor.attrs.get('target'), '_blank')
                    self.assertTrue({'noopener', 'noreferrer'} <= set(anchor.attrs.get('rel', '').split()))
                images = doc.all('img')
                self.assertEqual(len(images), 1)
                self.assertEqual(images[0].attrs.get('src'), '/ai-factory.png')
                self.assertEqual(images[0].attrs.get('alt'), copy['alt'])
                self.assertEqual((DIST / 'ai-factory.png').read_bytes(),
                                 (ROOT / 'public/ai-factory.png').read_bytes())

    def test_unprefixed_redirect_offers_both_locales(self):
        doc = document('projects/ai-factory/index.html')
        hrefs = {a.attrs.get('href', '').rstrip('/') for a in doc.all('a')}
        self.assertTrue({'/en/projects/ai-factory', '/es/projects/ai-factory'} <= hrefs)
        self.assertTrue(any(n.attrs.get('name') == 'robots' and
                            n.attrs.get('content') == 'noindex, follow'
                            for n in doc.all('meta')))


if __name__ == '__main__':
    unittest.main()
