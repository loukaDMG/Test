# ---------- Store banne intégré à la toiture + bande de lames au-dessus de l'ouverture ----------
SLATS = """  ue(-j + .02, j - .02, SX0 => o0.add(SX0, SX0 + A0, y0 + .012, a0 - .132, WF + .004, WF + .022, .43, (a0 - .144 - y0) / 1.4, B0(), 6e-4, as() * .57, as()));
  let ne = o0.done();"""
rep('  let ne = o0.done();', SLATS)
STORE = """
  let SB = 0, SBt = 0, SBg = new ke, SBP = 2.8, SBA = 0, SBW = 2 * j, SBY = a0 - .085, SBZ = WF + .06;
  b0.add(SBg);
  X(-j - .02, j + .02, a0 - .128, a0 - .008, WF - .05, WF + .075, G.frame, .006);
  X(-j - .02, j + .02, a0 - .132, a0 - .122, WF + .035, WF + .08, G.cap, .003);
  let SBM = new K0({ color: "#55585d", roughness: 1, metalness: 0, side: Mt, envMapIntensity: .6 }),
    SBf = new U0(new cn(1, 1), SBM);
  SBf.castShadow = !0, SBf.receiveShadow = !1, SBg.add(SBf);
  let SBb = X(-SBW / 2, SBW / 2, -.034, .034, -.045, .045, G.frame, .008, SBg),
    SBarms = [];
  for (let sd of [-1, 1]) {
    let au = X(-.022, .022, -.018, .018, 0, 1, G.frame, .006, SBg),
      av = X(-.018, .018, -.015, .015, 0, 1, G.frame, .006, SBg);
    au.rotation.order = av.rotation.order = "YXZ", SBarms.push({ s: sd, u: au, v: av });
  }
  let SBseg = (m, A, B) => {
    let dx = B[0] - A[0], dy = B[1] - A[1], dz = B[2] - A[2], L = Math.max(.001, Math.hypot(dx, dy, dz));
    m.position.set(A[0], A[1], A[2]), m.scale.z = L, m.rotation.y = Math.atan2(dx, dz), m.rotation.x = -Math.atan2(dy, Math.hypot(dx, dz));
  };
  function sbApply() {
    let e = K1(SB), L = Math.max(.001, SBP * e), dy = -Math.sin(SBA) * L, dz = Math.cos(SBA) * L, Fy = SBY + dy, Fz = SBZ + dz;
    SBg.visible = SB > .01;
    SBf.scale.set(SBW, L, 1), SBf.rotation.x = Math.PI / 2 + SBA, SBf.position.set(0, SBY + dy / 2, SBZ + dz / 2);
    SBb.position.set(0, Fy - .03, Fz);
    for (let R of SBarms) {
      let x0 = R.s * (j - .35), A = [x0, SBY - .035, SBZ - .02], B = [x0, Fy - .05, Fz - .02],
        half = Math.hypot(B[1] - A[1], B[2] - A[2]) / 2, ar = SBP / 2 + .03, e2 = Math.sqrt(Math.max(0, ar * ar - half * half)),
        E = [x0 - R.s * e2, (A[1] + B[1]) / 2, (A[2] + B[2]) / 2];
      SBseg(R.u, A, E), SBseg(R.v, E, B);
    }
    k = !0;
  }
  sbApply();
  let us = 0,"""
rep('  let us = 0,', STORE)
rep('''      friteuse: !0,
      gaz: !0
    },''', '''      friteuse: !0,
      gaz: !0,
      store: !1
    },''')
rep('T === "gaz" && (Gz.visible = te.gaz)', 'T === "gaz" && (Gz.visible = te.gaz), T === "store" && (SBt = te.store ? 1 : 0)')
rep('hs !== ks && (hs = io(hs, ks, z, .7), J1()), Yt) {', 'hs !== ks && (hs = io(hs, ks, z, .7), J1()), SB !== SBt && (SB = io(SB, SBt, z, .2), sbApply()), Yt) {')
rep('|| hs !== ks) && ia(), (Ui !== Vs || us !== Ws || ds !== Xs || hs !== ks) && (k = !0)', '|| hs !== ks || SB !== SBt) && ia(), (Ui !== Vs || us !== Ws || ds !== Xs || hs !== ks || SB !== SBt) && (k = !0)')
rep('us = Ws, ds = Xs, hs = ks, Ui = Vs, l2(), J1(), ec(), k = !0, ia()', 'us = Ws, ds = Xs, hs = ks, Ui = Vs, SB = SBt, l2(), J1(), ec(), sbApply(), k = !0, ia()')
rep('''        dedans: [''', '''        store: [
          [-6.4, 3.0, 9.4],
          [0, 1.5, 1.7]
        ],
        dedans: [''')
