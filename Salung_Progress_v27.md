# Salung — Progress & Brand File

อัปเดตล่าสุด: 11 มิถุนายน 2026 (v27)

> เดิมชื่อ "Sati / พี่สติ" → รีแบรนด์เป็น "Salung / สลึง" หลังบ้านเหมือนเดิม เปลี่ยนแค่หน้าบ้าน

-----

## Vision

Salung ไม่ใช่แค่ debt app — เป็น personal finance companion ที่อยู่กับ user ตั้งแต่ติดลบจนถึงอิสระทางการเงิน

**Core metaphor:** ถุงเงินที่โตไปพร้อม user — ยิ่ง user มีเงินมาก Salung ยิ่งตัวอ้วนขึ้น

**Scope:** หนี้ / รายรับ-รายจ่าย / budgeting / saving / net worth tracking / Financial Independence goal

**กลุ่มเป้าหมาย:** Gen Z ไทย เงินเดือน 15–60k

-----

## PART A — หน้าบ้าน (Brand / Persona / Voice / Visual)

### A1. แก่นแบรนด์

- ปรัชญา: "มีสลึงพึงบรรจบให้ครบบาท"
- แก่นตัวตน: "เพื่อนตัวเล็กที่อยู่เคียงข้างเธอ เติบโตไปด้วยกัน จนถึงวันที่เป็นอิสระทางการเงิน"
- สโลแกน: "เพื่อนตัวเล็ก เรื่องเงินตัวใหญ่"

### A2. Persona & บุคลิก

- เพื่อนตัวเล็กที่อยู่ข้าง ๆ (แกนหลัก) — "พลาดได้ เริ่มใหม่ได้ ไม่โดนตัดสิน"
- สูตรบุคลิก: อบอุ่น 40% · เพื่อน 25% · ซื่อสัตย์ 15% · ขี้เล่น 15% · จริงจังการเงิน 5%

### A3. สรรพนาม

- เรียกตัวเอง: "Salung" / "เรา"
- เรียกผู้ใช้: "เธอ" (default) / "คุณ" เฉพาะบริบททางการ
- เพศ: gender-neutral
- คำลงท้าย: "นะ" (default) · "น้า" (นุ่มขึ้น) — ไม่ใช้ครับ/ค่ะ

### A4. Visual Identity ✅

- โลโก้: retro cartoon — wordmark "Salung" + มาสคอตถุงเงิน
- สี: เขียวสด #3DDB5A / ทอง #FFD015 / ครีม #F5F0E8 / เส้นดำ #1A3D1F
- Assets: โลโก้ 4 พื้น · ไอคอน · avatar · LINE rich menu · expression set

### A5. Sass Mode ✅ (Phase 11.1)

- opt-in · 7 Sass Engines · context pools · crisis auto-off

### A6. Growth System

|Zone   |สถานะ                        |Salung          |
|-------|-----------------------------|----------------|
|🌱 เริ่มต้น|ติดลบ / เพิ่งเริ่ม                |ตัวเล็ก ผอม       |
|🪙 สะสม |ศูนย์ → มีเงินเก็บนิดหน่อย          |ตัวปกติ           |
|💰 กำลังโต|ปลดหนี้ + มีกองทุนฉุกเฉิน          |อ้วนขึ้น           |
|🏆 มั่นคง |net worth เป็นบวกชัด           |อ้วนมาก นั่งบนเหรียญ|
|✨ อิสระ |passive income cover fix cost|นอนพัก           |

### A7. Monetization

- Free: บันทึกรายจ่าย · ดูยอดหนี้ · budget พื้นฐาน · Salung คุยด้วย (จำกัด) · custom savings pots สูงสุด 3 กอง
- Premium (79–99 บาท/เดือน หรือ 790 บาท/ปี): Spicy mode · Salung Wrapped · Advanced insights · Milestone celebrate · LIFF dashboard เต็ม · custom savings pots ไม่จำกัด

-----

## PART B — หลังบ้าน (System / Progress)

### B1. Current Status — v27 (11 มิ.ย. 2026)

**LIFF — 4 tabs: Cash Flow / Save & Goal / Debt / More**

