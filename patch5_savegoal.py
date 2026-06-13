#!/usr/bin/env python3
"""SaveGoal usability:
1. Reduce savingsTxns slices from 10 to 5
2. Add showAllGoals state
3. Limit goals.map to 3 by default with expand button
"""

with open('/home/user/sati-assets/payoff-liff.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# ── 1. savingsTxns: reduce slice 10→5 (initial load) ──────────────────────
old1a = (
    '.filter(function (t) {\n'
    '        return t.category_id === "savings";\n'
    '      }).slice(0, 10))'
)
new1a = (
    '.filter(function (t) {\n'
    '        return t.category_id === "savings";\n'
    '      }).slice(0, 5))'
)
changes.append(('savingsTxns initial load slice 10→5', old1a, new1a))

# ── 2. savingsTxns: reduce slice 10→5 (add entry prepend) ─────────────────
old1b = '[entry].concat(_toConsumableArray(ts)).slice(0, 10);\n'
new1b = '[entry].concat(_toConsumableArray(ts)).slice(0, 5);\n'
changes.append(('savingsTxns add entry slice 10→5', old1b, new1b))

# ── 3. savingsTxns: reduce slice 10→5 (add goal-fund prepend) ─────────────
old1c = '[_newEntry].concat(_toConsumableArray(ts)).slice(0, 10);\n'
new1c = '[_newEntry].concat(_toConsumableArray(ts)).slice(0, 5);\n'
changes.append(('savingsTxns goal-fund slice 10→5', old1c, new1c))

# ── 4. Add showAllGoals state after bucketLimitSheet ──────────────────────
old4 = (
    '    bucketLimitSheet = _useStateBLSArr[0],\n'
    '    setBucketLimitSheet = _useStateBLSArr[1];'
)
new4 = (
    '    bucketLimitSheet = _useStateBLSArr[0],\n'
    '    setBucketLimitSheet = _useStateBLSArr[1];\n'
    '  var _useState_sag = useState(false),\n'
    '    _useState_sag_arr = _slicedToArray(_useState_sag, 2),\n'
    '    showAllGoals = _useState_sag_arr[0],\n'
    '    setShowAllGoals = _useState_sag_arr[1];'
)
changes.append(('add showAllGoals state', old4, new4))

# ── 5. Change goals.map to limit to 3 by default ──────────────────────────
old5 = (
    'goals.map(function (g) {\n'
    '    return /*#__PURE__*/React.createElement(Card, {\n'
    '      key: g.id,\n'
    '      style: {\n'
    '        background: g.fi'
)
new5 = (
    '(showAllGoals ? goals : goals.slice(0, 3)).map(function (g) {\n'
    '    return /*#__PURE__*/React.createElement(Card, {\n'
    '      key: g.id,\n'
    '      style: {\n'
    '        background: g.fi'
)
changes.append(('goals.map slice to 3', old5, new5))

# ── 6. Add expand button after goals.map ──────────────────────────────────
# Pattern: end of goals.map callback is "🗑️"))) then }), then next Card
old6 = '"\\uD83D\\uDDD1\\uFE0F")));\n  }), /*#__PURE__*/React.createElement(Card, {'
new6 = (
    '"\\uD83D\\uDDD1\\uFE0F")));\n'
    '  }), goals.length > 3 && /*#__PURE__*/React.createElement("button", {\n'
    '    onClick: function onClick() {\n'
    '      return setShowAllGoals(!showAllGoals);\n'
    '    },\n'
    '    style: {\n'
    '      width: "100%",\n'
    '      padding: "8px 0",\n'
    '      fontSize: 12,\n'
    '      fontWeight: 700,\n'
    '      background: "none",\n'
    '      color: "#888",\n'
    '      border: "1.5px solid #ddd",\n'
    '      borderRadius: 10,\n'
    '      cursor: "pointer",\n'
    '      marginTop: 2\n'
    '    }\n'
    '  }, showAllGoals ? "\\u0E0B\\u0E48\\u0E2D\\u0E19\\u0E40\\u0E1B\\u0E49\\u0E32\\u0E2B\\u0E21\\u0E32\\u0E22 \\u25B2" : "\\u0E14\\u0E39\\u0E40\\u0E1B\\u0E49\\u0E32\\u0E2B\\u0E21\\u0E32\\u0E22\\u0E17\\u0E31\\u0E49\\u0E07\\u0E2B\\u0E21\\u0E14 \\u25BE"), /*#__PURE__*/React.createElement(Card, {'
)
changes.append(('goals expand button', old6, new6))

# Apply
ok = True
for name, old, new in changes:
    count = content.count(old)
    if count == 1:
        content = content.replace(old, new)
        print(f'  ✓ {name}')
    else:
        print(f'  ✗ {name}: found {count} times (need 1)')
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
    print('Saved patch5.')
elif depth != 0:
    print('ERROR: paren imbalance, not saving')
else:
    print('WARNING: some patterns not found, not saving to avoid partial state')
