"""Build the profile README: every card in assets/ (light + dark, English + Korean)
and README.md / README.ko.md.

    python3 .github/readme/build.py

Edit the text in TX / WEB / RESEARCH / STACK / ABOUT / LEAD / FOOT / C below, then run it.
The activity card is drawn separately every day by .github/scripts/activity_card.py.
Brand icons in icons/ come from Simple Icons (CC0).
"""
import os
import re
import sys

import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(REPO, "assets")
ICONS = os.path.join(HERE, "icons")
os.makedirs(OUT, exist_ok=True)

SANS = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', Arial, sans-serif"
MONO = "'JetBrains Mono', 'SF Mono', ui-monospace, Menlo, Consolas, monospace"
T = {
    "dark": dict(card="#10141D", line="#2A3242", line2="#4A556B", ink="#F5F7FB", sub="#CDD4E1",
                 faint="#A3ADC0", accent="#8DB6FF", ok="#4ADE9B", dot="#FFFFFF"),
    "light": dict(card="#FFFFFF", line="#E6E9EF", line2="#D5DAE3", ink="#0F172A", sub="#3F4A5C",
                  faint="#667085", accent="#2160D4", ok="#16A34A", dot="#0F172A"),
}
LANGS = ("en", "ko")

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


ANIM = """<style>@keyframes p{0%,100%{opacity:.5;transform:scale(1)}50%{opacity:0;transform:scale(2.6)}}
.p{transform-box:fill-box;transform-origin:center;animation:p 2.8s ease-in-out infinite}
@media (prefers-reduced-motion: reduce){.p{animation:none}}</style>"""

def dot(c, x, y, state="live"):
    if state == "live":
        return f'<circle class="p" cx="{x}" cy="{y}" r="3.5" fill="{c["ok"]}"/><circle cx="{x}" cy="{y}" r="3.5" fill="{c["ok"]}"/>'
    if state == "next":
        return f'<circle cx="{x}" cy="{y}" r="4" fill="{c["card"]}" stroke="{c["accent"]}" stroke-width="2"/>'
    return f'<circle cx="{x}" cy="{y}" r="3.5" fill="none" stroke="{c["faint"]}" stroke-width="1.4"/>'


# ---------------------------------------------------------------- text
TX = {
 "en": dict(
   sub="Founder of JUNIXION. I design, build and ship software for every day.",
   status=[("live", "nalbom", "launching nov 2026"), ("idle", "junixion.com", "in review"), ("idle", "ssrn", "working paper")],
   est="est. 2026",
   now=[("PRODUCT", "Nalbom", "날봄", "A calendar for seeing your days.", "D-days, calendar, notes and work tools on your home screen.", "live", "launching nov 2026", "ios · ipados · macos · android"),
        ("WEBSITE", "junixion.com", "", "Software for every day, built and backed to last.", "Company story, the Nalbom page, policies in three languages.", "idle", "in review", "next.js 16 · ko · en · ja")],
   kpi=[("151", "countries' holidays"), ("4", "platforms"), ("3", "languages"), ("E2E", "encrypted sharing"), ("745", "nalbom commits")],
   features=[("cal", "Calendar", ["Year, month, week and day views", "Holidays for 151 countries", "Lunar dates, per-country rules", "Google and iCloud calendars"]),
             ("dday", "D-days & notes", ["D-days, count-ups, anniversaries", "Trip D-days and share cards", "Notes with photos, voice, links", "Locked notes with Face ID"]),
             ("work", "Work tools", ["Annual leave, Korean labor law", "Clock-in and the 52-hour week", "Shift-work roster calendar", "Work log to weekly report"]),
             ("widget", "Widgets & live", ["Home and lock-screen widgets", "Check or clock in from a widget", "Live Activities, Watch Smart Stack", "Galaxy Live Updates on Android"]),
             ("together", "Together", ["Spaces for couples, family, trips", "End-to-end encrypted sharing", "Key rotation when someone leaves", "iCloud sync across your devices"]),
             ("look", "Look & feel", ["13 themes, 19 accent colors", "Matching app icons on iOS", "Korean, English and Japanese", "Free, plus a one-time lifetime pass"])],
   roadmap_title="NALBOM ROADMAP",
   roadmap=[("done", "Oct 2026", "TestFlight beta", "50 builds so far"), ("done", "Oct 2026", "Google Play testing", "closed track"),
            ("next", "Nov 2026", "Launch", "App Store · Google Play"), ("idle", "After launch", "Updates", "about every two weeks"),
            ("idle", "2027", "App #2", "in research")],
   sections=[("now", "01", "Now", "what i am working on"), ("nalbom", "02", "Nalbom", "junixion's first app"),
             ("web", "03", "junixion.com", "the company website"), ("research", "04", "Research", "survival analysis"),
             ("projects", "05", "Projects", "ml · statistics · data"), ("stack", "06", "Stack", "tools i use"),
             ("about", "07", "About", "background · contact")],
   projects=[("krx", "RESEARCH CODE", "Survival Analysis — KRX", "365 KRX firms, Kaplan-Meier, Cox PH and AFT", "C-index 0.738", "repo"),
             ("lm", "MODEL · PRIVATE", "JunixionLM", "Decoder-only Transformer, written from scratch", "162M params · 817M tokens", "private"),
             ("crypto", "LIVE API", "Crypto Drawdown Survival", "Cox PH for 24-hour drawdowns on live data", "C-index 0.862", "live"),
             ("e2e", "LIVE API", "End-to-End ML System", "Telco churn, validation to Dockerized FastAPI", "ROC-AUC 0.83", "live"),
             ("grad", "LIVE API", "Graduate ML Portfolio", "Breast cancer survival on METABRIC", "C-index 0.638", "live"),
             ("sql", "SQL", "SQL Analytics Portfolio", "18 analyses in pure PostgreSQL", "9 assets × 5 years", "repo")],
   footer=("Software for every day, built and backed to last.", "junixion · seoul · contact@junixion.com"),
   social=[("company", "COMPANY", ["instagram", "threads", "x", "facebook"]),
           ("nalbom", "NALBOM", ["instagram", "threads", "x", "facebook", "tiktok"]),
           ("dev", "DEV", ["linkedin", "gitlab", "huggingface"])],
 ),
 "ko": dict(
   sub="주닉션 대표. 매일 쓰는 소프트웨어를 직접 설계하고 만들고 출시합니다.",
   status=[("live", "nalbom", "2026년 11월 출시"), ("idle", "junixion.com", "검토 중"), ("idle", "ssrn", "워킹 페이퍼")],
   est="since 2026",
   now=[("PRODUCT", "날봄", "Nalbom", "날을 보는 달력, 날봄", "D-day·캘린더·메모·일 도구를 홈 화면과 잠금화면에.", "live", "2026년 11월 출시", "ios · ipados · macos · android"),
        ("WEBSITE", "junixion.com", "", "매일 손이 가는 소프트웨어를, 끝까지 책임지고 만듭니다.", "회사 이야기, 날봄 소개, 3개 언어 방침·약관.", "idle", "검토 중", "next.js 16 · ko · en · ja")],
   kpi=[("151", "공휴일 나라"), ("4", "기기"), ("3", "언어"), ("E2E", "암호화 공유"), ("745", "날봄 커밋")],
   features=[("cal", "달력", ["연·월·주·일 보기", "151개 나라 공휴일", "나라별 기준 음력", "구글·iCloud 캘린더 연동"]),
             ("dday", "D-day·메모", ["D-day·카운트업·기념일", "여행 D-day와 공유 카드", "사진·음성·링크 메모", "Face ID 메모 잠금"]),
             ("work", "일 도구", ["근로기준법 연차 계산", "출퇴근 기록·주 52시간", "교대근무 근무표 달력", "업무 일지로 주간 보고"]),
             ("widget", "위젯·실시간", ["홈 화면·잠금화면 위젯", "위젯에서 바로 체크·출퇴근", "실시간 현황·워치 스마트 스택", "갤럭시 실시간 알림"]),
             ("together", "함께", ["연인·가족·여행 함께 공간", "종단간 암호화 공유", "누가 나가면 열쇠 교체", "내 기기끼리 iCloud 동기화"]),
             ("look", "꾸미기", ["테마 13개·강조색 19개", "iOS 앱 아이콘 맞추기", "한국어·영어·일본어", "무료 + 한 번 사는 평생 이용권"])],
   roadmap_title="NALBOM ROADMAP",
   roadmap=[("done", "2026.10", "TestFlight 베타", "지금까지 빌드 50개"), ("done", "2026.10", "Google Play 테스트", "비공개 테스트"),
            ("next", "2026.11", "출시", "App Store · Google Play"), ("idle", "출시 후", "업데이트", "약 2주마다"),
            ("idle", "2027", "두 번째 앱", "준비 중")],
   sections=[("now", "01", "지금", "하고 있는 일"), ("nalbom", "02", "날봄", "주닉션의 첫 앱"),
             ("web", "03", "junixion.com", "회사 웹사이트"), ("research", "04", "연구", "생존분석"),
             ("projects", "05", "프로젝트", "머신러닝 · 통계 · 데이터"), ("stack", "06", "기술", "쓰는 도구"),
             ("about", "07", "소개", "학력 · 연락처")],
   projects=[("krx", "RESEARCH CODE", "생존분석 — KRX", "KRX 365개 기업, 카플란-마이어·Cox PH·AFT", "C-index 0.738", "repo"),
             ("lm", "MODEL · PRIVATE", "JunixionLM", "처음부터 직접 짠 디코더 Transformer", "1억 6,200만 파라미터 · 8억 1,700만 토큰", "private"),
             ("crypto", "LIVE API", "암호화폐 하락 생존분석", "실시간 데이터로 24시간 급락 예측(Cox PH)", "C-index 0.862", "live"),
             ("e2e", "LIVE API", "엔드투엔드 ML 시스템", "통신사 이탈 예측, 검증부터 Docker API까지", "ROC-AUC 0.83", "live"),
             ("grad", "LIVE API", "대학원 ML 포트폴리오", "METABRIC 유방암 생존분석", "C-index 0.638", "live"),
             ("sql", "SQL", "SQL 분석 포트폴리오", "PostgreSQL만으로 분석 18개", "자산 9개 × 5년", "repo")],
   footer=("매일 손이 가는 소프트웨어를, 끝까지 책임지고 만듭니다.", "junixion · seoul · contact@junixion.com"),
   social=[("company", "COMPANY", ["instagram", "threads", "x", "facebook"]),
           ("nalbom", "NALBOM", ["instagram", "threads", "x", "facebook", "tiktok"]),
           ("dev", "DEV", ["linkedin", "gitlab", "huggingface"])],
 ),
}

# ---------------------------------------------------------------- pieces

def now(L, m):
    c, t = T[m], TX[L]; W, H = 1280, 206; gap = 16; cw = (W - gap) / 2
    b = ANIM
    for i, (eye, title, tk, lead, desc, state, st, meta) in enumerate(t["now"]):
        x = i * (cw + gap)
        b += box(c, x, 0, cw, H)
        b += f'<text x="{x+32:.1f}" y="44" font-family="{MONO}" font-size="13.5" letter-spacing="2.5" fill="{c["faint"]}">{eye}</text>'
        b += (f'<text x="{x+32:.1f}" y="88" font-size="28" font-weight="600" letter-spacing="-0.8" fill="{c["ink"]}">{esc(title)}'
              + (f'<tspan dx="10" font-size="20" font-weight="500" fill="{c["faint"]}">{tk}</tspan>' if tk else "") + '</text>')
        b += f'<text x="{x+32:.1f}" y="118" font-size="17" font-weight="500" fill="{c["ink"]}">{esc(lead)}</text>'
        b += f'<text x="{x+32:.1f}" y="142" font-size="16" fill="{c["sub"]}">{esc(desc)}</text>'
        b += f'<line x1="{x+32:.1f}" y1="164" x2="{x+cw-32:.1f}" y2="164" stroke="{c["line"]}"/>'
        b += dot(c, x + 37, 182, state)
        b += f'<text x="{x+50:.1f}" y="186.5" font-family="{MONO}" font-size="14" fill="{c["ink"]}">{esc(st)}</text>'
        b += f'<text x="{x+cw-32:.1f}" y="186.5" text-anchor="end" font-family="{MONO}" font-size="14" fill="{c["faint"]}">{meta}</text>'
    write("now", L, m, b, W, H)


