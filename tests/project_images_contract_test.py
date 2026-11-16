import hashlib
import json
import re
import subprocess
import unittest
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
BASELINE = ROOT / 'tests/fixtures/restyling-before.json'
PROJECTS = {
    'monitoring': ('monitoring.png', 'Monitoring'),
    'number-detection': ('number-detection.png', 'Number Detection'),
    'pullyt': ('pullyt.png', 'Pullyt'),
    'russian-cheatsheet': ('russian-cheatsheet.png', 'Russian Cheatsheet'),
    'sendif': ('sendif.png', 'SendIf'),
    'survey-monkey-webhook-manager': ('smwm.png', 'Survey Monkey Webhook Manager'),
    'translator': ('translate.png', 'Translator'),
    'volchik-cheburashka': ('volchik-cheburashka.png', 'Volchik & Cheburashka'),
}
REPLACED_IMAGE_PATHS = frozenset('public/' + item[0] for item in PROJECTS.values())
# These PNGs are served directly, including on mobile; cap each download.
MAX_IMAGE_BYTES = 128 * 1024


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_preserved_files(current, baseline):
    if set(current) != set(baseline):
        raise AssertionError('cambio del inventario de archivos protegidos')
    if not REPLACED_IMAGE_PATHS <= set(baseline):
        raise AssertionError('faltan imágenes originales en la baseline')
    for path, original_hash in baseline.items():
        if path in REPLACED_IMAGE_PATHS:
            if current[path] == original_hash:
                raise AssertionError(f'{path}: imagen original sin reemplazar')
        elif current[path] != original_hash:
            raise AssertionError(f'{path}: cambio fuera de las imágenes autorizadas')


class Images(HTMLParser):
    VOID = set('area base br col embed hr img input link meta param source track wbr'.split())

    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.images = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            in_prose = any('project-prose' in (a.get('class') or '').split()
                           for _, a in self.stack)
            self.images.append((attrs, in_prose))
        if tag not in self.VOID:
            self.stack.append((tag, attrs))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)


class SourceImages(unittest.TestCase):
    def test_each_served_image_stays_within_transfer_budget(self):
        for relative in sorted(REPLACED_IMAGE_PATHS):
            with self.subTest(path=relative):
                self.assertLessEqual((ROOT / relative).stat().st_size,
                                     MAX_IMAGE_BYTES,
                                     f'{relative}: excede 128 KiB por descarga')

    def test_all_eight_are_new_and_unique(self):
        original = json.loads(BASELINE.read_text())['protected']
        hashes = []
        for relative in sorted(REPLACED_IMAGE_PATHS):
            with self.subTest(path=relative):
                path = ROOT / relative
                self.assertTrue(path.is_file(), relative)
                self.assertFalse(path.is_symlink(), relative)
                current = digest(path)
                self.assertNotEqual(current, original[relative],
                                    f'{relative}: imagen original sin reemplazar')
                hashes.append(current)
        self.assertEqual(len(set(hashes)), 8, 'imágenes repetidas entre proyectos')

    def test_pngs_decode_with_nonzero_dimensions_and_unique_pixels(self):
        # sharp ya está en el lock de Astro. No instala ni modifica archivos.
        script = r'''
import sharp from 'sharp';
import { createHash } from 'node:crypto';
const output = [];
for (const file of process.argv.slice(1)) {
  const metadata = await sharp(file, { failOn: 'warning' }).metadata();
  const { data, info } = await sharp(file, { failOn: 'warning' })
    .ensureAlpha().raw().toBuffer({ resolveWithObject: true });
  output.push({ file, format: metadata.format, width: info.width,
    height: info.height, bytes: data.length,
    opaque: data.every((value, index) => index % 4 !== 3 || value === 255),
    pixels: createHash('sha256').update(data).digest('hex') });
}
process.stdout.write(JSON.stringify(output));
'''
        result = subprocess.run(
            ['node', '--input-type=module', '-e', script,
             *sorted(REPLACED_IMAGE_PATHS)],
            cwd=ROOT, text=True, capture_output=True, check=True)
        decoded = json.loads(result.stdout)
        self.assertEqual(len(decoded), 8)
        for item in decoded:
            with self.subTest(path=item['file']):
                self.assertEqual((ROOT / item['file']).read_bytes()[:8], b'\x89PNG\r\n\x1a\n')
                self.assertEqual(item['format'], 'png')
                self.assertGreaterEqual(item['width'], 960)
                self.assertGreaterEqual(item['height'], 640)
                self.assertEqual(item['width'] * 2, item['height'] * 3,
                                 'proporción 3:2 preservada')
                self.assertEqual(item['bytes'], item['width'] * item['height'] * 4)
                self.assertTrue(item['opaque'])
        self.assertEqual(len({item['pixels'] for item in decoded}), 8,
                         'mismos píxeles reutilizados con otra codificación')

    def test_sixteen_markdown_references_keep_paths_and_alt(self):
        for locale in ('en', 'es'):
            folder = ROOT / 'src/content/projects' / locale
            self.assertEqual({p.stem for p in folder.glob('*.md')}, set(PROJECTS))
            for slug, (filename, alt) in PROJECTS.items():
                with self.subTest(locale=locale, slug=slug):
                    references = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)',
                                            (folder / f'{slug}.md').read_text())
                    self.assertEqual(references, [(alt, '/' + filename)])
                    self.assertTrue((ROOT / 'public' / filename).is_file())


