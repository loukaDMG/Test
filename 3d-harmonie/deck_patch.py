# ---------- Terrasse bois : 1 m devant et sur les deux côtés, dessus au niveau du plancher ----------
DECK = """  let ne = o0.done();
  {
    let DX = j + .03, DO = DX + 1, DZ0 = -WB - .033, DZ1 = WF + .011, DZ2 = DZ1 + 1, DG = .006,
      DC = () => new G0().setHSL(.08, .22, .66 + as() * .06),
      DF = () => new G0().setHSL(.08, .22, .6 + as() * .04),
      rows = (a, b, n, f) => {
        let p = (b - a) / n;
        for (let i = 0; i < n; i++) f(a + i * p + DG / 2, a + (i + 1) * p - DG / 2, i)
      };
    rows(DZ1, DZ2, 7, (z0, z1, i) => {
      let jx = i % 2 ? .9 : -.9;
      Q.add(-DO, jx - DG / 2, -.013, .014, z0, z1, (DO + jx) / 1.1, (z1 - z0) / 1.1, DC(), .002);
      Q.add(jx + DG / 2, DO, -.013, .014, z0, z1, (DO - jx) / 1.1, (z1 - z0) / 1.1, DC(), .002);
    });
    X(-DO, DO, -.15, -.013, DZ1, DZ2, G.black, 0, b0, !1);
    Q.add(-DO - .02, DO + .02, -.15, .014, DZ2, DZ2 + .02, (2 * DO) / 1.1, .164 / 1.1, DF(), .002);
    for (let sd of [-1, 1]) {
      let xa = sd < 0 ? -DO : DX, xb = sd < 0 ? -DX : DO;
      rows(DZ0, DZ1, 11, (z0, z1) => Q.add(xa, xb, -.013, .014, z0, z1, 1 / 1.1, (z1 - z0) / 1.1, DC(), .002));
      X(xa, xb, -.15, -.013, DZ0, DZ1, G.black, 0, b0, !1);
      Q.add(sd < 0 ? -DO - .02 : DO, sd < 0 ? -DO : DO + .02, -.15, .014, DZ0 - .02, DZ2, (DZ2 - DZ0) / 1.1, .164 / 1.1, DF(), .002);
      Q.add(sd < 0 ? -DO - .02 : DX, sd < 0 ? -DX : DO + .02, -.15, .014, DZ0 - .02, DZ0, 1 / 1.1, .164 / 1.1, DF(), .002);
    }
  }"""
rep('  let ne = o0.done();\n  Q.done();', DECK + '\n  Q.done();')