FICONS = {
    "cal": '<rect x="1" y="3" width="18" height="16" rx="4"/><line x1="1" y1="8" x2="19" y2="8"/><line x1="6" y1="0.5" x2="6" y2="4.5"/><line x1="14" y1="0.5" x2="14" y2="4.5"/>',
    "dday": '<circle cx="10" cy="11" r="8.5"/><polyline points="10,6 10,11 14,13.5"/>',
    "work": '<rect x="1" y="5" width="18" height="13" rx="3.5"/><path d="M7 5V3a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 13 3v2"/><line x1="1" y1="11" x2="19" y2="11"/>',
    "widget": '<rect x="1" y="1" width="7.5" height="7.5" rx="2.5"/><rect x="11.5" y="1" width="7.5" height="7.5" rx="2.5"/><rect x="1" y="11.5" width="18" height="7.5" rx="2.5"/>',
    "together": '<circle cx="7" cy="7" r="3.5"/><circle cx="14" cy="7" r="3.5"/><path d="M1 18c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M11.5 12.3c.8-.2 1.6-.3 2.5-.3 3.3 0 5 2.7 5 6"/>',
    "look": '<path d="M10 1a9 9 0 1 0 0 18c1.3 0 2-.9 2-2 0-1.3-1.3-1.5-1.3-2.7 0-1 .9-1.8 2-1.8h2.6A3.7 3.7 0 0 0 19 8.8C19 4.5 15 1 10 1z"/><circle cx="5.8" cy="9" r="1.1" fill="currentColor"/><circle cx="9" cy="5.2" r="1.1" fill="currentColor"/><circle cx="13.4" cy="5.8" r="1.1" fill="currentColor"/>',
}

def roadmap(L, m):
    c, t = T[m], TX[L]; W, H = 1280, 196
    b = box(c, 0, 0, W, H)
    b += f'<text x="32" y="44" font-family="{MONO}" font-size="13.5" letter-spacing="2.5" fill="{c["faint"]}">{t["roadmap_title"]}</text>'
    n = len(t["roadmap"]); x0, x1 = 40, W - 40; step = (x1 - x0) / n; y = 88
    for i, (state, when, title, note) in enumerate(t["roadmap"]):
        x = x0 + i * step
        col = c["ok"] if state == "done" else c["accent"] if state == "next" else c["line2"]
        b += f'<line x1="{x:.1f}" y1="{y}" x2="{x+step-8:.1f}" y2="{y}" stroke="{col if state=="done" else c["line"]}" stroke-width="{2 if state=="done" else 1.5}"/>'
        if state == "done":
            b += f'<circle cx="{x:.1f}" cy="{y}" r="6" fill="{c["ok"]}"/><path d="M{x-2.6:.1f} {y} l1.9 1.9 l3.4 -3.8" fill="none" stroke="{c["card"]}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
        elif state == "next":
            b += f'<circle class="p" cx="{x:.1f}" cy="{y}" r="6" fill="{c["accent"]}"/><circle cx="{x:.1f}" cy="{y}" r="6" fill="{c["card"]}" stroke="{c["accent"]}" stroke-width="2.4"/>'
        else:
            b += f'<circle cx="{x:.1f}" cy="{y}" r="5.5" fill="{c["card"]}" stroke="{c["line2"]}" stroke-width="1.5"/>'
        b += (f'<text x="{x-6:.1f}" y="{y+40}" font-family="{MONO}" font-size="13.5" fill="{c["accent"] if state=="next" else c["faint"]}">{esc(when)}</text>'
              f'<text x="{x-6:.1f}" y="{y+66}" font-size="17" font-weight="600" fill="{c["ink"]}">{esc(title)}</text>'
              f'<text x="{x-6:.1f}" y="{y+90}" font-size="15" fill="{c["sub"]}">{esc(note)}</text>')
    b = ANIM + b
    write("roadmap", L, m, b, W, H)




# ---------------------------------------------------------------- social segments (language-neutral)
NAMES = {"instagram": "Instagram", "threads": "Threads", "x": "X", "facebook": "Facebook", "tiktok": "TikTok",
         "linkedin": "LinkedIn", "gitlab": "GitLab", "huggingface": "Hugging Face"}
def icon_path(n):
    s = open(os.path.join(ICONS, f"{n}.svg")).read()
    return re.search(r'<path d="([^"]+)"', s).group(1)

def seg_shape(w, h, r, left, right):
    # outline path with rounded corners only on the outer ends
    lr = r if left else 0; rr = r if right else 0
    return (f"M{lr+0.5},0.5 H{w-rr-0.5} " + (f"A{rr},{rr} 0 0 1 {w-0.5},{rr+0.5} " if rr else "") +
            f"V{h-rr-0.5} " + (f"A{rr},{rr} 0 0 1 {w-rr-0.5},{h-0.5} " if rr else "") +
            f"H{lr+0.5} " + (f"A{lr},{lr} 0 0 1 0.5,{h-lr-0.5} " if lr else "") +
            f"V{lr+0.5} " + (f"A{lr},{lr} 0 0 1 {lr+0.5},0.5 " if lr else "") + "Z")

def social(m):
    c = T[m]; H = 34; R = 9
    for gkey, label, items in TX["en"]["social"]:
        # label segment
        w = int(len(label) * 8.4 + 28)
        b = (f'<path d="{seg_shape(w, H, R, True, False)}" fill="{c["card"]}" stroke="{c["line"]}"/>'
             f'<text x="14" y="21.5" font-family="{MONO}" font-size="11.5" letter-spacing="1.8" fill="{c["faint"]}">{label}</text>')
        with open(os.path.join(OUT, f"social-{gkey}-label-{m}.svg"), "w") as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{H}" viewBox="0 0 {w} {H}" font-family="{SANS}">{b}</svg>\n')
        for k, n in enumerate(items):
            name = NAMES[n]; last = k == len(items) - 1
            w = int(len(name) * 7.3 + 48)
            # left edge is shared with the previous segment, so draw only top/right/bottom + a divider
            b = (f'<path d="{seg_shape(w, H, R, False, last)}" fill="{c["card"]}" stroke="{c["line"]}"/>'
                 f'<line x1="0.5" y1="1.5" x2="0.5" y2="{H-1.5}" stroke="{c["card"]}" stroke-width="1.2"/>'
                 f'<g transform="translate(13,10) scale(0.5833)" fill="{c["sub"]}"><path d="{icon_path(n)}"/></g>'
                 f'<text x="33" y="21.5" font-size="13" fill="{c["ink"]}">{name}</text>')
            with open(os.path.join(OUT, f"social-{gkey}-{n}-{m}.svg"), "w") as f:
                f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{H}" viewBox="0 0 {w} {H}" font-family="{SANS}">{b}</svg>\n')


# ---- website grid, research, stack, about

ICONS2 = {
    "globe": '<circle cx="10" cy="10" r="9"/><path d="M1 10h18"/><path d="M10 1c2.6 2.6 3.8 5.6 3.8 9s-1.2 6.4-3.8 9c-2.6-2.6-3.8-5.6-3.8-9S7.4 3.6 10 1z"/>',
    "phone": '<rect x="4" y="1" width="12" height="18" rx="3"/><line x1="8" y1="15.5" x2="12" y2="15.5"/>',
    "doc": '<path d="M4 1h8l4 4v14H4z"/><path d="M12 1v4h4"/><line x1="7" y1="10" x2="13" y2="10"/><line x1="7" y1="14" x2="13" y2="14"/>',
    "lock": '<rect x="3" y="9" width="14" height="10" rx="3"/><path d="M6 9V6a4 4 0 0 1 8 0v3"/><circle cx="10" cy="14" r="1.2" fill="currentColor"/>',
    "leaf": '<path d="M3 17C3 8 8 3 17 3c0 9-5 14-14 14z"/><path d="M3 17l8-8"/>',
    "check": '<circle cx="10" cy="10" r="9"/><polyline points="6,10.5 8.8,13.2 14,7.5"/>',
}

WEB = {
 "en": [("globe", "Three languages", ["Korean, English, Japanese", "Japanese line-breaking and fonts"]),
        ("phone", "Nalbom pages", ["Real app screenshots, light and dark", "Pricing table and FAQ"]),
        ("doc", "Legal pages match the app", ["Privacy policy and terms in 3 languages", "Updated with each app build"]),
        ("lock", "Private invite links", ["Secret key stays in the browser", "No analytics, no forms, not indexed"]),
        ("leaf", "Small and quiet", ["No database of its own", "No visit analytics"]),
        ("check", "Checked on every change", ["Typecheck, lint, build", "Lighthouse quality gate in CI"])],
 "ko": [("globe", "3개 언어", ["한국어·영어·일본어", "일본어 줄바꿈과 글꼴 따로 맞춤"]),
        ("phone", "날봄 소개", ["실제 앱 화면, 라이트·다크", "요금표와 자주 묻는 질문"]),
        ("doc", "앱에 맞춘 법적 문서", ["방침·약관을 3개 언어로", "앱 빌드마다 함께 고침"]),
        ("lock", "비밀 초대 링크", ["비밀 열쇠는 브라우저 안에만", "분석·입력 폼 없음, 검색 제외"]),
        ("leaf", "작고 조용하게", ["자체 DB 없음", "방문 통계 없음"]),
        ("check", "바꿀 때마다 검사", ["타입 검사·린트·빌드", "CI에서 Lighthouse 기준 검사"])],
}


RESEARCH = {
 "en": dict(eye="WORKING PAPER · SSRN · APRIL 2026",
            title=["Survival Analysis of Corporate Delisting Risk", "in the Korean Stock Market"],
            sub="Cox proportional hazards and AFT models · KOSPI / KOSDAQ panel, 2000–2023",
            tiles=[("0.738", "C-index"), ("365", "firms"), ("158", "delisting events"), ("276", "months observed")],
            finds=[("12-month momentum", "HR 0.496 · p = 0.001"), ("Price volatility", "HR 1.827 · p = 0.004"),
                   ("Best model", "Weibull AFT · ΔAIC 318.1")]),
 "ko": dict(eye="WORKING PAPER · SSRN · 2026년 4월",
            title=["한국 주식시장 상장폐지 위험의 생존분석", ""],
            sub="Cox 비례위험 모형과 AFT 모형 · KOSPI / KOSDAQ 패널, 2000–2023",
            tiles=[("0.738", "C-index"), ("365", "기업"), ("158", "상장폐지"), ("276", "관측 개월")],
            finds=[("12개월 모멘텀", "HR 0.496 · p = 0.001"), ("가격 변동성", "HR 1.827 · p = 0.004"),
                   ("가장 좋은 모형", "와이블 AFT · ΔAIC 318.1")]),
}

def research(L, m):
    c, r = T[m], RESEARCH[L]; W = 1280
    two = bool(r["title"][1]); ty = 98; H = 372 if two else 340; off = 0 if two else -32
    b = box(c, 0, 0, W, H)
    b += f'<text x="32" y="46" font-family="{MONO}" font-size="13.5" letter-spacing="2.5" fill="{c["faint"]}">{esc(r["eye"])}</text>'
    b += f'<text x="{W-32}" y="46" text-anchor="end" font-family="{MONO}" font-size="14" fill="{c["accent"]}">read on ssrn ↗</text>'
    b += f'<text x="32" y="{ty}" font-size="30" font-weight="600" letter-spacing="-0.8" fill="{c["ink"]}">{esc(r["title"][0])}</text>'
    if two:
        b += f'<text x="32" y="{ty+38}" font-size="30" font-weight="600" letter-spacing="-0.8" fill="{c["ink"]}">{esc(r["title"][1])}</text>'
    b += f'<text x="32" y="{ty+74+off}" font-size="16.5" fill="{c["sub"]}">{esc(r["sub"])}</text>'
    y0 = ty + 104 + off; tw = (W - 64) / 4
    b += f'<line x1="32" y1="{y0}" x2="{W-32}" y2="{y0}" stroke="{c["line"]}"/>'
    for i, (n, l) in enumerate(r["tiles"]):
        x = 32 + i * tw
        if i:
            b += f'<line x1="{x-16:.1f}" y1="{y0+20}" x2="{x-16:.1f}" y2="{y0+76}" stroke="{c["line"]}"/>'
        b += f'<text x="{x:.1f}" y="{y0+52}" font-size="30" font-weight="600" letter-spacing="-0.8" fill="{c["ink"] if i else c["accent"]}">{n}</text>'
        b += f'<text x="{x:.1f}" y="{y0+78}" font-family="{MONO}" font-size="14" fill="{c["faint"]}">{esc(l)}</text>'
    y1 = y0 + 100
    b += f'<line x1="32" y1="{y1}" x2="{W-32}" y2="{y1}" stroke="{c["line"]}"/>'
    fw = (W - 64) / 3
    for i, (k, v) in enumerate(r["finds"]):
        x = 32 + i * fw
        b += f'<text x="{x:.1f}" y="{y1+36}" font-size="15.5" fill="{c["sub"]}">{esc(k)}<tspan dx="10" font-family="{MONO}" font-size="14.5" fill="{c["ink"]}">{esc(v)}</tspan></text>'
    write("research", L, m, b, W, H)

