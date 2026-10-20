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
# entrer dans la cuisine : caméra à hauteur d'yeux, on regarde autour en faisant glisser (champ de vision élargi)
rep('''        accueil: [''', '''        entree: [
          [1, 1.75, 1.15],
          [.955, 1.733, 1.114]
        ],
        accueil: [''')
rep('l.position.lerpVectors(Yt.p0, Yt.p1, _0), h.target.lerpVectors(Yt.q0, Yt.q1, _0), Yt.t >= 1 && (Yt = null)',
    'l.position.lerpVectors(Yt.p0, Yt.p1, _0), h.target.lerpVectors(Yt.q0, Yt.q1, _0), Yt.f1 && (FVo = Yt.f0 + (Yt.f1 - Yt.f0) * _0, l.fov = FVo, l.updateProjectionMatrix(), Yt.t >= 1 && !Yt.in && (FVo = 0)), Yt.t >= 1 && (Yt = null)')
rep('l.fov = Math.min(52, 30 * Math.max(1, Math.pow(1.35 / l.aspect, .75)))', 'l.fov = FVo || FVb()')
rep('    setHalf(T) {', '''    enter(T, I) {
      clearTimeout(EXt), EXin = !!T, T ? (h.minDistance = .02, h.enableZoom = !1, h.maxPolarAngle = Math.PI * .85, h.autoRotate = !1, this.view("entree")) : (h.enableZoom = !0, h.maxPolarAngle = Math.PI * .495, this.view("trois"), EXt = setTimeout(() => { EXin || (h.minDistance = 1) }, 1500)), I && Yt && (l.position.copy(Yt.p1), h.target.copy(Yt.q1), FVo = T ? 64 : 0, l.fov = Yt.f1, l.updateProjectionMatrix(), Yt = null), k = !0, ia()
    },
    setHalf(T) {''')
rep('  let HF = new ke, HFon = !1,', '  let EXt = 0, EXin = !1, FVo = 0, FVb = () => Math.min(52, 30 * Math.max(1, Math.pow(1.35 / l.aspect, .75))), HF = new ke, HFon = !1,')
# toute transition de caméra ramène aussi le champ de vision (large dedans, normal dehors)
rep('''      q0: h.target.clone(),
      q1: new P(...z)
    }''', '''      q0: h.target.clone(),
      q1: new P(...z),
      f0: l.fov,
      f1: EXin ? 64 : FVb(),
      in: EXin
    }''')
# store piloté directement (défilement de l'accueil) : 0 = rentré, 1 = sorti, sans animation propre
rep('    getCladding() {', '''    setStoreAmount(T) {
      T = Math.max(0, Math.min(1, T)), te.store = T > 0, SB = SBt = T, sbApply(), ia()
    },
    getCladding() {''')
# séquence de l'accueil pilotée par le défilement : caméra entre deux vues, volet, bar, bardage mixte
rep('    setStoreAmount(T) {', '''    pose(A, B, t) {
      let a = this.view(A), b = this.view(B || A);
      Yt = null, h.autoRotate = !1, a && b && (l.position.set(...a[0]).lerp(new P(...b[0]), t), h.target.set(...a[1]).lerp(new P(...b[1]), t)), k = !0, ia()
    },
    setBlindAmount(T) {
      Ui = Vs = Math.max(0, Math.min(1, T)), ec(), k = !0, ia()
    },
    setBarIn(T) {
      te.bar && (BRi = BRit = Math.max(0, Math.min(1, T)), brApply()), ia()
    },
    setHalfAmount(T) {
      T = Math.max(0, Math.min(1, T)), HFon = T > 0, HF.visible = HFon && $ !== "fundermax", HF.scale.z = Math.max(.001, T), HF.position.z = (-WB + .045) * (1 - HF.scale.z), k = !0, ia()
    },
    setStoreAmount(T) {''')
