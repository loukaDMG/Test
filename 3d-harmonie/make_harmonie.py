import re, json, sys
src = open('model.js', encoding='utf-8').read()
s = src
def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)

# ---------- Configuration d'Harmonie (mètres, x = 0 au centre de la cuisine) ----------
HRM = {
  "car": 1.57,                 # demi-largeur du caisson bas
  "doors": [[-1.57, -0.97, "L"], [-0.97, -0.45, "L"], [0.45, 0.97, "R"], [0.97, 1.57, "R"]],
  "drawers": [[-0.45, 0.45]],
  "div": [-0.97, -0.45, 0.45, 0.97],
  "shelves": [[-0.952, -0.468], [0.468, 0.952]],
  "feet": [-1.45, -0.5, 0.5, 1.45],
  "frigoDx": -1.27 - 0.7505,   # le froid passe dans le module de gauche
  "si": 0.0,                   # plancha centrée sous la hotte
  "sink": 1.27,
  "frit": [-0.675, -0.385],
  "gaz": [0.385, 0.675],
  "hood": 1.40,
  "bz": [-0.72, 0.72],         # crédence noire derrière la cuisson
  "sockDx": 0.80 - (-0.9),
  "orchid": [-1.2, None, -0.14],
}
rep('function u7(s, e = {}) {', 'function u7(s, e = {}) {\n  const HRM = ' + json.dumps(HRM) + ';')

# largeur : +1 m
rep('    j = 1.25,\n', '    j = 1.75,\n')
rep('    n0 = 1.085,\n', '    n0 = 1.585,\n')

# crédence noire au centre, bois de part et d'autre
rep('R0(-n0, -.49, F0, y0, l0, .018), R0(.51, n0, F0, y0, l0, .018)', 'R0(-n0, HRM.bz[0], F0, y0, l0, .018), R0(HRM.bz[1], n0, F0, y0, l0, .018)')

# prises électriques : sur le plan libre de droite
rep('X(-.9, -.745, 1.07, 1.155, l0 + .008, l0 + .02, G.socket, .006);\n  for (let T of [-.861, -.784])',
    'X(-.9 + HRM.sockDx, -.745 + HRM.sockDx, 1.07, 1.155, l0 + .008, l0 + .02, G.socket, .006);\n  for (let T of [-.861 + HRM.sockDx, -.784 + HRM.sockDx])')

# spots : un au-dessus de chaque plan libre (la hotte occupe le centre)
rep('S0(.034, .034, .008, 40, G.steel, -.04, y0 - .006, -.04), S0(.026, .026, .004, 40, G.lamp, -.04, y0 - .011, -.04);\n  let I0 = new Br("#ffd9a3", 7, 1.12, Math.PI / 2.8, .9, 1.4);\n  I0.position.set(-.04, y0 - .02, -.04), I0.target.position.set(-.04, i0, -.12), b0.add(I0, I0.target);',
    'for (let SX of [-1.12, 1.0]) S0(.034, .034, .008, 40, G.steel, SX, y0 - .006, -.04), S0(.026, .026, .004, 40, G.lamp, SX, y0 - .011, -.04);\n  let I0 = new Br("#ffd9a3", 6, 1.12, Math.PI / 2.8, .9, 1.4);\n  I0.position.set(1.0, y0 - .02, -.04), I0.target.position.set(1.0, i0, -.12), b0.add(I0, I0.target);\n  let I1 = new Br("#ffd9a3", 6, 1.12, Math.PI / 2.8, .9, 1.4);\n  I1.position.set(-1.12, y0 - .02, -.04), I1.target.position.set(-1.12, i0, -.12), b0.add(I1, I1.target);')

