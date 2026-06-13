#!/usr/bin/env python3
with open('/home/user/sati-assets/payoff-liff.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Structure:
#   txns.map(cb) → } closes cb, ) closes .map, ) closes Card, ) closes wrapper, ; return
# Old: "✕"));\n  })));\n}    (2 parens line1, 3 parens line2)
# New: insert FAB after Card closes, before wrapper closes
#   "✕"));\n  })),\n  FAB));\n}    (2 line1, 2 line2, FAB opens+closes, 2 line3)

old = (
    '    }, "\\u2715"));\n'
    '  })));\n'
    '}\n'
    '\n'
    '// ══════════════════════════════════════════════════════════════════════════════\n'
    '// SAVE'
)
new = (
    '    }, "\\u2715"));\n'
    '  })),\n'
    '  /*#__PURE__*/React.createElement("button", {\n'
    '    onClick: function() { setSheet(true); },\n'
    '    style: {\n'
    '      position: "fixed", right: 20, bottom: 88,\n'
    '      width: 52, height: 52,\n'
    '      borderRadius: 99,\n'
    '      background: GOLD, color: DARK,\n'
    '      border: "2.5px solid " + DARK,\n'
    '      fontSize: 24, fontWeight: 900,\n'
    '      cursor: "pointer",\n'
    '      boxShadow: "3px 3px 0 " + DARK,\n'
    '      zIndex: 50,\n'
    '      display: "flex", alignItems: "center", justifyContent: "center",\n'
    '      lineHeight: 1\n'
    '    }\n'
    '  }, "+"));\n'
    '}\n'
    '\n'
    '// ══════════════════════════════════════════════════════════════════════════════\n'
    '// SAVE'
)

count = content.count(old)
print(f'Pattern found: {count} times')

if count == 1:
    content = content.replace(old, new)
    depth = 0
    for ch in content:
        if ch == '(': depth += 1
        elif ch == ')': depth -= 1
    print(f'Paren depth: {depth}')
    if depth == 0:
        with open('/home/user/sati-assets/payoff-liff.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Saved.')
    else:
        print('ERROR: paren imbalance, not saving')
else:
    print('ERROR: pattern not unique')
