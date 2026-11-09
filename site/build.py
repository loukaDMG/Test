#!/usr/bin/env python3
"""Assemble le site DMG Concept en un seul fichier HTML (photos intégrées).

Usage : python3 build.py <dossier_source> <sortie_artifact.html> <sortie_autonome.html>
- sortie_artifact : contenu seul (la page publiée ajoute elle-même doctype/head/body)
- sortie_autonome : document HTML complet, à ouvrir directement dans un navigateur
"""
import base64, os, re, sys

src_dir, out_page, out_full = sys.argv[1:4]
html = open(os.path.join(src_dir, 'src.html'), encoding='utf-8').read()

def data_uri(name):
    for ext, mime, sub in (('.svg', 'image/svg+xml', ''), ('.webp', 'image/webp', 'w'), ('.jpg', 'image/jpeg', ''), ('.png', 'image/png', '')):
        p = os.path.join(src_dir, 'img', sub, name + ext)
        if os.path.exists(p):
            return 'data:%s;base64,%s' % (mime, base64.b64encode(open(p, 'rb').read()).decode())
    raise SystemExit('image manquante : ' + name)

html = re.sub(r'\{\{([A-Za-z0-9_]+)\}\}', lambda m: data_uri(m.group(1)), html)
html = re.sub(r'<!--JS:([^>]+)-->', lambda m: '<script>' + open(os.path.join(src_dir, m.group(1)), encoding='utf-8').read() + '</script>', html)
open(out_page, 'w', encoding='utf-8').write(html)
full = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + html.replace('<header class="hdr"', '</head>\n<body>\n<header class="hdr"', 1)
        + '\n</body>\n</html>\n')
open(out_full, 'w', encoding='utf-8').write(full)
print('ok', len(html) // 1024, 'Ko')