# caisson bas sur 3,14 m, ouverture du plan au droit de l'évier
old = 'X(-1.07, -1.07 + pe, fe, Te, Ve, ut, G.carcass, .001), X(1.07 - pe, 1.07, fe, Te, Ve, ut, G.carcass, .001), X(-1.07, 1.07, fe, fe + pe, Ve, ut, G.carcass, .001), X(-1.07, 1.07, fe, Te, Ve, Ve + .01, G.carcass, 0), X(-1.07, 1.07, Te - pe, Te, Ve, -.28, G.carcass, .001), X(-1.07, 1.07, Te - pe, Te, .256, ut, G.carcass, .001), X(-1.07, -.905, Te - pe, Te, -.28, .256, G.carcass, .001), X(-.535, 1.07, Te - pe, Te, -.28, .256, G.carcass, .001);'
new = old.replace('-1.07 + pe', '-HRM.car + pe').replace('1.07 - pe', 'HRM.car - pe').replace('-1.07', '-HRM.car').replace('1.07', 'HRM.car').replace('-.905', '(HRM.sink - .185)').replace('-.535', '(HRM.sink + .185)')
rep(old, new)
rep('for (let T of [-.415, .44]) X(T - pe / 2, T + pe / 2, fe, Te, Ve, ut, G.carcass, .001);', 'for (let T of HRM.div) X(T - pe / 2, T + pe / 2, fe, Te, Ve, ut, G.carcass, .001);')
rep('X(-1.052, -.424, .5, .518, Ve + .03, ut - .03, G.carcass, .001), X(-1.04, 1.04, .01, fe, -.3, .2, G.black, 0, b0, !1);',
    'for (let [SA, SB] of HRM.shelves) X(SA, SB, .5, .518, Ve + .03, ut - .03, G.carcass, .001);\n  X(-HRM.car + .03, HRM.car - .03, .01, fe, -.3, .2, G.black, 0, b0, !1);')
rep('for (let T of [-.95, .95])\n    for (let z of [-.25, .15])', 'for (let T of HRM.feet)\n    for (let z of [-.25, .15])')

# portes : une par module « porte », charnière à gauche ou à droite
old = '''  for (let T of [-1, 1]) {
    let z = T < 0 ? -1.068 : 1.068,
      e0 = T < 0 ? -.415 - ii / 2 : .44 + ii / 2,
      g0 = new ke;'''
new = '''  for (let [DA, DB, DH] of HRM.doors) {
    let T = DH === "L" ? -1 : 1,
      z = T < 0 ? DA + .002 : DB - .002,
      e0 = T < 0 ? DB - ii / 2 : DA + ii / 2,
      g0 = new ke;'''
rep(old, new)
rep('Vn(_0, T < 0 ? -.45 : .475, .8, .128, !0);', 'Vn(_0, T < 0 ? DB - .035 : DA + .035, .8, .128, !0);')

# tiroirs : un bloc par module « tiroirs »
old = '''    os = -.415 + ii / 2,
    Yr = .44 - ii / 2;
  eo.forEach(([T, z, e0], g0) => {'''
new = '''    os, Yr;
  for (let [KA, KB] of HRM.drawers) { os = KA + ii / 2, Yr = KB - ii / 2;
  eo.forEach(([T, z, e0], g0) => {'''
rep(old, new)
rep('g0 < 2 && Vn(_0, .0125, z - .042, .128, !1)', 'g0 < 2 && Vn(_0, (os + Yr) / 2, z - .042, .128, !1)')
rep('''      travel: .42 - g0 * .02
    })
  });''', '''      travel: .42 - g0 * .02
    })
  }); }''')

# froid : déplacé dans le module de gauche
rep('''  }
  let Jr = .73,''', '''  }
  Kr.position.x = HRM.frigoDx, cs.position.x = HRM.frigoDx;
  let Jr = .73,''')

# plancha et évier
rep('    si = .0125,\n', '    si = HRM.si,\n')
rep('    j0 = -.72,\n', '    j0 = HRM.sink,\n')

# options : friteuse et plaque gaz
rep('''      plancha: !0,
      evier: !0,
      frigo: !0
    },''', '''      plancha: !0,
      evier: !0,
      frigo: !0,
      friteuse: !0,
      gaz: !0
    },''')
rep('''    let T = [];
    if (te.evier && T.push([j0 - re, j0 + re]), te.plancha && T.push([v0, L0]), !T.length) {''',
    '''    let T = [];
    te.evier && T.push([j0 - re, j0 + re]), te.plancha && T.push([v0, L0]), te.friteuse && T.push([HRM.frit[0] + .012, HRM.frit[1] - .012]), T.sort((a, b) => a[0] - b[0]);
    if (!T.length) {''')

