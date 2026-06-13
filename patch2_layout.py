#!/usr/bin/env python3
"""Restructure CashFlow layout:
- Remove view tabs
- Show category card always (no duplicate inner headers)
- Show transaction list always
- Move allocation card to bottom (month only)
"""
with open('/home/user/sati-assets/payoff-liff.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Identify the exact boundaries of the block to replace
sec_start = content.find('// ── Cash breakdown section\n')
fab_start = content.find(
    '/*#__PURE__*/React.createElement("button", {\n    onClick: function() { setSheet(true); }',
    sec_start
)

if sec_start == -1 or fab_start == -1:
    print('ERROR: could not find boundaries')
    print(f'  sec_start={sec_start}, fab_start={fab_start}')
    exit(1)

print(f'Block: bytes {sec_start} → {fab_start}')
old_block = content[sec_start:fab_start]
print(f'Old block length: {len(old_block)} bytes')

# Count paren balance of old block (should be 0)
depth = 0
for ch in old_block:
    if ch == '(': depth += 1
    elif ch == ')': depth -= 1
print(f'Old block paren depth: {depth}')

# Build the new block
# Cats content (from the existing summary card, minus the inner duplicate headers)
cats_content = (
    'cats.length === 0 ? /*#__PURE__*/React.createElement("div", {\n'
    '    style: { textAlign: "center", padding: "16px 0" }\n'
    '  },\n'
    '  /*#__PURE__*/React.createElement(SalungMascot, { mood: "budgeting", size: 56 }),\n'
    '  /*#__PURE__*/React.createElement("div", {\n'
    '    style: { fontSize: 12, fontWeight: 900, color: DARK, marginTop: 8, marginBottom: 4 }\n'
    '  }, "\\u0E22\\u0E31\\u0E07\\u0E44\\u0E21\\u0E48\\u0E21\\u0E35\\u0E23\\u0E32\\u0E22\\u0E08\\u0E48\\u0E32\\u0E22\\u0E41\\u0E22\\u0E01\\u0E2B\\u0E21\\u0E27\\u0E14"),\n'
    '  /*#__PURE__*/React.createElement("div", {\n'
    '    style: { fontSize: 11, color: MID, fontWeight: 700, lineHeight: 1.6 }\n'
    '  }, "\\u0E1A\\u0E31\\u0E19\\u0E17\\u0E36\\u0E01\\u0E23\\u0E32\\u0E22\\u0E01\\u0E32\\u0E23\\u0E41\\u0E23\\u0E01\\u0E01\\u0E48\\u0E2D\\u0E19 \\u0E41\\u0E25\\u0E49\\u0E27 Salung \\u0E08\\u0E30\\u0E2A\\u0E23\\u0E38\\u0E1B\\u0E43\\u0E2B\\u0E49\\u0E40\\u0E2D\\u0E07 \\uD83E\\uDDFE")\n'
    ') : cats.map(function (c) {\n'
    '    var pct = c.max > 0 ? Math.round(c.val / c.max * 100) : 0;\n'
    '    return /*#__PURE__*/React.createElement("div", {\n'
    '      key: c.label,\n'
    '      style: { marginBottom: 10 }\n'
    '    },\n'
    '      /*#__PURE__*/React.createElement("div", {\n'
    '        style: { display: "flex", alignItems: "center", gap: 8, marginBottom: 4 }\n'
    '      },\n'
    '        /*#__PURE__*/React.createElement("span", { style: { fontSize: 16, width: 22, textAlign: "center", flexShrink: 0 } }, c.icon),\n'
    '        /*#__PURE__*/React.createElement("span", {\n'
    '          style: { flex: 1, fontSize: 12, fontWeight: 700, color: spicy ? "#ccc" : DARK }\n'
    '        }, c.label),\n'
    '        /*#__PURE__*/React.createElement("span", {\n'
    '          style: { fontSize: 10, fontWeight: 700, color: spicy ? "#88aa88" : "#aaa", marginRight: 6 }\n'
    '        }, pct + "%"),\n'
    '        /*#__PURE__*/React.createElement("span", {\n'
    '          style: { fontSize: 12, fontWeight: 900, color: spicy ? "#FF9999" : "#E53E3E" }\n'
    '        }, "\\u0E3F", c.val.toLocaleString())\n'
    '      ),\n'
    '      /*#__PURE__*/React.createElement(Bar, { pct: Math.min(100, pct), color: c.color })\n'
    '    );\n'
    '  })'
)

txns_content = (
    'React.createElement(SectionHeader, { icon: "\\uD83D\\uDCCB", text: "\\u0E23\\u0E32\\u0E22\\u0E01\\u0E32\\u0E23\\u0E25\\u0E48\\u0E32\\u0E2A\\u0E38\\u0E14", spicy: spicy }),\n'
    '  txns.length === 0 && /*#__PURE__*/React.createElement("div", {\n'
    '    style: { textAlign: "center", padding: "20px 16px 24px" }\n'
    '  },\n'
    '    /*#__PURE__*/React.createElement(SalungMascot, { mood: "budgeting", size: 64 }),\n'
    '    /*#__PURE__*/React.createElement("div", {\n'
    '      style: { fontSize: 13, fontWeight: 900, color: DARK, marginTop: 10, marginBottom: 4 }\n'
    '    }, "\\u0E22\\u0E31\\u0E07\\u0E44\\u0E21\\u0E48\\u0E21\\u0E35\\u0E23\\u0E32\\u0E22\\u0E01\\u0E32\\u0E23\\u0E27\\u0E31\\u0E19\\u0E19\\u0E35\\u0E49"),\n'
    '    /*#__PURE__*/React.createElement("div", {\n'
    '      style: { fontSize: 11, color: MID, fontWeight: 700, lineHeight: 1.6, marginBottom: 12 }\n'
    '    }, "\\u0E40\\u0E23\\u0E34\\u0E48\\u0E21\\u0E08\\u0E32\\u0E01\\u0E01\\u0E32\\u0E41\\u0E1F\\u0E41\\u0E01\\u0E49\\u0E27\\u0E41\\u0E23\\u0E01\\u0E01\\u0E47\\u0E44\\u0E14\\u0E49 Salung \\u0E08\\u0E30\\u0E08\\u0E33\\u0E43\\u0E2B\\u0E49\\u0E40\\u0E2D\\u0E07 \\u2615"),\n'
    '    /*#__PURE__*/React.createElement("button", {\n'
    '      onClick: function() { setSheet(true); },\n'
    '      style: {\n'
    '        padding: "10px 24px", fontSize: 13, fontWeight: 900,\n'
    '        background: GOLD, color: DARK, border: "2px solid " + DARK,\n'
    '        borderRadius: 99, cursor: "pointer", boxShadow: "2px 2px 0 " + DARK\n'
    '      }\n'
    '    }, "+ \\u0E1A\\u0E31\\u0E19\\u0E17\\u0E36\\u0E01\\u0E23\\u0E32\\u0E22\\u0E01\\u0E32\\u0E23")\n'
    '  ),\n'
    '  txns.map(function (t, i) {\n'
    '    return /*#__PURE__*/React.createElement("div", {\n'
    '      key: i,\n'
    '      style: {\n'
    '        display: "flex",\n'
    '        alignItems: "center",\n'
    '        gap: 10,\n'
    '        padding: "9px 0",\n'
    '        borderBottom: i < txns.length - 1 ? "1px solid #f0f0f0" : "none"\n'
    '      }\n'
    '    }, /*#__PURE__*/React.createElement("span", {\n'
    '      style: {\n'
    '        fontSize: 16\n'
    '      }\n'
    '    }, t.cat), /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        flex: 1\n'
    '      }\n'
    '    }, /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        fontSize: 12,\n'
    '        fontWeight: 700,\n'
    '        color: DARK\n'
    '      }\n'
    '    }, t.note), /*#__PURE__*/React.createElement("div", {\n'
    '      style: {\n'
    '        fontSize: 10,\n'
    '        color: "#aaa"\n'
    '      }\n'
    '    }, t.time)), /*#__PURE__*/React.createElement("span", {\n'
    '      style: {\n'
    '        fontSize: 13,\n'
    '        fontWeight: 900,\n'
    '        color: t.amt > 0 ? G : "#E53E3E",\n'
    '        marginRight: 4\n'
    '      }\n'
    '    }, t.amt > 0 ? "+" : "", "\\u0E3F", Math.abs(t.amt).toLocaleString()), /*#__PURE__*/React.createElement("button", {\n'
    '      onClick: function onClick() {\n'
    '        return deleteTx(t, i);\n'
    '      },\n'
    '      style: {\n'
    '        background: "none",\n'
    '        border: "none",\n'
    '        cursor: "pointer",\n'
    '        fontSize: 14,\n'
    '        color: "#ccc",\n'
    '        padding: "2px 4px",\n'
    '        flexShrink: 0\n'
    '      }\n'
    '    }, "\\u2715"));\n'
    '  })'
)

alloc_content = (
    '/*#__PURE__*/React.createElement("div", {\n'
    '    style: { display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12 }\n'
    '  }, /*#__PURE__*/React.createElement("div", {\n'
    '    style: { fontSize: 12, fontWeight: 900, color: spicy ? G : DARK }\n'
    '  }, "\\uD83D\\uDCB0 \\u0E40\\u0E07\\u0E34\\u0E19\\u0E40\\u0E14\\u0E37\\u0E2D\\u0E19\\u0E19\\u0E35\\u0E49\\u0E44\\u0E1B\\u0E44\\u0E2B\\u0E19\\u0E1A\\u0E49\\u0E32\\u0E07?"),\n'
    '  allocLoading && /*#__PURE__*/React.createElement("div", {\n'
    '    style: { fontSize: 10, color: "#aaa" }\n'
    '  }, "\\u0E01\\u0E33\\u0E25\\u0E31\\u0E07\\u0E42\\u0E2B\\u0E25\\u0E14..."),\n'
    '  !allocLoading && alloc.length === 0 && /*#__PURE__*/React.createElement("div", {\n'
    '    style: { fontSize: 10, color: "#aaa" }\n'
    '  }, "\\u0E22\\u0E31\\u0E07\\u0E44\\u0E21\\u0E48\\u0E21\\u0E35\\u0E02\\u0E49\\u0E2D\\u0E21\\u0E39\\u0E25\\u0E40\\u0E14\\u0E37\\u0E2D\\u0E19\\u0E19\\u0E35\\u0E49")),\n'
    '  alloc.map(function (row, i) {\n'
    '    var _alloc$find;\n'
    '    return /*#__PURE__*/React.createElement("div", { key: i, style: { marginBottom: 8 } },\n'
    '      /*#__PURE__*/React.createElement("div", {\n'
    '        style: { display: "flex", justifyContent: "space-between", marginBottom: 3 }\n'
    '      },\n'
    '        /*#__PURE__*/React.createElement("div", {\n'
    '          style: { display: "flex", gap: 6, alignItems: "center" }\n'
    '        },\n'
    '          /*#__PURE__*/React.createElement("span", { style: { fontSize: 13 } }, row.icon),\n'
    '          /*#__PURE__*/React.createElement("span", {\n'
    '            style: { fontSize: 12, fontWeight: 700, color: spicy ? "#ccc" : DARK }\n'
    '          }, row.label)\n'
    '        ),\n'
    '        /*#__PURE__*/React.createElement("span", {\n'
    '          style: { fontSize: 12, fontWeight: 900, color: row.amt > 0 ? G : spicy ? "#FF9999" : "#E53E3E" }\n'
    '        }, row.amt > 0 ? "+" : "-", "\\u0E3F", Math.abs(row.amt).toLocaleString())\n'
    '      ),\n'
    '      /*#__PURE__*/React.createElement(Bar, {\n'
    '        pct: alloc.length ? Math.abs(row.amt) / Math.max(1, ((_alloc$find = alloc.find(function(r){ return r.label === "\\u0E23\\u0E32\\u0E22\\u0E23\\u0E31\\u0E1A"; })) === null || _alloc$find === void 0 ? void 0 : _alloc$find.amt) || 1) * 100 : 0,\n'
    '        color: row.color\n'
    '      })\n'
    '    );\n'
    '  }),\n'
    '  /*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      borderTop: "2px dashed " + (spicy ? "#444" : "#ccc"),\n'
    '      marginTop: 10, paddingTop: 10,\n'
    '      display: "flex", justifyContent: "space-between", alignItems: "center"\n'
    '    }\n'
    '  },\n'
    '    /*#__PURE__*/React.createElement("div", null,\n'
    '      /*#__PURE__*/React.createElement("div", {\n'
    '        style: { fontSize: 12, fontWeight: 800, color: spicy ? "#aaa" : "#666" }\n'
    '      }, "\\uD83D\\uDCB8 \\u0E43\\u0E0A\\u0E49\\u0E08\\u0E48\\u0E32\\u0E22\\u0E44\\u0E14\\u0E49\\u0E08\\u0E23\\u0E34\\u0E07"),\n'
    '      /*#__PURE__*/React.createElement("div", {\n'
    '        style: { fontSize: 10, color: "#aaa" }\n'
    '      }, "\\u0E43\\u0E0A\\u0E49\\u0E41\\u0E25\\u0E49\\u0E27 \\u0E3F", d.exp.toLocaleString(), " \\xB7 \\u0E40\\u0E2B\\u0E25\\u0E37\\u0E2D \\u0E3F", Math.max(0, d.net).toLocaleString())\n'
    '    ),\n'
    '    /*#__PURE__*/React.createElement("div", {\n'
    '      style: { fontSize: 22, fontWeight: 900, color: spicy ? G : DARK }\n'
    '    }, "\\u0E3F", Math.max(0, d.net).toLocaleString())\n'
    '  ),\n'
    '  /*#__PURE__*/React.createElement(Bar, { pct: d.inc > 0 ? d.exp / d.inc * 100 : 0, color: G, height: 10 })'
)

new_block = (
    '// ── Category section\n'
    '  /*#__PURE__*/React.createElement(SectionHeader, { icon: "\\uD83D\\uDCB8", text: "\\u0E40\\u0E07\\u0E34\\u0E19\\u0E44\\u0E2B\\u0E25\\u0E44\\u0E1B\\u0E17\\u0E32\\u0E07\\u0E44\\u0E2B\\u0E19 \\u2728", spicy: spicy }),\n'
    '  /*#__PURE__*/React.createElement(Card, null,\n'
    '    ' + cats_content + '\n'
    '  ),\n'
    '  // ── Transaction list\n'
    '  /*#__PURE__*/React.createElement(Card, {\n'
    '    style: {\n'
    '      padding: "12px 12px 6px"\n'
    '    }\n'
    '  },\n'
    '  ' + txns_content + '\n'
    '  ),\n'
    '  // ── Monthly breakdown (at bottom)\n'
    '  period === "month" && /*#__PURE__*/React.createElement(React.Fragment, null,\n'
    '    /*#__PURE__*/React.createElement(SectionHeader, { icon: "\\uD83D\\uDCB0", text: "\\u0E40\\u0E07\\u0E34\\u0E19\\u0E40\\u0E14\\u0E37\\u0E2D\\u0E19\\u0E19\\u0E35\\u0E49\\u0E44\\u0E1B\\u0E44\\u0E2B\\u0E19\\u0E1A\\u0E49\\u0E32\\u0E07?", spicy: spicy }),\n'
    '    /*#__PURE__*/React.createElement(Card, {\n'
    '      style: { background: spicy ? DARK : CREAM }\n'
    '    },\n'
    '    ' + alloc_content + '\n'
    '    )\n'
    '  ),\n'
    '  '
)

# Count paren balance of new block
depth_new = 0
for ch in new_block:
    if ch == '(': depth_new += 1
    elif ch == ')': depth_new -= 1
print(f'New block paren depth: {depth_new}')

if depth_new != depth:
    print(f'ERROR: paren mismatch old={depth} new={depth_new}')
    exit(1)

# Build new content
new_content = content[:sec_start] + new_block + content[fab_start:]

# Final paren check on whole file
file_depth = 0
for ch in new_content:
    if ch == '(': file_depth += 1
    elif ch == ')': file_depth -= 1
print(f'File paren depth: {file_depth}')

if file_depth != 0:
    print('ERROR: file paren imbalance, not saving')
    exit(1)

with open('/home/user/sati-assets/payoff-liff.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Saved patch2.')
