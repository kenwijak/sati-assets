#!/usr/bin/env python3
"""Simple targeted fixes:
1. Expand CAT_MAP with missing category labels
2. Fix newTx category_id to use mapped value
3. Reduce header padding + mascot size slightly
4. Increase scroll area bottom padding (FAB clearance)
5. Reduce FAB from 52px to 44px
"""
with open('/home/user/sati-assets/payoff-liff.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# ── 1. Expand CAT_MAP ──────────────────────────────────────────────────────
old1 = '''\
  var CAT_MAP = {
    food: { label: "อาหาร", color: "#FF6B6B", icon: "🍚" },
    travel: { label: "เดินทาง", color: "#4ECDC4", icon: "🚇" },
    transport: { label: "เดินทาง", color: "#4ECDC4", icon: "🚇" },
    shop: { label: "ช้อปปิ้ง", color: G, icon: "🛍️" },
    shopping: { label: "ช้อปปิ้ง", color: G, icon: "🛍️" },
    entertain: { label: "บันเทิง", color: GOLD, icon: "🎮" },
    entertainment: { label: "บันเทิง", color: GOLD, icon: "🎮" },
    health: { label: "สุขภาพ", color: "#FF9F43", icon: "💊" },
    bill: { label: "บิล/ยูทิลิตี้", color: "#A29BFE", icon: "📄" },
    utilities: { label: "บิล/ยูทิลิตี้", color: "#A29BFE", icon: "📄" },
    other: { label: "อื่นๆ", color: "#DFE6E9", icon: "📦" }
  };'''
new1 = '''\
  var CAT_MAP = {
    food: { label: "อาหาร", color: "#FF6B6B", icon: "🍚" },
    travel: { label: "เดินทาง", color: "#4ECDC4", icon: "🚆" },
    transport: { label: "เดินทาง", color: "#4ECDC4", icon: "🚆" },
    shop: { label: "ช้อปปิ้ง", color: G, icon: "🛍️" },
    shopping: { label: "ช้อปปิ้ง", color: G, icon: "🛍️" },
    entertain: { label: "บันเทิง", color: GOLD, icon: "🎮" },
    entertainment: { label: "บันเทิง", color: GOLD, icon: "🎮" },
    health: { label: "สุขภาพ", color: "#FF9F43", icon: "💊" },
    bill: { label: "บิล/ค่าน้ำไฟ", color: "#A29BFE", icon: "🧾" },
    utilities: { label: "บิล/ค่าน้ำไฟ", color: "#A29BFE", icon: "🧾" },
    education: { label: "การศึกษา", color: "#74B9FF", icon: "📚" },
    savings: { label: "ออมเงิน", color: G, icon: "🌱" },
    saving: { label: "ออมเงิน", color: G, icon: "🌱" },
    debt_auto: { label: "ผ่อนรถ", color: "#FDCB6E", icon: "🚗" },
    auto_debt: { label: "ผ่อนรถ", color: "#FDCB6E", icon: "🚗" },
    car_loan: { label: "ผ่อนรถ", color: "#FDCB6E", icon: "🚗" },
    debt_card: { label: "บัตรเครดิต", color: "#A29BFE", icon: "💳" },
    credit_card: { label: "บัตรเครดิต", color: "#A29BFE", icon: "💳" },
    income: { label: "รายรับ", color: G, icon: "💰" },
    other: { label: "อื่น ๆ", color: "#DFE6E9", icon: "📦" }
  };'''
changes.append(('CAT_MAP expand', old1, new1))

# ── 2. newTx category_id: use mapped value not raw cat ──────────────────────
old2 = '        category_id: cat,\n        note: note || cat,'
new2 = '        category_id: category_id,\n        note: note || cat,'
changes.append(('newTx category_id fix', old2, new2))

# ── 3. Header: smaller mascot (44→40) and slightly less padding ─────────────
old3 = (
    '      padding: "10px 18px 14px",\n'
    '      display: "flex",\n'
    '      justifyContent: "space-between",\n'
    '      alignItems: "center",\n'
    '      background: spicy ? "#0d1a0e" : CREAM,\n'
    '      borderBottom: "2.5px solid " + DARK,\n'
    '      transition: "background .3s"'
)
new3 = (
    '      padding: "8px 16px 10px",\n'
    '      display: "flex",\n'
    '      justifyContent: "space-between",\n'
    '      alignItems: "center",\n'
    '      background: spicy ? "#0d1a0e" : CREAM,\n'
    '      borderBottom: "2.5px solid " + DARK,\n'
    '      transition: "background .3s"'
)
changes.append(('header padding reduce', old3, new3))

old3b = '/*#__PURE__*/React.createElement(SalungMascot, { mood: spicy ? "cool" : "happy", size: 44 }),'
new3b = '/*#__PURE__*/React.createElement(SalungMascot, { mood: spicy ? "cool" : "happy", size: 40 }),'
changes.append(('header mascot size', old3b, new3b))

old3c = '      style: { fontSize: 18, fontWeight: 900, color: spicy ? G : DARK, lineHeight: 1.1, letterSpacing: "-.01em" }\n      }, "Salung 👋")'
new3c = '      style: { fontSize: 16, fontWeight: 900, color: spicy ? G : DARK, lineHeight: 1.1, letterSpacing: "-.01em" }\n      }, "Salung 👋")'
changes.append(('header title size', old3c, new3c))

# ── 4. Main scroll area: more bottom padding for FAB clearance ──────────────
old4 = (
    '    id: "main-scroll",\n'
    '    style: {\n'
    '      flex: 1,\n'
    '      padding: "12px 16px 16px",\n'
    '      overflowY: "auto"\n'
    '    }'
)
new4 = (
    '    id: "main-scroll",\n'
    '    style: {\n'
    '      flex: 1,\n'
    '      padding: "12px 16px 100px",\n'
    '      overflowY: "auto"\n'
    '    }'
)
changes.append(('scroll bottom padding', old4, new4))

# ── 5. FAB: reduce size 52→44 ────────────────────────────────────────────────
old5 = (
    '      position: "fixed", right: 20, bottom: 88,\n'
    '      width: 52, height: 52,\n'
    '      borderRadius: 99,\n'
    '      background: GOLD, color: DARK,\n'
    '      border: "2.5px solid " + DARK,\n'
    '      fontSize: 24, fontWeight: 900,'
)
new5 = (
    '      position: "fixed", right: 20, bottom: 88,\n'
    '      width: 44, height: 44,\n'
    '      borderRadius: 99,\n'
    '      background: GOLD, color: DARK,\n'
    '      border: "2.5px solid " + DARK,\n'
    '      fontSize: 22, fontWeight: 900,'
)
changes.append(('FAB size reduce', old5, new5))

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

# Paren check
depth = 0
for ch in content:
    if ch == '(': depth += 1
    elif ch == ')': depth -= 1

print(f'\nParen depth: {depth}')
if depth == 0 and ok:
    with open('/home/user/sati-assets/payoff-liff.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Saved patch1.')
elif depth != 0:
    print('ERROR: paren imbalance, not saving')
else:
    print('Saved with warnings (some patterns not found).')
    with open('/home/user/sati-assets/payoff-liff.html', 'w', encoding='utf-8') as f:
        f.write(content)