# nouveaux éléments : friteuse, plaque gaz, hotte (insérés avant le bloc évier)
NEW = r'''
  let Fq = new ke, Gz = new ke, Hd = new ke;
  b0.add(Fq, Gz, Hd);
  {
    let FA = HRM.frit[0], FB = HRM.frit[1], FZ0 = W, FZ1 = U, FY = i0 + .004, FC = (FA + FB) / 2;
    X(FA, FB, i0 - .004, FY, FZ0, FZ1, G.steel, .003, Fq);
    X(FA + .028, FB - .028, i0 - .14, FY + 4e-4, FZ0 + .045, FZ1 - .13, G.steelDark, .003, Fq);
    for (let gx = FA + .042; gx < FB - .04; gx += .013) X(gx, gx + .0035, FY - .03, FY - .026, FZ0 + .06, FZ1 - .15, G.steel, 0, Fq, !1);
    X(FA + .036, FA + .042, FY - .03, FY + .012, FZ0 + .06, FZ1 - .15, G.steel, 0, Fq, !1), X(FB - .042, FB - .036, FY - .03, FY + .012, FZ0 + .06, FZ1 - .15, G.steel, 0, Fq, !1);
    S0(.006, .006, .12, 16, G.black, FC, FY + .03, FZ1 - .11, Math.PI / 2, 0, Fq);
    X(FC - .004, FC + .004, FY + .012, FY + .03, FZ1 - .14, FZ1 - .136, G.steel, 0, Fq, !1);
    X(FA + .02, FB - .02, FY, FY + .004, FZ1 - .085, FZ1 - .02, G.lidBlack, .002, Fq);
    S0(.017, .017, .014, 32, G.knob, FC - .05, FY + .011, FZ1 - .052, 0, 0, Fq), S0(.006, .006, .003, 16, G.led, FC + .05, FY + .005, FZ1 - .052, 0, 0, Fq);
  }
  {
    let GA = HRM.gaz[0], GB = HRM.gaz[1], GZ0 = W + .01, GZ1 = U - .01, GY = i0 + .006, GC = (GA + GB) / 2;
    X(GA, GB, i0, GY, GZ0, GZ1, G.lidBlack, .003, Gz);
    for (let [BZ, BR] of [[GZ0 + .15, .048], [GZ1 - .17, .038]]) {
      S0(BR + .014, BR + .014, .006, 48, G.steelDark, GC, GY + .003, BZ, 0, 0, Gz);
      S0(BR * .72, BR * .72, .014, 40, G.black, GC, GY + .009, BZ, 0, 0, Gz);
      for (let k = 0; k < 4; k++) {
        let Bm = X(-(BR + .05) / 2, (BR + .05) / 2, -.004, .004, -.006, .006, G.black, .002, Gz);
        Bm.position.set(GC + Math.cos(k * Math.PI / 2) * (BR + .05) / 2, GY + .022, BZ + Math.sin(k * Math.PI / 2) * (BR + .05) / 2), Bm.rotation.y = -k * Math.PI / 2;
      }
      X(GC - BR - .07, GC + BR + .07, GY + .026, GY + .032, BZ - .006, BZ + .006, G.black, .002, Gz);
      X(GC - .006, GC + .006, GY + .026, GY + .032, BZ - BR - .07, BZ + BR + .07, G.black, .002, Gz);
    }
    for (let KX of [GC - .05, GC + .05]) S0(.016, .016, .013, 32, G.knob, KX, GY + .007, GZ1 - .035, 0, 0, Gz);
  }
  {
    let HW = HRM.hood, HB = 1.62, HT = 1.79, ZB = l0 + .012, ZF = .2, ZT = .07;
    let Hs0 = new Si;
    Hs0.moveTo(ZB, HB), Hs0.lineTo(ZF, HB), Hs0.lineTo(ZF, HB + .04), Hs0.lineTo(ZT, HT), Hs0.lineTo(ZB, HT), Hs0.lineTo(ZB, HB);
    let Hg = new g1(Hs0, { depth: HW, bevelEnabled: !0, bevelThickness: .003, bevelSize: .003, bevelSegments: 2, curveSegments: 2 });
    Hg.rotateY(-Math.PI / 2), Hg.translate(HW / 2, 0, 0);
    let HSt = new xe({ color: "#d3d7db", metalness: .7, roughness: .3, roughnessMap: w0, anisotropy: .4, clearcoat: .15, clearcoatRoughness: .4 });
    let Hm = new U0(Hg, HSt);
    Hm.castShadow = !0, Hm.receiveShadow = !0, Hd.add(Hm);
    X(-.3, .3, HT - .01, y0 - .002, ZB + .01, ZB + .26, HSt, .003, Hd);
    X(-HW / 2 + .035, HW / 2 - .035, HB - .006, HB + .001, ZB + .03, ZF - .03, G.steelDark, .002, Hd);
    for (let FX = -HW / 2 + .06; FX < HW / 2 - .05; FX += .028) X(FX, FX + .012, HB - .009, HB - .005, ZB + .05, ZF - .05, G.steel, 0, Hd, !1);
    for (let LX of [-.38, .38]) S0(.022, .022, .004, 32, G.lamp, LX, HB - .011, ZF - .09, 0, 0, Hd);
    let Ih = new Br("#ffd9a3", 5, 1.1, Math.PI / 2.5, .8, 1.4);
    Ih.position.set(0, HB - .02, -.05), Ih.target.position.set(0, i0, -.05), Hd.add(Ih, Ih.target);
  }
'''
rep('''  {
    let T = new ke;
    b0.add(T), Zr = T;''', NEW + '''  {
    let T = new ke;
    b0.add(T), Zr = T;''')
