#!/usr/bin/env python3
with open('/home/user/sati-assets/payoff-liff.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# ── 1. Type toggle: shared-border box → gap-based pill buttons ──
old1 = (
    '/*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      display: "flex",\n'
    '      border: "2px solid ".concat(DARK),\n'
    '      borderRadius: 12,\n'
    '      overflow: "hidden",\n'
    '      marginBottom: 14\n'
    '    }\n'
    '  }, [["expense", "รายจ่าย"], ["income", "รายรับ"]].map(function (_ref12) {\n'
    '    var _ref13 = _slicedToArray(_ref12, 2),\n'
    '      id = _ref13[0],\n'
    '      lbl = _ref13[1];\n'
    '    return /*#__PURE__*/React.createElement("button", {\n'
    '      key: id,\n'
    '      onClick: function onClick() {\n'
    '        return setType(id);\n'
    '      },\n'
    '      style: {\n'
    '        flex: 1,\n'
    '        padding: "9px 0",\n'
    '        fontSize: 12,\n'
    '        fontWeight: 800,\n'
    '        border: "none",\n'
    '        cursor: "pointer",\n'
    '        background: type === id ? DARK : "#fff",\n'
    '        color: type === id ? "#fff" : "#888"\n'
    '      }\n'
    '    }, lbl);\n'
    '  }))'
)
new1 = (
    '/*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      display: "flex",\n'
    '      gap: 8,\n'
    '      marginBottom: 14\n'
    '    }\n'
    '  }, [["expense", "รายจ่าย"], ["income", "รายรับ"]].map(function (_ref12) {\n'
    '    var _ref13 = _slicedToArray(_ref12, 2),\n'
    '      id = _ref13[0],\n'
    '      lbl = _ref13[1];\n'
    '    return /*#__PURE__*/React.createElement("button", {\n'
    '      key: id,\n'
    '      onClick: function onClick() {\n'
    '        return setType(id);\n'
    '      },\n'
    '      style: {\n'
    '        flex: 1,\n'
    '        padding: "11px 0",\n'
    '        fontSize: 13,\n'
    '        fontWeight: 900,\n'
    '        border: "2px solid " + DARK,\n'
    '        borderRadius: 99,\n'
    '        cursor: "pointer",\n'
    '        background: type === id ? DARK : "#fff",\n'
    '        color: type === id ? "#fff" : "#888",\n'
    '        boxShadow: type === id ? "2px 2px 0 " + DARK : "none",\n'
    '        transition: "all .15s"\n'
    '      }\n'
    '    }, lbl);\n'
    '  }))'
)
changes.append(('type toggle', old1, new1))

# ── 2. Category chips: DARK active → GOLD active, #f5f5f5 → CREAM, borderRadius 12 → 99 ──
old2 = (
    '      style: {\n'
    '        padding: "10px 0",\n'
    '        background: cat === c.id ? DARK : "#f5f5f5",\n'
    '        color: cat === c.id ? "#fff" : DARK,\n'
    '        border: "2px solid ".concat(cat === c.id ? DARK : "transparent"),\n'
    '        borderRadius: 12,\n'
    '        cursor: "pointer",\n'
    '        fontSize: 11,\n'
    '        fontWeight: 800,\n'
    '        boxShadow: cat === c.id ? "0 4px 12px rgba(26,61,31,.25)" : "none",\n'
    '        transition: "all .15s"\n'
    '      }'
)
new2 = (
    '      style: {\n'
    '        padding: "10px 0",\n'
    '        background: cat === c.id ? GOLD : CREAM,\n'
    '        color: DARK,\n'
    '        border: "2px solid " + (cat === c.id ? DARK : "transparent"),\n'
    '        borderRadius: 99,\n'
    '        cursor: "pointer",\n'
    '        fontSize: 11,\n'
    '        fontWeight: 800,\n'
    '        boxShadow: cat === c.id ? "2px 2px 0 " + DARK : "none",\n'
    '        transition: "all .15s"\n'
    '      }'
)
changes.append(('category chips', old2, new2))

# ── 3. Sticky confirm button wrapper ──
old3 = (
    '}), /*#__PURE__*/React.createElement(ConfirmBtn, {\n'
    '    label: "\\u0E1A\\u0E31\\u0E19\\u0E17\\u0E36\\u0E01".concat(type === "income" ? "รายรับ" : "รายจ่าย"),\n'
    '    disabled: !amt || Number(amt) <= 0,\n'
    '    onClick: submit\n'
    '  })))'
)
new3 = (
    '}), /*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      position: "sticky", bottom: 0,\n'
    '      background: CREAM,\n'
    '      paddingTop: 12, paddingBottom: 20,\n'
    '      marginLeft: -20, marginRight: -20,\n'
    '      paddingLeft: 20, paddingRight: 20,\n'
    '      borderTop: "1.5px solid " + DARK + "15"\n'
    '    }\n'
    '  }, /*#__PURE__*/React.createElement(ConfirmBtn, {\n'
    '    label: "\\u0E1A\\u0E31\\u0E19\\u0E17\\u0E36\\u0E01".concat(type === "income" ? "รายรับ" : "รายจ่าย"),\n'
    '    disabled: !amt || Number(amt) <= 0,\n'
    '    onClick: submit\n'
    '  }))))'
)
changes.append(('sticky confirm', old3, new3))

# Apply changes
for name, old, new in changes:
    count = content.count(old)
    print(f'{name}: found {count} times')
    if count == 1:
        content = content.replace(old, new)
        print(f'  → applied')
    else:
        print(f'  → SKIPPED (need exactly 1)')

# Check paren balance
depth = 0
for ch in content:
    if ch == '(': depth += 1
    elif ch == ')': depth -= 1
print(f'\nParen depth: {depth}')

with open('/home/user/sati-assets/payoff-liff.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Saved.')