STACK = {
 "en": [("APPS", ["React Native", "Expo", "TypeScript", "Swift", "Kotlin", "SQLite", "CloudKit"]),
        ("WEB & BACKEND", ["Next.js", "Tailwind CSS", "Supabase", "PostgreSQL", "Deno", "Vercel", "GitLab CI"]),
        ("ML & STATISTICS", ["Python", "PyTorch", "scikit-learn", "pandas", "R", "SAS", "FastAPI", "Docker"])],
 "ko": [("앱", ["React Native", "Expo", "TypeScript", "Swift", "Kotlin", "SQLite", "CloudKit"]),
        ("웹·서버", ["Next.js", "Tailwind CSS", "Supabase", "PostgreSQL", "Deno", "Vercel", "GitLab CI"]),
        ("ML·통계", ["Python", "PyTorch", "scikit-learn", "pandas", "R", "SAS", "FastAPI", "Docker"])],
}


ABOUT = {
 "en": dict(left=[("EDUCATION", "Yonsei University", "Economics × Information Statistics", "Expected February 2027"),
                  ("RESEARCH", "Undergraduate Research Assistant", "Survival analysis and healthcare risk modeling", ""),
                  ("COMPANY", "Founder, JUNIXION", "Application software, opened August 2026", "")],
            open_title="OPEN TO",
            open=[("Apps", "Nalbom feedback, bug reports, localization"), ("Research", "Survival analysis · LLM / NLP · statistics"),
                  ("Roles", "App · ML research · AI · quant engineering"), ("Academia", "Financial Engineering / AI grad school, 2027")]),
 "ko": dict(left=[("EDUCATION", "연세대학교", "경제학 × 정보통계학", "2027년 2월 졸업 예정"),
                  ("RESEARCH", "학부 연구원", "생존분석·헬스케어 위험 모델링", ""),
                  ("COMPANY", "주닉션(JUNIXION) 대표", "응용 소프트웨어, 2026년 8월 개업", "")],
            open_title="OPEN TO",
            open=[("앱", "날봄 의견, 버그 제보, 번역 도움"), ("연구", "생존분석 · LLM / NLP · 통계 모델링"),
                  ("직무", "앱 · ML 연구 · AI · 퀀트 엔지니어"), ("학업", "금융공학 / AI 대학원, 2027년 입학")]),
}

def about(L, m):
    c, a = T[m], ABOUT[L]; W, H = 1280, 300; gap = 16; cw = (W - gap) / 2
    b = box(c, 0, 0, cw, H) + box(c, cw + gap, 0, cw, H)
    for i, (eye, title, line, note) in enumerate(a["left"]):
        y = 26 + i * 88
        if i:
            b += f'<line x1="32" y1="{y-6}" x2="{cw-32:.1f}" y2="{y-6}" stroke="{c["line"]}"/>'
        b += f'<text x="32" y="{y+20}" font-family="{MONO}" font-size="12.5" letter-spacing="2" fill="{c["faint"]}">{eye}</text>'
        b += f'<text x="32" y="{y+46}" font-size="18" font-weight="600" fill="{c["ink"]}">{esc(title)}</text>'
        b += f'<text x="32" y="{y+70}" font-size="15.5" fill="{c["sub"]}">{esc(line)}</text>'
        if note:
            b += f'<text x="{cw-32:.1f}" y="{y+46}" text-anchor="end" font-family="{MONO}" font-size="14" fill="{c["accent"]}">{esc(note)}</text>'
    x0 = cw + gap
    b += f'<text x="{x0+32:.1f}" y="46" font-family="{MONO}" font-size="12.5" letter-spacing="2" fill="{c["faint"]}">{a["open_title"]}</text>'
    for i, (k, v) in enumerate(a["open"]):
        y = 92 + i * 52
        b += f'<line x1="{x0+32:.1f}" y1="{y-30}" x2="{x0+cw-32:.1f}" y2="{y-30}" stroke="{c["line"]}"/>'
        b += f'<text x="{x0+32:.1f}" y="{y}" font-size="16" font-weight="600" fill="{c["ink"]}">{esc(k)}</text>'
        b += f'<text x="{x0+150:.1f}" y="{y}" font-size="15.5" fill="{c["sub"]}">{esc(v)}</text>'
    write("about", L, m, b, W, H)


# ---- premium styling (overrides)

T["dark"].update(card="#121828", card2="#0C111C", line="#263049", line2="#45516B", ink="#F5F7FB",
                 sub="#CDD4E1", faint="#A3ADC0", accent="#8DB6FF", violet="#C3A6FF", ok="#4ADE9B",
                 glow1="#2D5BD8", glow2="#6B47D6", bg0="#0B1020", bg1="#121533", dot="#FFFFFF")
T["light"].update(card="#FFFFFF", card2="#F5F8FE", line="#DFE5F0", line2="#C9D2E2", ink="#0F172A",
                  sub="#3F4A5C", faint="#667085", accent="#2160D4", violet="#7C5CE0", ok="#16A34A",
                  glow1="#9CC0FF", glow2="#D3C2FF", bg0="#F4F7FF", bg1="#FAF7FF", dot="#2160D4")

def _defs(c):
    return (f'<defs>'
            f'<linearGradient id="cardg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c["card"]}"/><stop offset="1" stop-color="{c["card2"]}"/></linearGradient>'
            f'<linearGradient id="edge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["accent"]}" stop-opacity="0"/><stop offset="0.25" stop-color="{c["accent"]}" stop-opacity="0.9"/><stop offset="0.6" stop-color="{c["violet"]}" stop-opacity="0.8"/><stop offset="1" stop-color="{c["violet"]}" stop-opacity="0"/></linearGradient>'
            f'<linearGradient id="accg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["accent"]}"/><stop offset="1" stop-color="{c["violet"]}"/></linearGradient>'
            f'<linearGradient id="inkg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["ink"]}"/><stop offset="0.7" stop-color="{c["ink"]}"/><stop offset="1" stop-color="{c["accent"]}"/></linearGradient>'
            f'</defs>')

def write(name, lang, mode, body, w, h):
    suffix = "" if lang == "en" else "-ko"
    with open(os.path.join(OUT, f"{name}{suffix}-{mode}.svg"), "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
                f'font-family="{SANS}">{_defs(T[mode])}{body}</svg>\n')

def box(c, x, y, w, h, r=14):
    hw = min(w * 0.6, 520)
    return (f'<rect x="{x+0.5:.1f}" y="{y+0.5:.1f}" width="{w-1:.1f}" height="{h-1:.1f}" rx="{r}" fill="url(#cardg)" stroke="{c["line"]}"/>'
            f'<rect x="{x+r+6:.1f}" y="{y+0.2:.1f}" width="{hw:.1f}" height="1.6" rx="0.8" fill="url(#edge)"/>')

