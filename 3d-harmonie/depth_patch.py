# ---------- Profondeur d'Harmonie : 1,66 m avec plancher (Évidence : 0,90 m) ----------
rep('    w = .4,\n', '    w = .4,\n    WB = .4,\n    WF = 1.202,\n')
a = s.index('  for (let T of [-1, 1]) {\n    X(T < 0 ? -j : n0, T < 0 ? -n0 : j, .008, a0, -w, w, G.frame, .005);')
b = s.index('  let Ee = {', a)
seg = s[a:b]
seg = seg.replace('y0 + .005, a0, .3, w, G.frame', 'y0 + .005, a0, WF - .1, WF, G.frame')
seg = seg.replace('X(-n0, n0, y0 - .005, a0, l0, .3, G.black, 0, b0, !0)', 'X(-n0, n0, y0 - .005, a0, l0, WF - .1, G.black, 0, b0, !0)')
seg = seg.replace('X(-n0 + .01, n0 - .01, y0 - .06, y0, .23, .33, G.frame, .01)', 'X(-n0 + .01, n0 - .01, y0 - .06, y0, WF - .17, WF - .07, G.frame, .01)')
seg = re.sub(r'(?<![A-Za-z0-9_$.])-w(?![A-Za-z0-9_$])', '-WB', seg)
seg = re.sub(r'(?<![A-Za-z0-9_$.\-])w(?![A-Za-z0-9_$:])', 'WF', seg)
seg = seg.replace('for (let g0 of [-WB + .06, WF - .06]) S0(', 'for (let g0 of [-WB + .06, (WF - WB) / 2, WF - .06]) S0(')
seg = seg.replace('R0(l0 + .018, .29, F0, y0, -n0, .016, "z"), R0(l0 + .018, .29, F0, y0, n0 - .016, .016, "z")', 'R0(l0 + .018, WF - .1, F0, y0, -n0, .016, "z"), R0(l0 + .018, WF - .1, F0, y0, n0 - .016, .016, "z")')
FLOOR = """  for (let PZ = .2; PZ < WF - .03; PZ += .12) {
    let PZ1 = Math.min(PZ + .116, WF - .03), PC = new G0().setHSL(.08, .22, .66 + as() * .06);
    Q.add(-n0, n0, -.004, .014, PZ, PZ1, (2 * n0) / 1.1, (PZ1 - PZ) / 1.1, PC, .002);
  }
  X(-n0, n0, -.02, -.004, .18, WF - .02, G.black, 0, b0, !1);
  let ne = o0.done();"""
assert seg.count('  let ne = o0.done();') == 1
seg = seg.replace('  let ne = o0.done();', FLOOR)
s = s[:a] + seg + s[b:]
rep('for (let T of [-1, 1]) X(T < 0 ? -n0 : n0 - .018, T < 0 ? -n0 + .018 : n0, .008, y0, .325, .37, G.frame, .003);', 'for (let T of [-1, 1]) X(T < 0 ? -n0 : n0 - .018, T < 0 ? -n0 + .018 : n0, .008, y0, WF - .077, WF - .032, G.frame, .003);')
rep('X(-n0 + .017, n0 - .017, .006, .038, .328, .368, G.frame, .006, to), X(-n0 + .019, n0 - .019, 0, .007, .335, .362, G.rubber, .002, to);', 'X(-n0 + .017, n0 - .017, .006, .038, WF - .074, WF - .034, G.frame, .006, to), X(-n0 + .019, n0 - .019, 0, .007, WF - .067, WF - .04, G.rubber, .002, to);')
rep('Gs.position.set(0, T - e0 / 2, .348)', 'Gs.position.set(0, T - e0 / 2, WF - .054)')
rep('h.target.set(0, 1.08, 0), h.enableDamping', 'h.target.set(0, 1.08, .4), h.enableDamping')
OLDV = """        face: [
          [0, 1.3, 8.2],
          [0, 1.1, 0]
        ],
        trois: [
          [-5.0, 1.55, 6.0],
          [0, 1.08, 0]
        ],
        cote: [
          [-7.8, 1.35, 1.1],
          [0, 1.1, 0]
        ],
        arriere: [
          [4.2, 1.6, -7],
          [0, 1.1, 0]
        ],"""
