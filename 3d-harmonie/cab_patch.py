# ---------- Meubles bas comme la réalisation : porte | bandeau + (2 tiroirs | porte | porte) | porte ----------
# Le bandeau fixe cache le dessous de la friteuse et de la plancha ; les portes du bas ont une poignée horizontale en haut.
rep('for (let [DA, DB, DH] of HRM.doors) {', 'for (let [DA, DB, DH, DT = .908, DS] of HRM.doors) {')
rep('.112, .908, zt, Di, G.front, .0025, _0), Vn(_0, T < 0 ? DB - .035 : DA + .035, .8, .128, !0);',
    '.112, DT, zt, Di, G.front, .0025, _0), DS ? Vn(_0, (DA + DB) / 2, DT - .045, .16, !1) : Vn(_0, T < 0 ? DB - .035 : DA + .035, .8, .128, !0);')
rep('for (let s0 of [.2, .82]) X(T < 0 ? z + .02', 'for (let s0 of [.2, DT - .088]) X(T < 0 ? z + .02')
rep('''      [.112, .376, .2],
      [.376, .642, .17],
      [.642, .908, .07]''', '''      [.112, .418, .2],
      [.418, HRM.band[2], .14]''')
rep('g0 < 2 && Vn(_0, (os + Yr) / 2, z - .042, .128, !1)', 'g0 < 2 && Vn(_0, (os + Yr) / 2, z - .042, .16, !1)')
rep('  for (let T of HRM.div) X(T - pe / 2, T + pe / 2, fe, Te, Ve, ut, G.carcass, .001);',
    '''  for (let T of HRM.div) X(T - pe / 2, T + pe / 2, fe, Te, Ve, ut, G.carcass, .001);
  for (let T of HRM.divLow) X(T - pe / 2, T + pe / 2, fe, HRM.band[2] - .018, Ve, ut, G.carcass, .001);
  X(HRM.band[0] + pe / 2, HRM.band[1] - pe / 2, HRM.band[2] - .018, HRM.band[2], Ve, ut, G.carcass, .001);''')
rep('''  let zt = .265,
    Di = .285,
    ii = .0035;''', '''  let zt = .265,
    Di = .285,
    ii = .0035;
  X(HRM.band[0] + ii / 2, HRM.band[1] - ii / 2, HRM.band[2] + ii / 2, .908, zt, Di, G.front, .0025);''')
