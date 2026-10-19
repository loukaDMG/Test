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
# vue large pour l'accueil (cuisine, terrasse et bar dans le cadre)
rep('''        bar: [''', '''        accueil: [
          [-6.5, 2.1, 8.3],
          [.25, .95, .75]
        ],
        bar: [''')
# bardage mixte : Fundermax anthracite sur la moitié arrière des murs latéraux, lames sur la moitié avant
rep('  D0.visible = !1, b0.add(D0);\n', '''  D0.visible = !1, b0.add(D0);
  let HF = new ke, HFon = !1, HFz = (WF - WB) / 2;
  HF.visible = !1, b0.add(HF);
  for (let T of [-1, 1]) X(T < 0 ? -j - .024 : j + .006, T < 0 ? -j - .006 : j + .024, .025, a0 - .055, -WB + .045, HFz, ee, .002, HF);
''')
rep('    BRs.visible = BRk.visible = !T, BRp.visible = T;', '    BRs.visible = BRk.visible = !T, BRp.visible = T, HF.visible = HFon && !T;')
rep('    getCladding() {', '''    setHalf(T) {
      HFon = !!T, HF.visible = HFon && $ !== "fundermax", k = !0, qn = 60
    },
    getCladding() {''')