NEWV = """        face: [
          [0, 1.35, 8.7],
          [0, 1.1, .4]
        ],
        trois: [
          [-5.2, 1.65, 6.6],
          [0, 1.05, .4]
        ],
        cote: [
          [-7.9, 1.4, 1.5],
          [0, 1.1, .4]
        ],
        arriere: [
          [4.2, 1.6, -6.4],
          [0, 1.1, .4]
        ],
        dedans: [
          [-1.05, 1.62, 2.5],
          [.35, 1.15, -.1]
        ],"""
rep(OLDV, NEWV)
rep('l.position.set(-5.0, 1.55, 6.0);', 'l.position.set(-5.2, 1.65, 6.6);')
# ---------- Côtés intérieurs tout en bois, plancher de 15 cm ----------
rep('R0(l0 + .018, WF - .1, F0, y0, -n0, .016, "z"), R0(l0 + .018, WF - .1, F0, y0, n0 - .016, .016, "z"), X(-n0, -n0 + .012, i0, F0, l0 + .008, .29, G.black, 0), X(n0 - .012, n0, i0, F0, l0 + .008, .29, G.black, 0);',
    'R0(l0 + .018, WF - .08, .014, y0, -n0, .016, "z"), R0(l0 + .018, WF - .08, .014, y0, n0 - .016, .016, "z");')
# toute la cuisine pose sur le plancher : on la remonte de 15 cm et on dessine le plancher dessous
rep('  let b0 = new ke;\n  i.add(b0);', '  let b0 = new ke;\n  i.add(b0), b0.position.y = .15;')
PLAT = """  X(-n0, n0, -.02, -.004, .18, WF - .02, G.black, 0, b0, !1);
  X(-j - .024, j + .024, -.15, -.004, -WB - .027, WF + .005, G.frame, .004);
  X(-j - .03, j + .03, -.15, -.13, -WB - .033, WF + .011, G.cap, .003);"""
rep('  X(-n0, n0, -.02, -.004, .18, WF - .02, G.black, 0, b0, !1);', PLAT)
# caméras : on vise 15 cm plus haut
for v in ['[0, 1.1, .4]', '[0, 1.05, .4]']:
    s = s.replace(v, v.replace('1.1,', '1.22,').replace('1.05,', '1.17,'))
rep('h.target.set(0, 1.08, .4), h.enableDamping', 'h.target.set(0, 1.2, .4), h.enableDamping')
for a, b2 in [('[0, 1, -.05]', '[0, 1.15, -.05]'), ('[-.2, .55, .3]', '[-.2, .7, .3]'), ('[1.27, .98, -.05]', '[1.27, 1.13, -.05]'), ('[-1.27, .5, 0]', '[-1.27, .65, 0]'), ('[.35, 1.15, -.1]', '[.35, 1.3, -.1]')]:
    s = s.replace(a, b2)
for a, b2 in [('[.45, 1.6, 1.45]', '[.45, 1.75, 1.45]'), ('[-1.6, .95, 3.2]', '[-1.6, 1.1, 3.2]'), ('[1.55, 1.65, 1.15]', '[1.55, 1.8, 1.15]'), ('[-.6, .85, 1.75]', '[-.6, 1.0, 1.75]'), ('[-1.05, 1.62, 2.5]', '[-1.05, 1.77, 2.5]')]:
    s = s.replace(a, b2)
# ---------- +10 cm de hauteur ----------
rep('    a0 = 2.2,\n', '    a0 = 2.3,\n')
rep('    y0 = 1.975,\n', '    y0 = 2.075,\n')
rep('f0.position.set(n0 - .1, 2.12, WF + .002)', 'f0.position.set(n0 - .1, 2.22, WF + .002)')
rep('G.screw, T * (n0 - .06), 2.1, WF + .002', 'G.screw, T * (n0 - .06), 2.2, WF + .002')