- ✅ CashFlow: month nav + alloc waterfall จาก DB + transactions list + บันทึกรายการ + ลบรายการ
- ✅ Save & Goal: Net Worth + กองทุนฉุกเฉิน + custom savings pots (balance + เติมกอง + ลบ) + savings list + ถอนเงิน + goals + ลบ
- ✅ Debt: debts จาก DB + Avalanche timeline + ชำระหนี้ + จดหนี้ใหม่ + ลบหนี้
- ✅ More: ชื่อจาก LIFF profile + zone จาก net worth จริง
- ✅ NBA text dynamic จาก real data ทุก tab
- ✅ Spicy mode modal centered
- ✅ Scroll to top on tab switch
- ✅ LIFF auth = HMAC signed token (POST /liff/auth → liffFetch wrapper)
- ✅ Cache-Control: no-store ทั้ง worker response + LIFF fetch
- ✅ Delete endpoints: /liff/delete-transaction, /liff/delete-goal, /liff/delete-debt, /liff/delete-saving-pot
- ✅ Withdrawal: /liff/saving รับ amount_thb ติดลบ
- ✅ Custom savings pots: bucket cap 3 (free) / ไม่จำกัด (premium) + BUCKET_LIMIT_REACHED sheet
- ✅ savings-summary return custom_pots[] พร้อม icon + total_thb

**LIFF (payoff-liff.html) — deployed บน GitHub kenwijak/sati-assets**

- ✅ 4 tabs: Cash Flow · Save & Goal · Debt · More
- ✅ Real data: transactions, debts, savings, goals จาก DB
- ✅ CashFlow: period toggle + month nav + บันทึกรายการ (Sheet form)
- ✅ Save tab: Net Worth จริง + กองทุนฉุกเฉิน % จริง + custom pots cards + ออมเดือนนี้จริง
- ✅ Debt tab: ยอดหนี้จริง + Avalanche timeline คำนวณจาก real debts + จดหนี้ใหม่ button
- ✅ Goals tab: goals จาก DB + เพิ่มเป้าหมาย + เพิ่มเงิน
- ✅ More tab: profile + spicy toggle
- ✅ Spicy mode toggle + confirm modal
- ✅ liffFetch() wrapper — inject HMAC token อัตโนมัติทุก API call
- ⚠️ ErrorBoundary (debug — ต้องเอาออกก่อน public)
- ✅ Full screen (เอา phone frame 375px ออกแล้ว — แต่ต้องเปลี่ยน LIFF size เป็น Full ใน LINE Dev Console)

