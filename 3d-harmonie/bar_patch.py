# ---------- Bar sur roulettes (option) : lames bois comme le bardage, plateau noir, 4 roulettes ----------
# Il arrive en roulant depuis la droite et se gare devant la cuisine, sur le sol de la terrasse.
BAR = """  D0.visible = !1, b0.add(D0);
  let BRv = 0, BRt = 0, BRg = new ke, BRp = new ke, BL = 1.2, BD = .5, BH = 1.05, BC = .105, BXS = 5.5, BRz = WF + .6 + BD / 2;
  BRg.visible = !1, BRg.position.set(BXS, -.15, BRz), b0.add(BRg), BRp.visible = !1, BRg.add(BRp);
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
    let e = K1(BRv);
    BRg.visible = BRv > .002, BRg.position.x = BXS * (1 - e), k = !0;
  }"""
rep('  D0.visible = !1, b0.add(D0);', BAR)
rep('    for (let z of J) z.visible = !T;', '    for (let z of J) z.visible = !T;\n    BRs.visible = BRk.visible = !T, BRp.visible = T;')
rep('''      gaz: !0,
      store: !1
    },''', '''      gaz: !0,
      store: !1,
      bar: !1
    },''')
rep('T === "store" && (SBt = te.store ? 1 : 0)', 'T === "store" && (SBt = te.store ? 1 : 0), T === "bar" && (BRt = te.bar ? 1 : 0)')
rep('SB !== SBt && (SB = io(SB, SBt, z, .2), sbApply()), Yt) {', 'SB !== SBt && (SB = io(SB, SBt, z, .2), sbApply()), BRv !== BRt && (BRv = io(BRv, BRt, z, .28), brApply()), Yt) {')
rep('|| SB !== SBt) && ia(), (Ui !== Vs || us !== Ws || ds !== Xs || hs !== ks || SB !== SBt) && (k = !0)', '|| SB !== SBt || BRv !== BRt) && ia(), (Ui !== Vs || us !== Ws || ds !== Xs || hs !== ks || SB !== SBt || BRv !== BRt) && (k = !0)')
rep('SB = SBt, l2(), J1(), ec(), sbApply(), k = !0, ia()', 'SB = SBt, BRv = BRt, l2(), J1(), ec(), sbApply(), brApply(), k = !0, ia()')
rep('''        store: [''', '''        bar: [
          [-2.2, 1.9, 8.4],
          [-.1, 1.05, 1.5]
        ],
        store: [''')
