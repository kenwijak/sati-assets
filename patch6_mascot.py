#!/usr/bin/env python3
"""Add real mascot image assets (MascotAsset component) to payoff-liff.html.

Changes:
1. Add MASCOT_ASSETS + MASCOT_BY_CONTEXT constants after color vars
2. Add MascotAsset component after Face component
3. Update HeroCard to accept mascotContext + use MascotAsset (size 92)
4. Add mascotContext to each HeroCard caller
5. Success/empty state mascots → MascotAsset
6. Header mascot → MascotAsset
"""

with open('/home/user/sati-assets/payoff-liff.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# ── 1. Add mascot constants after color vars ────────────────────────────────
old1 = (
    'var G = "#3DDB5A",\n'
    '  GOLD = "#FFD015",\n'
    '  CREAM = "#F5F0E8",\n'
    '  DARK = "#1A3D1F",\n'
    '  MID = "#2D5A35";'
)
new1 = (
    'var G = "#3DDB5A",\n'
    '  GOLD = "#FFD015",\n'
    '  CREAM = "#F5F0E8",\n'
    '  DARK = "#1A3D1F",\n'
    '  MID = "#2D5A35";\n'
    'var MASCOT_ASSETS = {\n'
    '  happy: "/salung-happy.jpeg",\n'
    '  receipt: "/salung-receipt.jpeg",\n'
    '  save: "/salung-save.jpeg",\n'
    '  budget: "/salung-budget.jpeg",\n'
    '  detective: "/salung-detective.jpeg",\n'
    '  cool: "/salung-cool.jpeg",\n'
    '  success: "/salung-success.jpeg",\n'
    '  thinking: "/salung-thinking.jpeg",\n'
    '  warning: "/salung-warning.jpeg",\n'
    '  sleeping: "/salung-sleeping.jpeg"\n'
    '};\n'
    'var MASCOT_BY_CONTEXT = {\n'
    '  header:      MASCOT_ASSETS.happy,\n'
    '  cashflowHero: MASCOT_ASSETS.receipt,\n'
    '  saveHero:    MASCOT_ASSETS.save,\n'
    '  debtHero:    MASCOT_ASSETS.detective,\n'
    '  moreHero:    MASCOT_ASSETS.budget,\n'
    '  success:     MASCOT_ASSETS.success,\n'
    '  warning:     MASCOT_ASSETS.warning,\n'
    '  empty:       MASCOT_ASSETS.thinking,\n'
    '  spicy:       MASCOT_ASSETS.cool,\n'
    '  sleeping:    MASCOT_ASSETS.sleeping\n'
    '};'
)
changes.append(('add MASCOT constants', old1, new1))

# ── 2. Add MascotAsset component right after Face component ─────────────────
old2 = (
    '  return /*#__PURE__*/React.createElement(SalungMascot, { mood: mascotMood, size: size });\n'
    '}\n'
    'function Card('
)
new2 = (
    '  return /*#__PURE__*/React.createElement(SalungMascot, { mood: mascotMood, size: size });\n'
    '}\n'
    'function MascotAsset(props) {\n'
    '  var context = props.context;\n'
    '  var mood = props.mood || "happy";\n'
    '  var size = props.size || 72;\n'
    '  var src;\n'
    '  if (context && MASCOT_BY_CONTEXT[context]) src = MASCOT_BY_CONTEXT[context];\n'
    '  else if (mood && MASCOT_ASSETS[mood]) src = MASCOT_ASSETS[mood];\n'
    '  else src = MASCOT_ASSETS.happy;\n'
    '  var _msa = useState(false),\n'
    '    _msa2 = _slicedToArray(_msa, 2),\n'
    '    failed = _msa2[0],\n'
    '    setFailed = _msa2[1];\n'
    '  if (failed || !src) {\n'
    '    return /*#__PURE__*/React.createElement(SalungMascot, { mood: mood, size: size });\n'
    '  }\n'
    '  return /*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      width: size, height: size, flexShrink: 0,\n'
    '      display: "flex", alignItems: "center", justifyContent: "center",\n'
    '      borderRadius: 18,\n'
    '      background: "rgba(255,255,255,0.55)",\n'
    '      overflow: "hidden"\n'
    '    }\n'
    '  }, /*#__PURE__*/React.createElement("img", {\n'
    '    src: src,\n'
    '    alt: "Salung mascot",\n'
    '    onError: function() { setFailed(true); },\n'
    '    className: "sl-mascot",\n'
    '    style: Object.assign({\n'
    '      width: size,\n'
    '      height: size,\n'
    '      objectFit: "contain",\n'
    '      display: "block"\n'
    '    }, props.style || {})\n'
    '  }));\n'
    '}\n'
    'function Card('
)
changes.append(('add MascotAsset component', old2, new2))

# ── 3. Update HeroCard: add mascotContext var + use MascotAsset ─────────────
old3 = '  var salungText = props.salungText;'
new3 = (
    '  var salungText = props.salungText;\n'
    '  var mascotContext = props.mascotContext;'
)
changes.append(('HeroCard: add mascotContext var', old3, new3))

old3b = 'React.createElement(SalungMascot, { mood: spicy ? "cool" : mood, size: 80 })'
new3b = 'React.createElement(MascotAsset, { context: spicy ? "spicy" : mascotContext, mood: spicy ? "cool" : mood, size: 92 })'
changes.append(('HeroCard: use MascotAsset', old3b, new3b))

# ── 4. HeroCard callers: add mascotContext ──────────────────────────────────

# 4a. CashFlow HeroCard
old4a = '    mood: d.net >= 0 ? "happy" : "sad",'
new4a = (
    '    mood: d.net >= 0 ? "happy" : "sad",\n'
    '    mascotContext: d.net >= 0 ? "cashflowHero" : "warning",'
)
changes.append(('CashFlow HeroCard: mascotContext', old4a, new4a))

# 4b. Debt HeroCard
old4b = (
    'React.createElement(HeroCard, {\n'
    '  mood: debts.length ? "detective" : "happy",\n'
)
new4b = (
    'React.createElement(HeroCard, {\n'
    '  mood: debts.length ? "detective" : "happy",\n'
    '  mascotContext: debts.length ? "debtHero" : "empty",\n'
)
changes.append(('Debt HeroCard: mascotContext', old4b, new4b))

# 4c. More HeroCard (unique via profile.name)
old4c = (
    '" + (profile.name || ""), \n'
    '  sub: "Zone " + profile.zone,\n'
    '  accent: GOLD,\n'
    '  spicy: spicy\n'
    '})'
)
new4c = (
    '" + (profile.name || ""), \n'
    '  sub: "Zone " + profile.zone,\n'
    '  accent: GOLD,\n'
    '  mascotContext: "moreHero",\n'
    '  spicy: spicy\n'
    '})'
)
changes.append(('More HeroCard: mascotContext', old4c, new4c))

# 4d. SaveGoal HeroCard (unique via saveSummary.total, 2-space indent)
old4d = '  mood: saveSummary.total > 0 ? "proud" : "budgeting",'
new4d = (
    '  mood: saveSummary.total > 0 ? "proud" : "budgeting",\n'
    '  mascotContext: "saveHero",'
)
changes.append(('SaveGoal HeroCard: mascotContext', old4d, new4d))

# ── 5. Success component: SalungMascot → MascotAsset ───────────────────────
old5 = 'React.createElement(SalungMascot, { mood: "proud", size: 72 })'
new5 = 'React.createElement(MascotAsset, { context: "success", mood: "proud", size: 72 })'
changes.append(('Success: use MascotAsset', old5, new5))

# ── 6. Empty states: SalungMascot → MascotAsset ────────────────────────────

# 6a. Add-txn sheet header (small inline, size 36)
old6a = 'React.createElement(SalungMascot, { mood: "happy", size: 36 })'
new6a = 'React.createElement(MascotAsset, { context: "header", mood: "happy", size: 36 })'
changes.append(('Sheet header: use MascotAsset', old6a, new6a))

# 6b. CashFlow no-categories empty state (size 56)
old6b = 'React.createElement(SalungMascot, { mood: "budgeting", size: 56 })'
new6b = 'React.createElement(MascotAsset, { context: "empty", mood: "thinking", size: 56 })'
changes.append(('No-cats empty: use MascotAsset', old6b, new6b))

# 6c. CashFlow no-transactions empty state (size 64)
old6c = 'React.createElement(SalungMascot, { mood: "budgeting", size: 64 })'
new6c = 'React.createElement(MascotAsset, { context: "sleeping", mood: "thinking", size: 64 })'
changes.append(('No-txns empty: use MascotAsset', old6c, new6c))

# 6d. Goal empty state (size 64)
old6d = 'React.createElement(SalungMascot, { mood: "proud", size: 64 })'
new6d = 'React.createElement(MascotAsset, { context: "empty", mood: "thinking", size: 64 })'
changes.append(('Goal empty: use MascotAsset', old6d, new6d))

# 6e. SaveGoal empty state (size 56)
old6e = 'React.createElement(SalungMascot, { mood: "proud", size: 56 })'
new6e = 'React.createElement(MascotAsset, { context: "empty", mood: "thinking", size: 56 })'
changes.append(('SaveGoal empty: use MascotAsset', old6e, new6e))

# ── 7. Header mascot ─────────────────────────────────────────────────────────
old7 = 'React.createElement(SalungMascot, { mood: spicy ? "cool" : "happy", size: 40 })'
new7 = 'React.createElement(MascotAsset, { context: spicy ? "spicy" : "header", mood: spicy ? "cool" : "happy", size: 40 })'
changes.append(('Header: use MascotAsset', old7, new7))

# ── Apply ────────────────────────────────────────────────────────────────────
ok = True
for name, old, new in changes:
    cnt = content.count(old)
    if cnt == 1:
        content = content.replace(old, new)
        print(f'  ✓ {name}')
    else:
        print(f'  ✗ {name}: found {cnt} times (need 1)')
        ok = False

# Paren balance check
depth = 0
for ch in content:
    if ch == '(': depth += 1
    elif ch == ')': depth -= 1

print(f'\nParen depth: {depth}')
if depth == 0 and ok:
    with open('/home/user/sati-assets/payoff-liff.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Saved patch6_mascot.')
elif depth != 0:
    print('ERROR: paren imbalance, not saving')
else:
    print('WARNING: some patterns not found, not saving')
