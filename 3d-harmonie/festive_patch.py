# ---------- La Festive : 4 m de façade, 3 m de profondeur, îlot bar fixe à l'intérieur ----------
# Même construction qu'Harmonie ; la cuisine reste contre le mur du fond, l'avant s'allonge.
rep('    WF = 1.202,\n', '    WF = 2.542,\n')

# Îlot bar fixe : parallèle à la façade, contre le mur de gauche, juste derrière le volet.
# Côté terrasse : lames (même bardage que la cuisine). Côté cuisine : plateau en débord pour les tabourets,
# fond noir en retrait et un meuble tiroir + porte au bout, contre le mur.
ILOT = '''  D0.visible = !1, b0.add(D0);
  let ILg = new ke, ILp = new ke, IX0 = -n0 + .016, IX1 = .35, IZ1 = WF - .26, IZ0 = IZ1 - .4, IY0 = .014, IY1 = .014 + 1.1;
  b0.add(ILg), ILp.visible = !1, ILg.add(ILp);
  let ILk = X(IX0, IX1 - .022, IY0, IY1 - .012, IZ0, IZ1 - .022, G.black, 0, ILg, !1),
    ILb = Y0(M);
  ue(IX0, IX1, x => ILb.add(x, x + A0, IY0, IY1 - .012, IZ1 - .022, IZ1, .43, (IY1 - .012 - IY0) / 1.4, B0(), 6e-4, as() * .57, as()));
  ue(IZ0, IZ1 - .022, z => ILb.add(IX1 - .022, IX1, IY0, IY1 - .012, z, z + A0, .43, (IY1 - .012 - IY0) / 1.4, B0(), 6e-4, as() * .57, as()));
  X(IX0, IX1, IY0, IY1 - .012, IZ1 - .012, IZ1, ee, .002, ILp), X(IX1 - .012, IX1, IY0, IY1 - .012, IZ0, IZ1 - .012, ee, .002, ILp);
  let ILs = ILb.done(ILg);
  X(IX0, IX1 + .02, IY1 - .012, IY1, IZ0 - .22, IZ1 + .02, G.stone, .002, ILg);
  {
    let CX0 = IX0 + .004, CX1 = IX0 + .5, CZ = IZ0, DY = IY1 - .012 - .17;
    X(CX0, CX1, DY + .002, IY1 - .016, CZ - .02, CZ, G.front, .0025, ILg), X(CX0, CX1, IY0 + .1, DY - .002, CZ - .02, CZ, G.front, .0025, ILg);
    X(IX0, IX1 - .022, IY0, IY0 + .1, IZ0 + .05, IZ0 + .07, G.black, 0, ILg, !1);
    for (let HY of [IY1 - .06, DY - .05]) {
      let HX = (CX0 + CX1) / 2;
      S0(.006, .006, .16, 24, G.handle, HX, HY, CZ - .048, 0, Math.PI / 2, ILg);
      for (let s of [-1, 1]) X(HX + s * .068 - .004, HX + s * .068 + .004, HY - .004, HY + .004, CZ - .046, CZ - .02, G.handle, .002, ILg);
    }
    let pl = new U0(new Ns(.11, .055, .004, 2, .0015), [G.frame, G.frame, G.frame, G.frame, G.logo, G.frame]);
    pl.position.set(IX1 - .32, IY1 - .12, IZ1 + .002), pl.castShadow = !0, ILg.add(pl);
  }
'''
rep('  D0.visible = !1, b0.add(D0);\n', ILOT)
rep('BRp.visible = T, HF.visible = HFon && !T;', 'BRp.visible = T, HF.visible = HFon && !T, ILs.visible = ILk.visible = !T, ILp.visible = T;')

# caméra et vues pour une cuisine plus profonde
rep('  l.position.set(-5.2, 1.65, 6.6);', '  l.position.set(-6.4, 2, 8.8);')
rep('h.target.set(0, 1.2, .4), h.enableDamping', 'h.target.set(0, 1.1, 1.1), h.enableDamping')
def setview(name, cam, tgt):
    global s
    pat = re.compile(r'(        ' + name + r': \[\n          \[)[^\]]*(\],\n          \[)[^\]]*(\])')
    s, n = pat.subn(lambda m: m.group(1) + cam + m.group(2) + tgt + m.group(3), s)
    assert n == 1, name
for v in [('face', '0, 1.6, 11.2', '0, 1.15, 1.1'), ('trois', '-6.4, 2, 8.8', '0, 1.1, 1.1'), ('cote', '-10.5, 1.6, 2.2', '0, 1.1, 1.2'),
          ('arriere', '5.2, 1.8, -8', '0, 1.1, 1'), ('accueil', '-7.4, 2.4, 10', '.3, 1, 1.4'), ('store', '-7.6, 3.4, 12', '0, 1.5, 3'),
          ('dedans', '-.6, 1.8, 3.4', '.3, 1.2, .3'), ('rangement', '1.2, 1, 2.4', '-.1, .6, .3'), ('frigo', '-.4, .85, 1.45', '-1.485, .5, 0')]:
    setview(*v)
# lumière principale du studio : avancée de la profondeur en plus, pour rester devant la cuisine
rep('g.position.set(-.6, 2.1, 2.4), g.lookAt(0, 1.2, -.3)', 'g.position.set(-.6, 2.1, 3.74), g.lookAt(0, 1.2, 1.04)')
rep('g.lookAt(0, 1.2, -.3);', 'g.lookAt(0, 1.2, 1.04);')

