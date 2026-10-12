"""Génère le flyer A5 recto-verso DMG Concept (v2, « Tectonique silencieuse »).

Sortie : flyer-dmg-concept-v2.html (polices embarquées), à imprimer en PDF avec Chromium.
Toutes les coordonnées de page sont en millimètres (A5 + 3 mm de fond perdu = 154 x 216).
"""
import base64
import math
import pathlib

HERE = pathlib.Path(__file__).parent
W, H = 154.0, 216.0
M = 12.0  # 3 mm fond perdu + 9 mm de marge

CARBONE = "#131313"
ANTHRACITE = "#1e1f21"
GALVA = "#8e8c87"
GRIS = "#bfbcb5"
CHENE = "#bb8c5f"
PAPIER = "#f1ede6"
BLANC = "#f7f5f0"

SANS = "Instrument Sans"
SERIF = "Instrument Serif"
MONO = "Geist Mono"


def f(v):
    return f"{v:.3f}".rstrip("0").rstrip(".")


def pts(points):
    return " ".join(f"{f(x)},{f(y)}" for x, y in points)


def text(x, y, s, size, family=SANS, fill=BLANC, anchor="start", weight=400, spacing=0, style="normal", opacity=1):
    return (f'<text x="{f(x)}" y="{f(y)}" font-family="{family}" font-size="{f(size)}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}" letter-spacing="{f(spacing)}" '
            f'font-style="{style}" opacity="{opacity}">{s}</text>')


PT = 0.3528  # 1 pt en mm


def wordmark(x, y, fill):
    return (text(x, y, "DMG", 9.5 * PT, SANS, fill, weight=700, spacing=0.35)
            + text(x + 10.6, y, "CONCEPT", 9.5 * PT, SANS, fill, spacing=1.05))


# ---------------------------------------------------------------- isométrie
C30, S30 = math.cos(math.radians(30)), 0.5


