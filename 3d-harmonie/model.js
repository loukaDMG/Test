function u7(s, e = {}) {
  let t = new t1({
    canvas: s,
    antialias: !1,
    powerPreference: "high-performance"
  });
  t.outputColorSpace = yt, t.toneMapping = Va, t.shadowMap.enabled = !0, t.shadowMap.type = T1;
  let n = t.capabilities.getMaxAnisotropy(),
    i = new Ir;
  i.background = new G0(1, 1, 1);
  let r = new Pr(t);
  i.environment = r.fromScene(new F1, .04).texture, i.environmentIntensity = .7;

  function a(T, z) {
    let e0 = g0 => new Promise((_0, s0) => {
      let N0 = new Image;
      N0.onload = () => _0(N0), N0.onerror = s0, N0.src = g0
    });
    return Promise.all([e0(T), e0(z)]).then(([g0, _0]) => {
      let s0 = g0.width,
        N0 = g0.height,
        Q0 = We => {
          let me = document.createElement("canvas");
          me.width = s0, me.height = N0;
          let Je = me.getContext("2d");
          return Je.drawImage(We, 0, 0), Je.getImageData(0, 0, s0, N0).data
        },
        ve = Q0(g0),
        le = Q0(_0),
        X0 = new Float32Array(s0 * N0 * 4);
      for (let We = 0; We < N0; We++)
        for (let me = 0; me < s0; me++) {
          let Je = (We * s0 + me) * 4,
            vt = ((N0 - 1 - We) * s0 + me) * 4,
            xn = le[Je] / 255 * 16 / 255;
          X0[vt] = ve[Je] * xn, X0[vt + 1] = ve[Je + 1] * xn, X0[vt + 2] = ve[Je + 2] * xn, X0[vt + 3] = 1
        }
      let he = new $t(X0, s0, N0, gt, Wt);
      he.magFilter = he.minFilter = ct, he.needsUpdate = !0, he.mapping = Ma;
      let we = r.fromEquirectangular(he).texture;
      return he.dispose(), we
    })
  }
  let o = {
      studio: i.environment,
      garden: null
    },
    c = null;
  e.envRgb && e.envM && a(e.envRgb, e.envM).then(T => {
    o.studio = T, Ys()
  }).catch(() => {});
  let l = new Et(30, 16 / 9, .06, 320);
  l.position.set(-4.3, 1.55, 5.2);
  let h = new O1(l, s);
  h.target.set(0, 1.08, 0), h.enableDamping = !0, h.dampingFactor = .07, h.enablePan = !1, h.minDistance = 1, h.maxDistance = 11, h.maxPolarAngle = Math.PI * .495, h.autoRotate = !0, h.autoRotateSpeed = .55, h.rotateSpeed = .7;
  let u = new is("#fff4e6", 2.4);
  u.position.set(-4.5, 8, 3.5), u.castShadow = !0, u.shadow.mapSize.set(4096, 4096), Object.assign(u.shadow.camera, {
    left: -3.2,
    right: 3.2,
    top: 3.2,
    bottom: -3.2,
    near: 2,
    far: 22
  }), u.shadow.bias = -3e-4, u.shadow.normalBias = .012, u.shadow.radius = 5, i.add(u);
  let d = new is("#e8efff", .6);
  d.position.set(5, 4, -4), i.add(d);
  let f = new is("#ffffff", .35);
  f.position.set(.5, 2.5, 6), i.add(f), Y1.init();
  let g = new Ha("#fff7ee", 4, 2.6, 1.2);
  g.position.set(-.6, 2.1, 2.4), g.lookAt(0, 1.2, -.3), i.add(g);
  let b = new Ha("#eef3ff", 1.2, 1.6, 1.6);
  b.position.set(3.2, 1.6, 1.2), b.lookAt(0, 1, 0), i.add(b);
  let m = new U0(new cn(40, 40), new x1({
    opacity: .1,
    depthWrite: !1
  }));
  m.rotation.x = -Math.PI / 2, m.receiveShadow = !0, i.add(m);
  let p = 4.6,
    y = 3,
    x = 2.4,
    _ = new xt(1024, 1024);
  _.texture.generateMipmaps = !1;
  let D = new xt(1024, 1024);
  D.texture.generateMipmaps = !1;
  let C = new cn(p, y).rotateX(Math.PI / 2),
    R = new U0(C, new qt({
      map: _.texture,
      opacity: 1,
      transparent: !0,
      depthWrite: !1,
      toneMapped: !1
    }));
  R.renderOrder = 2, R.scale.y = -1, R.position.y = .003, i.add(R);
  let I = new U0(C);
  I.visible = !1, i.add(I);
  let q = new ei(-p / 2, p / 2, y / 2, -y / 2, 0, x);
  q.rotation.x = Math.PI / 2, i.add(q);
  let v = new Aa({
    side: Mt
  });
  v.customProgramCacheKey = () => "dmg-contact-shadow", v.onBeforeCompile = T => {
    T.fragmentShader = T.fragmentShader.replace("gl_FragColor = vec4( vec3( 1.0 - fragCoordZ ), opacity );", "gl_FragColor = vec4( vec3( 0.0 ), clamp( pow( 1.0 - fragCoordZ, 1.2 ) * 3.6, 0.0, 1.0 ) );")
  };
  let S = new Ke(Dh);
  S.depthTest = !1;
  let F = new Ke(Ih);
  F.depthTest = !1;

  function B(T) {
    I.visible = !0, I.material = S, S.uniforms.tDiffuse.value = _.texture, S.uniforms.h.value = T / 256, t.setRenderTarget(D), t.render(I, q), I.material = F, F.uniforms.tDiffuse.value = D.texture, F.uniforms.v.value = T / 256, t.setRenderTarget(_), t.render(I, q), I.visible = !1
  }
  let k = !0;

  function c0() {
    let T = i.background,
      z = t.getClearAlpha(),
      e0 = t.toneMapping,
      g0 = Pn.visible;
    Pn.visible = !1, R.visible = !1, m.visible = !1, i.background = null, i.overrideMaterial = v, t.setClearAlpha(0), t.toneMapping = Jn, t.setRenderTarget(_), t.clear(), t.render(i, q), i.overrideMaterial = null, B(11), B(6), B(3), B(1.2), t.setRenderTarget(null), t.setClearAlpha(z), t.toneMapping = e0, i.background = T, R.visible = !0, m.visible = ea !== "jardin" || !Pt, Pn.visible = g0, k = !1
  }
  let H = new Or;

  function r0(T, z) {
    if (!T) return null;
    let e0 = H.load(T);
    return e0.wrapS = e0.wrapT = Bt, e0.anisotropy = n, z && (e0.colorSpace = yt), e0
  }
  let Y = {
      pine: r0(e.pine, !0),
      pineN: r0(e.pineNor),
      pineR: r0(e.pineRough),
      slat: r0(e.slat, !0),
      slatN: r0(e.slatNor)
    },
    m0 = o2(7, 300, 2);
  m0.repeat.set(6, 6);
  let T0 = o2(11, 120, 0);
  T0.repeat.set(8, 8);
  let w0 = Lh(9),
    ce = Lh(3, 90),
    G = {
      frame: new xe({
        color: "#4d4f54",
        roughness: .5,
        metalness: .12,
        clearcoat: .25,
        clearcoatRoughness: .45,
        normalMap: m0,
        normalScale: new t0(.12, .12)
      }),
      cap: new K0({
        color: "#1d1e20",
        roughness: .6,
        metalness: .3
      }),
      black: new K0({
        color: "#1b1c1f",
        roughness: .78
      }),
      carcass: new K0({
        color: "#2c2d31",
        roughness: .65
      }),
      front: new xe({
        color: "#2b2d31",
        roughness: .55,
        metalness: .02,
        clearcoat: .1,
        clearcoatRoughness: .6,
        sheen: .2,
        sheenColor: "#555555"
      }),
      drawerSide: new K0({
        color: "#3a3c40",
        roughness: .4,
        metalness: .6
      }),
      stone: new xe({
        color: "#141517",
        roughness: .55,
        specularIntensity: .35,
        clearcoat: .08,
        clearcoatRoughness: .5,
        normalMap: T0,
        normalScale: new t0(.05, .05)
      }),
      steel: new xe({
        color: "#d6d9dc",
        metalness: 1,
        roughness: .3,
        roughnessMap: w0,
        anisotropy: .5
      }),
      steelPlate: new xe({
        color: "#b9bcc0",
        metalness: 1,
        roughness: .3,
        roughnessMap: ce,
        map: a7()
      }),
      groove: new K0({
        color: "#3a3b3d",
        metalness: .9,
        roughness: .55
      }),
      steelDark: new K0({
        color: "#6c6f73",
        metalness: 1,
        roughness: .45
      }),
      lidBlack: new xe({
        color: "#141516",
        roughness: .55,
        metalness: .1,
        clearcoat: .2,
        clearcoatRoughness: .45,
        normalMap: m0,
        normalScale: new t0(.08, .08)
      }),
      handle: new xe({
        color: "#d4d6d9",
        metalness: 1,
        roughness: .18,
        anisotropy: .6
      }),
      screw: new K0({
        color: "#3b3d41",
        metalness: .6,
        roughness: .4
      }),
      fabric: new K0({
        map: o7(),
        roughness: .92,
        side: Mt
      }),
      rubber: new K0({
        color: "#111111",
        roughness: .9
      }),
      hole: new qt({
        color: "#050505"
      }),
      lamp: new K0({
        color: "#fff4de",
        emissive: "#ffe2b0",
        emissiveIntensity: 3
      }),
      led: new K0({
        color: "#ff7a1a",
        emissive: "#ff6a00",
        emissiveIntensity: 1.5
      }),
      knob: new xe({
        color: "#141414",
        roughness: .45,
        clearcoat: .3
      }),
      scale: new K0({
        map: h7(),
        transparent: !0,
        roughness: .5,
        depthWrite: !1
      }),
      badge: new K0({
        map: l7(),
        roughness: .4
      }),
      pan: new xe({
        color: "#1b1b1c",
        roughness: .35,
        metalness: .5,
        clearcoat: .3
      }),
      ceramic: new xe({
        color: "#f6f5f2",
        roughness: .12,
        clearcoat: 1
      }),
      petal: new xe({
        color: "#fbf8fb",
        roughness: .5,
        sheen: 1,
        sheenColor: "#ffffff",
        side: Mt
      }),
      lip: new K0({
        color: "#d9a6c6",
        roughness: .5
      }),
      stem: new K0({
        color: "#4f5a2e",
        roughness: .7
      }),
      leaf: new xe({
        color: "#2f5a26",
        roughness: .35,
        clearcoat: .5,
        side: Mt
      }),
      socket: new K0({
        color: "#232427",
        roughness: .45
      }),
      logo: new xe({
        map: c7(),
        metalness: .6,
        roughness: .3
      })
    },
    Z = new K0({
      map: Y.slat,
      normalMap: Y.slatN,
      roughness: .5,
      vertexColors: !0
    });
  Z.normalScale.set(.6, .6);
  let d0 = new K0({
    map: Y.pine,
    normalMap: Y.pineN,
    roughnessMap: Y.pineR,
    roughness: 1,
    vertexColors: !0
  });
  d0.normalScale.set(.6, .6), Y.slat || Z.color.set("#c27a45"), Y.pine || d0.color.set("#9a6842");
  let b0 = new ke;
  i.add(b0);

  function p0(T, z, e0, g0, _0, s0, N0) {
    let Q0 = z - T,
      ve = g0 - e0,
      le = s0 - _0,
      X0 = Math.min(N0, Q0 / 2.2, ve / 2.2, le / 2.2),
      he = X0 > 6e-4 ? new Ns(Q0, ve, le, 3, X0) : new bn(Q0, ve, le);
    return he.translate((T + z) / 2, (e0 + g0) / 2, (_0 + s0) / 2), he
  }

  function X(T, z, e0, g0, _0, s0, N0, Q0 = .004, ve = b0, le = !0) {
    let X0 = new U0(p0(T, z, e0, g0, _0, s0, Q0), N0);
    return X0.castShadow = le, X0.receiveShadow = !0, ve.add(X0), X0
  }

  function S0(T, z, e0, g0, _0, s0, N0, Q0, ve = 0, le = 0, X0 = b0) {
    let he = new U0(new en(T, z, e0, g0), _0);
    return he.position.set(s0, N0, Q0), he.rotation.set(ve, 0, le), he.castShadow = !0, he.receiveShadow = !0, X0.add(he), he
  }

  function Y0(T) {
    let z = [];
    return {
      add(e0, g0, _0, s0, N0, Q0, ve, le, X0, he = .002, we, We) {
        let me = p0(e0, g0, _0, s0, N0, Q0, he).toNonIndexed ? p0(e0, g0, _0, s0, N0, Q0, he) : null,
          Je = me.attributes.uv,
          vt = we ?? as(),
          xn = We ?? as();
        for (let nt = 0; nt < Je.count; nt++) Je.setXY(nt, Je.getX(nt) * ve + vt, Je.getY(nt) * le + xn);
        let Ot = new Float32Array(me.attributes.position.count * 3);
        for (let nt = 0; nt < Ot.length; nt += 3) Ot[nt] = X0.r, Ot[nt + 1] = X0.g, Ot[nt + 2] = X0.b;
        me.setAttribute("color", new dt(Ot, 3)), z.push(me.index ? me.toNonIndexed() : me)
      },
      done(e0 = b0) {
        if (!z.length) return;
        let g0 = new U0(Vr(z), T);
        return g0.castShadow = g0.receiveShadow = !0, e0.add(g0), g0
      }
    }
  }
  let te = {
      plancha: !0,
      evier: !0,
      frigo: !0
    },
    j = 1.25,
    w = .4,
    a0 = 2.2,
    n0 = 1.085,
    l0 = -.36,
    i0 = .95,
    F0 = 1.24,
    y0 = 1.975,
    A = {};
  for (let T of ["teak", "cedar", "ipe", "darkgrey"]) {
    let z = e.weo && e.weo[T];
    A[T] = z ? {
      d: r0(z.d, !0),
      n: r0(z.n)
    } : null
  }
  let M = new xe({
    map: A.teak?.d || null,
    normalMap: A.teak?.n || null,
    roughness: .62,
    vertexColors: !0,
    clearcoat: .08,
    clearcoatRoughness: .6
  });
  M.normalScale.set(.22, .22);
  let O = new K0({
      roughness: .8,
      color: new G0(.45, .45, .45)
    }),
    J = [],
    o0 = Y0(M),
    Q = Y0(d0),
    B0 = () => {
      let T = .97 + as() * .03;
      return new G0(T, T, T)
    },
    M0 = .07,
    A0 = .062;

  function ue(T, z, e0) {
    let g0 = Math.floor((z - T - A0) / M0) + 1,
      _0 = (z - T - ((g0 - 1) * M0 + A0)) / 2;
    for (let s0 = 0; s0 < g0; s0++) e0(T + _0 + s0 * M0)
  }
  for (let T of [-1, 1]) {
    X(T < 0 ? -j : n0, T < 0 ? -n0 : j, .008, a0, -w, w, G.frame, .005);
    let z = T < 0 ? -j - .022 : j,
      e0 = T < 0 ? -j : j + .022;
    X(z, e0, .008, a0, w - .045, w, G.frame, .003), X(z, e0, .008, a0, -w - .022, -w + .045, G.frame, .003), X(z, e0, a0 - .05, a0, -w + .045, w - .045, G.frame, .003), J.push(X(T < 0 ? -j - .017 : j, T < 0 ? -j : j + .017, .025, a0 - .055, -w + .045, w - .045, O, 0, b0, !1)), ue(-w + .048, w - .048, g0 => o0.add(T < 0 ? -j - .02 : j + .016, T < 0 ? -j - .016 : j + .02, .025, a0 - .055, g0, g0 + A0, .43, (a0 - .08) / 1.4, B0(), 6e-4, as() * .57, as()));
    for (let g0 of [-w + .06, w - .06]) S0(.022, .026, .008, 24, G.rubber, T * (j - .08), .004, g0);
    for (let g0 of [.18, .62, 1.06, 1.5, 1.94]) S0(.0055, .0055, .004, 20, G.screw, T * (j - .035), g0, w + .002, Math.PI / 2)
  }
  X(-j, -j + .045, .008, a0, -w - .022, -w, G.frame, .003), X(j - .045, j, .008, a0, -w - .022, -w, G.frame, .003), X(-j + .045, j - .045, a0 - .05, a0, -w - .022, -w, G.frame, .003), J.push(X(-j + .045, j - .045, .025, a0 - .055, -w - .017, -w, O, 0, b0, !1)), ue(-j + .048, j - .048, T => o0.add(T, T + A0, .025, a0 - .055, -w - .02, -w - .016, .43, (a0 - .08) / 1.4, B0(), 6e-4, as() * .57, as()));
  for (let T of [.18, .62, 1.06, 1.5, 1.94])
    for (let z of [-1, 1]) S0(.0055, .0055, .004, 20, G.screw, z * (j - .022), T, -w - .024, Math.PI / 2);
  X(-j - .024, j + .024, a0, a0 + .075, -w - .027, w + .005, G.frame, .004), X(-j - .034, j + .034, a0 + .075, a0 + .09, -w - .04, w + .018, G.cap, .003), X(-j - .034, j + .034, a0 + .05, a0 + .09, w + .012, w + .018, G.cap, .002), X(-.07, .07, a0 + .09, a0 + .13, .05, .16, G.cap, .008), X(-.05, .05, a0 + .1, a0 + .12, .16, .162, G.steel, .002), X(-n0, n0, y0 + .005, a0, .3, w, G.frame, .004);
  for (let T of [-1, 1]) S0(.0055, .0055, .004, 20, G.screw, T * (n0 - .06), 2.1, w + .002, Math.PI / 2);
  let f0 = new U0(new Ns(.11, .055, .004, 2, .0015), [G.frame, G.frame, G.frame, G.frame, G.logo, G.frame]);
  f0.position.set(n0 - .1, 2.12, w + .002), f0.castShadow = !0, b0.add(f0), X(-n0, n0, y0 - .005, a0, l0, .3, G.black, 0, b0, !0), X(-n0 + .01, n0 - .01, y0 - .06, y0, .23, .33, G.frame, .01), X(-n0, n0, .008, a0, -w, l0, G.black, 0);

  function R0(T, z, e0, g0, _0, s0, N0) {
    let le = g0;
    for (; le - e0 > .02;) {
      let X0 = Math.max(e0, le - .118),
        he = Math.abs(z - T),
        we = new G0().setHSL(.07, .2, .9 + as() * .14);
      N0 === "z" ? Q.add(_0, _0 + s0, X0 + .003 / 2, le - .003 / 2, Math.min(T, z), Math.max(T, z), he / 1.1, (le - X0) / 1.1, we, .0025) : Q.add(T, z, X0 + .003 / 2, le - .003 / 2, _0, _0 + s0, he / 1.1, (le - X0) / 1.1, we, .0025), le = X0
    }
  }
  R0(-n0, -.49, F0, y0, l0, .018), R0(.51, n0, F0, y0, l0, .018), X(-n0, n0, i0, y0, l0, l0 + .008, G.black, 0), R0(l0 + .018, .29, F0, y0, -n0, .016, "z"), R0(l0 + .018, .29, F0, y0, n0 - .016, .016, "z"), X(-n0, -n0 + .012, i0, F0, l0 + .008, .29, G.black, 0), X(n0 - .012, n0, i0, F0, l0 + .008, .29, G.black, 0);
  let ne = o0.done();
  Q.done();
  let ee = new xe({
      color: "#33353a",
      roughness: .42,
      metalness: .05,
      clearcoat: .35,
      clearcoatRoughness: .35
    }),
    D0 = new ke;
  D0.visible = !1, b0.add(D0);
  for (let T of [-1, 1]) X(T < 0 ? -j - .02 : j + .004, T < 0 ? -j - .004 : j + .02, .025, a0 - .055, -w + .05, w - .05, ee, .002, D0);
  {
    let T = [-j + .05, -.0015, .0015, j - .05];
    X(T[0], T[1], .025, a0 - .055, -w - .02, -w - .004, ee, .002, D0), X(T[2], T[3], .025, a0 - .055, -w - .02, -w - .004, ee, .002, D0)
  }
  let Ee = {
      teak: 1,
      cedar: 1,
      ipe: 1,
      darkgrey: 1
    },
    Z0 = (T, z, e0) => new G0(T, z, e0),
    De = {
      studio: {
        teak: Z0(.844, .895, .953),
        cedar: Z0(.842, .889, .922),
        ipe: Z0(.867, .948, 1.023),
        darkgrey: Z0(.824, .876, .893)
      },
      jardin: {
        teak: Z0(.844, .895, .953),
        cedar: Z0(.842, .889, .922),
        ipe: Z0(.867, .948, 1.023),
        darkgrey: Z0(.824, .876, .893)
      }
    },
    L = "studio",
    C0 = new Proxy({}, {
      get: (T, z) => De[L][z]
    }),
    K = {
      teak: "#8a7155",
      cedar: "#dfbc8b",
      ipe: "#674a38",
      darkgrey: "#686460"
    },
    $ = "teak";

  function P0() {
    let T = $ === "fundermax";
    D0.visible = T, ne && (ne.visible = !T);
    for (let z of J) z.visible = !T;
    if (!T) {
      let z = A[$];
      if (z && z.d) {
        M.map = z.d, M.normalMap = z.n, M.color.copy(C0[$]);
        let e0 = z.d.clone();
        e0.repeat.set(.3, 1), e0.needsUpdate = !0, O.map = e0, O.color.copy(C0[$]).multiplyScalar(.62)
      } else M.map = null, M.color.set(K[$]), O.map = null, O.color.set(K[$]).multiplyScalar(.5);
      M.needsUpdate = !0, O.needsUpdate = !0
    }
  }
  P0(), X(-.9, -.745, 1.07, 1.155, l0 + .008, l0 + .02, G.socket, .006);
  for (let T of [-.861, -.784]) S0(.024, .024, .006, 32, G.black, T, 1.1125, l0 + .022, Math.PI / 2);
  S0(.034, .034, .008, 40, G.steel, -.04, y0 - .006, -.04), S0(.026, .026, .004, 40, G.lamp, -.04, y0 - .011, -.04);
  let I0 = new Br("#ffd9a3", 7, 1.12, Math.PI / 2.8, .9, 1.4);
  I0.position.set(-.04, y0 - .02, -.04), I0.target.position.set(-.04, i0, -.12), b0.add(I0, I0.target);
  let fe = .11,
    Te = .91,
    ut = .265,
    pe = .018,
    Ve = l0 + .004;
  X(-1.07, -1.07 + pe, fe, Te, Ve, ut, G.carcass, .001), X(1.07 - pe, 1.07, fe, Te, Ve, ut, G.carcass, .001), X(-1.07, 1.07, fe, fe + pe, Ve, ut, G.carcass, .001), X(-1.07, 1.07, fe, Te, Ve, Ve + .01, G.carcass, 0), X(-1.07, 1.07, Te - pe, Te, Ve, -.28, G.carcass, .001), X(-1.07, 1.07, Te - pe, Te, .256, ut, G.carcass, .001), X(-1.07, -.905, Te - pe, Te, -.28, .256, G.carcass, .001), X(-.535, 1.07, Te - pe, Te, -.28, .256, G.carcass, .001);
  for (let T of [-.415, .44]) X(T - pe / 2, T + pe / 2, fe, Te, Ve, ut, G.carcass, .001);
  X(-1.052, -.424, .5, .518, Ve + .03, ut - .03, G.carcass, .001), X(-1.04, 1.04, .01, fe, -.3, .2, G.black, 0, b0, !1);
  for (let T of [-.95, .95])
    for (let z of [-.25, .15]) S0(.015, .018, .1, 16, G.rubber, T, .06, z);
  let zt = .265,
    Di = .285,
    ii = .0035;

  function Vn(T, z, e0, g0, _0) {
    let s0 = new ke;
    S0(.006, .006, g0, 32, G.handle, 0, 0, 0, 0, 0, s0);
    for (let N0 of [-1, 1]) {
      S0(.0048, .0048, .028, 20, G.handle, 0, N0 * (g0 / 2 - .011), -.014, Math.PI / 2, 0, s0);
      let Q0 = new U0(new Ps(.006, 20, 10, 0, Math.PI * 2, 0, Math.PI / 2), G.handle);
      Q0.position.y = N0 * g0 / 2, N0 < 0 && (Q0.rotation.x = Math.PI), s0.add(Q0)
    }
    _0 || (s0.rotation.z = Math.PI / 2), s0.position.set(z, e0, Di + .028), T.add(s0)
  }
  let Fs = [];
  for (let T of [-1, 1]) {
    let z = T < 0 ? -1.068 : 1.068,
      e0 = T < 0 ? -.415 - ii / 2 : .44 + ii / 2,
      g0 = new ke;
    g0.position.set(z, 0, Di), b0.add(g0);
    let _0 = new ke;
    _0.position.set(-z, 0, -Di), g0.add(_0), X(Math.min(z, e0), Math.max(z, e0), .112, .908, zt, Di, G.front, .0025, _0), Vn(_0, T < 0 ? -.45 : .475, .8, .128, !0);
    for (let s0 of [.2, .82]) X(T < 0 ? z + .02 : z - .07, T < 0 ? z + .07 : z - .02, s0 - .02, s0 + .02, zt - .012, zt, G.drawerSide, .003, _0);
    Fs.push({
      pivot: g0,
      s: T
    })
  }
  let jr = [],
    eo = [
      [.112, .376, .2],
      [.376, .642, .17],
      [.642, .908, .07]
    ],
    os = -.415 + ii / 2,
    Yr = .44 - ii / 2;
  eo.forEach(([T, z, e0], g0) => {
    let _0 = new ke;
    if (b0.add(_0), X(os, Yr, T + ii / 2, z - ii / 2, zt, Di, G.front, .0025, _0), g0 < 2 && Vn(_0, .0125, z - .042, .128, !1), g0 === 2) return;
    let s0 = os + .02,
      N0 = Yr - .02,
      Q0 = T + .03,
      ve = T + .03 + e0,
      le = zt - .5,
      X0 = zt;
    X(s0, s0 + .014, Q0, ve, le, X0, G.drawerSide, .004, _0), X(N0 - .014, N0, Q0, ve, le, X0, G.drawerSide, .004, _0), X(s0, N0, Q0, Q0 + .012, le, X0, G.carcass, .001, _0), X(s0, N0, Q0, ve - .01, le, le + .014, G.drawerSide, .002, _0), jr.push({
      g: _0,
      delay: (2 - g0) * .12,
      travel: .42 - g0 * .02
    })
  });
  let cs = X(.449, 1.052, .5, .518, Ve + .03, ut - .03, G.carcass, .001);
  cs.visible = !1;
  let Kr, Zr;
  {
    let T = new ke;
    b0.add(T), Kr = T;
    let z = .452,
      e0 = 1.049,
      g0 = .131,
      _0 = .889,
      s0 = -.33,
      N0 = .245,
      Q0 = z + .025,
      ve = e0 - .025,
      le = g0 + .095,
      X0 = _0 - .04,
      he = s0 + .015,
      we = N0 - .035,
      We = new K0({
        color: "#c9ccd0",
        roughness: .35,
        metalness: .55
      }),
      me = new xe({
        color: "#141517",
        roughness: .35,
        metalness: .4,
        clearcoat: .4
      }),
      Je = new K0({
        color: "#e4e6e8",
        roughness: .15,
        metalness: 1
      }),
      vt = new xe({
        color: "#0e1114",
        roughness: .04,
        metalness: 0,
        transparent: !0,
        opacity: .38,
        clearcoat: 1,
        clearcoatRoughness: .03,
        depthWrite: !1
      }),
      xn = new K0({
        color: "#ffffff",
        emissive: "#dfeaff",
        emissiveIntensity: 2.6
      });
    X(z, z + .02, g0, _0, s0, N0 - .03, me, .002, T), X(e0 - .02, e0, g0, _0, s0, N0 - .03, me, .002, T), X(z, e0, _0 - .02, _0, s0, N0 - .03, me, .002, T), X(z, e0, g0, le, s0, N0 - .03, me, .002, T), X(Q0 - .005, ve + .005, le - .005, X0 + .005, s0, he, We, 0, T), X(Q0 - .005, Q0, le, X0, he, we, We, 0, T), X(ve, ve + .005, le, X0, he, we, We, 0, T), X(Q0, ve, X0, X0 + .005, he, we, We, 0, T), X(Q0, ve, le - .005, le, he, we, We, 0, T);
    for (let O0 of [.42, .62])
      for (let J0 of [Q0, ve - .006]) X(J0, J0 + .006, O0 - .012, O0 - .004, he, we - .02, We, .002, T);
    X(z + .003, e0 - .003, g0 + .003, g0 + .075, N0 - .03, N0 - .012, me, .003, T);
    let Ot = [];
    for (let O0 = z + .04; O0 < e0 - .05; O0 += .022) Ot.push(p0(O0, O0 + .012, g0 + .02, g0 + .058, N0 - .0125, N0 - .0115, 0));
    T.add(new U0(Vr(Ot), G.hole));
    let nt = N0 - .03,
      Fe = g0 + .078,
      Ne = _0 - .003,
      $0 = z + .003,
      q0 = e0 - .003,
      vn = .032;
    X($0, q0, Ne - vn, Ne, nt, N0, me, .003, T), X($0, q0, Fe, Fe + vn, nt, N0, me, .003, T), X($0, $0 + vn, Fe, Ne, nt, N0, me, .003, T), X(q0 - vn, q0, Fe, Ne, nt, N0, me, .003, T);
    let Oi = new U0(new bn(q0 - $0 - 2 * vn + .004, Ne - Fe - 2 * vn + .004, .004), vt);
    Oi.position.set(($0 + q0) / 2, (Fe + Ne) / 2, N0 - .012), T.add(Oi), X($0 + .008, $0 + .02, Fe + .12, Ne - .12, N0, N0 + .012, Je, .003, T), X($0 + .008, $0 + .02, Fe + .12, Ne - .12, N0 + .009, N0 + .012, G.handle, .002, T);
    let pt = Cn(256, 64, O0 => {
        O0.fillStyle = "#05070a", O0.fillRect(0, 0, 256, 64), O0.fillStyle = "#8fd0ff", O0.font = "600 40px Arial, sans-serif", O0.textAlign = "right", O0.fillText("4\xB0C", 236, 46), O0.strokeStyle = "#8fd0ff", O0.lineWidth = 3, O0.beginPath(), O0.arc(34, 32, 12, 0, Math.PI * 2), O0.stroke(), O0.beginPath(), O0.moveTo(34, 20), O0.lineTo(34, 30), O0.stroke()
      }),
      Ht = new U0(new cn(.08, .02), new K0({
        map: pt,
        emissive: "#ffffff",
        emissiveMap: pt,
        emissiveIntensity: .9,
        roughness: .2
      }));
    Ht.position.set(q0 - .075, Ne - vn / 2, N0 + 6e-4), T.add(Ht), X(Q0 + .03, ve - .03, X0 - .012, X0 - .004, we - .05, we - .03, xn, .002, T, !1);
    let sn = new Ri("#e9f1ff", .9, .9, 2);
    sn.position.set((Q0 + ve) / 2, X0 - .05, (he + we) / 2 + .05), T.add(sn);
    let jn = [];
    for (let O0 of [.42, .62]) {
      for (let J0 = Q0 + .015; J0 < ve - .01; J0 += .024) jn.push(p0(J0, J0 + .004, O0 - .004, O0, he + .01, we - .02, 0));
      for (let J0 of [he + .012, (he + we) / 2, we - .025]) jn.push(p0(Q0 + .004, ve - .004, O0 - .006, O0 - .002, J0, J0 + .006, 0))
    }
    let Kt = new U0(Vr(jn), Je);
    Kt.castShadow = Kt.receiveShadow = !0, T.add(Kt);
    let Qe = new xe({
        color: "#2f5d2b",
        roughness: .06,
        transparent: !0,
        opacity: .8,
        clearcoat: 1
      }),
      gs = new xe({
        color: "#5a3415",
        roughness: .06,
        transparent: !0,
        opacity: .85,
        clearcoat: 1
      }),
      In = new xe({
        color: "#e7a08f",
        roughness: .05,
        transparent: !0,
        opacity: .7,
        clearcoat: 1
      }),
      it = new K0({
        color: "#c8a24a",
        roughness: .3,
        metalness: 1
      }),
      $e = new K0({
        color: "#f1ece2",
        roughness: .6
      }),
      Fi = new K0({
        color: "#1d2433",
        roughness: .5
      }),
      un = O0 => new Ur(O0.map(J0 => new t0(J0[0], J0[1])), 32),
      _e = un([
        [0, 0],
        [.026, 0],
        [.027, .004],
        [.027, .1],
        [.022, .124],
        [.012, .146],
        [.0105, .168],
        [.0115, .17],
        [.0115, .176],
        [0, .176]
      ]),
      st = un([
        [0, 0],
        [.036, 0],
        [.037, .004],
        [.037, .19],
        [.03, .222],
        [.016, .246],
        [.0145, .29],
        [.0155, .292],
        [.0155, .3],
        [0, .3]
      ]),
      Re = (O0, J0, ae, rt, Ln, Yn = 0, rc = 0) => {
        let oi = new U0(O0, J0);
        return oi.position.set(ae, rt, Ln), oi.rotation.set(Yn, 0, rc), oi.castShadow = !0, T.add(oi), oi
      };
    ["#b3121b", "#c9ccd1", "#1f4fa0", "#b3121b", "#e3b023", "#c9ccd1"].forEach((O0, J0) => {
      let ae = new K0({
          color: O0,
          roughness: .25,
          metalness: .85
        }),
        rt = Q0 + .06 + J0 % 3 * .075 + (J0 > 2 ? .035 : 0),
        Ln = J0 > 2 ? we - .08 : he + .12;
      Re(new en(.033, .033, .115, 32), ae, rt, le + .0575, Ln), Re(new en(.028, .033, .008, 32), G.steelDark, rt, le + .119, Ln)
    });
    for (let O0 = 0; O0 < 3; O0++) Re(_e, O0 % 2 ? gs : Qe, ve - .17 + O0 * .06, le, we - .07 - O0 % 2 * .05);
    for (let O0 = 0; O0 < 6; O0++) {
      let J0 = Q0 + .05 + O0 * .085,
        ae = we - .07 - O0 % 2 * .06,
        rt = O0 % 3 === 1 ? gs : Qe;
      Re(_e, rt, J0, .42, ae), Re(new en(.0275, .0275, .05, 32, 1, !0), O0 % 2 ? Fi : $e, J0, .42 + .05, ae), Re(new en(.013, .013, .008, 20), it, J0, .42 + .179, ae)
    } [
      [Q0 + .07, Qe],
      [Q0 + .155, In],
      [Q0 + .24, Qe],
      [ve - .12, In]
    ].forEach(([O0, J0], ae) => {
      let Ln = he + .06;
      Re(st, J0, O0, .657, Ln, Math.PI / 2);
      let Yn = Re(new en(.0375, .0375, .09, 32, 1, !0), ae % 2 ? $e : Fi, O0, .657, Ln + .11, Math.PI / 2);
      Re(new en(.0165, .0165, .05, 20), ae % 2 ? it : G.steelDark, O0, .657, Ln + .28, Math.PI / 2)
    })
  }
  let Jr = .73,
    Qr = .56,
    si = .0125,
    E = -.012,
    N = si - Jr / 2,
    V = si + Jr / 2,
    W = E - Qr / 2,
    U = E + Qr / 2,
    v0 = N + .012,
    L0 = V - .012,
    z0 = W + .012,
    H0 = U - .012,
    j0 = -.72,
    re = .185,
    k0 = new ke;
  b0.add(k0);

  function Le() {
    for (let e0 of [...k0.children]) k0.remove(e0), e0.geometry.dispose();
    let T = [];
    if (te.evier && T.push([j0 - re, j0 + re]), te.plancha && T.push([v0, L0]), !T.length) {
      X(-n0, n0, Te, i0, l0 + .008, .305, G.stone, .003, k0);
      return
    }
    X(-n0, n0, Te, i0, l0 + .008, z0, G.stone, .002, k0), X(-n0, n0, Te, i0, H0, .305, G.stone, .003, k0);
    let z = -n0;
    for (let [e0, g0] of T) X(z, e0, Te, i0, z0, H0, G.stone, .001, k0), z = g0;
    X(z, n0, Te, i0, z0, H0, G.stone, .001, k0)
  }
  Le();
  let ie = new ke;
  b0.add(ie);
  let se = i0 + .006;
  X(v0 + .005, L0 - .005, i0 - .2, i0 - .032, z0 + .005, H0 - .005, G.steelDark, .004, ie, !1);
  let kt = .1,
    Ue = .06,
    V0 = .1,
    Oe = N + kt,
    de = V - kt,
    Ze = W + Ue,
    Ct = U - V0;
  X(N, V, i0, se, W, Ze, G.steel, .003, ie), X(N, V, i0, se, Ct, U, G.steel, .003, ie), X(N, Oe, i0, se, Ze, Ct, G.steel, .002, ie), X(de, V, i0, se, Ze, Ct, G.steel, .002, ie);
  let ft = .03;
  X(Oe, Oe + .004, se - ft, se - 5e-4, Ze, Ct, G.steelDark, .001, ie), X(de - .004, de, se - ft, se - 5e-4, Ze, Ct, G.steelDark, .001, ie), X(Oe, de, se - ft, se - 5e-4, Ct - .004, Ct, G.steelDark, .001, ie), X(Oe, de, se - ft, se - 5e-4, Ze, Ze + .004, G.steelDark, .001, ie);
  let Bs = X(Oe + .004, de - .004, se - ft - .005, se - ft + .001, Ze + .004, Ct - .004, G.steelPlate, .0015, ie),
    tt = Bs.geometry.attributes.position,
    Wn = Bs.geometry.attributes.uv;
  for (let T = 0; T < tt.count; T++) Wn.setXY(T, (tt.getX(T) - Oe) / (de - Oe), (tt.getZ(T) - Ze) / (Ct - Ze));
  let Xn = se - ft + .001,
    jt = [];
  for (let T = Oe + .018; T < (Oe + de) / 2 - .012; T += .016) jt.push(p0(T, T + .007, Xn, Xn + .006, Ze + .025, Ct - .03, .0025));
  let zs = [];
  for (let T = Oe + .025; T < (Oe + de) / 2 - .012; T += .016) zs.push(p0(T, T + .009, Xn, Xn + 8e-4, Ze + .025, Ct - .03, 0));
  ie.add(new U0(Vr(zs), G.groove));
  let $r = new U0(Vr(jt), G.steelPlate);
  $r.castShadow = $r.receiveShadow = !0, ie.add($r), X(Oe + .01, de - .01, Xn - 5e-4, Xn, Ze + .006, Ze + .02, G.steelDark, 0, ie, !1);
  for (let T = Oe + .03; T < de - .03; T += .022) X(T, T + .012, se - 5e-4, se + 3e-4, W + .02, W + .04, G.hole, 0, ie, !1);
  for (let T of [si - .17, si + .17]) {
    let z = U - V0 / 2,
      e0 = new U0(new Na(.036, 48), G.scale);
    e0.rotation.x = -Math.PI / 2, e0.position.set(T, se + 6e-4, z), ie.add(e0);
    let g0 = [
        [0, 0],
        [.024, 0],
        [.024, .004],
        [.021, .006],
        [.02, .022],
        [.018, .025],
        [0, .026]
      ].map(N0 => new t0(N0[0], N0[1])),
      _0 = new U0(new Ur(g0, 48), G.knob);
    _0.position.set(T, se, z), _0.castShadow = !0, ie.add(_0);
    let s0 = new U0(new Ba(.0205, .0012, 10, 48), G.handle);
    s0.rotation.x = Math.PI / 2, s0.position.set(T, se + .02, z), ie.add(s0), X(T - .003, T + .003, se + .026, se + .031, z - .017, z + .017, G.knob, .002, ie), X(T - .0012, T + .0012, se + .031, se + .0315, z + .006, z + .016, G.handle, 0, ie, !1)
  }
  S0(.009, .009, .006, 32, G.handle, si, se + .003, U - V0 / 2, 0, 0, ie), S0(.003, .003, .002, 16, G.led, si + .05, se + .001, U - V0 / 2, 0, 0, ie);
  let Ii = new ke;
  Ii.position.set(si, se + .002, W - .004), ie.add(Ii);
  let hn = Jr + .01,
    ls = Qr + .008,
    Li = .05,
    ri = .004,
    Ni = new ke;
  Ii.add(Ni), X(-hn / 2, hn / 2, Li - ri, Li, 0, ls, G.lidBlack, .0035, Ni), X(-hn / 2, -hn / 2 + ri, .004, Li - .001, 0, ls, G.lidBlack, .0015, Ni), X(hn / 2 - ri, hn / 2, .004, Li - .001, 0, ls, G.lidBlack, .0015, Ni), X(-hn / 2, hn / 2, .004, Li - .001, ls - ri, ls, G.lidBlack, .0015, Ni), X(-hn / 2 + ri, hn / 2 - ri, Li - ri - .0015, Li - ri, .004, ls - ri, G.lidBlack, 0, Ni, !1);
  let Z1 = new U0(new cn(.028, .028), G.badge);
  Z1.rotation.x = -Math.PI / 2, Z1.position.set(hn / 2 - .035, Li + 4e-4, ls - .035), Ni.add(Z1);
  for (let T of [-hn / 2 + .07, hn / 2 - .07]) S0(.006, .006, .05, 24, G.handle, T, .006, 0, 0, Math.PI / 2, Ii), X(T - .02, T + .02, -.004, .012, -.012, .002, G.handle, .002, Ii);
  let hs = 1,
    ks = 1;

  function J1() {
    Ni.rotation.x = -Math.PI / 2 * K1(hs) * .98
  }
  J1();
  {
    let T = new ke;
    b0.add(T), Zr = T;
    let z = new xe({
        color: "#d2d5d8",
        metalness: 1,
        roughness: .8,
        roughnessMap: w0,
        anisotropy: .35,
        side: Mt
      }),
      e0 = new xe({
        color: "#dcdee1",
        metalness: 1,
        roughness: .34,
        anisotropy: .3
      }),
      g0 = new xe({
        color: "#c3c6ca",
        metalness: 1,
        roughness: .85,
        roughnessMap: ce,
        side: Mt
      }),
      _0 = new K0({
        color: "#8b8e92",
        roughness: .5
      }),
      s0 = new K0({
        color: "#b9bcc0",
        roughness: .45,
        metalness: .8
      }),
      N0 = (_e, st, Re, Xe, O0, J0) => {
        let ae = -O0,
          rt = -Re;
        return _e.moveTo(st + J0, ae), _e.lineTo(Xe - J0, ae), _e.quadraticCurveTo(Xe, ae, Xe, ae + J0), _e.lineTo(Xe, rt - J0), _e.quadraticCurveTo(Xe, rt, Xe - J0, rt), _e.lineTo(st + J0, rt), _e.quadraticCurveTo(st, rt, st, rt - J0), _e.lineTo(st, ae + J0), _e.quadraticCurveTo(st, ae, st + J0, ae), _e
      },
      Q0 = (_e, st, Re, Xe) => {
        let O0 = new g1(_e, {
          depth: Re,
          bevelEnabled: Xe > 0,
          bevelThickness: Xe,
          bevelSize: Xe,
          bevelSegments: 3,
          curveSegments: 10
        });
        O0.rotateX(-Math.PI / 2), O0.translate(0, st, 0);
        let J0 = O0.attributes.position,
          ae = O0.attributes.uv;
        for (let rt = 0; rt < J0.count; rt++) ae.setXY(rt, J0.getZ(rt) * 2, J0.getX(rt) * 2 + J0.getY(rt) * 2);
        return O0
      },
      ve = j0 - .2,
      le = j0 + .2,
      X0 = W,
      he = W + .56,
      we = j0 - .17,
      We = j0 + .17,
      me = X0 + .125,
      Je = he - .03,
      vt = .2,
      xn = N0(new Si, ve, X0, le, he, .014);
    xn.holes.push(N0(new Mi, we, me, We, Je, .012));
    let Ot = new U0(Q0(xn, i0, .0025, .001), z);
    Ot.castShadow = Ot.receiveShadow = !0, T.add(Ot);
    let nt = N0(new Si, we - .0015, me - .0015, We + .0015, Je + .0015, .0135);
    nt.holes.push(N0(new Mi, we, me, We, Je, .012));
    let Fe = new U0(Q0(nt, i0 - vt, vt + .0025, 0), g0);
    Fe.castShadow = Fe.receiveShadow = !0, T.add(Fe);
    let Ne = N0(new Si, we, me, We, Je, .012),
      $0 = we + .075,
      q0 = Je - .075;
    Ne.holes.push(new Mi().absarc($0, -q0, .042, 0, Math.PI * 2, !0));
    let vn = new U0(Q0(Ne, i0 - vt - .0015, .0015, 0), g0);
    vn.receiveShadow = !0, T.add(vn);
    let Oi = new U0(new Ba(.042, .004, 12, 48), G.handle);
    Oi.rotation.x = Math.PI / 2, Oi.position.set($0, i0 - vt + .001, q0), T.add(Oi), S0(.041, .041, .002, 48, G.steelDark, $0, i0 - vt - .004, q0, 0, 0, T);
    for (let _e = 0; _e < 6; _e++) {
      let st = new U0(new bn(.05, .0012, .004), G.hole);
      st.position.set($0, i0 - vt - .0025, q0), st.rotation.y = _e * Math.PI / 6, T.add(st)
    }
    S0(.012, .012, .004, 32, G.handle, $0, i0 - vt - .001, q0, 0, 0, T), X(we + .03, we + .075, i0 - .045, i0 - .03, me - 5e-4, me + .002, G.handle, .003, T), X(we + .036, we + .069, i0 - .042, i0 - .033, me + .0018, me + .0025, G.hole, 0, T, !1);
    let pt = j0 - .03,
      Ht = X0 + .06,
      sn = i0 + .0025;
    S0(.026, .028, .006, 48, e0, pt, sn + .003, Ht, 0, 0, T), S0(.0205, .0205, .115, 48, e0, pt, sn + .0635, Ht, 0, 0, T), S0(.0215, .0215, .004, 48, e0, pt, sn + .12, Ht, 0, 0, T);
    let jn = new ke;
    jn.position.set(pt + .02, sn + .085, Ht), T.add(jn), S0(.011, .011, .03, 32, e0, .012, 0, 0, 0, Math.PI / 2, jn), S0(.0045, .0045, .085, 20, e0, .026, .04, 0, 0, 0, jn);
    let Kt = new Rs,
      Qe = (_e, st, Re) => new P(pt + _e, sn + st, Ht + Re);
    Kt.add(new ti(Qe(0, .12, 0), Qe(0, .29, 0))), Kt.add(new Tn(Qe(0, .29, 0), Qe(0, .33, 0), Qe(0, .33, .04))), Kt.add(new ti(Qe(0, .33, .04), Qe(0, .33, .17))), Kt.add(new Tn(Qe(0, .33, .17), Qe(0, .33, .2), Qe(0, .3, .2))), Kt.add(new ti(Qe(0, .3, .2), Qe(0, .255, .2)));
    let gs = new U0(new $i(Kt, 160, .0115, 32, !1), e0);
    gs.castShadow = !0, T.add(gs), S0(.0118, .0118, .006, 32, e0, pt, sn + .252, Ht + .2, 0, 0, T), S0(.0085, .0085, .002, 32, G.steelDark, pt, sn + .2485, Ht + .2, 0, 0, T), S0(.045, .045, .04, 32, G.steelDark, $0, i0 - vt - .022, q0, 0, 0, T);
    let In = new Rs,
      it = (_e, st, Re) => new P(_e, st, Re),
      $e = i0 - vt - .04,
      Fi = j0 - .25;
    In.add(new ti(it($0, $e, q0), it($0, $e - .08, q0))), In.add(new Tn(it($0, $e - .08, q0), it($0, $e - .14, q0), it($0, $e - .14, q0 - .05))), In.add(new Tn(it($0, $e - .14, q0 - .05), it($0, $e - .14, q0 - .1), it($0, $e - .08, q0 - .1))), In.add(new Tn(it($0, $e - .08, q0 - .1), it($0, $e - .05, q0 - .1), it($0, $e - .05, q0 - .16))), In.add(new ti(it($0, $e - .05, q0 - .16), it($0, $e - .05, Ve + .012)));
    let un = new U0(new $i(In, 120, .02, 24, !1), _0);
    un.castShadow = !0, T.add(un);
    for (let _e of [-.012, .012]) {
      let st = new Nr([it(pt + _e, i0 - .01, Ht), it(pt + _e, i0 - .12, Ht), it(pt + _e * 3, i0 - .25, Ht - .03), it(pt + _e * 5, i0 - .32, Ve + .03), it(pt + _e * 5, i0 - .32, Ve + .012)]),
        Re = new U0(new $i(st, 60, .0055, 12, !1), s0);
      Re.castShadow = !0, T.add(Re), S0(.012, .012, .03, 20, G.handle, pt + _e * 5, i0 - .32, Ve + .025, Math.PI / 2, 0, T)
    }
  }
  let Hs = new ke;
  Hs.position.set(.78, i0, -.14), b0.add(Hs);
  let Nh = [
      [0, 0],
      [.05, 0],
      [.066, .035],
      [.065, .085],
      [.05, .118],
      [.043, .128],
      [.046, .132],
      [.04, .132],
      [.036, .12],
      [0, .11]
    ].map(T => new t0(T[0], T[1])),
    Q1 = new U0(new Ur(Nh, 64), G.ceramic);
  Q1.castShadow = Q1.receiveShadow = !0, Hs.add(Q1);
  for (let T = 0; T < 4; T++) {
    let z = new cn(.2, .06, 8, 1),
      e0 = z.attributes.position;
    for (let _0 = 0; _0 < e0.count; _0++) {
      let s0 = e0.getX(_0) + .1,
        N0 = e0.getY(_0) * Math.sin(Math.PI * Math.min(1, s0 / .2 + .05));
      e0.setXYZ(_0, s0, N0, -s0 * s0 * 2.2)
    }
    z.computeVertexNormals();
    let g0 = new U0(z, G.leaf);
    g0.position.y = .125, g0.rotation.set(-Math.PI / 2 + .35, T * Math.PI / 2 + .4, 0, "YXZ"), g0.castShadow = !0, Hs.add(g0)
  }
  let c2 = T => new Nr(T.map(z => new P(...z))),
    Uh = [c2([
      [0, .12, 0],
      [.005, .3, .01],
      [0, .46, .02],
      [.05, .56, .04],
      [.14, .6, .05]
    ]), c2([
      [.01, .12, 0],
      [-.01, .32, -.01],
      [-.02, .44, 0],
      [-.07, .52, .03],
      [-.15, .53, .05]
    ])],
    $1 = new Na(1, 24);
  $1.scale(.55, 1, 1), $1.translate(0, .9, 0);

  function Oh(T) {
    let z = new ke;
    for (let g0 = 0; g0 < 5; g0++) {
      let _0 = new U0($1, G.petal);
      _0.scale.setScalar(T * (g0 % 2 ? 1.1 : .8)), _0.rotation.z = g0 * (Math.PI * 2 / 5) + .3, _0.position.z = g0 % 2 * .001, _0.castShadow = !0, z.add(_0)
    }
    let e0 = new U0(new Ps(T * .35, 12, 8), G.lip);
    return e0.scale.set(1, 1.2, .6), e0.position.set(0, -T * .25, .004), z.add(e0), z
  }
  for (let T of Uh) {
    let z = new U0(new $i(T, 40, .0025, 8), G.stem);
    z.castShadow = !0, Hs.add(z);
    for (let e0 = 0; e0 < 5; e0++) {
      let g0 = T.getPoint(Math.min(.62 + e0 * .085, 1)),
        _0 = Oh(.022 - e0 * .0015);
      _0.position.copy(g0).add(new P(0, -.02, .025)), _0.rotation.set(-.25, e0 % 2 ? .4 : -.3, 0), Hs.add(_0)
    }
  }
  for (let T of [-1, 1]) X(T < 0 ? -n0 : n0 - .018, T < 0 ? -n0 + .018 : n0, .008, y0, .325, .37, G.frame, .003);
  let Gs = new U0(new cn(2.134, 1), G.fabric);
  Gs.castShadow = !0, Gs.receiveShadow = !0, b0.add(Gs);
  let to = new ke;
  b0.add(to), X(-1.068, 1.068, .006, .038, .328, .368, G.frame, .006, to), X(-1.066, 1.066, 0, .007, .335, .362, G.rubber, .002, to);
  let Ui = 0,
    Vs = 0;

  function ec() {
    let T = y0 - .03,
      z = T - .05,
      e0 = Math.max(.001, z * Ui);
    Gs.scale.y = e0, Gs.position.set(0, T - e0 / 2, .348), Gs.visible = Ui > .003, G.fabric.map.repeat.set(110, 50 * e0), to.position.y = T - e0 - .038
  }
  ec();
  let us = 0,
    Ws = 0,
    ds = 0,
    Xs = 0;

  function l2() {
    for (let T of jr) {
      let z = Math.min(1, Math.max(0, (us - T.delay) / .76));
      T.g.position.z = K1(z) * T.travel
    }
    for (let T of Fs) T.pivot.rotation.y = T.s * K1(ds) * (Math.PI * .52)
  }
  let Pt = e.garden || null,
    Pn = new ke;
  Pn.visible = !1, i.add(Pn), Pn.rotation.y = Math.PI, Pn.position.set(6.5, 0, 0);
  let h2 = !1,
    ea = Pt ? "jardin" : "studio",
    ta = null,
    qs = null,
    js = null,
    na = new ot;
  i.add(na), u.target = na;
  let tc = -1.68;

  function ai(T, z, e0, g0, _0 = 0, s0 = 0) {
    let N0 = new K0(Object.assign({
        roughness: 1
      }, g0 || {})),
      Q0 = ve => {
        if (!ve) return null;
        let le = ve.clone();
        return le.repeat.set(z, e0), le.offset.set(_0, s0), le.needsUpdate = !0, le
      };
    return T.d && (N0.map = Q0(T.d)), T.n && (N0.normalMap = Q0(T.n)), T.r && (N0.roughnessMap = Q0(T.r)), N0
  }

  function Fh() {
    h2 = !0;
    let T = Pn,
      z = {
        d: r0(Pt.tileD, !0),
        n: r0(Pt.tileN),
        r: r0(Pt.tileR)
      },
      e0 = {
        d: r0(Pt.grassD, !0),
        n: r0(Pt.grassN),
        r: r0(Pt.grassR)
      },
      g0 = {
        d: r0(Pt.plasterD, !0),
        n: r0(Pt.plasterN),
        r: r0(Pt.plasterR)
      },
      _0 = (h0, x0, u0, W0, ge, be = !0) => {
        let Ce = new U0(h0, x0);
        return Ce.position.set(u0, W0, ge), Ce.castShadow = be, Ce.receiveShadow = !0, T.add(Ce), Ce
      },
      s0 = (h0, x0, u0, W0, ge, be, Ce, On = .004, li = !0) => X(h0, x0, u0, W0, ge, be, Ce, On, T, li),
      N0 = r0(Pt.bg, !0);
    N0.wrapS = Bt, N0.anisotropy = n;
    let Q0 = new Ps(140, 128, 64);
    Q0.scale(1, 1, -1);
    {
      let h0 = Q0.getAttribute("position"),
        x0 = new P,
        u0 = 1.7;
      for (let W0 = 0; W0 < h0.count; W0++)
        if (x0.fromBufferAttribute(h0, W0), x0.y < 0) {
          let ge = -u0 * 3 / 2,
            be = x0.y < ge ? -u0 / x0.y : 1 - x0.y * x0.y / (3 * ge * ge);
          x0.multiplyScalar(be), x0.toArray(h0.array, 3 * W0)
        } h0.needsUpdate = !0
    }
    ta = new U0(Q0, new qt({
      map: N0,
      depthWrite: !1,
      fog: !1,
      toneMapped: !1,
      color: new G0(1.08, 1.08, 1.08)
    })), ta.position.y = 1.7 - .06, ta.rotation.y = tc - Math.PI, ta.renderOrder = -1, T.add(ta);
    let ve = Cn(256, 256, h0 => {
      let x0 = h0.createRadialGradient(128, 128, 60, 128, 128, 128);
      x0.addColorStop(0, "#fff"), x0.addColorStop(.55, "#fff"), x0.addColorStop(1, "#000"), h0.fillStyle = x0, h0.fillRect(0, 0, 256, 256)
    }, !1);
    ve.wrapS = ve.wrapT = St;
    let le = ai(e0, 75, 75, {
      color: new G0(1, 1.08, .78),
      transparent: !0,
      depthWrite: !1
    });
    le.alphaMap = ve, le.normalScale.set(.8, .8);
    let X0 = 150,
      he = 2,
      we = -4,
      We = new Si;
    We.moveTo(he - X0 / 2, -(we - X0 / 2)), We.lineTo(he + X0 / 2, -(we - X0 / 2)), We.lineTo(he + X0 / 2, -(we + X0 / 2)), We.lineTo(he - X0 / 2, -(we + X0 / 2)), We.lineTo(he - X0 / 2, -(we - X0 / 2));
    let me = new Mi;
    me.moveTo(2.4, 5.4), me.lineTo(2.4, 10.6), me.lineTo(10.6, 10.6), me.lineTo(10.6, 5.4), me.lineTo(2.4, 5.4), We.holes.push(me);
    let Je = new b1(We, 4);
    Je.rotateX(-Math.PI / 2);
    {
      let h0 = Je.attributes.position,
        x0 = Je.attributes.uv;
      for (let u0 = 0; u0 < h0.count; u0++) x0.setXY(u0, (h0.getX(u0) - (he - X0 / 2)) / X0, (h0.getZ(u0) - (we - X0 / 2)) / X0)
    }
    let vt = _0(Je, le, 0, -.035, 0, !1);
    vt.renderOrder = 0;
    let xn = -.05,
      Ot = 2.4,
      nt = (h0, x0, u0, W0) => s0(h0, x0, xn, 0, u0, W0, ai(z, (x0 - h0) / Ot, (W0 - u0) / Ot, {
        color: new G0(1.45, 1.42, 1.36)
      }, h0 / Ot, -W0 / Ot), .006, !1),
      Fe = 2.5,
      Ne = 10.5,
      $0 = -10.5,
      q0 = -5.5;
    nt(-5, 12.5, q0, 1), nt(-5, 12.5, -14.5, $0), nt(-5, Fe, $0, q0), nt(Ne, 12.5, $0, q0);
    let vn = Cn(512, 512, h0 => {
        let x0 = qr(5),
          u0 = 16,
          W0 = 512 / u0;
        h0.fillStyle = "#e9f1f0", h0.fillRect(0, 0, 512, 512);
        for (let ge = 0; ge < u0; ge++)
          for (let be = 0; be < u0; be++) {
            let Ce = 62 + x0() * 10,
              On = 186 + x0() * 8;
            h0.fillStyle = `hsl(${On},${38+x0()*14}%,${Ce}%)`, h0.fillRect(be * W0 + 1.5, ge * W0 + 1.5, W0 - 3, W0 - 3)
          }
      }),
      Oi = Cn(512, 64, h0 => {
        let x0 = qr(9);
        h0.fillStyle = "#e9f1f0", h0.fillRect(0, 0, 512, 64);
        for (let u0 = 0; u0 < 16; u0++)
          for (let W0 = 0; W0 < 2; W0++) h0.fillStyle = `hsl(${200+x0()*8},45%,${30+x0()*8}%)`, h0.fillRect(u0 * 32 + 1.5, W0 * 32 + 1.5, 29, 29)
      });
    js = Cn(512, 512, h0 => {
      let x0 = h0.createImageData(512, 512),
        u0 = Math.PI * 2;
      for (let W0 = 0; W0 < 512; W0++)
        for (let ge = 0; ge < 512; ge++) {
          let be = ge / 512,
            Ce = W0 / 512,
            On = Math.sin(u0 * (3 * be + .35 * Math.sin(u0 * (2 * Ce + .2 * Math.sin(u0 * 3 * be))))),
            li = Math.sin(u0 * (3 * Ce + .35 * Math.sin(u0 * (2 * be + .25 * Math.sin(u0 * 2 * Ce))))),
            $s = Math.pow(Math.max(0, 1 - Math.abs(On * li) * 1.6), 6) + .6 * Math.pow(Math.max(0, 1 - Math.abs(On + li) * 1.2), 10),
            hi = (W0 * 512 + ge) * 4,
            Dt = Math.min(255, $s * 255);
          x0.data[hi] = Dt, x0.data[hi + 1] = Dt, x0.data[hi + 2] = Dt, x0.data[hi + 3] = 255
        }
      h0.putImageData(x0, 0, 0)
    }, !1);
    let pt = 1.45,
      Ht = (h0, x0) => {
        let u0 = new K0({
          map: vn.clone(),
          roughness: .25,
          emissive: "#bfe9f0",
          emissiveIntensity: .18
        });
        return u0.map.repeat.set(h0 / .4, x0 / .4), u0.map.needsUpdate = !0, u0
      },
      sn = Ht(Ne - Fe, q0 - $0);
    sn.emissiveMap = js, sn.emissiveIntensity = .55, js.repeat.set(3, 2), s0(Fe, Ne, -pt - .05, -pt, $0, q0, sn, 0, !1);
    let jn = [
      [Fe - .02, Fe, $0, q0, q0 - $0],
      [Ne, Ne + .02, $0, q0, q0 - $0],
      [Fe, Ne, $0 - .02, $0, Ne - Fe],
      [Fe, Ne, q0, q0 + .02, Ne - Fe]
    ];
    for (let [h0, x0, u0, W0, ge] of jn) {
      s0(h0, x0, -pt, -.16, u0, W0, Ht(ge, pt), 0, !1);
      let be = new K0({
        map: Oi.clone(),
        roughness: .2
      });
      be.map.repeat.set(ge / .5, 1), be.map.needsUpdate = !0, s0(h0, x0, -.16, -.02, u0, W0, be, 0, !1)
    }
    let Kt = ai(z, 1, 1, {
        color: new G0(1.6, 1.58, 1.52)
      }),
      Qe = .36;
    s0(Fe - Qe, Ne + Qe, -.02, .025, q0 - .03, q0 + Qe - .03, Kt, .02), s0(Fe - Qe, Ne + Qe, -.02, .025, $0 - Qe + .03, $0 + .03, Kt, .02), s0(Fe - Qe + .03, Fe + .03, -.02, .025, $0 + .03, q0 - .03, Kt, .02), s0(Ne - .03, Ne + Qe - .03, -.02, .025, $0 + .03, q0 - .03, Kt, .02), qs = o2(21, 90, 3), qs.repeat.set(5, 3);
    let gs = new xe({
        color: "#7fd3dc",
        metalness: 0,
        roughness: .04,
        transparent: !0,
        opacity: .42,
        depthWrite: !1,
        normalMap: qs,
        normalScale: new t0(.22, .22),
        specularIntensity: 1,
        clearcoat: 1,
        clearcoatRoughness: .02,
        envMapIntensity: 1.3
      }),
      In = _0(new cn(Ne - Fe, q0 - $0).rotateX(-Math.PI / 2), gs, (Fe + Ne) / 2, -.11, ($0 + q0) / 2, !1);
    In.receiveShadow = !1;
    let it = G.handle;
    for (let h0 of [-.25, .25]) {
      let x0 = new Rs,
        u0 = (W0, ge) => new P(9.4 + h0, W0, ge);
      x0.add(new ti(u0(-1.1, q0 - .12), u0(.45, q0 - .12))), x0.add(new Tn(u0(.45, q0 - .12), u0(.75, q0 - .12), u0(.75, q0 + .15))), x0.add(new Tn(u0(.75, q0 + .15), u0(.75, q0 + .4), u0(.02, q0 + .4))), _0(new $i(x0, 80, .021, 20, !1), it, 0, 0, 0)
    }
    for (let h0 of [-.35, -.65, -.95]) s0(9.15, 9.65, h0 - .02, h0, q0 - .2, q0 - .06, it, .005);
    let $e = new K0({
        color: "#3a3c40",
        roughness: .45,
        metalness: .5
      }),
      Fi = new xe({
        color: "#efece5",
        roughness: .9,
        sheen: 1,
        sheenColor: "#ffffff",
        sheenRoughness: .6
      });
    for (let h0 of [3.6, 5, 9.4]) {
      for (let be of [-.33, .33]) s0(h0 + be - .02, h0 + be + .02, .24, .27, -13.9, -11.9, $e, .008);
      for (let be of [-13.9 + .08, -11.9 - .08])
        for (let Ce of [-.33, .33]) s0(h0 + Ce - .02, h0 + Ce + .02, 0, .27, be - .02, be + .02, $e, .008);
      s0(h0 - .33, h0 + .33, .27, .36, -13.9 + .62, -11.9, Fi, .04);
      let W0 = new U0(new Ns(.66, .09, .66, 4, .04), Fi);
      W0.position.set(h0, .47, -13.9 + .3), W0.rotation.x = .85, W0.castShadow = W0.receiveShadow = !0, T.add(W0);
      let ge = new U0(new Ns(.5, .08, .3, 4, .035), Fi);
      ge.position.set(h0, .62, -13.9 + .2), ge.rotation.x = .85, ge.castShadow = !0, T.add(ge)
    }
    _0(new en(.22, .22, .03, 48), $e, 4.3, .45, -13.2), _0(new en(.03, .03, .44, 16), $e, 4.3, .22, -13.2), _0(new en(.16, .16, .012, 48), $e, 4.3, .006, -13.2);
    let un = ai(g0, 4, 2, {
      color: new G0(1.12, 1.1, 1.06)
    });
    un.normalScale.set(.25, .25);
    let _e = new K0({
        color: "#1d1e20",
        roughness: .45,
        metalness: .4
      }),
      st = new xe({
        color: "#7f8d94",
        metalness: .15,
        roughness: .02,
        transparent: !0,
        opacity: .24,
        envMapIntensity: 2.2,
        clearcoat: 1,
        depthWrite: !1
      }),
      Re = -1,
      Xe = 15,
      O0 = -21,
      J0 = -14.5,
      ae = 3.3;
    s0(Re, Xe, -.05, .05, O0, J0 + .4, ai(z, 6, 3, {
      color: "#d9d5cc"
    }), .01, !1), s0(Re, Re + .3, 0, ae, O0, J0, un, .01), s0(Xe - .3, Xe, 0, ae, O0, J0, un, .01), s0(Re, Xe, 0, ae, O0, O0 + .3, un, .01), s0(Re, Xe, ae - .5, ae, J0 - .3, J0, un, .01), s0(Re - .05, Xe + .05, ae - .05, ae + .12, O0 - .05, J0 + .05, un, .01), s0(Re + .3, Xe - .3, .05, .07, O0 + .3, J0 - .3, new K0({
      color: "#a88a68",
      roughness: .55
    }), 0, !1), s0(Re + .3, Xe - .3, ae - .52, ae - .5, O0 + .3, J0 - .3, new K0({
      color: "#f1efea",
      roughness: .9
    }), 0, !1), s0(4, 8, .07, .08, -18.6, -16.4, new K0({
      color: "#cfc6b8",
      roughness: 1
    }), 0, !1);
    let rt = new xe({
      color: "#5b5f63",
      roughness: .95,
      sheen: .8,
      sheenColor: "#8a8e92"
    });
    s0(4.2, 7.8, .07, .45, -19.6, -18.7, rt, .05), s0(4.2, 7.8, .45, .85, -19.6, -19.35, rt, .05), s0(9.5, 12.5, .73, .77, -18.5, -17.5, new K0({
      color: "#2a2422",
      roughness: .4
    }), .01);
    for (let [h0, x0] of [
        [10.3, -18],
        [11.7, -18],
        [6, -17.5]
      ]) {
      _0(new en(.004, .004, .9, 6), _e, h0, ae - .95, x0, !1);
      let u0 = _0(new en(.07, .16, .18, 32, 1, !0), _e, h0, ae - 1.45, x0, !1);
      u0.material = new K0({
        color: "#1d1e20",
        side: Mt,
        roughness: .5
      }), _0(new Ps(.05, 16, 8), new K0({
        color: "#fff3dc",
        emissive: "#ffd9a0",
        emissiveIntensity: 4
      }), h0, ae - 1.5, x0, !1)
    }
    let Ln = new Ri("#ffd9a8", 6, 14, 2);
    Ln.position.set(7, 2.3, -18), T.add(Ln);
    let Yn = J0 - .15;
    for (let h0 = Re + .3; h0 <= Xe - .3 + 1e-6; h0 += (Xe - Re - .6) / 6) s0(h0 - .035, h0 + .035, 0, ae - .5, Yn - .06, Yn + .06, _e, .004);
    s0(Re + .3, Xe - .3, 0, .06, Yn - .06, Yn + .06, _e, .004), s0(Re + .3, Xe - .3, ae - .56, ae - .5, Yn - .06, Yn + .06, _e, .004);
    let rc = _0(new cn(Xe - Re - .6, ae - .56), st, (Re + Xe) / 2, (ae - .5) / 2, Yn, !1);
    rc.castShadow = !1;
    let oi = 2.5,
      ac = 12.5,
      v2 = -21.3,
      Ft = -13.9,
      _n = ae + 3,
      ci = new K0({
        map: Y.slat ? Y.slat.clone() : null,
        normalMap: Y.slatN ? Y.slatN.clone() : null,
        roughness: .7,
        color: "#b49a84"
      });
    ci.map && (ci.map.repeat.set(1.6, 1), ci.map.needsUpdate = !0, ci.normalMap.repeat.set(1.6, 1), ci.normalMap.needsUpdate = !0), s0(oi, ac, ae + .12, _n, v2, Ft - .02, un, .01), s0(oi - .02, 5.2, ae + .12, _n, Ft - .04, Ft, ci, .003), s0(10.6, ac + .02, ae + .12, _n, Ft - .04, Ft, ci, .003), s0(5.2, 10.6, ae + .12, ae + .6, Ft - .04, Ft, ci, .003), s0(5.2, 10.6, _n - .45, _n, Ft - .04, Ft, ci, .003), s0(5.2, 10.6, ae + .6, ae + .66, Ft - .05, Ft + .01, _e, .003), s0(5.2, 10.6, _n - .51, _n - .45, Ft - .05, Ft + .01, _e, .003);
    for (let h0 of [5.2, 7.9, 10.6]) s0(h0 - .03, h0 + .03, ae + .6, _n - .45, Ft - .05, Ft + .01, _e, .003);
    _0(new cn(5.4, _n - ae - 1.05), st, 7.9, (ae + .6 + _n - .45) / 2, Ft - .03, !1), s0(oi - .04, ac + .04, _n, _n + .08, v2 - .04, Ft + .04, _e, .004);
    let oc = ai(e0, 6, 1, {
      color: "#4f6233"
    });
    oc.normalScale.set(2.2, 2.2), s0(-9.5, -8.7, 0, 1.7, -16, 6, oc, .25), s0(-9.5, 15, 0, 1.7, -24, -23.2, oc, .25);
    let Ks = new K0({
      map: Y.slat ? Y.slat.clone() : null,
      color: "#d8b48c",
      roughness: .6
    });
    Ks.map && (Ks.map.repeat.set(.3, 2), Ks.map.rotation = Math.PI / 2, Ks.map.needsUpdate = !0);
    let Zs = 2.4,
      Js = -2.3;
    s0(Zs - 1.1, Zs + 1.1, .72, .76, Js - .48, Js + .48, Ks, .008);
    for (let h0 of [-.95, .95])
      for (let x0 of [-.38, .38]) s0(Zs + h0 - .03, Zs + h0 + .03, 0, .72, Js + x0 - .03, Js + x0 + .03, $e, .006);
    let _2 = (h0, x0, u0) => {
      let W0 = new ke;
      W0.position.set(h0, 0, x0), W0.rotation.y = u0, T.add(W0);
      let ge = (be, Ce, On, li, $s, hi, Dt, ro) => X(be, Ce, On, li, $s, hi, Dt, ro, W0);
      for (let be of [-.22, .22])
        for (let Ce of [-.2, .2]) ge(be - .015, be + .015, 0, .45, Ce - .015, Ce + .015, $e, .006);
      ge(-.24, .24, .43, .47, -.22, .22, $e, .006), ge(-.23, .23, .47, .53, -.21, .21, Fi, .025);
      for (let be of [-.22, .22]) ge(be - .015, be + .015, .45, .85, .19, .22, $e, .006);
      ge(-.23, .23, .62, .84, .2, .22, Ks, .006)
    };
    for (let h0 of [-.6, 0, .6]) _2(Zs + h0, Js - .72, Math.PI), _2(Zs + h0, Js + .72, 0);
    let Bi = new K0({
        color: "#2b2c2f",
        roughness: .55,
        metalness: .6
      }),
      Xh = new K0({
        color: "#3a2f27",
        roughness: 1
      }),
      y2 = ai(z, 6, 1, {
        color: "#8a837a"
      });
    y2.normalScale.set(2.5, 2.5);
    let zi = -1.5,
      ki = 12.5,
      rn = 1,
      Qs = 3,
      dn = .42;
    s0(zi, ki, 0, dn, rn, rn + .012, Bi, .002), s0(zi, ki, 0, dn, Qs - .012, Qs, Bi, .002), s0(zi, zi + .012, 0, dn, rn, Qs, Bi, .002), s0(ki - .012, ki, 0, dn, rn, Qs, Bi, .002), s0(zi + .012, ki - .012, 0, dn - .04, rn + .012, Qs - .012, Xh, 0, !1), s0(zi + .012, ki - .012, dn - .04, dn - .035, rn + .012, Qs - .012, y2, 0, !1);
    let so = ai(z, 1, 4, {
      color: "#bdb5a8"
    });
    so.normalScale.set(3, 3), s0(Ne + .6, Ne + 1.6, -.01, .008, $0 - .2, q0 + .2, so, 0, !1), s0(Fe - 1.6, Fe - .6, -.01, .008, $0 - .2, q0 + .2, so, 0, !1);
    let Nn = Pt.models || {},
      M2 = new q1;
    M2.setMeshoptDecoder(Ph);
    let qh = h0 => h0.traverse(x0 => {
        if (!x0.isMesh) return;
        x0.castShadow = !0, x0.receiveShadow = !0;
        let u0 = x0.material;
        u0 && (u0.transparent || u0.alphaTest > 0 || u0.map && u0.alphaMap) && (u0.transparent = !1, u0.alphaTest = .45, u0.side = Mt, u0.depthWrite = !0), u0 && (u0.envMapIntensity = .8, u0.map && (u0.map.anisotropy = n))
      }),
      Un = h0 => new Promise(x0 => {
        if (!h0) return x0(null);
        M2.load(h0, u0 => {
          qh(u0.scene), x0(u0.scene)
        }, void 0, () => x0(null))
      }),
      Be = qr(77),
      at = (h0, x0, u0, W0, ge, be) => {
        let Ce = h0.clone();
        return Ce.position.set(x0, u0, W0), Ce.scale.setScalar(ge), Ce.rotation.y = be ?? Be() * Math.PI * 2, T.add(Ce), Ce
      },
      sa = h0 => {
        let x0 = [];
        h0.updateMatrixWorld(!0);
        for (let u0 of h0.children) {
          let W0 = u0.clone();
          u0.matrixWorld.decompose(W0.position, W0.quaternion, W0.scale);
          let ge = new ke;
          ge.add(W0), ge.updateMatrixWorld(!0);
          let be = new on().setFromObject(W0),
            Ce = be.getCenter(new P);
          W0.position.x -= Ce.x, W0.position.z -= Ce.z, W0.position.y -= be.min.y, x0.push(ge)
        }
        return x0
      },
      S2 = (h0, x0, u0) => {
        s0(h0 - u0 / 2, h0 + u0 / 2, -.01, .012, x0 - u0 / 2, x0 + u0 / 2, so, 0, !1), s0(h0 - u0 / 2, h0 + u0 / 2, 0, .03, x0 - u0 / 2, x0 - u0 / 2 + .01, Bi, .001), s0(h0 - u0 / 2, h0 + u0 / 2, 0, .03, x0 + u0 / 2 - .01, x0 + u0 / 2, Bi, .001), s0(h0 - u0 / 2, h0 - u0 / 2 + .01, 0, .03, x0 - u0 / 2, x0 + u0 / 2, Bi, .001), s0(h0 + u0 / 2 - .01, h0 + u0 / 2, 0, .03, x0 - u0 / 2, x0 + u0 / 2, Bi, .001)
      };
    S2(-.4, -3.4, 1.8), S2(11.9, -12.6, 1.6);
    let jh = ai(z, .4, .2, {
      color: new G0(1.3, 1.27, 1.2)
    });
    for (let h0 = 0; h0 < 9; h0++) {
      let x0 = -5.6 - h0 * .78,
        u0 = -1.5 + Math.sin(h0 * .6) * .6,
        W0 = s0(x0 - .24, x0 + .24, -.03, .02, u0 - .45, u0 + .45, jh, .03, !1);
      W0.rotation.y = .08 * Math.sin(h0)
    }
    Promise.all([Un(Nn.olive1), Un(Nn.olive2), Un(Nn.grass1), Un(Nn.grass2), Un(Nn.flowers), Un(Nn.pot), Un(Nn.rock), Un(Nn.fir), Un(Nn.umbrella), Un(Nn.olive3), Un(Nn.fern)]).then(([h0, x0, u0, W0, ge, be, Ce, On, li, $s, hi]) => {
      let Dt = Se => Se[Math.floor(Be() * Se.length)],
        ro = On ? sa(On) : [],
        er = hi ? sa(hi) : [],
        ui = [].concat(u0 ? sa(u0) : [], W0 ? sa(W0) : []),
        ao = ge ? sa(ge) : [],
        cc = (Se, He, It, fn) => {
          if (It === "fir" && ro.length) return at(Dt(ro), Se, 0, He, fn ?? .75 + Be() * .35);
          if (It === "umb" && li) return at(li, Se, 0, He, fn ?? 1.25 + Be() * .35);
          if (It === "o2" && x0) return at(x0, Se, 0, He, fn ?? 1.1 + Be() * .3);
          if (It === "o3" && $s) return at($s, Se, 0, He, fn ?? 1.3 + Be() * .4)
        },
        E2 = (Se, He, It, fn) => {
          for (let ra = 0; ra < fn; ra++) {
            let T2 = Be() * Math.PI * 2,
              w2 = Math.sqrt(Be()) * It,
              A2 = Se + Math.cos(T2) * w2,
              R2 = He + Math.sin(T2) * w2;
            er.length && Be() < .55 ? at(Dt(er), A2, 0, R2, .9 + Be() * .5) : ui.length && at(Dt(ui), A2, 0, R2, 4 + Be() * 2.5)
          }
        },
        Yh = [
          [-12, 15, "fir"],
          [-8.5, 18.5, "fir"],
          [-5, 13.5, "umb"],
          [-2, 19, "fir"],
          [1.2, 11.8, "o3"],
          [4.5, 16.5, "fir"],
          [7.8, 12.5, "umb"],
          [10.5, 18, "fir"],
          [13.5, 13, "o3"],
          [16.5, 17.5, "fir"],
          [19.5, 12, "umb"],
          [22.5, 16, "fir"],
          [-15, 9, "umb"],
          [25, 10, "fir"],
          [2.5, 23, "fir"],
          [14, 24, "fir"],
          [-6, 24, "fir"]
        ];
      for (let [Se, He, It] of Yh) cc(Se + (Be() - .5) * 1.2, He + (Be() - .5) * 1.2, It), He < 17 && E2(Se, He - 1.5, 2.6, 9);
      for (let [Se, He, It] of [
          [-12.5, 2, "fir"],
          [-13.5, -5, "umb"],
          [-12, -11, "fir"],
          [-14, -17, "fir"],
          [-10.5, -21, "umb"],
          [19, -1, "umb"],
          [21, -7, "fir"],
          [19.5, -13, "o3"],
          [21.5, -19, "fir"],
          [18, -24, "umb"]
        ]) cc(Se, He, It), E2(Se + (Se < 0 ? 1.5 : -1.5), He, 2.2, 8);
      cc(-.4, -3.4, "umb", 1.15), x0 && (at(x0, 11.9, 0, -12.6, 1.05, 2.4), at(x0, -3.4, 0, -17.2, 1.1, 4.1)), h0 && at(h0, 1.2, dn - .04, 2, 1.15, .6);
      for (let [Se, He] of [
          [-.4, -3.4],
          [11.9, -12.6]
        ])
        for (let It = 0; It < 7; It++) {
          let fn = It / 7 * Math.PI * 2;
          ui.length && at(Dt(ui), Se + Math.cos(fn) * .55, .012, He + Math.sin(fn) * .55, 3.4 + Be())
        }
      if (ui.length) {
        for (let Se = zi + .25; Se < ki - .2; Se += .26)
          for (let He of [rn + .3, rn + .65, rn + 1, rn + 1.35, rn + 1.7]) {
            if (Se < 2.4 && He > rn + .6 && He < rn + 1.5) continue;
            let It = (Be() - .5) * .16,
              fn = (Be() - .5) * .16,
              ra = He > rn + 1.2;
            ao.length && !ra && Be() < .35 ? at(Dt(ao), Se + It, dn - .04, He + fn, 2.3 + Be() * .9) : er.length && (Se < zi + 1.2 || Se > ki - 1.2) && Be() < .5 ? at(Dt(er), Se + It, dn - .04, He + fn, .8 + Be() * .4) : at(Dt(ui), Se + It, dn - .04, He + fn, ra ? 5.5 + Be() * 2.5 : 4 + Be() * 2)
          }
        for (let Se of [Ne + .85, Ne + 1.35, Fe - .85, Fe - 1.35])
          for (let He = $0 + .05; He < q0 - .05; He += .36) at(Dt(ui), Se + (Be() - .5) * .2, .008, He + (Be() - .5) * .15, 4.5 + Be() * 2.5);
        for (let Se = Re + .6; Se < Xe - .5; Se += .7)(Se < 5 || Se > 10) && at(ao.length && Be() < .3 ? Dt(ao) : Dt(ui), Se, .05, J0 + .45, 3.5 + Be() * 1.5);
        for (let Se = -15.5; Se < 5.5; Se += .6) {
          let He = er.length && Be() < .4;
          at(Dt(He ? er : ui), -8.2 + (Be() - .5) * .3, 0, Se, He ? .9 + Be() * .4 : 4 + Be() * 2)
        }
      }
      Ce && (at(Ce, 3.4, dn - .06, 1.9, .55, .3), at(Ce, 9.8, dn - .06, 2.2, .42, 2.1), at(Ce, Ne + 1, -.02, $0 + .6, .5, 1.4), at(Ce, -6.5, -.05, 3, .9, .7), at(Ce, 17.5, -.05, -4, 1.1, 2.7)), be && (at(be, Re + 2, .05, J0 + .7, 1.6, .4), at(be, Xe - 2.2, .05, J0 + .7, 1.6, 2.2), at(be, 4.6, 0, -.6, 1.3, 1)), T.updateMatrixWorld(!0), qn = 90, k = !0
    }), T.updateMatrixWorld(!0)
  }
  let u2 = [.6001, .2666],
    Bh = (() => {
      let T = u2[0] * Math.PI * 2,
        z = u2[1] * Math.PI;
      return new P(-Math.cos(T) * Math.sin(z), Math.cos(z), -Math.sin(T) * Math.sin(z)).applyAxisAngle(new P(0, 1, 0), tc).normalize()
    })();
  Pt && Pt.envRgb && a(Pt.envRgb, Pt.envM).then(T => {
    o.garden = T, Ys()
  }).catch(() => {});

  function Ys() {
    let T = ea === "jardin" && Pt;
    L = T ? "jardin" : "studio", P0(), T && !h2 && Fh(), Pn.visible = !!T, i.background = T ? null : new G0(1, 1, 1), i.environment = T && o.garden || o.studio, i.environmentRotation.y = T ? tc : 1.2, i.environmentIntensity = T ? 1.25 : .9, t.toneMappingExposure = T ? 1.55 : 1, g.visible = !T, b.visible = !T, f.intensity = T ? .15 : .35, d.intensity = T ? .25 : .6, m.visible = !T, R.material.opacity = T ? .75 : 1, T && !Ys.done && (Ys.done = !0, l.position.set(4.4, 2.1, 10.8), h.target.set(.2, .9, 1.4)), T ? (na.position.set(0, 0, 6), u.position.copy(Bh).multiplyScalar(30).add(na.position), u.color.set("#fff1dc"), u.intensity = 5.2, Object.assign(u.shadow.camera, {
      left: -26,
      right: 26,
      top: 26,
      bottom: -26,
      near: 5,
      far: 90
    }), h.maxDistance = 22) : (na.position.set(0, 0, 0), u.position.set(-4.5, 8, 3.5), u.color.set("#fff4e6"), u.intensity = 2.4, Object.assign(u.shadow.camera, {
      left: -3.2,
      right: 3.2,
      top: 3.2,
      bottom: -3.2,
      near: 2,
      far: 22
    }), h.maxDistance = 11), u.shadow.camera.updateProjectionMatrix(), c && (c.uniforms.wp.value = T ? 1 : .946), k = !0, qn = 90
  }
  let zh = new xt(1, 1, {
      type: Nt,
      samples: 0
    }),
    Dn = new z1(t, zh);
  Dn.addPass(new k1(i, l));
  let fs = new Za(i, l, 1280, 720);
  fs.updateGtaoMaterial({
    radius: .11,
    distanceExponent: 1.5,
    thickness: 1,
    scale: 1.1,
    samples: 24
  }), fs.updatePdMaterial({
    lumaPhi: 10,
    depthPhi: 2,
    normalPhi: 3,
    radius: 6,
    rings: 2,
    samples: 16
  }), fs.blendIntensity = .8;
  let kh = fs.overrideVisibility.bind(fs);
  fs.overrideVisibility = () => {
    kh(), m.visible = !1, R.visible = !1, i.traverse(T => {
      T.isMesh && T.material && T.material.transparent && (T.visible = !1)
    })
  }, Dn.addPass(fs), Dn.addPass(new V1), c = new Us({
    uniforms: {
      tDiffuse: {
        value: null
      },
      wp: {
        value: .946
      }
    },
    vertexShader: "varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }",
    fragmentShader: "uniform sampler2D tDiffuse; uniform float wp; varying vec2 vUv; void main(){ vec4 c = texture2D(tDiffuse, vUv); gl_FragColor = vec4(min(c.rgb / wp, 1.0), 1.0); }"
  }), Dn.addPass(c), Dn.addPass(new X1(1280, 720));
  let d2 = new Us({
    uniforms: {
      tDiffuse: {
        value: null
      },
      texel: {
        value: new t0(1 / 1280, 1 / 720)
      },
      amount: {
        value: .6
      }
    },
    vertexShader: "varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }",
    fragmentShader: "uniform sampler2D tDiffuse; uniform vec2 texel; uniform float amount; varying vec2 vUv;void main(){ vec3 c = texture2D(tDiffuse, vUv).rgb; vec3 n = texture2D(tDiffuse, vUv + vec2(0.0, texel.y)).rgb; vec3 s = texture2D(tDiffuse, vUv - vec2(0.0, texel.y)).rgb;vec3 e = texture2D(tDiffuse, vUv + vec2(texel.x, 0.0)).rgb; vec3 w = texture2D(tDiffuse, vUv - vec2(texel.x, 0.0)).rgb;vec3 mn = min(c, min(min(n, s), min(e, w))); vec3 mx = max(c, max(max(n, s), max(e, w)));vec3 amp = sqrt(clamp(min(mn, 1.0 - mx) / max(mx, vec3(1e-4)), 0.0, 1.0)); vec3 wt = -amp * mix(0.125, 0.2, amount);gl_FragColor = vec4(clamp((c + (n + s + e + w) * wt) / (1.0 + 4.0 * wt), 0.0, 1.0), 1.0); }"
  });
  Dn.addPass(d2);
  let Yt = null;

  function Hh(T, z) {
    h.autoRotate = !1, Yt = {
      t: 0,
      p0: l.position.clone(),
      p1: new P(...T),
      q0: h.target.clone(),
      q1: new P(...z)
    }
  }
  h.addEventListener("start", () => {
    Yt = null, ms.onInteract && ms.onInteract()
  });
  let f2 = 1.5,
    ps = 1,
    Gh = 95e5,
    p2 = 0,
    m2 = 0,
    nc = 0;

  function Vh(T, z) {
    let e0 = s.getBoundingClientRect(),
      g0 = e0.width > 0 ? e0.width / T : 1,
      _0 = (window.devicePixelRatio || 1) * g0 * f2 * ps;
    return _0 = Math.min(_0, Math.sqrt(Gh / (T * z)), 3), Math.max(1, Math.round(_0 * 8) / 8)
  }

  function ic() {
    let T = s.clientWidth || 1280,
      z = s.clientHeight || 720,
      e0 = Vh(T, z);
    return T === p2 && z === m2 && Math.abs(e0 - nc) < .12 ? !1 : (p2 = T, m2 = z, nc = e0, t.setPixelRatio(e0), t.setSize(T, z, !1), Dn.setPixelRatio(e0), Dn.setSize(T, z), d2.uniforms.texel.value.set(1 / (T * e0), 1 / (z * e0)), l.aspect = T / z, l.fov = Math.min(52, 30 * Math.max(1, Math.pow(1.35 / l.aspect, .75))), l.updateProjectionMatrix(), !0)
  }
  ic();
  let g2 = new ResizeObserver(ic);
  g2.observe(s);
  let Wh = new zr,
    b2 = !0,
    qn = 90,
    no = 1 / 60,
    sc = 0,
    ia = () => {
      qn = Math.max(qn, 20)
    };
  h.addEventListener("change", ia), N1.onLoad = () => {
    qn = 60, ms.onReady && ms.onReady()
  }, N1.onProgress = (T, z, e0) => {
    ms.onProgress && ms.onProgress(z / e0)
  };
  let io = (T, z, e0, g0) => T < z ? Math.min(z, T + e0 * g0) : Math.max(z, T - e0 * g0);

  function x2() {
    if (!b2) return;
    let T = Wh.getDelta(),
      z = Math.min(T, .05);
    if (Ui !== Vs && (Ui = io(Ui, Vs, z, .3), ec()), (us !== Ws || ds !== Xs) && (us = io(us, Ws, z, .8), ds = io(ds, Xs, z, .7), l2()), hs !== ks && (hs = io(hs, ks, z, .7), J1()), Yt) {
      Yt.t = Math.min(1, Yt.t + z / 1.3);
      let _0 = K1(Yt.t);
      l.position.lerpVectors(Yt.p0, Yt.p1, _0), h.target.lerpVectors(Yt.q0, Yt.q1, _0), Yt.t >= 1 && (Yt = null)
    }
    let e0 = ic();
    Pn.visible && qs && (qs.offset.x += z * .012, qs.offset.y += z * .007, js && (js.offset.x += z * .02, js.offset.y -= z * .013)), (h.update(z) || e0 || Pn.visible || h.autoRotate || Yt || Ui !== Vs || us !== Ws || ds !== Xs || hs !== ks) && ia(), (Ui !== Vs || us !== Ws || ds !== Xs || hs !== ks) && (k = !0), qn > 0 && (qn--, k && c0(), Dn.render(), no = no * .9 + Math.min(T, .2) * .1, sc += T, sc > 1.2 && (sc = 0, no > 1 / 28 && ps > .55 ? ps = Math.max(.55, ps - .15) : no < 1 / 55 && ps < 1 && (ps = Math.min(1, ps + .1)))), requestAnimationFrame(x2)
  }
  Ys(), x2();
  let ms = {
    setBlind(T) {
      Vs = T ? 1 : 0
    },
    setDrawers(T) {
      Ws = T ? 1 : 0
    },
    setDoors(T) {
      Xs = T ? 1 : 0
    },
    setLid(T) {
      ks = T ? 1 : 0
    },
    setAuto(T) {
      h.autoRotate = T, Yt = null, ia()
    },
    setCladding(T) {
      return $ = T in Ee || T === "fundermax" ? T : "teak", P0(), k = !0, qn = 60, $
    },
    getCladding() {
      return $
    },
    _cal: (T, z, e0, g0) => {
      De[L][T].setRGB(z, e0, g0), P0(), qn = 30
    },
    setOption(T, z) {
      T in te && (te[T] = !!z, T === "plancha" && (ie.visible = te.plancha, Le()), T === "evier" && (Zr.visible = te.evier, Le()), T === "frigo" && (Kr.visible = te.frigo, cs.visible = !te.frigo), qn = 60, k = !0)
    },
    setDecor(T) {
      return ea = T === "studio" ? "studio" : "jardin", Ys(), ea
    },
    getDecor() {
      return ea
    },
    setSupersample(T) {
      f2 = T, nc = 0, ia()
    },
    view(T) {
      let e0 = {
        face: [
          [0, 1.3, 6.4],
          [0, 1.1, 0]
        ],
        trois: [
          [-4.3, 1.55, 5.2],
          [0, 1.08, 0]
        ],
        cote: [
          [-6.4, 1.35, .9],
          [0, 1.1, 0]
        ],
        arriere: [
          [3.2, 1.6, -5.6],
          [0, 1.1, 0]
        ],
        detail: [
          [.35, 1.55, 1.25],
          [0, .98, -.05]
        ],
        rangement: [
          [-1.3, .95, 3],
          [0, .55, .3]
        ],
        jardin: [
          [4.4, 2.1, 10.8],
          [.2, .9, 1.4]
        ],
        piscine: [
          [.2, 1.65, 1.35],
          [0, .7, 10]
        ],
        evier: [
          [-.45, 1.65, 1.15],
          [-.72, .98, -.05]
        ],
        frigo: [
          [.05, .85, 1.75],
          [.72, .5, 0]
        ]
      } [T];
      return e0 && Hh(e0[0], e0[1]), e0
    },
    jump(T) {
      let z = this.view(T);
      Yt = null, z && (l.position.set(...z[0]), h.target.set(...z[1]))
    },
    snap() {
      us = Ws, ds = Xs, hs = ks, Ui = Vs, l2(), J1(), ec(), k = !0, ia()
    },
    dispose() {
      b2 = !1, g2.disconnect(), h.dispose(), Dn.dispose(), t.dispose()
    },
    snapshot(T = "image/jpeg", z = .92) {
      return Dn.render(), s.toDataURL(T, z)
    },
    onInteract: null,
    onProgress: null,
    onReady: null
  };
  return ms
}
window.DMG3D = {
mount: u7
};
})();
/*! Bundled license information:

three/build/three.module.js:
  (**
   * @license
   * Copyright 2010-2024 Three.js Authors
   * SPDX-License-Identifier: MIT
   *)
*/