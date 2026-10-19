# ---------- Planet Oasi 80 lisse + feu dual : 115 x 56 cm, plaque lisse 79 x 40 cm, feu double couronne à droite ----------
rep('  let Jr = .73,', '  let Jr = 1.15,')
rep('''  let kt = .1,
    Ue = .06,
    V0 = .1,
    Oe = N + kt,
    de = V - kt,''', '''  let kt = .05,
    Ue = .06,
    V0 = .1,
    Oe = N + kt,
    de = Oe + .79,''')
# cadre : le côté droit laisse la place au feu
rep('X(de, V, i0, se, Ze, Ct, G.steel, .002, ie);', 'X(de, de + .02, i0, se, Ze, Ct, G.steel, .002, ie), X(V - .05, V, i0, se, Ze, Ct, G.steel, .002, ie);')
# plaque lisse : plus de rainures
a = s.index('  let Xn = se - ft + .001,\n    jt = [];')
b = s.index('ie.add($r), X(Oe + .01, de - .01, Xn - 5e-4, Xn', a)
s = s[:a] + '  let Xn = se - ft + .001;\n  ' + s[b + len('ie.add($r), '):]
# commandes : deux pour la plaque, une pour le feu
rep('for (let T of [si - .17, si + .17]) {', 'for (let T of [Oe + .2, de - .2, (de + .02 + V - .05) / 2]) {')
rep('S0(.009, .009, .006, 32, G.handle, si, se + .003, U - V0 / 2, 0, 0, ie), S0(.003, .003, .002, 16, G.led, si + .05, se + .001, U - V0 / 2, 0, 0, ie);',
    'S0(.009, .009, .006, 32, G.handle, (Oe + de) / 2, se + .003, U - V0 / 2, 0, 0, ie), S0(.003, .003, .002, 16, G.led, (Oe + de) / 2 + .05, se + .001, U - V0 / 2, 0, 0, ie);')
FEU = '''  {
    let BX0 = de + .02, BX1 = V - .05, BXc = (BX0 + BX1) / 2, BZc = (Ze + Ct) / 2, BY = se - .028;
    X(BX0, BX1, BY - .004, BY, Ze, Ct, G.black, .001, ie, !1);
    X(BX0, BX0 + .003, BY, se - 5e-4, Ze, Ct, G.steelDark, .001, ie, !1), X(BX1 - .003, BX1, BY, se - 5e-4, Ze, Ct, G.steelDark, .001, ie, !1), X(BX0, BX1, BY, se - 5e-4, Ze, Ze + .003, G.steelDark, .001, ie, !1), X(BX0, BX1, BY, se - 5e-4, Ct - .003, Ct, G.steelDark, .001, ie, !1);
    S0(.07, .074, .014, 48, G.steelDark, BXc, BY + .007, BZc, 0, 0, ie);
    S0(.06, .06, .008, 48, G.black, BXc, BY + .017, BZc, 0, 0, ie);
    S0(.038, .042, .012, 40, G.steelDark, BXc, BY + .02, BZc, 0, 0, ie);
    S0(.022, .022, .008, 32, G.black, BXc, BY + .029, BZc, 0, 0, ie);
    let GW = (BX1 - BX0) / 2 - .006, GD = (Ct - Ze) / 2 - .008, GY = se + .012;
    X(BXc - GW, BXc + GW, GY - .007, GY, BZc - GD, BZc - GD + .012, G.black, .002, ie), X(BXc - GW, BXc + GW, GY - .007, GY, BZc + GD - .012, BZc + GD, G.black, .002, ie);
    X(BXc - GW, BXc - GW + .012, GY - .007, GY, BZc - GD, BZc + GD, G.black, .002, ie), X(BXc + GW - .012, BXc + GW, GY - .007, GY, BZc - GD, BZc + GD, G.black, .002, ie);
    X(BXc - GW, BXc - .05, GY - .007, GY, BZc - .006, BZc + .006, G.black, .002, ie), X(BXc + .05, BXc + GW, GY - .007, GY, BZc - .006, BZc + .006, G.black, .002, ie);
    X(BXc - .006, BXc + .006, GY - .007, GY, BZc - GD, BZc - .05, G.black, .002, ie), X(BXc - .006, BXc + .006, GY - .007, GY, BZc + .05, BZc + GD, G.black, .002, ie);
  }
  let hs = 1,
    ks = 1;'''
rep('  let hs = 1,\n    ks = 1;', FEU)
# le couvercle de la friteuse suit celui de la plancha
rep('    Ni.rotation.x = -Math.PI / 2 * K1(hs) * .98\n', '    Ni.rotation.x = -Math.PI / 2 * K1(hs) * .98, FNi && (FNi.rotation.x = Ni.rotation.x)\n')