class Iso:
    def __init__(self, k, ox, oy):
        self.k, self.ox, self.oy = k, ox, oy

    def p(self, x, y, z):
        return (self.ox + (x - y) * C30 * self.k, self.oy + ((x + y) * S30 - z) * self.k)

    def poly(self, pts3, fill="none", stroke=BLANC, sw=0.18, extra=""):
        return (f'<polygon points="{pts([self.p(*q) for q in pts3])}" fill="{fill}" stroke="{stroke}" '
                f'stroke-width="{f(sw)}" stroke-linejoin="round" {extra}/>')

    def line(self, a, b, stroke=BLANC, sw=0.12, extra=""):
        (x1, y1), (x2, y2) = self.p(*a), self.p(*b)
        return (f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{stroke}" '
                f'stroke-width="{f(sw)}" stroke-linecap="round" {extra}/>')

    def box(self, x0, x1, y0, y1, z0, z1, top, front, side, stroke=BLANC, sw=0.18):
        return (self.poly([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, stroke, sw)
                + self.poly([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], front, stroke, sw)
                + self.poly([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], side, stroke, sw))


def exploded_view():
    """Vue éclatée isométrique de la cuisine. Renvoie (svg, ancres des repères)."""
    G = 26  # écart d'éclatement
    z_plot = (0, 20)
    z_ch = (z_plot[1] + G, z_plot[1] + G + 12)
    zb = z_ch[1] + G                       # base des caissons
    z_mod = (zb, zb + 85)
    z_wt = (z_mod[1] + G, z_mod[1] + G + 5)  # plan de travail
    z_wall = (zb, zb + 236)
    z_roof = (z_wall[1] + G, z_wall[1] + G + 14)

    iso = Iso(0.192, 0, 0)
    # cadrage : on calcule l'emprise puis on recentre dans la zone de dessin
    corners = [iso.p(x, y, z) for x in (-10, 410) for y in (-10, 100) for z in (0, z_roof[1])]
    minx = min(c[0] for c in corners); maxx = max(c[0] for c in corners)
    miny = min(c[1] for c in corners); maxy = max(c[1] for c in corners)
    area_x0, area_y0, area_h = M + 2.5, 31, 124
    iso.ox = area_x0 - minx
    iso.oy = area_y0 + (area_h - (maxy - miny)) / 2 - miny

    o = []
    # lignes d'assemblage (pointillés), dessinées en premier : visibles seulement dans les vides
    for (x, y) in ((0, 80), (400, 80), (400, 0)):
        o.append(iso.line((x, y, z_plot[1]), (x, y, z_roof[0]), GALVA, 0.1, 'stroke-dasharray="0.6 0.9" opacity="0.7"'))

    # plots béton
    for (x0, y0) in ((15, 8), (15, 47), (355, 8), (355, 47)):
        o.append(iso.box(x0, x0 + 30, y0, y0 + 25, *z_plot, "#2a2b2d", "#232426", "#1a1b1c", GRIS, 0.16))

    # châssis galvanisé : cadre + hachures acier à 45°
    o.append(iso.box(0, 400, 0, 80, *z_ch, "none", "none", "none", GRIS, 0.18))
    o.append(iso.poly([(0, 0, z_ch[1]), (400, 0, z_ch[1]), (400, 80, z_ch[1]), (0, 80, z_ch[1])], ANTHRACITE, GRIS, 0.18))
    o.append(iso.poly([(10, 10, z_ch[1]), (390, 10, z_ch[1]), (390, 70, z_ch[1]), (10, 70, z_ch[1])], CARBONE, GRIS, 0.12))
    for cx in (100, 200, 300):
        o.append(iso.poly([(cx - 5, 10, z_ch[1]), (cx + 5, 10, z_ch[1]), (cx + 5, 70, z_ch[1]), (cx - 5, 70, z_ch[1])], ANTHRACITE, GRIS, 0.1))
    o.append(iso.poly([(0, 80, z_ch[0]), (400, 80, z_ch[0]), (400, 80, z_ch[1]), (0, 80, z_ch[1])], ANTHRACITE, GRIS, 0.18))
    o.append(iso.poly([(400, 0, z_ch[0]), (400, 80, z_ch[0]), (400, 80, z_ch[1]), (400, 0, z_ch[1])], "#19191b", GRIS, 0.18))
    step = 9
    for t in range(-12, 400, step):  # hachures façade
        a, b = max(t, 0), min(t + 12, 400)
        if b <= a:
            continue
        za = z_ch[0] + (a - t); zb_ = z_ch[0] + (b - t)
        o.append(iso.line((a, 80, za), (b, 80, zb_), GALVA, 0.07))
    for t in range(-12, 80, step):   # hachures côté
        a, b = max(t, 0), min(t + 12, 80)
        if b <= a:
            continue
        o.append(iso.line((400, a, z_ch[0] + (a - t)), (400, b, z_ch[0] + (b - t)), GALVA, 0.07))

    # bardage bois (paroi arrière) : lames verticales + crédence noire
    o.append(iso.box(0, 400, 0, 10, *z_wall, "#2a2420", "#221d19", "#1b1714", CHENE, 0.16))
    for x in range(8, 400, 8):
        o.append(iso.line((x, 10, z_wall[0]), (x, 10, z_wall[1]), CHENE, 0.07, 'opacity="0.85"'))
    z_cr = (z_wt[1], z_wt[1] + 38)
    o.append(iso.poly([(0, 10, z_cr[0]), (400, 10, z_cr[0]), (400, 10, z_cr[1]), (0, 10, z_cr[1])], "#0c0c0c", BLANC, 0.12))
    for x in (40, 352):  # prises
        o.append(iso.poly([(x, 10, z_cr[0] + 14), (x + 9, 10, z_cr[0] + 14), (x + 9, 10, z_cr[0] + 23), (x, 10, z_cr[0] + 23)], "none", BLANC, 0.09))

    # caissons : quatre modules identiques, façades détaillées
    for i in range(4):
        x0, x1 = i * 100 + 1.2, (i + 1) * 100 - 1.2
        o.append(iso.box(x0, x1, 10, 80, *z_mod, "#252628", "#18191a", "#111112", BLANC, 0.18))
        y, za, zz = 80, z_mod[0] + 5, z_mod[1] - 5
        if i in (0, 2):      # deux portes
            xm = (x0 + x1) / 2
            o.append(iso.line((xm, y, za), (xm, y, zz), BLANC, 0.08))
            for xh in (xm - 5, xm + 5):
                o.append(iso.line((xh, y, zz - 8), (xh, y, zz - 22), BLANC, 0.14))
        elif i == 1:         # tiroirs
            for zt in (za + 25, za + 50):
                o.append(iso.line((x0 + 4, y, zt), (x1 - 4, y, zt), BLANC, 0.08))
            for zt in (za + 12, za + 37, za + 63):
                o.append(iso.line((x0 + 38, y, zt), (x1 - 38, y, zt), BLANC, 0.14))
        else:                # réfrigérateur intégré
            o.append(iso.poly([(x0 + 6, y, za), (x1 - 6, y, za), (x1 - 6, y, zz), (x0 + 6, y, zz)], "none", BLANC, 0.08))
            o.append(iso.line((x0 + 12, y, zz - 7), (x0 + 36, y, zz - 7), BLANC, 0.14))

    # plan de travail Dekton + équipements en symboles de plan
    o.append(iso.box(-4, 404, 10, 86, *z_wt, "#0b0b0b", "#0b0b0b", "#070707", BLANC, 0.2))
    zt = z_wt[1]
    o.append(iso.poly([(112, 24, zt), (188, 24, zt), (188, 72, zt), (112, 72, zt)], "#1d1d1e", BLANC, 0.12))
    for xx in range(118, 186, 5):  # plancha : stries
        o.append(iso.line((xx, 28, zt), (xx, 68, zt), GALVA, 0.06))
    o.append(iso.poly([(222, 30, zt), (278, 30, zt), (278, 68, zt), (222, 68, zt)], "#000", BLANC, 0.12))
    drain = [(250 + 3.4 * math.cos(a), 52 + 3.4 * math.sin(a), zt) for a in [i * math.pi / 12 for i in range(24)]]
    o.append(iso.poly(drain, "none", BLANC, 0.08))
    faucet = [(250, 18, zt), (250, 18, zt + 30), (250, 34, zt + 30), (250, 34, zt + 23)]
    for a, b in zip(faucet, faucet[1:]):
        o.append(iso.line(a, b, BLANC, 0.3))

    # toiture plate, membrane EPDM
    o.append(iso.box(-10, 410, -10, 100, *z_roof, "#0f0f10", "#1c1d1f", "#151516", BLANC, 0.2))
    o.append(iso.poly([(-4, -4, z_roof[1]), (404, -4, z_roof[1]), (404, 94, z_roof[1]), (-4, 94, z_roof[1])], "none", GALVA, 0.06))

    anchors = {
        "A": iso.p(410, 45, (z_roof[0] + z_roof[1]) / 2),
        "B": iso.p(400, 5, z_wall[1] - 30),
        "C": iso.p(404, 48, (z_wt[0] + z_wt[1]) / 2),
        "D": iso.p(398.8, 45, (z_mod[0] + z_mod[1]) / 2),
        "E": iso.p(400, 40, (z_ch[0] + z_ch[1]) / 2),
        "F": iso.p(385, 60, 10),
    }
    return "".join(o), anchors


def recto():
    o = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="{CARBONE}"/>']
    o.append(wordmark(M, M + 4, BLANC))
    o.append(text(W - M, M + 4, "FIG. 01 — VUE ÉCLATÉE", 5.6 * PT, MONO, GALVA, "end", spacing=0.25))
    o.append(f'<line x1="{M}" y1="{M + 8}" x2="{W - M}" y2="{M + 8}" stroke="{BLANC}" stroke-width="0.1" opacity="0.18"/>')

    svg, anchors = exploded_view()
    o.append(svg)

    labels = {
        "A": "Toiture plate EPDM",
        "B": "Bardage bois",
        "C": "Plan Dekton",
        "D": "Modules",
        "E": "Châssis galvanisé",
        "F": "Plots béton",
    }
    lx = W - M - 26.5
    for key, (ax, ay) in anchors.items():
        o.append(f'<line x1="{f(ax + 1.2)}" y1="{f(ay)}" x2="{f(lx - 1.6)}" y2="{f(ay)}" stroke="{CHENE}" stroke-width="0.1"/>')
        o.append(f'<circle cx="{f(ax)}" cy="{f(ay)}" r="0.55" fill="{CHENE}"/>')
        o.append(text(lx, ay + 0.75, key, 6 * PT, MONO, CHENE))
        o.append(text(lx + 3.4, ay + 0.75, labels[key], 6.4 * PT, SANS, GRIS))

    # titre
    ty = 172
    o.append(text(M - 0.6, ty, "Cuisines extérieures", 25 * PT, SANS, BLANC, spacing=-0.25))
    o.append(text(M - 0.2, ty + 10.2, "modulaires.", 31 * PT, SERIF, CHENE, style="italic", spacing=-0.1))
    o.append(text(W - M, ty + 10.2, "HAUTE-SAVOIE", 5.6 * PT, MONO, GALVA, "end", spacing=0.25))

    by = H - M - 1
    o.append(f'<line x1="{M}" y1="{by - 8}" x2="{W - M}" y2="{by - 8}" stroke="{BLANC}" stroke-width="0.1" opacity="0.18"/>')
    o.append(text(M, by, "07 49 66 12 56", 12 * PT, SANS, BLANC, weight=700, spacing=0.1))
    o.append(text(W - M, by, "dmg-concept.com   ·   @dmg_concept", 6.6 * PT, MONO, GRIS, "end"))
    return "".join(o)


# ---------------------------------------------------------------- plans (verso)
def plan_symbol(kind, x, y, w, h, ink):
    """Symbole de plan dans un module de w x h mm (le mur est en haut)."""
    o = []
    cx, cy = x + w / 2, y + h / 2
    if kind == "plancha":
        o.append(f'<rect x="{f(x + 2.4)}" y="{f(y + 2.2)}" width="{f(w - 4.8)}" height="{f(h - 4.4)}" fill="none" stroke="{ink}" stroke-width="0.14"/>')
        n = 9
        for i in range(1, n):
            xx = x + 2.4 + (w - 4.8) * i / n
            o.append(f'<line x1="{f(xx)}" y1="{f(y + 2.9)}" x2="{f(xx)}" y2="{f(y + h - 2.9)}" stroke="{ink}" stroke-width="0.07"/>')
    elif kind == "barbecue":
        r = min(w, h) / 2 - 2
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="none" stroke="{ink}" stroke-width="0.14"/>')
        for i in range(-3, 4):
            dx = i * r / 4
            dy = math.sqrt(max(r * r - dx * dx, 0)) - 0.5
            o.append(f'<line x1="{f(cx + dx)}" y1="{f(cy - dy)}" x2="{f(cx + dx)}" y2="{f(cy + dy)}" stroke="{ink}" stroke-width="0.07"/>')
    elif kind == "four":
        r = w / 2 - 2.6
        base = y + h - 2.4
        o.append(f'<path d="M{f(cx - r)} {f(base)} A{f(r)} {f(r * 0.95)} 0 0 1 {f(cx + r)} {f(base)} Z" fill="none" stroke="{ink}" stroke-width="0.14"/>')
        r2 = r * 0.55
        o.append(f'<path d="M{f(cx - r2)} {f(base)} A{f(r2)} {f(r2)} 0 0 1 {f(cx + r2)} {f(base)}" fill="none" stroke="{ink}" stroke-width="0.08"/>')
    elif kind == "evier":
        o.append(f'<rect x="{f(x + 3)}" y="{f(y + 2.6)}" width="{f(w - 6)}" height="{f(h - 5.2)}" rx="1.4" fill="none" stroke="{ink}" stroke-width="0.14"/>')
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy + 0.4)}" r="0.7" fill="none" stroke="{ink}" stroke-width="0.09"/>')
        o.append(f'<line x1="{f(cx)}" y1="{f(y + 0.9)}" x2="{f(cx)}" y2="{f(y + 2.6)}" stroke="{ink}" stroke-width="0.22"/>')
    elif kind == "froid":
        o.append(f'<line x1="{f(x + 1.6)}" y1="{f(y + 1.6)}" x2="{f(x + w - 1.6)}" y2="{f(y + h - 1.6)}" stroke="{ink}" stroke-width="0.09"/>')
        o.append(f'<line x1="{f(x + w - 1.6)}" y1="{f(y + 1.6)}" x2="{f(x + 1.6)}" y2="{f(y + h - 1.6)}" stroke="{ink}" stroke-width="0.09"/>')
    elif kind == "rangement":  # débattement de porte, convention de plan
        r = w / 2 - 0.6
        o.append(f'<path d="M{f(x + 0.6)} {f(y + h)} L{f(x + 0.6)} {f(y + h + r * 0.0)} M{f(x + 0.6)} {f(y + h)} '
                 f'A{f(r)} {f(r)} 0 0 0 {f(x + 0.6 + r)} {f(y + h - r)}" fill="none" stroke="{ink}" stroke-width="0.08" stroke-dasharray="0.5 0.5"/>')
        o.append(f'<line x1="{f(x + 0.6 + r)}" y1="{f(y + h)}" x2="{f(x + 0.6 + r)}" y2="{f(y + h - r)}" stroke="{ink}" stroke-width="0.12"/>')
    return "".join(o)


