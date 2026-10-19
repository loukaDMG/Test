# ---------- Bar sur roulettes (option) : lames bois comme le bardage, plateau noir, 4 roulettes ----------
# Il part de la terrasse de droite, tourne au coin et se gare devant la cuisine, à droite.
# Quand on ferme, il rentre contre les meubles avant que le volet descende ; à l'ouverture, le volet remonte puis il ressort.
BAR = """  D0.visible = !1, b0.add(D0);
  let BRv = 0, BRt = 0, BRi = 0, BRit = 0, BRg = new ke, BRp = new ke, BL = 1.2, BD = .5, BH = 1.05, BC = .105;
  b0.add(BRg), BRp.visible = !1, BRg.add(BRp);
  let BRk = X(-BL / 2 + .022, BL / 2 - .022, BC, BH - .012, -BD / 2 + .022, BD / 2 - .022, O, 0, BRg, !1),
    BRb = Y0(M);
  for (let sz of [-1, 1]) {
    ue(-BL / 2, BL / 2, x => BRb.add(x, x + A0, BC, BH - .012, sz < 0 ? -BD / 2 : BD / 2 - .022, sz < 0 ? -BD / 2 + .022 : BD / 2, .43, (BH - .012 - BC) / 1.4, B0(), 6e-4, as() * .57, as()));
    ue(-BD / 2 + .022, BD / 2 - .022, z => BRb.add(sz < 0 ? -BL / 2 : BL / 2 - .022, sz < 0 ? -BL / 2 + .022 : BL / 2, BC, BH - .012, z, z + A0, .43, (BH - .012 - BC) / 1.4, B0(), 6e-4, as() * .57, as()));
    X(-BL / 2, BL / 2, BC, BH - .012, sz < 0 ? -BD / 2 : BD / 2 - .012, sz < 0 ? -BD / 2 + .012 : BD / 2, ee, .002, BRp);
    X(sz < 0 ? -BL / 2 : BL / 2 - .012, sz < 0 ? -BL / 2 + .012 : BL / 2, BC, BH - .012, -BD / 2 + .012, BD / 2 - .012, ee, .002, BRp);
  }
  let BRs = BRb.done(BRg);
  X(-BL / 2 - .025, BL / 2 + .025, BH - .012, BH, -BD / 2 - .025, BD / 2 + .025, G.stone, .002, BRg);
  X(-BL / 2 + .02, BL / 2 - .02, BC - .014, BC + .004, -BD / 2 + .02, BD / 2 - .02, G.frame, .003, BRg);
  {
    let pl = new U0(new Ns(.11, .055, .004, 2, .0015), [G.frame, G.frame, G.frame, G.frame, G.logo, G.frame]);
    pl.position.set(-BL / 2 - .002, BH - .09, BD / 2 - .12), pl.rotation.y = -Math.PI / 2, pl.castShadow = !0, BRg.add(pl);
  }
  for (let cx of [-1, 1])
    for (let cz of [-1, 1]) {
      let x = cx * (BL / 2 - .08), z = cz * (BD / 2 - .08);
      X(x - .03, x + .03, BC - .02, BC - .014, z - .03, z + .03, G.steel, .002, BRg);
      S0(.018, .018, .012, 20, G.steel, x, BC - .027, z, 0, 0, BRg);
      for (let fz of [-1, 1]) X(x - .02, x + .02, .03, BC - .033, z + fz * .0155, z + fz * .0185, G.steel, .001, BRg);
      S0(.0375, .0375, .024, 28, G.rubber, x, .0375, z, Math.PI / 2, 0, BRg);
      S0(.016, .016, .028, 20, G.steel, x, .0375, z, Math.PI / 2, 0, BRg);
    }

  function brApply() {
    let XR = j + .515, ZP = WF + .66, ZT = ZP - .46, ZS = -WB + .65, XT = XR - .135, XE = n0 - .7, ZIN = .595, LA = ZT - ZS, LB = .9,
      s = K1(BRv) * (LA + LB + XT - XE), x, z, yw;
    if (s < LA) x = XR, z = ZS + s, yw = Math.PI / 2;
    else if (s < LA + LB) {
      let u = (s - LA) / LB, uu = u * u * (3 - 2 * u);
      x = XR - .135 * uu, z = ZT + .46 * uu, yw = Math.PI / 2 * (1 - uu);
    } else x = XT - (s - LA - LB), z = ZP + (ZIN - ZP) * K1(BRi), yw = 0;
    BRg.visible = BRv > .002, BRg.position.set(x, .014, z), BRg.rotation.y = yw, k = !0;
  }
  brApply();"""
rep('  D0.visible = !1, b0.add(D0);', BAR)
rep('    for (let z of J) z.visible = !T;', '    for (let z of J) z.visible = !T;\n    BRs.visible = BRk.visible = !T, BRp.visible = T;')
rep('''      gaz: !0,
      store: !1
    },''', '''      gaz: !0,
      store: !1,
      bar: !1
    },''')
rep('T === "store" && (SBt = te.store ? 1 : 0)', 'T === "store" && (SBt = te.store ? 1 : 0), T === "bar" && (BRt = te.bar ? 1 : 0, BRit = te.bar && Vs ? 1 : 0, Vs && (BRv = BRi = te.bar ? 1 : 0, brApply()))')
rep('SB !== SBt && (SB = io(SB, SBt, z, .2), sbApply()), Yt) {', 'SB !== SBt && (SB = io(SB, SBt, z, .2), sbApply()), BRv !== BRt && (BRt > BRv || BRi === 0) && (BRv = io(BRv, BRt, z, .28), brApply()), BRi !== BRit && (BRit > BRi ? BRv === 1 : Ui === 0 || !te.bar) && (BRi = io(BRi, BRit, z, .45), brApply()), Yt) {')
rep('|| SB !== SBt) && ia(), (Ui !== Vs || us !== Ws || ds !== Xs || hs !== ks || SB !== SBt) && (k = !0)', '|| SB !== SBt || BRv !== BRt || BRi !== BRit) && ia(), (Ui !== Vs || us !== Ws || ds !== Xs || hs !== ks || SB !== SBt || BRv !== BRt || BRi !== BRit) && (k = !0)')
rep('SB = SBt, l2(), J1(), ec(), sbApply(), k = !0, ia()', 'SB = SBt, BRv = BRt, BRi = BRit, l2(), J1(), ec(), sbApply(), brApply(), k = !0, ia()')
rep('''        store: [''', '''        bar: [
          [-1.8, 1.9, 8.4],
          [.3, 1.05, 1.5]
        ],
        store: [''')
rep('Ui !== Vs && (Ui = io(Ui, Vs, z, .3), ec())', 'Ui !== Vs && (Vs < Ui || BRi >= BRit) && (Ui = io(Ui, Vs, z, .3), ec())')
rep('      Vs = T ? 1 : 0\n', '      Vs = T ? 1 : 0, BRit = te.bar && Vs ? 1 : 0\n')
