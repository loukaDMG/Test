# ---------- Planet Oasi 80 lisse : 103 x 56 cm, plaque lisse 79 x 40 cm, 3 brûleurs ----------
rep('  let Jr = .73,', '  let Jr = 1.03,')
rep('''  let kt = .1,
    Ue = .06,
    V0 = .1,''', '''  let kt = .12,
    Ue = .06,
    V0 = .1,''')
# plaque lisse : plus de rainures
a = s.index('  let Xn = se - ft + .001,\n    jt = [];')
b = s.index('ie.add($r), X(Oe + .01, de - .01, Xn - 5e-4, Xn', a)
s = s[:a] + '  let Xn = se - ft + .001;\n  ' + s[b + len('ie.add($r), '):]
# trois manettes (une par brûleur), allumage à gauche, voyant à droite
rep('for (let T of [si - .17, si + .17]) {', 'for (let T of [si - .26, si, si + .26]) {')
rep('S0(.009, .009, .006, 32, G.handle, si, se + .003, U - V0 / 2, 0, 0, ie), S0(.003, .003, .002, 16, G.led, si + .05, se + .001, U - V0 / 2, 0, 0, ie);',
    'S0(.009, .009, .006, 32, G.handle, si - .43, se + .003, U - V0 / 2, 0, 0, ie), S0(.003, .003, .002, 16, G.led, si + .43, se + .001, U - V0 / 2, 0, 0, ie);')
# le couvercle de la friteuse suit celui de la plancha
rep('    Ni.rotation.x = -Math.PI / 2 * K1(hs) * .98\n', '    Ni.rotation.x = -Math.PI / 2 * K1(hs) * .98, FNi && (FNi.rotation.x = Ni.rotation.x)\n')