MW, MH = 17.6, 12.3  # module canonique en plan


def symbol(kind, x, y, scale, ink):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(scale)})">'
            f'<rect x="0" y="0" width="{MW}" height="{MH}" fill="none" stroke="{ink}" stroke-width="0.2"/>'
            f'{plan_symbol(kind, 0, 0, MW, MH, ink)}</g>')


def module_row(kinds, x, y, mw, mh, ink, wood):
    o = []
    n = len(kinds)
    # paroi bois en fond (haut du plan)
    o.append(f'<rect x="{f(x)}" y="{f(y - 1.7)}" width="{f(n * mw)}" height="1.7" fill="none" stroke="{wood}" stroke-width="0.1"/>')
    xx = x + 0.8
    while xx < x + n * mw - 0.4:
        o.append(f'<line x1="{f(xx)}" y1="{f(y - 1.7)}" x2="{f(xx)}" y2="{f(y)}" stroke="{wood}" stroke-width="0.06"/>')
        xx += 0.8
    for i, k in enumerate(kinds):
        mx = x + i * mw
        o.append(symbol(k, mx, y, mw / MW, ink))
    return "".join(o)


def verso():
    ink = CARBONE
    o = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PAPIER}"/>']
    o.append(wordmark(M, M + 4, CARBONE))
    o.append(text(W - M, M + 4, "FIG. 02 — COMPOSITIONS", 5.6 * PT, MONO, GALVA, "end", spacing=0.25))
    o.append(f'<line x1="{M}" y1="{M + 8}" x2="{W - M}" y2="{M + 8}" stroke="{CARBONE}" stroke-width="0.1" opacity="0.2"/>')

    o.append(text(M - 0.4, 37, "Chaque cuisine se compose", 17 * PT, SANS, CARBONE, spacing=-0.15))
    o.append(text(M - 0.1, 44.6, "module par module.", 21 * PT, SERIF, CHENE, style="italic"))

    rows = [
        ("02", ["plancha", "evier"]),
        ("03", ["barbecue", "rangement", "evier"]),
        ("04", ["plancha", "rangement", "evier", "froid"]),
        ("05", ["four", "plancha", "rangement", "evier", "froid"]),
    ]
    mw = 16.6
    mh = mw * MH / MW
    x0 = M + 20
    y = 60
    for num, kinds in rows:
        o.append(text(M, y + 5.4, num, 13 * PT, SANS, CHENE))
        o.append(text(M, y + 9.6, "MODULES", 5 * PT, MONO, GALVA, spacing=0.25))
        o.append(module_row(kinds, x0, y, mw, mh, ink, CHENE))
        y += 18.4
    o.append(text(W - M, 60 - 4.6, "EXEMPLES — VUE DE DESSUS", 5 * PT, MONO, GALVA, "end", spacing=0.25))

    # légende
    ly = y + 2.5
    o.append(f'<line x1="{M}" y1="{f(ly - 3)}" x2="{W - M}" y2="{f(ly - 3)}" stroke="{CARBONE}" stroke-width="0.1" opacity="0.2"/>')
    legend = [("plancha", "Plancha"), ("barbecue", "Barbecue"), ("four", "Four à pizza"),
              ("evier", "Évier"), ("froid", "Réfrigérateur"), ("rangement", "Rangement")]
    sw_ = 11.4
    sh_ = sw_ * MH / MW
    colw = (W - 2 * M) / 3
    for i, (k, name) in enumerate(legend):
        cx = M + (i % 3) * colw
        cy = ly + (i // 3) * 11.2
        o.append(symbol(k, cx, cy, sw_ / MW, ink))
        o.append(text(cx + sw_ + 2.6, cy + sh_ / 2 + 1, name, 7 * PT, SANS, CARBONE))

    fy = ly + 11.2 + sh_ + 7.5
    o.append(text(M, fy, "FINITIONS", 5 * PT, MONO, GALVA, spacing=0.25))
    o.append(text(M + 17, fy, "Façades compact · plan Dekton · bardage bois · crédence et appareillage noirs",
                  6.6 * PT, SANS, "#3b3a37"))

    # bandeau contact
    band = H - 47
    o.append(f'<rect x="0" y="{f(band)}" width="{W}" height="{f(H - band)}" fill="{CARBONE}"/>')
    o.append(text(M, band + 12, "ÉTUDE ET DEVIS GRATUITS", 5.6 * PT, MONO, CHENE, spacing=0.3))
    o.append(text(M - 0.3, band + 23.5, "07 49 66 12 56", 19 * PT, SANS, BLANC, weight=700, spacing=0.05))
    right = [("contact@dmg-concept.com", 0), ("dmg-concept.com", 1), ("@dmg_concept", 2)]
    for s, i in right:
        o.append(text(W - M, band + 12 + i * 4.3, s, 6.8 * PT, SANS, GRIS, "end"))
    o.append(f'<line x1="{M}" y1="{f(band + 29.5)}" x2="{W - M}" y2="{f(band + 29.5)}" stroke="{BLANC}" stroke-width="0.1" opacity="0.15"/>')
    o.append(text(M, H - M - 0.5, "58 impasse des Roseaux, 74570 Évires — Fillière", 6.2 * PT, SANS, GRIS))
    o.append(text(W - M, H - M - 0.5, "DMG CONCEPT SASU", 5 * PT, MONO, GALVA, "end", spacing=0.25))
    return "".join(o)


def font_face(name, file, style="normal", weight=400):
    data = base64.b64encode((HERE / "fonts" / file).read_bytes()).decode()
    return (f'@font-face{{font-family:"{name}";font-style:{style};font-weight:{weight};'
            f'src:url(data:font/ttf;base64,{data}) format("truetype");}}')


def page(svg):
    return (f'<section class="page"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(W)} {f(H)}" '
            f'width="{f(W)}mm" height="{f(H)}mm">{svg}</svg></section>')


def main():
    css = "".join([
        font_face(SANS, "InstrumentSans-Regular.ttf"),
        font_face(SANS, "InstrumentSans-Bold.ttf", weight=700),
        font_face(SERIF, "InstrumentSerif-Italic.ttf", style="italic"),
        font_face(MONO, "GeistMono-Regular.ttf"),
    ])
    html = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Flyer DMG Concept</title>
<style>{css}
@page {{ size: {f(W)}mm {f(H)}mm; margin: 0; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ background: #8f8d88; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width: {f(W)}mm; height: {f(H)}mm; margin: 10mm auto; overflow: hidden; }}
.page svg {{ display: block; }}
@media print {{ html, body {{ background: none; }} .page {{ margin: 0; break-after: page; }} .page:last-child {{ break-after: auto; }} }}
</style></head><body>
{page(recto())}
{page(verso())}
</body></html>"""
    (HERE / "flyer-dmg-concept-v2.html").write_text(html)


if __name__ == "__main__":
    main()