**Worker endpoints /liff/* (ทั้งหมด deployed)**

- POST /liff/auth — verify LINE access token → issue HMAC session token (4hr TTL)
- POST /liff/transaction — บันทึกรายจ่าย/รายรับ
- POST /liff/saving — บันทึกเงินออม + bucket cap check + atomic batch write
- POST /liff/debt-payment — ชำระหนี้ (map debt_type → category)
- POST /liff/goal — add/fund goal
- POST /liff/add-debt — จดหนี้ใหม่ (push LINE nudge ถ้าข้อมูลไม่ครบ)
- POST /liff/delete-saving-pot — ลบ custom pot (DELETE ทุก tx ที่ชื่อตรง)
- GET /liff/transactions — รายการล่าสุด + summary (auth: token)
- GET /liff/payoff-data — debt list (auth: token)
- GET /liff/goals — goal list (auth: token)
- GET /liff/savings-summary — emergency/general/goal/custom_pots/total/this_month + emergency_pct (auth: token)
- GET /liff/cashflow-summary — alloc waterfall (auth: token)

### B2. Completed Phases

|Phase      |Description                                       |Version  |
|-----------|--------------------------------------------------|---------|
|1          |Initial LINE bot integration                      |v1       |
|2          |Refund chip, retry semantics                      |v2       |
|2.1        |Async pattern (ctx.waitUntil)                     |v3       |
|3.1–3.4    |D1 database + HMAC                                |v4–v5    |
|4.1        |Consent flow (PDPA)                               |v5       |
|4.2.1–4.2.5|Facts + transactions + debt + crisis + quiz       |v5–v9    |
|4.3–4.6    |Debt tools + budgets + weekly insights            |v10–v12  |
|5.1–5.4    |Slip OCR + Sentry + PII encryption + credit report|v13      |
|6a–6c      |Premium + referral + B2B                          |v14–v15  |
|7–7.x      |Admin ops + dashboard                             |v16      |
|8–8.x      |RAG knowledge + LIFF Debt Payoff Dashboard        |v17–v18  |
|9          |Payment automation (Omise PromptPay)              |v19      |
|10         |Overdue tracking + cron                           |v20      |
|11         |Rich Menu + Navigation                            |v21      |
|11.1       |Salung Persona Rebrand + Sass Mode                |v22      |
|11.2       |Reskin chat.js / handlers.js / payoff-liff.js     |v23      |
|12C        |Streak System (backend)                           |v24      |
|LIFF v1    |5-tab LIFF redesign — real data all tabs          |v24.1–v25|
|LIFF v2    |4-tab redesign + full wire + delete + withdraw     |v26      |
|LIFF v3    |Custom pots + bucket cap + signed token auth      |v27      |

### B3. Up Next

**Phase 12A — วันปลดแอก scenarios**

- แสดง 3 scenarios (ขั้นต่ำ / +฿500 / +฿1,000)
- shareTargetPicker — แชร์วันปลดแอกให้เพื่อนใน LINE

**Phase 12B — ทำนายดวง**

- วิเคราะห์ spending 3 เดือน → ทำนาย 6 เดือน
- ต้องมี tx ≥ 3 เดือน

**Phase 13 — Salung Wrapped (ธ.ค.)**

- year-in-review แบบ Spotify Wrapped + shareTargetPicker

**CashFlow alloc waterfall**

- "เงินเดือนนี้ไปไหนบ้าง?" ยังเป็น hardcode — ต้องดึง income + debt payment + savings จริงจาก DB

### B4c. Recent Decisions (v27 session — 11 มิ.ย. 2026)

**Custom Savings Pots + Bucket Cap + Security**

| วันที่ | Decision |
|--------|----------|
| 2026-06-11 | custom savings pots แสดงแยก card เหมือน emergency fund (balance + เติมกอง + ลบ) |
| 2026-06-11 | bucket key = TRIM(note) ใน transactions table — ไม่มี table แยก |
| 2026-06-11 | Free cap = 3 custom pots, Premium bypass cap ด้วย isPremium() |
| 2026-06-11 | BUCKET_LIMIT_REACHED → bottom sheet "ลบกองเก่าหรืออัปเกรด Premium" + 2 ปุ่ม |
| 2026-06-11 | POST /liff/saving ใช้ db.batch() สำหรับ atomic write (INSERT tx + UPDATE facts) |
| 2026-06-11 | savings-summary return custom_pots[] + total_thb รวม custom pots ด้วย |
| 2026-06-11 | POST /liff/delete-saving-pot: DELETE ทุก tx ที่ TRIM(note) = pot_name |
| 2026-06-11 | LIFF auth เปลี่ยนจาก userId-in-URL → HMAC signed token (4hr TTL) |
| 2026-06-11 | POST /liff/auth: verify กับ LINE API (api.line.me/v2/profile) → issue token |
| 2026-06-11 | liffFetch() wrapper inject token อัตโนมัติ — replace fetch("/liff/ ทั้ง 25 calls |
| 2026-06-11 | legacy userId fallback ยังอยู่ใน getLiffUserId() — ลบได้เมื่อ client ทุกตัว update |
| 2026-06-11 | Worker secret ใหม่ที่ต้องเพิ่ม: `LIFF_SECRET` (32-char random) |

**Bug fixes v27**

| Bug | สาเหตุ | วิธีแก้ |
|-----|--------|---------|
| Cannot find name 'isPremium' | ไม่ได้ import isPremium จาก subscription.js | เพิ่ม isPremium ใน import statement |
| Cannot find name 'consented' (ln 525) | ลบ consent check ออกจาก cashflow-summary แต่ลืมลบ `if (!consented)` orphan line | ลบบรรทัด orphan ออก |
| subscription status='expired' ทั้งที่ expires_at ยังไม่ถึง | data inconsistency — isPremium() ใช้ row.status ตรงๆ ไม่ผ่าน isExpired logic | UPDATE subscriptions SET status='active' ใน D1 โดยตรง |

**Worker endpoints เพิ่มใหม่ v27**
- `POST /liff/auth` — LINE access token → HMAC session token
- `POST /liff/delete-saving-pot` — ลบ custom pot ทั้งกอง
- `POST /liff/saving` ปรับปรุง: bucket cap check + atomic db.batch() + custom pot grouping
- `GET /liff/savings-summary` ปรับปรุง: return custom_pots[] + net balance per pot

### B4b. Recent Decisions (v26 session — 11 มิ.ย. 2026)

**LIFF Redesign — 4 tabs (CashFlow / Save & Goal / Debt / More)**

| วันที่ | Decision |
|--------|----------|
| 2026-06-11 | รวม Save + Goal เป็น tab เดียว "Save & Goal" → เหลือ 4 tabs |
| 2026-06-11 | ลบ FAB (+) button ออกทุกหน้า ใช้ inline buttons แทน |
| 2026-06-11 | NBA text คำนวณจาก real data ทุก tab แทน hardcode |
| 2026-06-11 | เพิ่ม delete ทุก tab: transaction ✕, savings ✕, goal 🗑️, debt 🗑️ |
| 2026-06-11 | เพิ่ม withdrawal feature สำหรับกองทุนฉุกเฉิน (negative savings) |
| 2026-06-11 | savings list แสดง chip icon + สี per category |
| 2026-06-11 | Debt tab ดึงจาก DB จริง + calcFreeDate() dynamic |
| 2026-06-11 | CashFlow month navigation ส่ง year+month params ไป worker |
| 2026-06-11 | worker API responses เพิ่ม Cache-Control: no-store |
| 2026-06-11 | LIFF fetch ทุก GET เพิ่ม cache:"no-store" |
| 2026-06-11 | LIFF HTML ส่ง Cache-Control: no-store จาก worker route /liff/payoff |

**Bug fixes สำคัญ v26**

| Bug | สาเหตุ | วิธีแก้ |
|-----|--------|---------|
| LIFF หมุนค้าง (spinner ไม่หาย) | Babel compile เป็น CommonJS `exports.default` ซึ่งไม่มีใน browser UMD | Compile ด้วย `modules:false` + ลบ `export default` + mount ด้วย `window.addEventListener('load')` |
| ข้อมูลทุกเดือนเหมือนกัน (1) | LINE webview cache API GET responses | เพิ่ม `Cache-Control: no-store` ใน worker LIFF_CORS + `cache:"no-store"` ใน fetch |
| ข้อมูลทุกเดือนเหมือนกัน (2) | `monthOffset` state ถูกประกาศ **หลัง** useEffect ที่ใช้มัน → Babel hoist เป็น `var` → deps เห็น `undefined` ตลอด → effect ไม่ re-run | ย้าย `monthOffset` state declaration ขึ้นมาก่อน useEffect |
| จอขาว (white screen) SaveGoal | state `savingsTxns` เพิ่มผิด component — ใส่ใน Goal component เก่า (dead code) แต่ render ใน SaveGoal → `savingsTxns` undefined | ย้าย state/effect ไปใส่ใน SaveGoal ที่ถูก |
| ถอนกองทุนฉุกเฉินไม่ได้ | worker saving endpoint: `if (Number(amount_thb) <= 0)` reject ค่าติดลบ | แก้เป็น `if (amount_thb == null \|\| Number(amount_thb) === 0)` |
| submit goal/save ไม่ได้ | userId ไม่มีใน URL query params | เปลี่ยนจาก `URLSearchParams` เป็น `liff.getProfile()` ผ่าน LIFF SDK + `window.__LIFF_UID` |
| Goals "กำลังโหลด" ค้าง | fetch ส่ง field ผิด (`target_amount_thb`) แทน `target_satang` ตามจริงใน DB | แก้ field mapping ให้ตรง DB schema |

### B4. Recent Decisions (v25 session — 8 มิ.ย. 2026)

|วันที่       |Decision                                                                                                                                                    |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|2026-06-08|LIFF full screen — เอา phone frame 375px wrapper ออก ใช้ width 100%                                                                                          |
|2026-06-08|Debt tab: ปุ่ม "จดหนี้ใหม่" แทน FAB floating button                                                                                                              |
|2026-06-08|Save tab: ดึง savings data จริงจาก GET /liff/savings-summary                                                                                                  |
|2026-06-08|Debt timeline: คำนวณ Avalanche จาก real debts แทน hardcode                                                                                                   |
|2026-06-08|Min payment fallback = 5% ของยอดหนี้ (ถ้า DB เป็น null)                                                                                                         |
|2026-06-08|LIFF size mode ยังเป็น Tall — ต้องเปลี่ยนเป็น Full ใน LINE Dev Console                                                                                            |
|2026-06-07|Phase 12C deployed v24 — Streak System                                                                                                                      |
|2026-06-07|LIFF: category_id hotfix (travel→transport, shop→shopping, etc.)                                                                                            |

### B5. Known Issues / Tech Debt

**ต้องทำก่อน public**

- ⚠️ ErrorBoundary + debug try-catch ยังอยู่ใน payoff-liff.html — เอาออกก่อน launch
- ⚠️ LIFF size = Tall → เปลี่ยนเป็น Full ใน LINE Dev Console
- ⚠️ debts.minimum_payment_satang = NULL ทุกรายการ → timeline ใช้ 5% estimate
- ⚠️ wrangler.toml: ต้องเพิ่ม cron "0 13 * * *" สำหรับ streak reminder ด้วยตนเอง
- ⚠️ Worker secret `LIFF_SECRET` ต้องเพิ่มใน Cloudflare dashboard ก่อน deploy

**Tech debt (ไม่ urgent)**

- LLM cost growing ~3x base
- No CI/CD — deploy ผ่าน dashboard
- handlers.js ไม่มีปุ่ม "ข้าม" ใน quiz quick reply
- PII: debts.nickname ยังไม่ encrypt
- LIFF auth legacy fallback (userId-in-body) — ลบได้เมื่อ user ทุกคน update LIFF ใหม่
- 9: card tokenization ยังไม่ทำ · Omise test mode (ต้อง KYC)
- CashFlow alloc waterfall ยัง hardcode
- subscription status bug (status='expired' ทั้งที่ยังไม่หมด) — ควรตรวจ cron/webhook logic
- infra ยังใช้ชื่อ sati-* — decision: rename เป็น salung-* ไหม

### B6. Code Structure (v27 — 28 files + LIFF)

**Entry:** worker.js → handlers/chat/cron/ocr/referral/b2b/admin-ui/payoff-liff/payment/richmenu/postback → claude/db/line/prompts/tools-*/sentry/crypto-utils/subscription → config

