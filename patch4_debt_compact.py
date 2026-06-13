#!/usr/bin/env python3
"""Debt page usability:
1. Remove + จดหนี้ใหม่ button from before HeroCard
2. Replace debts.map with compact cards (type label + inline delete icon)
   and add the + button at the very end of the Debt return
"""

with open('/home/user/sati-assets/payoff-liff.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# ── 1. Remove + button from before HeroCard ────────────────────────────────
old1 = (
    '  }, "\\u0E01\\u0E33\\u0E25\\u0E31\\u0E07\\u0E42\\u0E2B\\u0E25\\u0E14\\u0E02\\u0E49\\u0E2D\\u0E21\\u0E39\\u0E25\\u0E2B\\u0E19\\u0E35\\u0E49...")), /*#__PURE__*/React.createElement("button", {\n'
    '    onClick: function onClick() {\n'
    '      return setAddDebtSheet(true);\n'
    '    },\n'
    '    style: {\n'
    '      width: "100%",\n'
    '      padding: "11px 0",\n'
    '      fontSize: 12,\n'
    '      fontWeight: 900,\n'
    '      background: "#fff",\n'
    '      color: DARK,\n'
    '      border: "2px solid ".concat(DARK),\n'
    '      borderRadius: 12,\n'
    '      boxShadow: "2px 2px 0 ".concat(DARK),\n'
    '      cursor: "pointer",\n'
    '      marginBottom: 10\n'
    '    }\n'
    '  }, "+ \\u0E08\\u0E14\\u0E2B\\u0E19\\u0E35\\u0E49\\u0E43\\u0E2B\\u0E21\\u0E48"), /*#__PURE__*/React.createElement(HeroCard, {'
)
new1 = (
    '  }, "\\u0E01\\u0E33\\u0E25\\u0E31\\u0E07\\u0E42\\u0E2B\\u0E25\\u0E14\\u0E02\\u0E49\\u0E2D\\u0E21\\u0E39\\u0E25\\u0E2B\\u0E19\\u0E35\\u0E49...")), /*#__PURE__*/React.createElement(HeroCard, {'
)
changes.append(('remove + button before HeroCard', old1, new1))

# ── 2. Replace full debts.map with compact version + + button at end ────────
old2 = (
    'debts.map(function (d, i) {\n'
    '    return /*#__PURE__*/React.createElement(Card, {\n'
    '      key: i,\n'
    '      style: {\n'
    '        opacity: paidDone[d.name] ? .7 : 1\n'
    '      }\n'
    '    }, /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        display: "flex",\n'
    '        justifyContent: "space-between",\n'
    '        alignItems: "flex-start",\n'
    '        marginBottom: 8\n'
    '      }\n'
    '    }, /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        flex: 1\n'
    '      }\n'
    '    }, /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        display: "flex",\n'
    '        alignItems: "center",\n'
    '        gap: 6,\n'
    '        marginBottom: 2\n'
    '      }\n'
    '    }, /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        fontSize: 12,\n'
    '        fontWeight: 800,\n'
    '        color: DARK\n'
    '      }\n'
    '    }, d.name), d.priority && /*#__PURE__*/React.createElement(Tag, {\n'
    '      color: "#FF6B6B"\n'
    '    }, "\\u26A1 \\u0E08\\u0E48\\u0E32\\u0E22\\u0E01\\u0E48\\u0E2D\\u0E19"), paidDone[d.name] && /*#__PURE__*/React.createElement(Tag, {\n'
    '      color: G\n'
    '    }, "\\u2713 \\u0E3F", paidDone[d.name].toLocaleString())), /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        fontSize: 10,\n'
    '        color: "#888"\n'
    '      }\n'
    '    }, "\\u0E14\\u0E2D\\u0E01\\u0E40\\u0E1A\\u0E35\\u0E49\\u0E22 ", d.rate, "% \\xB7 \\u0E02\\u0E31\\u0E49\\u0E19\\u0E15\\u0E48\\u0E33 \\u0E3F", d.min.toLocaleString(), "/\\u0E40\\u0E14\\u0E37\\u0E2D\\u0E19")), /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        fontSize: 15,\n'
    '        fontWeight: 900,\n'
    '        color: DARK\n'
    '      }\n'
    '    }, "\\u0E3F", d.bal.toLocaleString())), /*#__PURE__*/React.createElement(Bar, {\n'
    '      pct: d.bal / 50000 * 100,\n'
    '      color: d.color\n'
    '    }), /*#__PURE__*/React.createElement("button", {\n'
    '      onClick: function onClick() {\n'
    '        setPayModal(d);\n'
    '        setPayAmt(String(d.min));\n'
    '      },\n'
    '      style: {\n'
    '        width: "100%",\n'
    '        marginTop: 8,\n'
    '        padding: "8px 0",\n'
    '        fontSize: 12,\n'
    '        fontWeight: 800,\n'
    '        background: paidDone[d.name] ? "#f5f5f5" : "".concat(G, "22"),\n'
    '        color: paidDone[d.name] ? "#aaa" : MID,\n'
    '        border: "1.5px solid ".concat(paidDone[d.name] ? "#ddd" : G),\n'
    '        borderRadius: 10,\n'
    '        cursor: "pointer"\n'
    '      }\n'
    '    }, paidDone[d.name] ? "✓ ชำระแล้วเดือนนี้" : "💸 ชำระหนี้งวดนี้"), /*#__PURE__*/React.createElement("button", {\n'
    '      onClick: function onClick() {\n'
    '        return deleteDebt(d);\n'
    '      },\n'
    '      style: {\n'
    '        width: "100%",\n'
    '        marginTop: 6,\n'
    '        padding: "6px 0",\n'
    '        fontSize: 11,\n'
    '        fontWeight: 700,\n'
    '        background: "none",\n'
    '        color: "#bbb",\n'
    '        border: "none",\n'
    '        cursor: "pointer"\n'
    '      }\n'
    '    }, "\\uD83D\\uDDD1\\uFE0F \\u0E25\\u0E1A\\u0E2B\\u0E19\\u0E35\\u0E49\\u0E19\\u0E35\\u0E49"));\n'
    '  }));\n'
    '}'
)
new2 = (
    'debts.map(function (d, i) {\n'
    '    return /*#__PURE__*/React.createElement(Card, {\n'
    '      key: i,\n'
    '      style: {\n'
    '        padding: "10px 14px",\n'
    '        opacity: paidDone[d.name] ? .7 : 1\n'
    '      }\n'
    # Row 1: name + priority tag | balance
    '    }, /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        display: "flex",\n'
    '        justifyContent: "space-between",\n'
    '        alignItems: "center",\n'
    '        marginBottom: 2\n'
    '      }\n'
    '    }, /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        display: "flex",\n'
    '        alignItems: "center",\n'
    '        gap: 6\n'
    '      }\n'
    '    }, /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        fontSize: 12,\n'
    '        fontWeight: 800,\n'
    '        color: DARK\n'
    '      }\n'
    '    }, d.name), d.priority && /*#__PURE__*/React.createElement(Tag, {\n'
    '      color: "#FF6B6B"\n'
    '    }, "\\u26A1"), paidDone[d.name] && /*#__PURE__*/React.createElement(Tag, {\n'
    '      color: G\n'
    '    }, "\\u2713")), /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        fontSize: 14,\n'
    '        fontWeight: 900,\n'
    '        color: DARK\n'
    '      }\n'
    # Row 2: type label + rate + min
    '    }, "\\u0E3F", d.bal.toLocaleString())), /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        fontSize: 10,\n'
    '        color: "#888",\n'
    '        marginBottom: 6\n'
    '      }\n'
    '    }, d.label || d.type, " \\xB7 \\u0E14\\u0E2D\\u0E01 ", d.rate, "% \\xB7 \\u0E02\\u0E31\\u0E49\\u0E19\\u0E15\\u0E48\\u0E33 \\u0E3F", d.min.toLocaleString()), /*#__PURE__*/React.createElement(Bar, {\n'
    '      pct: d.bal / 50000 * 100,\n'
    '      color: d.color\n'
    # Row 3: pay button + small delete icon in flex row
    '    }), /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        display: "flex",\n'
    '        gap: 8,\n'
    '        marginTop: 8,\n'
    '        alignItems: "center"\n'
    '      }\n'
    '    }, /*#__PURE__*/React.createElement("button", {\n'
    '      onClick: function onClick() {\n'
    '        setPayModal(d);\n'
    '        setPayAmt(String(d.min));\n'
    '      },\n'
    '      style: {\n'
    '        flex: 1,\n'
    '        padding: "7px 0",\n'
    '        fontSize: 12,\n'
    '        fontWeight: 800,\n'
    '        background: paidDone[d.name] ? "#f5f5f5" : "".concat(G, "22"),\n'
    '        color: paidDone[d.name] ? "#aaa" : MID,\n'
    '        border: "1.5px solid ".concat(paidDone[d.name] ? "#ddd" : G),\n'
    '        borderRadius: 10,\n'
    '        cursor: "pointer"\n'
    '      }\n'
    '    }, paidDone[d.name] ? "\\u2713 \\u0E0A\\u0E33\\u0E23\\u0E30\\u0E41\\u0E25\\u0E49\\u0E27" : "\\uD83D\\uDCB8 \\u0E0A\\u0E33\\u0E23\\u0E30\\u0E2B\\u0E19\\u0E35\\u0E49"), /*#__PURE__*/React.createElement("button", {\n'
    '      onClick: function onClick() {\n'
    '        return deleteDebt(d);\n'
    '      },\n'
    '      style: {\n'
    '        width: 32,\n'
    '        height: 32,\n'
    '        padding: 0,\n'
    '        fontSize: 15,\n'
    '        background: "none",\n'
    '        color: "#ccc",\n'
    '        border: "1px solid #ddd",\n'
    '        borderRadius: 8,\n'
    '        cursor: "pointer",\n'
    '        flexShrink: 0\n'
    '      }\n'
    '    }, "\\uD83D\\uDDD1\\uFE0F")));\n'
    '  }), /*#__PURE__*/React.createElement("button", {\n'
    '    onClick: function onClick() {\n'
    '      return setAddDebtSheet(true);\n'
    '    },\n'
    '    style: {\n'
    '      width: "100%",\n'
    '      padding: "11px 0",\n'
    '      fontSize: 12,\n'
    '      fontWeight: 900,\n'
    '      background: "#fff",\n'
    '      color: DARK,\n'
    '      border: "2px solid ".concat(DARK),\n'
    '      borderRadius: 12,\n'
    '      boxShadow: "2px 2px 0 ".concat(DARK),\n'
    '      cursor: "pointer",\n'
    '      marginTop: 10\n'
    '    }\n'
    '  }, "+ \\u0E08\\u0E14\\u0E2B\\u0E19\\u0E35\\u0E49\\u0E43\\u0E2B\\u0E21\\u0E48"));\n'
    '}'
)
changes.append(('compact debts.map + move + button', old2, new2))

# Apply all changes
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
    print('Saved patch4.')
elif depth != 0:
    print('ERROR: paren imbalance, not saving')
else:
    print('WARNING: some patterns not found, saving anyway')
    with open('/home/user/sati-assets/payoff-liff.html', 'w', encoding='utf-8') as f:
        f.write(content)
