#!/usr/bin/env python3
with open('/home/user/sati-assets/payoff-liff.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = (
    '/*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      display: "flex",\n'
    '      justifyContent: "space-between",\n'
    '      marginBottom: 8\n'
    '    }\n'
    '  }, /*#__PURE__*/React.createElement("span", {\n'
    '    style: {\n'
    '      fontSize: 12,\n'
    '      fontWeight: 800,\n'
    '      color: DARK\n'
    '    }\n'
    '  }, "\\u0E23\\u0E32\\u0E22\\u0E01\\u0E32\\u0E23"), /*#__PURE__*/React.createElement("span", {\n'
    '    style: {\n'
    '      fontSize: 10,\n'
    '      color: "#aaa"\n'
    '    }\n'
    '  }, "\\u2190 \\u0E40\\u0E25\\u0E37\\u0E48\\u0E2D\\u0E19\\u0E0B\\u0E49\\u0E32\\u0E22\\u0E40\\u0E1E\\u0E37\\u0E48\\u0E2D\\u0E25\\u0E1A")),\n'
    '  txns.length === 0 && /*#__PURE__*/React.createElement("div", {\n'
    '    style: { textAlign: "center", padding: "20px 16px 12px" }\n'
    '  },\n'
    '    /*#__PURE__*/React.createElement(SalungMascot, { mood: "budgeting", size: 64 }),\n'
    '    /*#__PURE__*/React.createElement("div", {\n'
    '      style: { fontSize: 13, fontWeight: 900, color: DARK, marginTop: 10, marginBottom: 4 }\n'
    '    }, "\\u0E22\\u0E31\\u0E07\\u0E44\\u0E21\\u0E48\\u0E21\\u0E35\\u0E23\\u0E32\\u0E22\\u0E01\\u0E32\\u0E23\\u0E27\\u0E31\\u0E19\\u0E19\\u0E35\\u0E49"),\n'
    '    /*#__PURE__*/React.createElement("div", {\n'
    '      style: { fontSize: 11, color: MID, fontWeight: 700, lineHeight: 1.6 }\n'
    '    }, "\\u0E40\\u0E23\\u0E34\\u0E48\\u0E21\\u0E08\\u0E32\\u0E01\\u0E01\\u0E32\\u0E41\\u0E1F\\u0E41\\u0E01\\u0E49\\u0E27\\u0E41\\u0E23\\u0E01\\u0E01\\u0E47\\u0E44\\u0E14\\u0E49 \\u2615 Salung \\u0E08\\u0E30\\u0E08\\u0E33\\u0E43\\u0E2B\\u0E49\\u0E40\\u0E2D\\u0E07")\n'
    '  ),'
)

new = (
    'React.createElement(SectionHeader, { icon: "\U0001F4CB", text: "รายการล่าสุด", spicy: spicy }),\n'
    '  txns.length === 0 && /*#__PURE__*/React.createElement("div", {\n'
    '    style: { textAlign: "center", padding: "20px 16px 24px" }\n'
    '  },\n'
    '    /*#__PURE__*/React.createElement(SalungMascot, { mood: "budgeting", size: 64 }),\n'
    '    /*#__PURE__*/React.createElement("div", {\n'
    '      style: { fontSize: 13, fontWeight: 900, color: DARK, marginTop: 10, marginBottom: 4 }\n'
    '    }, "ยังไม่มีรายการวันนี้"),\n'
    '    /*#__PURE__*/React.createElement("div", {\n'
    '      style: { fontSize: 11, color: MID, fontWeight: 700, lineHeight: 1.6, marginBottom: 12 }\n'
    '    }, "เริ่มจากกาแฟแก้วแรกก็ได้ Salung จะจำให้เอง ☕"),\n'
    '    /*#__PURE__*/React.createElement("button", {\n'
    '      onClick: function() { setSheet(true); },\n'
    '      style: {\n'
    '        padding: "10px 24px", fontSize: 13, fontWeight: 900,\n'
    '        background: GOLD, color: DARK, border: "2px solid " + DARK,\n'
    '        borderRadius: 99, cursor: "pointer", boxShadow: "2px 2px 0 " + DARK\n'
    '      }\n'
    '    }, "+ บันทึกรายการ")\n'
    '  ),'
)

count = content.count(old)
print(f'Pattern found: {count} times')

if count == 1:
    new_content = content.replace(old, new)
    with open('/home/user/sati-assets/payoff-liff.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Done! File saved.')
else:
    print('ERROR: Pattern not found or found multiple times')
    # Debug: find partial match
    partial = '}, "\\u0E23\\u0E32\\u0E22\\u0E01\\u0E32\\u0E23")'
    pos = content.find(partial, 60000)
    print(f'Partial search for รายการ span closing: {pos}')
    if pos != -1:
        print(repr(content[pos-20:pos+50]))