**LIFF:** payoff-liff.html (compiled React, ~3500 lines) บน GitHub kenwijak/sati-assets

|File                 |มีอะไร                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------|
|worker.js            |entry + LIFF routes /liff/* ทั้งหมด + signLiffToken/verifyLiffToken helpers                    |
|prompts.js           |system prompt + Sass Mode + streak context (12C)                                              |
|db.js                |D1 helpers + getStreak / updateStreakFacts (12C)                                              |
|chat.js              |conversation engine + streak check                                                            |
|knowledge.js         |interest_rates · debt_collection_law · debt_clinic · negotiation · refinance · lawyer_referral|
|tools-transactions.js|TRANSACTION_TOOLS + query_spending (income/expense/all)                                       |
|debt-tools.js        |debt tools + DTI + /debts handler                                                             |
|tools-payoff.js      |payoff planner + health score                                                                 |
|subscription.js      |isPremium() · getUserTier() · activateSubscription()                                          |

### B7. Deployment Info

- Worker: `sati-bot` · D1: `sati-db` (binding `DB`) · Schema: 0013 · Latest: v27
- LIFF: GitHub `kenwijak/sati-assets/payoff-liff.html` · LIFF ID: `2010030839-xs1nAvDg`
- Cron: `0 11 * * SUN` (weekly insight) · `0 13 * * *` (streak — ต้องเพิ่มใน wrangler.toml)
- Admin UI: `.../admin/ui` · Omise webhook: `.../webhook/omise`
- **Worker Secrets ที่ต้องมี:** `ANTHROPIC_TOKEN` · `LINE_TOKEN` · `LINE_CHANNEL_SECRET` · `ENCRYPTION_KEY` · `LIFF_SECRET` ← ใหม่ v27

### B8. Migration History

0001–0013 (ครบแล้ว) · Phase 12C: streak ไม่ต้อง migration ใช้ user_facts JSON blob

-----

## PART C — Open Items

### ทำได้เดี๋ยวนี้ (ไม่ต้องโค้ด)

- [ ] เพิ่ม `LIFF_SECRET` ใน Cloudflare dashboard → sati-bot → Settings → Variables → Secrets
- [ ] อัปเดต min_payment ของ KBank ใน DB → 10% ของยอด = ฿5,000 (BOT rule)
- [ ] ถามบอท "ผ่อนรถ Toyota เดือนละเท่าไหร่?" แล้วบอตจะจำ
- [ ] เปลี่ยน LIFF size Tall → Full ใน LINE Dev Console

### ทำรอบหน้า (โค้ด)

- [ ] เพิ่ม knowledge.js: min payment 10%/฿500 (BOT) + "คุณสู้ เราช่วย"
- [ ] เอา ErrorBoundary + debug try-catch ออกจาก payoff-liff.html
- [ ] CashFlow alloc waterfall จากข้อมูลจริง
- [ ] Phase 12A scenarios + shareTargetPicker
- [ ] Phase 12B ทำนายดวง
- [ ] Phase 13 Salung Wrapped
- [ ] ลบ legacy userId fallback ใน getLiffUserId() หลัง user ทุกคน update LIFF

### หน้าบ้าน (แบรนด์)

- [ ] ฟอนต์ไทย
- [ ] Export assets hi-res + rich menu 2500×1686
- [ ] สตอรี่ต้นกำเนิด

### ก่อน Public Launch

- [x] ~~LIFF auth → signed token~~ ✅ done v27
- [ ] เคลียร์ debug code (ErrorBoundary)
- [ ] ตรวจสอบ resources วิกฤต (1323 / คลินิกแก้หนี้ by SAM)
- [ ] Decision: rename infra sati-* → salung-*
