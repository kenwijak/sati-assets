#!/usr/bin/env python3
"""Remove duplicate profile card from More component.
Keep only HeroCard at top, remove the second Face-based profile card.
"""
with open('/home/user/sati-assets/payoff-liff.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The More component return has:
# 1. HeroCard (keep)
# 2. Card with Face + "สวัสดี name! 👋" + zone + tag (REMOVE)
# 3. Card with menu items (keep)
#
# Old:
# return React.createElement("div", null,
#   HeroCard,
#   Card(Face + greeting + zone),    <- remove this
#   Card(menu items)
# )
#
# Old pattern: HeroCard}) followed by , Card(Face...)
# ending before the menu items Card

old = (
    '}), /*#__PURE__*/React.createElement(Card, {\n'
    '    style: {\n'
    '      background: spicy ? DARK : CREAM\n'
    '    }\n'
    '  }, /*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      display: "flex",\n'
    '      alignItems: "center",\n'
    '      gap: 12\n'
    '    }\n'
    '  }, /*#__PURE__*/React.createElement(Face, {\n'
    '    size: 46,\n'
    '    mood: spicy ? "excited" : "happy"\n'
    '  }), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      fontSize: 14,\n'
    '      fontWeight: 900,\n'
    '      color: spicy ? G : DARK\n'
    '    }\n'
    '  }, "\\u0E2A\\u0E27\\u0E31\\u0E2A\\u0E14\\u0E35 ", profile.name, "! \\uD83D\\uDC4B"), /*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      fontSize: 11,\n'
    '      color: "#888"\n'
    '    }\n'
    '  }, "Zone: ", profile.zone), /*#__PURE__*/React.createElement("div", {\n'
    '    style: {\n'
    '      marginTop: 4\n'
    '    }\n'
    '  }, /*#__PURE__*/React.createElement(Tag, {\n'
    '    color: spicy ? G : GOLD\n'
    '  }, profile.zone))))), /*#__PURE__*/React.createElement(Card, {'
)
new = (
    '}), /*#__PURE__*/React.createElement(Card, {'
)

count = content.count(old)
print(f'Duplicate profile card pattern: found {count} times')

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
        print('Saved patch3.')
    else:
        print('ERROR: paren imbalance, not saving')
else:
    print('Pattern not found. Trying debug...')
    # Find the HeroCard in More
    pos = content.find('function More(')
    if pos != -1:
        more_section = content[pos:pos+3000]
        face_pos = more_section.find('React.createElement(Face,')
        print(f'  Face in More at offset: {face_pos}')
        if face_pos != -1:
            print(repr(more_section[face_pos-200:face_pos+200]))