rep('T === "frigo" && (Kr.visible = te.frigo, cs.visible = !te.frigo)', 'T === "frigo" && (Kr.visible = te.frigo, cs.visible = !te.frigo), T === "friteuse" && (Fq.visible = te.friteuse, Le()), T === "gaz" && (Gz.visible = te.gaz)')

# fleur sur le plan libre de gauche
rep('Hs.position.set(.78, i0, -.14)', 'Hs.position.set(HRM.orchid[0], i0, HRM.orchid[2])')

# store de fermeture sur toute la largeur
rep('new cn(2.134, 1)', 'new cn(2 * n0 - .036, 1)')
rep('X(-1.068, 1.068, .006, .038, .328, .368, G.frame, .006, to), X(-1.066, 1.066, 0, .007, .335, .362, G.rubber, .002, to);',
    'X(-n0 + .017, n0 - .017, .006, .038, .328, .368, G.frame, .006, to), X(-n0 + .019, n0 - .019, 0, .007, .335, .362, G.rubber, .002, to);')

# caméra et ombres pour une cuisine plus large
rep('l.position.set(-4.3, 1.55, 5.2);', 'l.position.set(-5.0, 1.55, 6.0);')
s = s.replace('h.maxDistance = 11', 'h.maxDistance = 13')
s = s.replace('left: -3.2,\n    right: 3.2,\n    top: 3.2,\n    bottom: -3.2,', 'left: -4,\n    right: 4,\n    top: 4,\n    bottom: -4,')
views = '''        face: [
          [0, 1.3, 8.2],
          [0, 1.1, 0]
        ],
        trois: [
          [-5.0, 1.55, 6.0],
          [0, 1.08, 0]
        ],
        cote: [
          [-7.8, 1.35, 1.1],
          [0, 1.1, 0]
        ],
        arriere: [
          [4.2, 1.6, -7],
          [0, 1.1, 0]
        ],
        detail: [
          [.45, 1.6, 1.45],
          [0, 1, -.05]
        ],
        rangement: [
          [-1.6, .95, 3.2],
          [-.2, .55, .3]
        ],'''
a = s.index('        face: [\n          [0, 1.3, 6.4],'); b = s.index('        jardin: [', a)
s = s[:a] + views + '\n' + s[b:]
rep('''        evier: [
          [-.45, 1.65, 1.15],
          [-.72, .98, -.05]
        ],
        frigo: [
          [.05, .85, 1.75],
          [.72, .5, 0]
        ]''', '''        evier: [
          [1.55, 1.65, 1.15],
          [1.27, .98, -.05]
        ],
        frigo: [
          [-.6, .85, 1.75],
          [-1.27, .5, 0]
        ]''')

exec(open('depth_patch.py', encoding='utf-8').read())
open('harmonie-model.js', 'w', encoding='utf-8').write(s)
head = open('head.min.js', encoding='utf-8').read()
open('site/harmonie.js', 'w', encoding='utf-8').write(head + s)
print('ok', len(s))