def header(L, m):
    c, t = T[m], TX[L]; W, H = 1280, 296
    b = (f'<defs><radialGradient id="h1" cx="0.88" cy="0.05" r="0.55"><stop offset="0" stop-color="{c["glow1"]}" stop-opacity="0.45"/><stop offset="1" stop-color="{c["glow1"]}" stop-opacity="0"/></radialGradient>'
         f'<radialGradient id="h2" cx="0.55" cy="1.1" r="0.5"><stop offset="0" stop-color="{c["glow2"]}" stop-opacity="0.35"/><stop offset="1" stop-color="{c["glow2"]}" stop-opacity="0"/></radialGradient>'
         f'<linearGradient id="hb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c["bg0"]}"/><stop offset="1" stop-color="{c["bg1"]}"/></linearGradient>'
         f'<clipPath id="hc"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>')
    b += ANIM + f'<g clip-path="url(#hc)"><rect width="{W}" height="{H}" fill="url(#hb)"/><rect width="{W}" height="{H}" fill="url(#h1)"/><rect width="{W}" height="{H}" fill="url(#h2)"/></g>'
    b += f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{c["line"]}"/>'
    b += f'<rect x="40" y="0.2" width="560" height="1.8" rx="0.9" fill="url(#edge)"/>'
    # mini month: a quiet nod to Nalbom
    cs, gap = 22, 7; gx = W - 56 - 7 * (cs + gap) + gap; gy = 38
    b += f'<g font-family="{MONO}" font-size="10" fill="{c["faint"]}">'
    for k, d in enumerate("MTWTFSS"):
        b += f'<text x="{gx + k*(cs+gap) + cs/2:.1f}" y="{gy-6}" text-anchor="middle">{d}</text>'
    b += '</g>'
    day = 1 - 6  # month starts on Sunday column
    for row in range(6):
        for col in range(7):
            x = gx + col * (cs + gap); y = gy + 6 + row * (cs + gap)
            n = row * 7 + col + day
            if n < 1 or n > 30:
                continue
            if n == 5:      # today
                b += f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" rx="7" fill="url(#accg)"/>'
                b += f'<text x="{x+cs/2}" y="{y+15}" text-anchor="middle" font-family="{MONO}" font-size="10.5" font-weight="600" fill="#FFFFFF">{n}</text>'
                continue
            fill_op = 0.10 if m == "dark" else 0.07
            b += f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" rx="7" fill="{c["accent"]}" fill-opacity="{fill_op}"/>'
            col_txt = c["violet"] if col >= 5 else c["faint"]
            b += f'<text x="{x+cs/2}" y="{y+15}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{col_txt}" fill-opacity="0.85">{n}</text>'
            if n in (12, 19, 24):
                b += f'<circle cx="{x+cs/2}" cy="{y+cs-3}" r="1.5" fill="{c["violet"] if n == 24 else c["accent"]}"/>'
            if n == 24:     # a D-day ring
                b += f'<rect x="{x-1.5}" y="{y-1.5}" width="{cs+3}" height="{cs+3}" rx="8.5" fill="none" stroke="{c["violet"]}" stroke-width="1.5"/>'
    st = ""
    for k, (state, name, note) in enumerate(t["status"]):
        x = 56 + k * 300
        st += dot(c, x + 5, 251, state) + f'<text x="{x+18}" y="256"><tspan fill="{c["ink"]}">{esc(name)}</tspan>  {esc(note)}</text>'
    b += f"""<text x="56" y="70" font-family="{MONO}" font-size="14" letter-spacing="3" fill="{c['accent']}">JUNIXION / SEOUL</text>
<text x="54" y="138" font-size="50" font-weight="600" letter-spacing="-1.6" fill="url(#inkg)">Junyeong Song</text>
<text x="56" y="176" font-size="19.5" fill="{c['sub']}">{esc(t['sub'])}</text>
<line x1="56" y1="222" x2="{W-56}" y2="222" stroke="{c['line']}"/>
<g font-family="{MONO}" font-size="15" fill="{c['faint']}">{st}<text x="{W-56}" y="256" text-anchor="end">{t['est']}</text></g>"""
    write("header", L, m, b, W, H)

def section(L, m, key, num, title, note):
    c = T[m]; W, H = 1280, 60
    b = (f'<rect x="0" y="16" width="34" height="26" rx="8" fill="{c["accent"]}" fill-opacity="0.13"/>'
         f'<text x="17" y="34" text-anchor="middle" font-family="{MONO}" font-size="13.5" font-weight="600" fill="{c["accent"]}">{num}</text>'
         f'<text x="48" y="37" font-size="24" font-weight="600" letter-spacing="-0.5" fill="{c["ink"]}">{esc(title)}</text>'
         f'<text x="{W}" y="36" text-anchor="end" font-family="{MONO}" font-size="14" fill="{c["faint"]}">{esc(note)}</text>'
         f'<line x1="0" y1="{H-1}" x2="{W}" y2="{H-1}" stroke="{c["line"]}"/>'
         f'<rect x="0" y="{H-2}" width="140" height="2" rx="1" fill="url(#accg)"/>')
    write(f"section-{key}", L, m, b, W, H)

def kpi(L, m):
    c, t = T[m], TX[L]; W, H = 1280, 108; cw = W / 5
    b = box(c, 0, 0, W, H)
    for i, (n, l) in enumerate(t["kpi"]):
        x = i * cw
        if i:
            b += f'<line x1="{x:.1f}" y1="24" x2="{x:.1f}" y2="{H-24}" stroke="{c["line"]}"/>'
        b += f'<text x="{x+32:.1f}" y="56" font-size="30" font-weight="650" letter-spacing="-0.8" fill="url(#accg)">{n}</text>'
        b += f'<text x="{x+32:.1f}" y="81" font-family="{MONO}" font-size="14" fill="{c["faint"]}">{esc(l)}</text>'
    write("kpi", L, m, b, W, H)

def _icon_tile(c, x, y, path_svg):
    return (f'<rect x="{x-8:.1f}" y="{y-8:.1f}" width="36" height="36" rx="10" fill="{c["accent"]}" fill-opacity="0.12"/>'
            f'<g transform="translate({x:.1f},{y:.1f})" fill="none" stroke="{c["accent"]}" color="{c["accent"]}" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{path_svg}</g>')

def features(L, m):
    c, t = T[m], TX[L]; W = 1280; gap = 16; tw = (W - gap * 2) / 3; th = 214; H = th * 2 + gap
    b = ""
    for i, (ic, title, lines) in enumerate(t["features"]):
        x = (i % 3) * (tw + gap); y = (i // 3) * (th + gap)
        b += box(c, x, y, tw, th) + _icon_tile(c, x + 34, y + 30, FICONS[ic])
        b += f'<text x="{x+80:.1f}" y="{y+50}" font-size="18.5" font-weight="600" letter-spacing="-0.3" fill="{c["ink"]}">{esc(title)}</text>'
        b += f'<text x="{x+tw-30:.1f}" y="{y+50}" text-anchor="end" font-family="{MONO}" font-size="13" fill="{c["faint"]}">0{i+1}</text>'
        for j, l in enumerate(lines):
            ly = y + 100 + j * 28
            b += (f'<circle cx="{x+35:.1f}" cy="{ly-5}" r="2.4" fill="{c["violet"] if j % 2 else c["accent"]}" fill-opacity="0.85"/>'
                  f'<text x="{x+48:.1f}" y="{ly}" font-size="16" fill="{c["sub"]}">{esc(l)}</text>')
    write("features", L, m, b, W, H)

def grid(L, m, name, items):
    c = T[m]; W = 1280; gap = 16; tw = (W - gap * 2) / 3; th = 156
    rows = (len(items) + 2) // 3; H = th * rows + gap * (rows - 1)
    b = ""
    for i, (ic, title, lines) in enumerate(items):
        x = (i % 3) * (tw + gap); y = (i // 3) * (th + gap)
        b += box(c, x, y, tw, th) + _icon_tile(c, x + 34, y + 30, ICONS2[ic])
        b += f'<text x="{x+80:.1f}" y="{y+50}" font-size="18.5" font-weight="600" letter-spacing="-0.3" fill="{c["ink"]}">{esc(title)}</text>'
        for j, l in enumerate(lines):
            b += f'<text x="{x+30:.1f}" y="{y+98+j*28}" font-size="16" fill="{c["sub"]}">{esc(l)}</text>'
    write(name, L, m, b, W, H)

# ---- lead cards, project bars, stack chips, footer (overrides)

LEAD = {
 "en": {
   "nalbom": dict(q1="날마다 봄, 나를 돌아봄. 거꾸로 읽으면 봄날.",
                  q2="Seeing your days, looking back on yourself. Read backwards: bomnal, spring days.",
                  body=["Nalbom puts the dates you care about, your calendar, daily notes and everyday work tools into one app,",
                        "and shows them on the home screen and lock screen. iPhone, iPad, Mac (Apple silicon) and Android."],
                  label="BUILT WITH",
                  chips=["React Native 0.81", "Expo SDK 54", "TypeScript", "SQLite", "Swift", "Kotlin", "CloudKit", "Supabase", "RevenueCat", "Sentry"]),
   "web": dict(q1="", q2="",
               body=["The company website, built and run by me.", "Private repository, mirrored on GitHub and GitLab."],
               label="BUILT WITH", chips=["Next.js 16", "React 19", "Tailwind v4", "Vercel", "GitLab CI"]),
 },
 "ko": {
   "nalbom": dict(q1="날마다 봄, 나를 돌아봄. 거꾸로 읽으면 봄날.",
                  q2="챙겨야 할 날을 날마다 보고, 하루 한 줄로 나를 돌아보는 달력.",
                  body=["날봄은 챙겨야 할 날, 캘린더, 하루 메모, 직장인 도구를 한 앱에 담고 홈 화면과 잠금화면에 보여 줍니다.",
                        "아이폰, 아이패드, 맥(Apple 실리콘), 안드로이드에서 쓸 수 있어요."],
                  label="BUILT WITH",
                  chips=["React Native 0.81", "Expo SDK 54", "TypeScript", "SQLite", "Swift", "Kotlin", "CloudKit", "Supabase", "RevenueCat", "Sentry"]),
   "web": dict(q1="", q2="",
               body=["회사 웹사이트입니다. 직접 만들고 운영해요.", "비공개 저장소이고 GitHub와 GitLab에 함께 올려요."],
               label="BUILT WITH", chips=["Next.js 16", "React 19", "Tailwind v4", "Vercel", "GitLab CI"]),
 },
}

def _chips(c, x, y, items, size=13, h=28, char=7.4, dotcol=None):
    out = ""
    for t in items:
        w = sum(1.75 if ord(ch) > 127 else 1 for ch in t) * char + 24 + (10 if dotcol else 0)
        out += f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="8" fill="{c["accent"]}" fill-opacity="0.07" stroke="{c["line2"]}" stroke-opacity="0.7"/>'
        tx = x + 12
        if dotcol:
            out += f'<circle cx="{x+13:.1f}" cy="{y+h/2:.1f}" r="3" fill="{dotcol}"/>'
            tx += 10
        out += f'<text x="{tx:.1f}" y="{y+h/2+4.6:.1f}" font-size="{size}" fill="{c["ink"]}">{esc(t)}</text>'
        x += w + 8
    return out

def lead(L, m, key):
    c, d = T[m], LEAD[L][key]; W = 1280
    has_q = bool(d["q1"])
    H = 232 if has_q else 156
    b = box(c, 0, 0, W, H)
    y = 46
    if has_q:
        b += f'<rect x="32" y="26" width="3" height="52" rx="1.5" fill="url(#accg)"/>'
        b += f'<text x="50" y="46" font-size="18" font-weight="600" fill="{c["ink"]}">{esc(d["q1"])}</text>'
        b += f'<text x="50" y="72" font-size="15.5" font-style="italic" fill="{c["sub"]}">{esc(d["q2"])}</text>'
        y = 118
    for i, line in enumerate(d["body"]):
        b += f'<text x="32" y="{y + i*26}" font-size="16" fill="{c["sub"]}">{esc(line)}</text>'
    ly = y + len(d["body"]) * 26 - 4
    b += f'<line x1="32" y1="{ly}" x2="{W-32}" y2="{ly}" stroke="{c["line"]}"/>'
    b += f'<text x="32" y="{ly+33}" font-family="{MONO}" font-size="12.5" letter-spacing="2" fill="{c["faint"]}">{d["label"]}</text>'
    b += _chips(c, 150, ly + 14, d["chips"])
    write(f"lead-{key}", L, m, b, W, H)

def project(L, m, key, eye, title, desc, metric, kind):
    c = T[m]; W, H = 632, 176
    b = ANIM + box(c, 0, 0, W, H)
    b += f'<text x="28" y="40" font-family="{MONO}" font-size="13" letter-spacing="2.2" fill="{c["faint"]}">{esc(eye)}</text>'
    if kind == "live":
        b += dot(c, 28 + len(eye) * 10.2 + 12, 35.5, "live")
    if kind != "private":
        b += f'<text x="{W-28}" y="41" text-anchor="end" font-family="{MONO}" font-size="15" fill="{c["accent"]}">↗</text>'
    b += f'<text x="28" y="80" font-size="22" font-weight="600" letter-spacing="-0.5" fill="{c["ink"]}">{esc(title)}</text>'
    b += f'<text x="28" y="108" font-size="15.5" fill="{c["sub"]}">{esc(desc)}</text>'
    b += f'<line x1="28" y1="128" x2="{W-28}" y2="128" stroke="{c["line"]}"/>'
    mm = re.match(r"(C-index|ROC-AUC) ([0-9.]+)", metric)
    if mm:
        v = float(mm.group(2))
        b += (f'<text x="28" y="155" font-family="{MONO}" font-size="14" fill="{c["faint"]}">{mm.group(1)}'
              f'<tspan dx="8" font-size="16" font-weight="600" fill="url(#accg)">{mm.group(2)}</tspan></text>')
        bx, bw = W - 28 - 240, 240
        b += f'<rect x="{bx}" y="146" width="{bw}" height="6" rx="3" fill="{c["line"]}"/>'
        b += f'<rect x="{bx}" y="146" width="{bw*v:.1f}" height="6" rx="3" fill="url(#accg)"/>'
        b += f'<line x1="{bx+bw*0.5:.1f}" y1="142" x2="{bx+bw*0.5:.1f}" y2="156" stroke="{c["faint"]}" stroke-opacity="0.6"/>'
    else:
        parts = [p.strip() for p in metric.split("·")]
        b += _chips(c, 28, 139, parts, size=12.5, h=26, char=7.6)
    write(f"project-{key}", L, m, b, W, H)

def stack(L, m):
    c = T[m]; W = 1280; rh = 64; H = 24 + rh * 3 + 8
    b = box(c, 0, 0, W, H)
    cols = [c["accent"], c["violet"], c["ok"]]
    for i, (label, tools) in enumerate(STACK[L]):
        y = 24 + i * rh
        if i:
            b += f'<line x1="32" y1="{y}" x2="{W-32}" y2="{y}" stroke="{c["line"]}"/>'
        b += f'<circle cx="37" cy="{y+33}" r="4" fill="{cols[i]}"/>'
        b += f'<text x="52" y="{y+38}" font-family="{MONO}" font-size="13.5" letter-spacing="2" fill="{c["faint"]}">{esc(label)}</text>'
        b += _chips(c, 250, y + 18, tools, size=15, h=32, char=8.4, dotcol=None)
    write("stack", L, m, b, W, H)

FOOT = {"en": ("Software for every day, built and backed to last.", "Questions, feedback or a hello — I read every message.",
               ["junixion.com", "contact@junixion.com", "seoul"]),
        "ko": ("매일 손이 가는 소프트웨어를, 끝까지 책임지고 만듭니다.", "질문, 의견, 인사 모두 환영해요. 메일은 모두 직접 읽어요.",
               ["junixion.com", "contact@junixion.com", "seoul"])}

def footer(L, m):
    c = T[m]; W, H = 1280, 188; t1, t2, links = FOOT[L]
    b = (f'<defs><radialGradient id="f1" cx="0.12" cy="1.1" r="0.6"><stop offset="0" stop-color="{c["glow1"]}" stop-opacity="0.4"/><stop offset="1" stop-color="{c["glow1"]}" stop-opacity="0"/></radialGradient>'
         f'<radialGradient id="f2" cx="0.92" cy="-0.1" r="0.55"><stop offset="0" stop-color="{c["glow2"]}" stop-opacity="0.35"/><stop offset="1" stop-color="{c["glow2"]}" stop-opacity="0"/></radialGradient>'
         f'<linearGradient id="fb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c["bg0"]}"/><stop offset="1" stop-color="{c["bg1"]}"/></linearGradient>'
         f'<clipPath id="fc"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>'
         f'<g clip-path="url(#fc)"><rect width="{W}" height="{H}" fill="url(#fb)"/><rect width="{W}" height="{H}" fill="url(#f1)"/><rect width="{W}" height="{H}" fill="url(#f2)"/></g>'
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{c["line"]}"/>'
         f'<rect x="40" y="0.2" width="560" height="1.8" rx="0.9" fill="url(#edge)"/>'
         f'<text x="56" y="70" font-family="{MONO}" font-size="13.5" letter-spacing="3" fill="{c["accent"]}">JUNIXION</text>'
         f'<text x="56" y="110" font-size="26" font-weight="600" letter-spacing="-0.6" fill="url(#inkg)">{esc(t1)}</text>'
         f'<text x="56" y="142" font-size="16" fill="{c["sub"]}">{esc(t2)}</text>')
    y = 70
    for i, l in enumerate(links):
        b += f'<text x="{W-56}" y="{y + i*30}" text-anchor="end" font-family="{MONO}" font-size="14.5" fill="{c["ink"] if i < 2 else c["faint"]}">{esc(l)}</text>'
    write("footer", L, m, b, W, H)

# ---- README text
# ---- phone layouts (shown under 600px wide through <picture media>)
MW = 480


def text_w(s, size, mono=False):
    w = 0.0
    for ch in s:
        if ord(ch) > 0x2E80:
            w += size * 0.98
        elif mono:
            w += size * 0.61
        elif ch in "il.,:;'|!·":
            w += size * 0.28
        elif ch.isupper() or ch in "mwMW":
            w += size * 0.68
        else:
            w += size * 0.53
    return w


def wrap(s, size, maxw, mono=False):
    words, lines, cur = s.split(" "), [], ""
    for wd in words:
        cand = (cur + " " + wd).strip()
        if cur and text_w(cand, size, mono) > maxw:
            lines.append(cur)
            cur = wd
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return lines


def mtext(x, y, lines, size, fill, step, weight=None, mono=False, italic=False, extra=""):
    attrs = f'font-size="{size}" fill="{fill}"'
    if weight:
        attrs += f' font-weight="{weight}"'
    if mono:
        attrs += f' font-family="{MONO}"'
    if italic:
        attrs += ' font-style="italic"'
    return "".join(f'<text x="{x}" y="{y + i*step:.1f}" {attrs} {extra}>{esc(l)}</text>' for i, l in enumerate(lines))


def mchips(c, x0, y, items, maxw, size=14, h=30, gap=8):
    out, x = "", x0
    for t in items:
        w = text_w(t, size) + 24
        if x > x0 and x + w > x0 + maxw:
            x, y = x0, y + h + gap
        out += (f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="8" fill="{T_CUR["accent"]}" fill-opacity="0.07" stroke="{T_CUR["line2"]}" stroke-opacity="0.7"/>'
                f'<text x="{x+12:.1f}" y="{y+h/2+5:.1f}" font-size="{size}" fill="{T_CUR["ink"]}">{esc(t)}</text>')
        x += w + gap
    return out, y + h


def glow_bg(c, W, H, pid):
    return (f'<defs><radialGradient id="{pid}1" cx="0.95" cy="0" r="0.8"><stop offset="0" stop-color="{c["glow1"]}" stop-opacity="0.45"/><stop offset="1" stop-color="{c["glow1"]}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="{pid}2" cx="0.1" cy="1.05" r="0.8"><stop offset="0" stop-color="{c["glow2"]}" stop-opacity="0.35"/><stop offset="1" stop-color="{c["glow2"]}" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{pid}b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c["bg0"]}"/><stop offset="1" stop-color="{c["bg1"]}"/></linearGradient>'
            f'<clipPath id="{pid}c"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>'
            f'<g clip-path="url(#{pid}c)"><rect width="{W}" height="{H}" fill="url(#{pid}b)"/><rect width="{W}" height="{H}" fill="url(#{pid}1)"/><rect width="{W}" height="{H}" fill="url(#{pid}2)"/></g>'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{c["line"]}"/>'
            f'<rect x="24" y="0.2" width="300" height="1.8" rx="0.9" fill="url(#edge)"/>')


def m_header(L, m):
    c, t = T[m], TX[L]; W = MW
    sub = wrap(t["sub"], 17, W - 56)
    y_sub = 120
    y_line = y_sub + len(sub) * 25 + 6
    H = y_line + 3 * 28 + 30
    b = ANIM + glow_bg(c, W, H, "mh")
    b += f'<text x="28" y="50" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{c["accent"]}">JUNIXION / SEOUL</text>'
    b += f'<text x="26" y="94" font-size="38" font-weight="600" letter-spacing="-1.2" fill="url(#inkg)">Junyeong Song</text>'
    b += mtext(28, y_sub, sub, 17, c["sub"], 25)
    b += f'<line x1="28" y1="{y_line}" x2="{W-28}" y2="{y_line}" stroke="{c["line"]}"/>'
    for k, (state, name, note) in enumerate(t["status"]):
        y = y_line + 32 + k * 28
        b += dot(c, 33, y - 5, state)
        b += f'<text x="46" y="{y}" font-family="{MONO}" font-size="14" fill="{c["faint"]}"><tspan fill="{c["ink"]}">{esc(name)}</tspan>  {esc(note)}</text>'
    write("header-m", L, m, b, W, H)


def m_section(L, m, key, num, title, note):
    c = T[m]; W, H = MW, 56
    b = (f'<rect x="0" y="14" width="34" height="26" rx="8" fill="{c["accent"]}" fill-opacity="0.13"/>'
         f'<text x="17" y="32" text-anchor="middle" font-family="{MONO}" font-size="13.5" font-weight="600" fill="{c["accent"]}">{num}</text>'
         f'<text x="46" y="35" font-size="23" font-weight="600" letter-spacing="-0.5" fill="{c["ink"]}">{esc(title)}</text>'
         f'<line x1="0" y1="{H-1}" x2="{W}" y2="{H-1}" stroke="{c["line"]}"/>'
         f'<rect x="0" y="{H-2}" width="110" height="2" rx="1" fill="url(#accg)"/>')
    write(f"section-{key}-m", L, m, b, W, H)


def m_now(L, m):
    c, t = T[m], TX[L]; W = MW; gap = 14
    parts, y = [], 0
    b = ANIM
    for (eye, title, tk, lead_, desc, state, st, meta) in t["now"]:
        lead_l = wrap(lead_, 16.5, W - 56)
        desc_l = wrap(desc, 15, W - 56)
        h = 92 + len(lead_l) * 23 + len(desc_l) * 22 + 70
        b += box(c, 0, y, W, h)
        b += f'<text x="28" y="{y+38}" font-family="{MONO}" font-size="12.5" letter-spacing="2.5" fill="{c["faint"]}">{eye}</text>'
        b += (f'<text x="28" y="{y+76}" font-size="27" font-weight="600" letter-spacing="-0.8" fill="{c["ink"]}">{esc(title)}'
              + (f'<tspan dx="8" font-size="18" font-weight="500" fill="{c["faint"]}">{tk}</tspan>' if tk else "") + '</text>')
        yy = y + 106
        b += mtext(28, yy, lead_l, 16.5, c["ink"], 23, weight=500)
        yy += len(lead_l) * 23
        b += mtext(28, yy, desc_l, 15, c["sub"], 22)
        yy += len(desc_l) * 22 - 6
        b += f'<line x1="28" y1="{yy}" x2="{W-28}" y2="{yy}" stroke="{c["line"]}"/>'
        b += dot(c, 33, yy + 22, state)
        b += f'<text x="46" y="{yy+27}" font-family="{MONO}" font-size="13.5" fill="{c["ink"]}">{esc(st)}</text>'
        b += f'<text x="28" y="{yy+51}" font-family="{MONO}" font-size="13" fill="{c["faint"]}">{meta}</text>'
        y += h + gap
    write("now-m", L, m, b, W, y - gap)


def m_roadmap(L, m):
    c, t = T[m], TX[L]; W = MW; row = 64
    H = 64 + row * len(t["roadmap"]) - 10
    b = ANIM + box(c, 0, 0, W, H)
    b += f'<text x="28" y="40" font-family="{MONO}" font-size="12.5" letter-spacing="2.5" fill="{c["faint"]}">{t["roadmap_title"]}</text>'
    for i, (state, when, title, note) in enumerate(t["roadmap"]):
        y = 76 + i * row
        if i < len(t["roadmap"]) - 1:
            done_next = state == "done"
            b += f'<line x1="36" y1="{y+8}" x2="36" y2="{y+row-8}" stroke="{c["ok"] if done_next else c["line2"]}" stroke-width="{2 if done_next else 1.4}"/>'
        if state == "done":
            b += f'<circle cx="36" cy="{y}" r="7" fill="{c["ok"]}"/><path d="M32.8 {y} l2.2 2.2 l4 -4.4" fill="none" stroke="{c["card"]}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>'
        elif state == "next":
            b += f'<circle class="p" cx="36" cy="{y}" r="7" fill="{c["accent"]}"/><circle cx="36" cy="{y}" r="7" fill="{c["card"]}" stroke="{c["accent"]}" stroke-width="2.4"/>'
        else:
            b += f'<circle cx="36" cy="{y}" r="6" fill="{c["card"]}" stroke="{c["line2"]}" stroke-width="1.5"/>'
        b += f'<text x="60" y="{y+5}" font-size="17" font-weight="600" fill="{c["ink"]}">{esc(title)}</text>'
        b += f'<text x="{W-28}" y="{y+5}" text-anchor="end" font-family="{MONO}" font-size="13" fill="{c["accent"] if state=="next" else c["faint"]}">{esc(when)}</text>'
        b += f'<text x="60" y="{y+28}" font-size="14.5" fill="{c["sub"]}">{esc(note)}</text>'
    write("roadmap-m", L, m, b, W, H)


def m_kpi(L, m):
    c, t = T[m], TX[L]; W = MW; cw = (W - 2) / 2; rh = 84
    items = t["kpi"]; rows = (len(items) + 1) // 2; H = rows * rh
    b = box(c, 0, 0, W, H)
    for i, (n, l) in enumerate(items):
        x = (i % 2) * cw; y = (i // 2) * rh
        if i % 2:
            b += f'<line x1="{x:.1f}" y1="{y+18}" x2="{x:.1f}" y2="{y+rh-18}" stroke="{c["line"]}"/>'
        if i >= 2 and i % 2 == 0:
            b += f'<line x1="24" y1="{y}" x2="{W-24}" y2="{y}" stroke="{c["line"]}"/>'
        b += f'<text x="{x+28:.1f}" y="{y+44}" font-size="30" font-weight="650" letter-spacing="-0.8" fill="url(#accg)">{n}</text>'
        b += f'<text x="{x+28:.1f}" y="{y+66}" font-family="{MONO}" font-size="13" fill="{c["faint"]}">{esc(l)}</text>'
    write("kpi-m", L, m, b, W, H)


def m_lead(L, m, key):
    global T_CUR
    c, d = T[m], LEAD[L][key]; W = MW; T_CUR = c
    b, y = "", 40
    if d["q1"]:
        q1 = wrap(d["q1"], 17.5, W - 70); q2 = wrap(d["q2"], 15, W - 70)
        qh = len(q1) * 25 + len(q2) * 22
        b += f'<rect x="28" y="{y-18}" width="3" height="{qh+2}" rx="1.5" fill="url(#accg)"/>'
        b += mtext(44, y, q1, 17.5, c["ink"], 25, weight=600)
        b += mtext(44, y + len(q1) * 25, q2, 15, c["sub"], 22, italic=True)
        y += qh + 24
    body = wrap(" ".join(d["body"]), 16, W - 56)
    b += mtext(28, y, body, 16, c["sub"], 24)
    y += len(body) * 24 + 2
    b += f'<line x1="28" y1="{y}" x2="{W-28}" y2="{y}" stroke="{c["line"]}"/>'
    b += f'<text x="28" y="{y+30}" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{c["faint"]}">{d["label"]}</text>'
    chips, end = mchips(c, 28, y + 44, d["chips"], W - 56, size=13.5, h=28)
    H = end + 24
    write(f"lead-{key}-m", L, m, box(c, 0, 0, W, H) + b + chips, W, H)


def m_cards(L, m, name, items, icons, numbered):
    c = T[m]; W = MW; gap = 12; y = 0; b = ""
    for i, (ic, title, lines) in enumerate(items):
        h = 74 + len(lines) * 26 + 6
        b += box(c, 0, y, W, h) + _icon_tile(c, 34, y + 26, icons[ic])
        b += f'<text x="80" y="{y+46}" font-size="18.5" font-weight="600" letter-spacing="-0.3" fill="{c["ink"]}">{esc(title)}</text>'
        if numbered:
            b += f'<text x="{W-28}" y="{y+46}" text-anchor="end" font-family="{MONO}" font-size="13" fill="{c["faint"]}">0{i+1}</text>'
        for j, l in enumerate(lines):
            ly = y + 92 + j * 26
            b += (f'<circle cx="35" cy="{ly-5}" r="2.4" fill="{c["violet"] if j % 2 else c["accent"]}" fill-opacity="0.85"/>'
                  f'<text x="48" y="{ly}" font-size="15.5" fill="{c["sub"]}">{esc(l)}</text>')
        y += h + gap
    write(name, L, m, b, W, y - gap)


def m_research(L, m):
    c, r = T[m], RESEARCH[L]; W = MW
    title = wrap(" ".join(x for x in r["title"] if x), 23, W - 56)
    sub = wrap(r["sub"], 14.5, W - 56)
    b = ""
    b += f'<text x="28" y="40" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{c["faint"]}">{esc(r["eye"])}</text>'
    b += mtext(28, 78, title, 23, c["ink"], 30, weight=600, extra='letter-spacing="-0.6"')
    y = 78 + len(title) * 30
    b += mtext(28, y, sub, 14.5, c["sub"], 21)
    y += len(sub) * 21 + 4
    cw = (W - 56) / 2
    for i, (n, l) in enumerate(r["tiles"]):
        x = 28 + (i % 2) * cw; yy = y + (i // 2) * 72
        b += f'<line x1="{x:.1f}" y1="{yy}" x2="{x+cw-12:.1f}" y2="{yy}" stroke="{c["line"]}"/>'
        b += f'<text x="{x:.1f}" y="{yy+38}" font-size="28" font-weight="600" letter-spacing="-0.8" fill="{c["ink"] if i else c["accent"]}">{n}</text>'
        b += f'<text x="{x:.1f}" y="{yy+60}" font-family="{MONO}" font-size="13" fill="{c["faint"]}">{esc(l)}</text>'
    y += 2 * 72 + 8
    b += f'<line x1="28" y1="{y}" x2="{W-28}" y2="{y}" stroke="{c["line"]}"/>'
    for i, (k, v) in enumerate(r["finds"]):
        yy = y + 30 + i * 28
        b += f'<text x="28" y="{yy}" font-size="14.5" fill="{c["sub"]}">{esc(k)}</text>'
        b += f'<text x="{W-28}" y="{yy}" text-anchor="end" font-family="{MONO}" font-size="13.5" fill="{c["ink"]}">{esc(v)}</text>'
    y += 30 + 3 * 28
    b += f'<text x="28" y="{y}" font-family="{MONO}" font-size="13.5" fill="{c["accent"]}">read on ssrn ↗</text>'
    H = y + 26
    write("research-m", L, m, box(c, 0, 0, W, H) + b, W, H)


def m_project(L, m, key, eye, title, desc, metric, kind):
    # each card shows at about half the phone width, so type is set large
    c = T[m]; W, H = 300, 300
    b = ANIM + box(c, 0, 0, W, H)
    b += f'<text x="22" y="40" font-family="{MONO}" font-size="16" letter-spacing="1.5" fill="{c["faint"]}">{esc(eye.split(" · ")[0])}</text>'
    if kind == "live":
        b += dot(c, W - 30, 35, "live")
    elif kind != "private":
        b += f'<text x="{W-22}" y="41" text-anchor="end" font-family="{MONO}" font-size="20" fill="{c["accent"]}">↗</text>'
    tl = wrap(title, 26, W - 44)[:3]
    b += mtext(22, 88, tl, 26, c["ink"], 32, weight=600, extra='letter-spacing="-0.6"')
    mm = re.match(r"(C-index|ROC-AUC) ([0-9.]+)", metric)
    if mm:
        v = float(mm.group(2))
        b += f'<text x="22" y="236" font-size="36" font-weight="650" letter-spacing="-1" fill="url(#accg)">{mm.group(2)}</text>'
        b += f'<text x="22" y="262" font-family="{MONO}" font-size="16" fill="{c["faint"]}">{mm.group(1)}</text>'
        b += f'<rect x="22" y="274" width="{W-44}" height="8" rx="4" fill="{c["line"]}"/><rect x="22" y="274" width="{(W-44)*v:.1f}" height="8" rx="4" fill="url(#accg)"/>'
    else:
        parts = [p.strip() for p in metric.split("·")]
        b += mtext(22, 236, parts, 20, c["ink"], 28, weight=600, mono=True)
    write(f"project-{key}-m", L, m, b, W, H)


def m_stack(L, m):
    global T_CUR
    c = T[m]; W = MW; T_CUR = c; cols = [c["accent"], c["violet"], c["ok"]]
    b, y = "", 22
    for i, (label, tools) in enumerate(STACK[L]):
        if i:
            b += f'<line x1="28" y1="{y-10}" x2="{W-28}" y2="{y-10}" stroke="{c["line"]}"/>'
        b += f'<circle cx="33" cy="{y+12}" r="4" fill="{cols[i]}"/>'
        b += f'<text x="46" y="{y+17}" font-family="{MONO}" font-size="12.5" letter-spacing="2" fill="{c["faint"]}">{esc(label)}</text>'
        chips, end = mchips(c, 28, y + 32, tools, W - 56, size=14.5, h=30)
        b += chips
        y = end + 30
    H = y - 6
    write("stack-m", L, m, box(c, 0, 0, W, H) + b, W, H)


def m_about(L, m):
    c, a = T[m], ABOUT[L]; W = MW; b = ""; y = 0
    h1 = 24 + len(a["left"]) * 86
    b += box(c, 0, 0, W, h1)
    for i, (eye, title, line, note) in enumerate(a["left"]):
        yy = 24 + i * 86
        if i:
            b += f'<line x1="28" y1="{yy-6}" x2="{W-28}" y2="{yy-6}" stroke="{c["line"]}"/>'
        b += f'<text x="28" y="{yy+18}" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{c["faint"]}">{eye}</text>'
        if note:
            b += f'<text x="{W-28}" y="{yy+18}" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{c["accent"]}">{esc(note)}</text>'
        b += f'<text x="28" y="{yy+44}" font-size="17.5" font-weight="600" fill="{c["ink"]}">{esc(title)}</text>'
        b += f'<text x="28" y="{yy+67}" font-size="15" fill="{c["sub"]}">{esc(line)}</text>'
    y = h1 + 14
    rows = [(k, wrap(v, 15, W - 56)) for k, v in a["open"]]
    h2 = 56 + sum(30 + len(v) * 21 for _, v in rows)
    b += box(c, 0, y, W, h2)
    b += f'<text x="28" y="{y+40}" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{c["faint"]}">{a["open_title"]}</text>'
    yy = y + 62
    for k, v in rows:
        b += f'<line x1="28" y1="{yy-8}" x2="{W-28}" y2="{yy-8}" stroke="{c["line"]}"/>'
        b += f'<text x="28" y="{yy+14}" font-size="15.5" font-weight="600" fill="{c["ink"]}">{esc(k)}</text>'
        b += mtext(28, yy + 37, v, 15, c["sub"], 21)
        yy += 30 + len(v) * 21
    write("about-m", L, m, b, W, y + h2)


def m_footer(L, m):
    c = T[m]; W = MW; t1, t2, links = FOOT[L]
    l1 = wrap(t1, 22, W - 56); l2 = wrap(t2, 15, W - 56)
    y = 92 + len(l1) * 30 + len(l2) * 22 + 10
    H = y + len(links) * 26 + 18
    b = glow_bg(c, W, H, "mf")
    b += f'<text x="28" y="50" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{c["accent"]}">JUNIXION</text>'
    b += mtext(28, 88, l1, 22, "url(#inkg)", 30, weight=600, extra='letter-spacing="-0.5"')
    b += mtext(28, 88 + len(l1) * 30, l2, 15, c["sub"], 22)
    b += f'<line x1="28" y1="{y-14}" x2="{W-28}" y2="{y-14}" stroke="{c["line"]}"/>'
    for i, l in enumerate(links):
        b += f'<text x="28" y="{y + 14 + i*26}" font-family="{MONO}" font-size="14" fill="{c["ink"] if i < 2 else c["faint"]}">{esc(l)}</text>'
    write("footer-m", L, m, b, W, H)


T_CUR = None


def build_mobile():
    for m in T:
        for L in LANGS:
            m_header(L, m); m_now(L, m); m_roadmap(L, m); m_kpi(L, m)
            for s in TX[L]["sections"]:
                m_section(L, m, *s)
            m_lead(L, m, "nalbom"); m_lead(L, m, "web")
            m_cards(L, m, "features-m", TX[L]["features"], FICONS, True)
            m_cards(L, m, "web-m", WEB[L], ICONS2, False)
            m_research(L, m); m_stack(L, m); m_about(L, m); m_footer(L, m)
            for p in TX[L]["projects"]:
                m_project(L, m, *p)



def pic(name, alt, lang="en", link=None, width="100%", height=None):
    """<picture> with light/dark images, plus phone-sized ones when they exist."""
    suf = "" if lang == "en" else "-ko"
    size = f'height="{height}"' if height else f'width="{width}"'
    srcs = ""
    if os.path.exists(os.path.join(OUT, f"{name}-m{suf}-light.svg")):
        srcs += (f'<source media="{PHONE} and (prefers-color-scheme: dark)" srcset="./assets/{name}-m{suf}-dark.svg" />'
                 f'<source media="{PHONE}" srcset="./assets/{name}-m{suf}-light.svg" />')
    p = (f'<picture>{srcs}<source media="(prefers-color-scheme: dark)" srcset="./assets/{name}{suf}-dark.svg" />'
         f'<img src="./assets/{name}{suf}-light.svg" {size} alt="{alt}" /></picture>')
    return f'<a href="{link}">{p}</a>' if link else p


PHONE = "(max-width: 600px)"


def neutral(name, alt, link, height=34):
    # language-neutral asset (social segments)
    p = (f'<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/{name}-dark.svg" />'
         f'<img src="./assets/{name}-light.svg" height="{height}" alt="{alt}" /></picture>')
    return f'<a href="{link}">{p}</a>' if link else p

SOCIAL = [
    ("company", "JUNIXION", [("instagram", "https://www.instagram.com/junixion.official/"), ("threads", "https://www.threads.com/@junixion.official"),
                              ("x", "https://x.com/junixion"), ("facebook", "https://www.facebook.com/junixion.official")]),
    ("nalbom", "Nalbom", [("instagram", "https://www.instagram.com/nalbom.app/"), ("threads", "https://www.threads.com/@nalbom.app"),
                          ("x", "https://x.com/nalbomapp"), ("facebook", "https://www.facebook.com/nalbomapp"), ("tiktok", "https://www.tiktok.com/@nalbom.app")]),
    ("dev", "Developer", [("linkedin", "https://www.linkedin.com/in/jun-yeong-song/"), ("gitlab", "https://gitlab.com/jjuunnii98"),
                          ("huggingface", "https://huggingface.co/JUNIXION")]),
]
NAMES = {"instagram": "Instagram", "threads": "Threads", "x": "X", "facebook": "Facebook", "tiktok": "TikTok",
         "linkedin": "LinkedIn", "gitlab": "GitLab", "huggingface": "Hugging Face"}

def social_bars():
    rows = []
    for key, who, items in SOCIAL:
        row = neutral(f"social-{key}-label", who, None)
        row += "".join(neutral(f"social-{key}-{n}", f"{who} on {NAMES[n]}", url) for n, url in items)
        rows.append(row)
    return "<br>\n".join(rows)

PROJECT_LINKS = {
    "krx": "https://github.com/jjuunnii98/survival-analysis-finance",
    "lm": "https://huggingface.co/JUNIXION",
    "crypto": "https://crypto-risk-scoring-demo.onrender.com/docs",
    "e2e": "https://ml-churn-api-2z9m.onrender.com/docs",
    "grad": "https://survival-api.onrender.com/docs",
    "sql": "https://github.com/jjuunnii98/sql-analytics-portfolio",
}

def project_grid(lang):
    keys = list(PROJECT_LINKS)
    lines = []
    for i in range(0, len(keys), 2):
        pair = keys[i:i + 2]
        lines.append(" ".join(pic(f"project-{k}", k, lang, PROJECT_LINKS[k], width="49.5%") for k in pair))
    return "\n<br>\n".join(lines)

# ------------------------------------------------------------------ text blocks
C = {}
C["en"] = dict(
    toggle='<p align="right"><sub><b>English</b> · <a href="./README.ko.md">한국어</a></sub></p>',
    header_alt="Junyeong Song — Founder of JUNIXION, app developer in Seoul",
    links='<sub><a href="https://junixion.com">junixion.com</a> · <a href="mailto:contact@junixion.com">contact@junixion.com</a> · <a href="https://papers.ssrn.com/abstract=6656258">SSRN paper</a></sub>',
    now_alt="Nalbom, launching November 2026, and junixion.com, the company website",
    roadmap_alt="Nalbom roadmap: TestFlight beta, Google Play testing, launch in November 2026, regular updates, app number two in 2027",
    kpi_alt="151 countries' holidays, 4 platforms, 3 languages, end-to-end encrypted sharing, 745 Nalbom commits",
    quote="> **날마다 봄, 나를 돌아봄. 거꾸로 읽으면 봄날.**  \n> *Seeing your days, looking back on yourself. Read backwards: bomnal, spring days.*",
    nalbom_intro="Nalbom puts the dates you care about, your calendar, daily notes and everyday work tools into one app, and shows them on the home screen and lock screen. It runs on iPhone, iPad, Mac (Apple silicon) and Android.",
    features_alt="Nalbom features: calendar, D-days and notes, work tools, widgets and live activities, shared spaces, themes",
    built_summary="How it is built",
    web_more="Website details", research_more="Full results", certs_alt="", web_alt="junixion.com: three languages, Nalbom pages, legal pages that match the app, private invite links, small and quiet, checked on every change", research_alt="Working paper: Survival Analysis of Corporate Delisting Risk in the Korean Stock Market. C-index 0.738, 365 firms, 158 delisting events, 276 months", stack_alt="Stack: apps, web and backend, ML and statistics", about_alt="Yonsei University, Economics and Information Statistics, expected February 2027. Founder of JUNIXION. Open to app feedback, research, roles and graduate study",
    built=None,  # taken from the current README
    nalbom_tech="React Native 0.81 · Expo SDK 54 · TypeScript · SQLite · Swift · Kotlin · CloudKit · Supabase · RevenueCat · Sentry",
    web_intro="The company website, built and run by me. Private repository, mirrored on GitHub and GitLab.",
    web_list=None,
    web_tech="Next.js 16 · React 19 · Tailwind v4 · Vercel · GitLab CI",
    research=None,
    projects_more=None,
    projects_summary="Details",
    stack="""| Area | Tools |
|---|---|
| **Apps** | React Native · Expo · TypeScript · Swift · Kotlin · SQLite · CloudKit |
| **Web & backend** | Next.js · Tailwind CSS · Supabase · PostgreSQL · Deno · Vercel · GitLab CI |
| **ML & statistics** | Python · PyTorch · scikit-learn · pandas · R · SAS · FastAPI · Docker |""",
    activity_alt="GitHub activity over the last 26 weeks",
    about="""**Yonsei University** — Economics × Information Statistics · Expected February 2027
Undergraduate Research Assistant — Survival Analysis & Healthcare Risk Modeling
Founder — JUNIXION (application software, opened August 2026)""",
    certs=None,
    connect="""| Area | Open to |
|---|---|
| Apps | Nalbom feedback, bug reports and localization help |
| Research | Survival analysis · LLM / NLP · statistical modeling |
| Roles | App engineer · ML researcher · AI engineer · Quant engineer |
| Academia | Financial Engineering / AI graduate programs (2027 entry) |""",
    footer_alt="Software for every day, built and backed to last. JUNIXION, Seoul, contact@junixion.com",
)

C["ko"] = dict(
    toggle='<p align="right"><sub><a href="./README.md">English</a> · <b>한국어</b></sub></p>',
    header_alt="Junyeong Song — 주닉션 대표, 서울의 앱 개발자",
    links='<sub><a href="https://junixion.com">junixion.com</a> · <a href="mailto:contact@junixion.com">contact@junixion.com</a> · <a href="https://papers.ssrn.com/abstract=6656258">SSRN 논문</a></sub>',
    now_alt="2026년 11월 출시 예정인 날봄과 회사 웹사이트 junixion.com",
    roadmap_alt="날봄 출시 길: TestFlight 베타, Google Play 테스트, 2026년 11월 출시, 정기 업데이트, 2027년 두 번째 앱",
    kpi_alt="공휴일 151개 나라, 기기 4종, 언어 3개, 종단간 암호화 공유, 날봄 커밋 745개",
    quote="> **날마다 봄, 나를 돌아봄. 거꾸로 읽으면 봄날.**  \n> 챙겨야 할 날을 날마다 보고, 하루 한 줄로 나를 돌아보는 달력이에요.",
    nalbom_intro="날봄은 챙겨야 할 날, 캘린더, 하루 메모, 직장인 도구를 한 앱에 담고 홈 화면과 잠금화면에 보여 줍니다. 아이폰, 아이패드, 맥(Apple 실리콘), 안드로이드에서 쓸 수 있어요.",
    features_alt="날봄 기능: 달력, D-day와 메모, 일 도구, 위젯과 실시간 현황, 함께 공간, 꾸미기",
    built_summary="어떻게 만들었나",
    web_more="웹사이트 자세히", research_more="전체 결과", web_alt="junixion.com: 3개 언어, 날봄 소개, 앱에 맞춘 법적 문서, 비밀 초대 링크, 작고 조용하게, 바꿀 때마다 검사", research_alt="워킹 페이퍼: 한국 주식시장 상장폐지 위험의 생존분석. C-index 0.738, 기업 365개, 상장폐지 158건, 276개월", stack_alt="기술: 앱, 웹·서버, ML·통계", about_alt="연세대학교 경제학 × 정보통계학, 2027년 2월 졸업 예정. 주닉션 대표. 앱 의견, 연구, 직무, 대학원 이야기 환영",
    built="""| 영역 | 한 일 |
|---|---|
| **기본은 기기 안** | 모든 기록은 휴대폰 안 SQLite에 저장해요(데이터 구조 변경 54번). 기본 기능은 계정 없이 다 돼요. 광고·분석 도구·AI 호출이 없어요. |
| **서버는 꼭 필요한 곳만** | 서울 리전의 작은 Supabase 프로젝트를 공휴일 표 업데이트, 함께 공간, D-day 웹 링크에만 써요. 행 단위 보안(RLS), 익명 로그인, Edge Function 4개, 남용 제한, 7일 뒤 지우기. |
| **암호화** | 함께 보는 기록과 사진은 올리기 전에 기기에서 OS 기본 AES-GCM으로 암호화해요. 서버에는 암호문만 남아요. 공간 열쇠는 세대별 열쇠 묶음으로 교체해요. |
| **iCloud 동기화** | 사용자 본인 CloudKit 개인 DB에서 `CKSyncEngine`으로 맞추는 Swift 모듈. 사진·음성 메모는 Wi-Fi에서만 맞춰요. |
| **네이티브 코드** | Swift·Kotlin으로 만든 모듈과 확장 10개: 위젯, 공유 확장, 실시간 현황, 안드로이드 실시간 알림, CloudKit 동기화, OS 암호화, 장소 찾기, 근무표 사진 읽기. |
| **품질** | 빌드마다 테스트 스크립트 70개와 타입 검사를 돌려요. 시뮬레이터에서 출시용(Release) 빌드로 한 번 더 확인하고, 올리기 전에 아카이브를 열어 점검해요. 충돌 보고(Sentry)는 사용자가 켤 때만, 개인 정보 칸은 지워서 받아요. |
| **출시** | iOS와 안드로이드를 같은 빌드 번호로 함께 내요. TestFlight·Google Play 출시 노트는 한국어·영어·일본어로 써요. |""",
    nalbom_tech="React Native 0.81 · Expo SDK 54 · TypeScript · SQLite · Swift · Kotlin · CloudKit · Supabase · RevenueCat · Sentry",
    web_intro="회사 웹사이트입니다. 직접 만들고 운영해요. 비공개 저장소이고 GitHub와 GitLab에 함께 올려요.",
    web_list="""- **3개 언어**: 한국어·영어·일본어. 머리글에서 언어를 바꾸고, 일본어는 줄바꿈과 글꼴을 따로 맞췄어요.
- **날봄 소개**: 기능 소개, 실제 앱 화면(라이트·다크, 3개 언어), 요금표, 자주 묻는 질문.
- **앱에 맞춘 법적 문서**: 날봄 개인정보처리방침과 이용약관을 3개 언어로, 앱 빌드마다 함께 고쳐요. 사용자에게 불리한 내용은 파란 굵은 글씨로, 문장마다 줄을 바꿔요.
- **초대·D-day 링크**: `#` 뒤 비밀 열쇠는 브라우저 안에서만 써요. 분석 도구·입력 폼·리퍼러 없음, 검색 제외.
- **작고 조용하게**: 자체 DB 없음, 방문 통계 없음(속도 측정만), 라이트·다크 모드.
- **바꿀 때마다 검사**: GitLab CI가 타입 검사, 린트, 빌드, Lighthouse 기준 검사를 돌려요.
- **지금**: 검토 기간이에요. 법적 문서, 앱 링크, 프레스 이미지는 계속 공개돼요.""",
    web_tech="Next.js 16 · React 19 · Tailwind v4 · Vercel · GitLab CI",
    research="""**한국 주식시장 상장폐지 위험의 생존분석**
Cox 비례위험 모형과 가속실패시간(AFT) 모형 — KOSPI/KOSDAQ 패널 데이터(2000–2023)

📄 [SSRN 워킹 페이퍼](https://papers.ssrn.com/abstract=6656258) · 2026년 4월 제출

> *정적 점수 모형(Altman Z-score, 로지스틱 회귀)은 실패를 예·아니오로만 보고 중도절단 관측을 버립니다. 이 논문은 대신 사건사 분석 방법을 씁니다.*

- KRX 생존 데이터셋 구축: 기업 365개, 상장폐지 158건, 276개월 관측(DART + FinanceDataReader)
- 카플란-마이어, Cox PH, 와이블·로그정규·로그로지스틱 AFT 모형 비교
- 시장 구분별 분산 차이를 담는 이분산 AFT 확장

| 결과 | 값 |
|---|---|
| 판별력 | **C-index = 0.738**, Shumway(2001) 미국 기준(C ≈ 0.74)과 비슷 |
| 가장 강한 예측 변수 | 12개월 모멘텀: HR = 0.496, p = 0.001 |
| 변동성 | 가격 변동성: HR = 1.827, p = 0.004 |
| 가장 좋은 모형 | 보조 척도를 둔 와이블 AFT: AIC = 1620.6, ΔAIC = 318.1 (p < 0.001) |
| 시장 차이 | KOSDAQ 대 KOSPI 로그순위 χ² = 10.57, p = 0.001 |

`생존분석` `Cox PH` `AFT` `KRX` `KOSPI` `KOSDAQ` `DART` `실증 연구`

**다음**: 시간에 따라 변하는 기저위험과 국면을 반영한 연속시간 위험 모형.""",
    projects_more="""**[생존분석 — KRX](https://github.com/jjuunnii98/survival-analysis-finance)**
위 SSRN 논문의 코드. KRX 365개 기업, 2000–2023, 사건 비율 43.3%. 논문의 모든 표와 그림을 다시 만들어요.
<sub>Python · lifelines · pandas</sub>

**JunixionLM** *(비공개 · 개인 연구)*
사전학습 가중치 없이 PyTorch로 처음부터 짠 디코더 Transformer: RMSNorm, RoPE, GQA, KV 캐시, SwiGLU. 크기 세 가지(약 1,400만·1억 6,200만·4억 8,900만). 1억 6,200만 모델을 8억 1,700만 토큰(wikitext-103, 한국어·영어 위키백과)으로 50,000 스텝까지 학습, 평균 손실 1.6946(Kaggle T4 ×2).
<sub>PyTorch · Python · Hugging Face</sub>

**[암호화폐 하락 생존분석 데모](https://github.com/jjuunnii98/crypto-risk-scoring-demo)** <sub>[live api ↗](https://crypto-risk-scoring-demo.onrender.com/docs)</sub>
실시간 Binance 데이터로 24시간 안 3% 넘는 하락을 예측하는 Cox PH 모형, C-index 0.862. 특성 16개, 테스트 40개 통과.
<sub>Python · FastAPI · lifelines</sub>

**[엔드투엔드 ML 분석 시스템](https://github.com/jjuunnii98/end-to-end-ml-analytics-system)** <sub>[live api ↗](https://ml-churn-api-2z9m.onrender.com/docs)</sub>
통신사 고객 이탈 예측을 실제 서비스처럼. 랜덤 포레스트(ROC-AUC 0.83), 데이터 검증부터 Docker FastAPI까지.
<sub>Python · scikit-learn · Docker</sub>

**[대학원 ML 포트폴리오](https://github.com/jjuunnii98/grad-portfolio-ml)** <sub>[live api ↗](https://survival-api.onrender.com/docs)</sub>
METABRIC 유방암 생존분석(환자 1,353명). 벌점 Cox PH, 검증 C-index 0.638, FastAPI 서비스로 배포.
<sub>Python · lifelines · FastAPI</sub>

**[SQL 분석 포트폴리오](https://github.com/jjuunnii98/sql-analytics-portfolio)**
PostgreSQL 16으로 자산 9개 × 5년(13,489행)을 분석한 18개 쿼리. 윈도 함수부터 샤프 비율, 최대 낙폭, RSI, VWAP까지.
<sub>PostgreSQL · SQL</sub>

**[Python 분석 실습](https://github.com/jjuunnii98/python-analysis-lab)**
세 분야를 노트북 4개씩(EDA → 특성 → 모형 → 인사이트): 리테일 세분화·이탈, 시계열 지표·백테스트, XGBoost·SHAP 헬스케어 위험 분류.
<sub>Python · Jupyter</sub>

**[Python 스네이크 게임](https://github.com/jjuunnii98/python-snake-game)**
난이도 세 가지, 점수에 따라 빨라지는 속도, 최고 점수 저장, PyInstaller 실행 파일.
<sub>Python · Pygame</sub>""",
    projects_summary="자세히",
    stack="""| 영역 | 도구 |
|---|---|
| **앱** | React Native · Expo · TypeScript · Swift · Kotlin · SQLite · CloudKit |
| **웹·서버** | Next.js · Tailwind CSS · Supabase · PostgreSQL · Deno · Vercel · GitLab CI |
| **ML·통계** | Python · PyTorch · scikit-learn · pandas · R · SAS · FastAPI · Docker |""",
    activity_alt="최근 26주 GitHub 활동",
    about="""**연세대학교** — 경제학 × 정보통계학 · 2027년 2월 졸업 예정
학부 연구원 — 생존분석·헬스케어 위험 모델링
주닉션(JUNIXION) 대표 — 응용 소프트웨어, 2026년 8월 개업""",
    certs="""<details>
<summary><b>자격증</b></summary>

<br>

**취득**
- ADsP · SQLD · CDS 빅데이터 전문가 과정
- 2024 제주 스마트관광 빅데이터 해커톤 우수상 — 팀장

**준비 중**
- 투자자산운용사
- 빅데이터분석기사 · 정보처리기사

**계획**
- 리눅스마스터 1급 · 정보보안기사
- 금융투자분석사

</details>""",
    connect="""| 분야 | 이런 이야기 환영해요 |
|---|---|
| 앱 | 날봄 의견, 버그 제보, 번역 도움 |
| 연구 | 생존분석 · LLM / NLP · 통계 모델링 |
| 직무 | 앱 엔지니어 · ML 연구원 · AI 엔지니어 · 퀀트 엔지니어 |
| 학업 | 금융공학 / AI 대학원 (2027년 입학) |""",
    footer_alt="매일 손이 가는 소프트웨어를, 끝까지 책임지고 만듭니다. 주닉션, 서울, contact@junixion.com",
)

C["en"]['built'] = "| Area | What I did |\n|---|---|\n| **On-device first** | All records live in SQLite on the phone (54 schema migrations). No account is needed for any basic feature. No ads, no analytics, no AI calls. |\n| **Server only where needed** | A small Supabase project (Seoul) for remote holiday tables, shared spaces and D-day web links: Row Level Security, anonymous sign-in, 4 Edge Functions, abuse limits, 7-day soft delete. |\n| **Encryption** | Shared records and photos are encrypted on the device with the OS's own AES-GCM before upload, so the server only stores ciphertext. Space keys rotate through an epoch key ring. |\n| **iCloud sync** | Native Swift module on `CKSyncEngine` in the user's private CloudKit database. Photos and voice notes sync on Wi-Fi only. |\n| **Native code** | 10 native modules and extensions in Swift and Kotlin: widgets, share extension, Live Activities, Android live notifications, CloudKit sync, OS crypto, place search, roster photo reading. |\n| **Quality** | 70 test scripts plus typecheck before every build. Each build is checked as a Release build on a simulator, then the archive is inspected before upload. Opt-in crash reports (Sentry) with personal fields scrubbed. |\n| **Release** | iOS and Android ship in step: the same build number on TestFlight and Google Play, with release notes in Korean, English and Japanese. |"
C["en"]['web_list'] = "- **Three languages**: Korean, English and Japanese, with a language menu in the header and Japanese line-breaking and fonts.\n- **Nalbom pages**: introduction, real app screenshots (light and dark, three languages), pricing table and FAQ.\n- **Legal pages written to match the app**: Nalbom's privacy policy and terms in three languages, updated with each app build. Facts that are unfavorable to users are shown in bold blue, one sentence per line.\n- **Invite and D-day links** for Nalbom: the secret key after `#` is only used inside the browser. No analytics, no forms, no referrer, not indexed.\n- **Small and quiet**: no database of its own, no visit analytics (Speed Insights only), light and dark modes.\n- **Checked on every change**: GitLab CI runs typecheck, lint, build and a Lighthouse gate.\n- **Now**: in a review period. The legal pages, app links and press images stay public."
C["en"]['research'] = '**Survival Analysis of Corporate Delisting Risk in the Korean Stock Market**  \nCox Proportional Hazards and Accelerated Failure Time Models — KOSPI/KOSDAQ Panel Data (2000–2023)\n\n📄 [SSRN Working Paper](https://papers.ssrn.com/abstract=6656258) · Submitted April 2026\n\n> *Static scoring models (Altman Z-score, logistic regression) treat failure as a yes-or-no outcome and drop censored observations. This paper uses event-history methods instead.*\n\n- Builds a KRX survival dataset: 365 firms, 158 delisting events, a 276-month window (DART + FinanceDataReader)\n- Compares Kaplan-Meier, Cox PH and Weibull / Log-Normal / Log-Logistic AFT models\n- Adds a heteroscedastic AFT extension that captures the variance gap between market segments\n\n| Finding | Result |\n|---|---|\n| Model discrimination | **C-index = 0.738**, close to the Shumway (2001) US benchmark (C ≈ 0.74) |\n| Strongest predictor | 12-month momentum: HR = 0.496, p = 0.001 |\n| Volatility | Price volatility: HR = 1.827, p = 0.004 |\n| Best specification | Weibull AFT with ancillary scale: AIC = 1620.6, ΔAIC = 318.1 (p < 0.001) |\n| Market difference | KOSDAQ vs. KOSPI log-rank χ² = 10.57, p = 0.001 |\n\n`survival analysis` `Cox PH` `AFT` `KRX` `KOSPI` `KOSDAQ` `DART` `empirical research`\n\n**Next**: continuous-time hazard models with time-varying baselines and regime conditioning.'
C["en"]['projects_more'] = '**[Survival Analysis — KRX](https://github.com/jjuunnii98/survival-analysis-finance)**  \nCode for the SSRN paper above. 365 KRX firms, 2000–2023, 43.3% event rate. Kaplan-Meier, Cox PH (C-index 0.738) and AFT models with a heteroscedastic extension. Reproduces every table and figure in the paper.  \n<sub>Python · lifelines · pandas</sub>\n\n**JunixionLM** *(private · personal research)*  \nA decoder-only Transformer written from scratch in PyTorch, with no pre-trained weights: RMSNorm, RoPE, Grouped Query Attention, KV cache and a SwiGLU FFN. Three sizes (about 14M, 162M and 489M). The 162M model was trained on 817M tokens (wikitext-103 and Korean/English Wikipedia) to step 50,000, avg loss 1.6946, on Kaggle T4 ×2.  \n<sub>PyTorch · Python · Hugging Face</sub>\n\n**[Crypto Drawdown Survival Demo](https://github.com/jjuunnii98/crypto-risk-scoring-demo)** <sub>[live api ↗](https://crypto-risk-scoring-demo.onrender.com/docs)</sub>  \nA Cox PH model for 24-hour drawdowns (> 3%) on live Binance data, C-index 0.862. 16 features (RSI, Bollinger, MACD, VWAP gap, ATR, Garman-Klass, Sortino, rolling MDD, funding-rate z-score). 40 passing tests.  \n<sub>Python · FastAPI · lifelines</sub>\n\n**[End-to-End ML Analytics System](https://github.com/jjuunnii98/end-to-end-ml-analytics-system)** <sub>[live api ↗](https://ml-churn-api-2z9m.onrender.com/docs)</sub>  \nTelco churn prediction as a production ML system. Random Forest (ROC-AUC 0.83) with data validation, feature engineering, artifact-based inference and a Dockerized FastAPI.  \n<sub>Python · scikit-learn · Docker</sub>\n\n**[Graduate ML Portfolio](https://github.com/jjuunnii98/grad-portfolio-ml)** <sub>[live api ↗](https://survival-api.onrender.com/docs)</sub>  \nBreast cancer survival analysis on METABRIC (1,353 patients). Penalized Cox PH, validation C-index 0.638, deployed as a FastAPI service.  \n<sub>Python · lifelines · FastAPI</sub>\n\n**[SQL Analytics Portfolio](https://github.com/jjuunnii98/sql-analytics-portfolio)**  \nPostgreSQL 16 on 9 assets × 5 years (13,489 rows): 18 analyses in pure SQL, from window functions to Sharpe ratio, max drawdown, RSI and VWAP. yfinance → CSV → PostgreSQL → Makefile → Python tests.  \n<sub>PostgreSQL · SQL</sub>\n\n**[Python Analysis Lab](https://github.com/jjuunnii98/python-analysis-lab)**  \nThree domains, each in four notebooks (EDA → features → model → insights): retail segmentation and churn, time-series indicators and backtests, and healthcare risk classification with XGBoost and SHAP.  \n<sub>Python · Jupyter</sub>\n\n**[Python Snake Game](https://github.com/jjuunnii98/python-snake-game)**  \nPygame snake with three difficulty modes, speed that grows with the score, saved high scores and a PyInstaller build.  \n<sub>Python · Pygame</sub>'
C["en"]['certs'] = '<details>\n<summary><b>Certifications</b></summary>\n\n<br>\n\n**Completed**\n- ADsP · SQLD · CDS 빅데이터 전문가 과정\n- 2024 제주 스마트관광 빅데이터 해커톤 우수상 — Team Leader\n\n**In progress**\n- 투자자산운용사 (Investment Asset Manager)\n- 빅데이터분석기사 (Big Data Analytics Engineer) · 정보처리기사 (Engineer Information Processing)\n\n**Planned**\n- 리눅스마스터 1급 (Linux Master Level 1) · 정보보안기사 (Engineer Information Security)\n- 금융투자분석사 (Financial Investment Analyst)\n\n</details>'

def build(lang):
    c = C[lang]
    S = lambda key, alt: pic(f"section-{key}", alt, lang)
    return f"""{c['toggle']}

<a href="https://junixion.com">{pic('header', c['header_alt'], lang)}</a>

<div align="center">

{social_bars()}

{c['links']}

</div>

<br>

{S('now', '01 Now')}

<a href="https://junixion.com">{pic('now', c['now_alt'], lang)}</a>

<br>

{pic('roadmap', c['roadmap_alt'], lang)}

<br>

{pic('kpi', c['kpi_alt'], lang)}

<br>

{S('nalbom', '02 Nalbom')}

{pic('lead-nalbom', c['nalbom_intro'], lang)}

{pic('features', c['features_alt'], lang)}

<details>
<summary><b>{c['built_summary']}</b></summary>

<br>

{c['built']}

</details>

<br>

{S('web', '03 junixion.com')}

{pic('lead-web', c['web_intro'], lang)}

{pic('web', c['web_alt'], lang)}

<details>
<summary><b>{c['web_more']}</b></summary>

<br>

{c['web_list']}

</details>

<br>

{S('research', '04 Research')}

<a href="https://papers.ssrn.com/abstract=6656258">{pic('research', c['research_alt'], lang)}</a>

<details>
<summary><b>{c['research_more']}</b></summary>

<br>

{c['research']}

</details>

<br>

{S('projects', '05 Projects')}

{project_grid(lang)}

<details>
<summary><b>{c['projects_summary']}</b></summary>

<br>

{c['projects_more']}

</details>

<br>

{S('stack', '06 Stack')}

{pic('stack', c['stack_alt'], lang)}

{pic('activity', c['activity_alt'], lang)}

<br>

{S('about', '07 About')}

{pic('about', c['about_alt'], lang)}

{c['certs']}

<br>

<a href="mailto:contact@junixion.com">{pic('footer', c['footer_alt'], lang)}</a>
"""


def build_assets():
    for m in T:
        social(m)
        for L in LANGS:
            for fn in (header, now, kpi, features, roadmap, footer):
                fn(L, m)
            for s in TX[L]["sections"]:
                section(L, m, *s)
            for p in TX[L]["projects"]:
                project(L, m, *p)
            grid(L, m, "web", WEB[L]); research(L, m); stack(L, m); about(L, m)
            lead(L, m, "nalbom"); lead(L, m, "web")
    build_mobile()


def build_readmes():
    for lang, fn in (("en", "README.md"), ("ko", "README.ko.md")):
        with open(os.path.join(REPO, fn), "w") as f:
            f.write(build(lang))


if __name__ == "__main__":
    build_assets()
    build_readmes()
    print("assets and READMEs written")