class PreservationGuard(unittest.TestCase):
    def test_only_eight_replacements_are_accepted(self):
        before = dict.fromkeys(REPLACED_IMAGE_PATHS, 'original')
        before['src/content/projects/en/pullyt.md'] = 'protected'
        after = {p: ('new-' + p if p in REPLACED_IMAGE_PATHS else h)
                 for p, h in before.items()}
        assert_preserved_files(after, before)
        mutations = []
        reverted = dict(after)
        reverted['public/pullyt.png'] = 'original'
        mutations.append(reverted)
        changed_copy = dict(after)
        changed_copy['src/content/projects/en/pullyt.md'] = 'changed'
        mutations.append(changed_copy)
        missing = dict(after)
        del missing['public/smwm.png']
        mutations.append(missing)
        extra = dict(after)
        extra['public/unrequested.png'] = 'extra'
        mutations.append(extra)
        for index, mutated in enumerate(mutations):
            with self.subTest(mutation=index):
                with self.assertRaises(AssertionError):
                    assert_preserved_files(mutated, before)


class BuiltImages(unittest.TestCase):
    def test_sixteen_details_render_the_local_image_inside_prose(self):
        for locale in ('en', 'es'):
            for slug, (filename, alt) in PROJECTS.items():
                with self.subTest(locale=locale, slug=slug):
                    page = DIST / locale / 'projects' / slug / 'index.html'
                    self.assertTrue(page.is_file(), 'ejecutar yarn build')
                    images = Images(page.read_text()).images
                    self.assertEqual(len(images), 1)
                    attrs, in_prose = images[0]
                    self.assertTrue(in_prose)
                    self.assertEqual(attrs.get('src'), '/' + filename)
                    self.assertEqual(attrs.get('alt'), alt)
                    self.assertEqual((DIST / filename).read_bytes(),
                                     (ROOT / 'public' / filename).read_bytes())

    def test_images_are_not_added_outside_details(self):
        details = {f'{locale}/projects/{slug}/index.html'
                   for locale in ('en', 'es') for slug in PROJECTS}
        baseline_pages = json.loads(BASELINE.read_text())['pages']
        pages = {p.relative_to(DIST).as_posix(): p
                 for p in DIST.rglob('*.html')}
        self.assertEqual(len(pages), 30, 'build vacío o inventario de rutas alterado')
        self.assertEqual(set(pages), set(baseline_pages), 'rutas alteradas')
        project_sources = {'/' + filename for filename, _ in PROJECTS.values()}
        for relative, page in pages.items():
            if relative not in details:
                with self.subTest(page=relative):
                    actual = Counter((attrs.get('src'), attrs.get('alt'))
                                     for attrs, _ in Images(page.read_text()).images)
                    expected = Counter(tuple(image)
                                       for image in baseline_pages[relative]['images'])
                    self.assertEqual(actual, expected,
                                     'imágenes src/alt alteradas fuera del detalle')
                    self.assertTrue(project_sources.isdisjoint(src for src, _ in actual),
                                    'imagen de proyecto añadida fuera del detalle')


if __name__ == '__main__':
    unittest.main()