# ---------- Porte vitrée coulissante dans le mur de droite, qui s'escamote dans l'épaisseur du mur ----------
# Passage de z .40 à 1.35 (juste devant le plan de travail), 1,90 m de haut ; la porte part vers la façade.
rep('''  for (let T of [-1, 1]) {
    X(T < 0 ? -j : n0, T < 0 ? -n0 : j, .008, a0, -WB, WF, G.frame, .005);''', '''  const GDZ0 = .4, GDZ1 = 1.35, GDY = 1.9;

  function XW(T, a, b, c, d, e, f, m, bv, p, cs) {
    if (T < 0 || f <= GDZ0 || e >= GDZ1) return [X(a, b, c, d, e, f, m, bv, p, cs)];
    let r = [X(a, b, c, d, e, GDZ0, m, bv, p, cs), X(a, b, c, d, GDZ1, f, m, bv, p, cs)];
    return d > GDY && r.push(X(a, b, Math.max(c, GDY), d, GDZ0, GDZ1, m, bv, p, cs)), r
  }
  for (let T of [-1, 1]) {
    XW(T, T < 0 ? -j : n0, T < 0 ? -n0 : j, .008, a0, -WB, WF, G.frame, .005);''')
rep('J.push(X(T < 0 ? -j - .017 : j, T < 0 ? -j : j + .017, .025, a0 - .055, -WB + .045, WF - .045, O, 0, b0, !1)), ue(-WB + .048, WF - .048, g0 => o0.add(T < 0 ? -j - .02 : j + .016, T < 0 ? -j - .016 : j + .02, .025,',
    'J.push(...XW(T, T < 0 ? -j - .017 : j, T < 0 ? -j : j + .017, .025, a0 - .055, -WB + .045, WF - .045, O, 0, b0, !1)), ue(-WB + .048, WF - .048, g0 => o0.add(T < 0 ? -j - .02 : j + .016, T < 0 ? -j - .016 : j + .02, T > 0 && g0 + A0 > GDZ0 && g0 < GDZ1 ? GDY : .025,')
rep('for (let T of [-1, 1]) X(T < 0 ? -j - .02 : j + .004, T < 0 ? -j - .004 : j + .02, .025, a0 - .055, -WB + .05, WF - .05, ee, .002, D0);',
    'for (let T of [-1, 1]) XW(T, T < 0 ? -j - .02 : j + .004, T < 0 ? -j - .004 : j + .02, .025, a0 - .055, -WB + .05, WF - .05, ee, .002, D0);')
rep('for (let T of [-1, 1]) X(T < 0 ? -j - .024 : j + .006, T < 0 ? -j - .006 : j + .024, .025, a0 - .055, -WB + .045, HFz, ee, .002, HF);',
    'for (let T of [-1, 1]) XW(T, T < 0 ? -j - .024 : j + .006, T < 0 ? -j - .006 : j + .024, .025, a0 - .055, -WB + .045, HFz, ee, .002, HF);')
rep('R0(l0 + .018, WF - .08, .014, y0, n0 - .016, .016, "z")',
    'R0(l0 + .018, GDZ0, .014, y0, n0 - .016, .016, "z"), R0(GDZ1, WF - .08, .014, y0, n0 - .016, .016, "z"), R0(GDZ0, GDZ1, GDY, y0, n0 - .016, .016, "z")')
DOOR = '''  var GD = new ke;
  {
    let FX0 = n0 - .02, FX1 = j + .026, fz = .045;
    X(FX0, FX1, .012, GDY + fz, GDZ0 - fz, GDZ0, G.frame, .003), X(FX0, FX1, .012, GDY + fz, GDZ1, GDZ1 + fz, G.frame, .003);
    X(FX0, FX1, GDY, GDY + fz, GDZ0 - fz, GDZ1 + fz, G.frame, .003), X(FX0, FX1, 0, .016, GDZ0, GDZ1, G.frame, .002);
    let GL = new xe({ color: "#b8c8cf", metalness: 0, roughness: .05, transparent: !0, opacity: .16, depthWrite: !1, envMapIntensity: 1.3 }),
      PX0 = (n0 + j) / 2 - .017, PX1 = (n0 + j) / 2 + .017, PZ0 = GDZ0, PZ1 = GDZ1 + .02;
    b0.add(GD);
    X(PX0, PX1, .016, .076, PZ0, PZ1, G.frame, .003, GD), X(PX0, PX1, GDY - .05, GDY - .002, PZ0, PZ1, G.frame, .003, GD);
    X(PX0, PX1, .076, GDY - .05, PZ0, PZ0 + .05, G.frame, .003, GD), X(PX0, PX1, .076, GDY - .05, PZ1 - .05, PZ1, G.frame, .003, GD);
    let gl = X(PX0 + .012, PX1 - .012, .076, GDY - .05, PZ0 + .05, PZ1 - .05, GL, 0, GD, !1);
    gl.receiveShadow = !1;
    for (let s of [-1, 1]) {
      let HX = s < 0 ? PX0 - .028 : PX1 + .028;
      X(HX - .005, HX + .005, .82, 1.32, PZ0 + .075, PZ0 + .09, G.black, .002, GD);
      for (let HY of [.86, 1.28]) X(Math.min(HX, s < 0 ? PX0 : PX1), Math.max(HX, s < 0 ? PX0 : PX1), HY - .006, HY + .006, PZ0 + .078, PZ0 + .088, G.black, .001, GD);
    }
  }
  let ILg = new ke,'''
rep('  let ILg = new ke,', DOOR)
# la porte vitrée s'escamote avec le bouton « Portes »
rep('    for (let T of Fs) T.pivot.rotation.y = T.s * K1(ds) * (Math.PI * .52)\n  }',
    '    for (let T of Fs) T.pivot.rotation.y = T.s * K1(ds) * (Math.PI * .52);\n    GD && (GD.position.z = K1(ds) * (GDZ1 - GDZ0 - .1))\n  }')
