"""Draw the minimal activity card (light/dark, English/Korean) from GitHub contributions.

Run in GitHub Actions with GITHUB_TOKEN set. `--sample` draws from made-up data for a local preview.
Counts private work only if "Include private contributions on my profile" is on in GitHub settings.
"""
import json
import os
import random
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone

USER = "jjuunnii98"
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
WEEKS = 26

SANS = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', Arial, sans-serif"
MONO = "'JetBrains Mono', 'SF Mono', ui-monospace, Menlo, Consolas, monospace"
THEMES = {
    "dark": dict(card="#121828", card2="#0C111C", line="#263049", ink="#F5F7FB", sub="#CDD4E1", faint="#A3ADC0",
                 bar="#8DB6FF", violet="#C3A6FF", empty="#1E2532"),
    "light": dict(card="#FFFFFF", card2="#F5F8FE", line="#DFE5F0", ink="#0F172A", sub="#3F4A5C", faint="#667085",
                  bar="#2160D4", violet="#7C5CE0", empty="#EEF1F6"),
}
TEXT = {
    "en": dict(title="ACTIVITY · LAST 26 WEEKS", updated="updated", total="contributions this year",
               current="day streak now", best="day best streak", active="active days this year",
               months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]),
    "ko": dict(title="ACTIVITY · 최근 26주", updated="갱신", total="올해 기여",
               current="일 연속 (지금)", best="일 최장 연속", active="올해 활동한 날",
               months=[f"{i}월" for i in range(1, 13)]),
}


def fetch_days():
    token = os.environ["GITHUB_TOKEN"]
    query = """{ user(login: "%s") { contributionsCollection { contributionCalendar {
      weeks { contributionDays { date contributionCount } } } } } }""" % USER
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return sorted(((d["date"], d["contributionCount"]) for w in weeks for d in w["contributionDays"]))


def sample_days():
    rnd = random.Random(7)
    today = date.today()
    return [((today - timedelta(days=i)).isoformat(), rnd.choice([0, 0, 1, 3, 6, 12, 20]))
            for i in range(364, -1, -1)]


def stats(days):
    today = datetime.now(timezone.utc).date().isoformat()
    days = [d for d in days if d[0] <= today]
    year = today[:4]
    total = sum(n for d, n in days if d.startswith(year))
    active = sum(1 for d, n in days if d.startswith(year) and n > 0)
    best = run = 0
    for _, n in days:
        run = run + 1 if n > 0 else 0
        best = max(best, run)
    current = 0
    for d, n in reversed(days):
        if n > 0:
            current += 1
        elif d < today:  # today may still be empty
            break
    # weekly sums for the last WEEKS weeks (Monday-based)
    end = date.fromisoformat(today)
    start = end - timedelta(days=end.weekday()) - timedelta(weeks=WEEKS - 1)
    weeks = [0] * WEEKS
    for d, n in days:
        dd = date.fromisoformat(d)
        if dd >= start:
            weeks[min((dd - start).days // 7, WEEKS - 1)] += n
    return dict(total=total, active=active, best=best, current=current, weeks=weeks, start=start, today=today)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def draw(s, lang, mode):
    c, t = THEMES[mode], TEXT[lang]
    W, H = 1280, 300
    out = [f'<defs><linearGradient id="cardg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c["card"]}"/><stop offset="1" stop-color="{c["card2"]}"/></linearGradient>'
           f'<linearGradient id="barg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c["violet"]}"/><stop offset="1" stop-color="{c["bar"]}"/></linearGradient>'
           f'<linearGradient id="edge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["bar"]}" stop-opacity="0"/><stop offset="0.25" stop-color="{c["bar"]}" stop-opacity="0.9"/><stop offset="0.6" stop-color="{c["violet"]}" stop-opacity="0.8"/><stop offset="1" stop-color="{c["violet"]}" stop-opacity="0"/></linearGradient></defs>',
           f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="url(#cardg)" stroke="{c["line"]}"/>',
           f'<rect x="20" y="0.2" width="520" height="1.6" rx="0.8" fill="url(#edge)"/>',
           f'<text x="32" y="44" font-family="{MONO}" font-size="13.5" letter-spacing="2.5" fill="{c["faint"]}">{esc(t["title"])}</text>',
           f'<text x="{W-32}" y="44" text-anchor="end" font-family="{MONO}" font-size="13.5" fill="{c["faint"]}">{t["updated"]} {s["today"]}</text>']
    x0, x1, top, base = 32, W - 32, 72, 186
    slot = (x1 - x0) / WEEKS
    peak = max(s["weeks"]) or 1
    last_month = None
    for i, n in enumerate(s["weeks"]):
        x = x0 + i * slot
        h = max(3, (base - top) * n / peak)
        fill = "url(#barg)" if n else c["empty"]
        op = 0.35 + 0.65 * (n / peak) if n else 1
        out.append(f'<rect x="{x+3:.1f}" y="{base-h:.1f}" width="{slot-6:.1f}" height="{h:.1f}" rx="3" fill="{fill}" fill-opacity="{op:.2f}"/>')
        month = (s["start"] + timedelta(weeks=i)).month
        if month != last_month:
            out.append(f'<text x="{x+3:.1f}" y="{base+24}" font-family="{MONO}" font-size="13" fill="{c["faint"]}">{t["months"][month-1]}</text>')
            last_month = month
    out.append(f'<line x1="32" y1="{base+42}" x2="{W-32}" y2="{base+42}" stroke="{c["line"]}"/>')
    items = [(f'{s["total"]:,}' if isinstance(s["total"], int) else s["total"], t["total"]), (str(s["current"]), t["current"]),
             (str(s["best"]), t["best"]), (str(s["active"]), t["active"])]
    cw = (W - 64) / 4
    for i, (num, label) in enumerate(items):
        x = 32 + i * cw
        out.append(f'<text x="{x:.1f}" y="{base+82}" font-size="24" font-weight="600" letter-spacing="-0.6" fill="{c["ink"]}">{num}'
                   f'<tspan dx="10" font-family="{MONO}" font-size="13.5" font-weight="400" letter-spacing="0" fill="{c["faint"]}">{esc(label)}</tspan></text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'font-family="{SANS}">{"".join(out)}</svg>\n')
    name = "activity" + ("" if lang == "en" else "-ko") + f"-{mode}.svg"
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)


def draw_phone(s, lang, mode):
    """Narrow version shown under 600px wide."""
    c, t = THEMES[mode], TEXT[lang]
    W, H = 480, 352
    out = [f'<defs><linearGradient id="cardg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c["card"]}"/><stop offset="1" stop-color="{c["card2"]}"/></linearGradient>'
           f'<linearGradient id="barg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c["violet"]}"/><stop offset="1" stop-color="{c["bar"]}"/></linearGradient>'
           f'<linearGradient id="edge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["bar"]}" stop-opacity="0"/><stop offset="0.25" stop-color="{c["bar"]}" stop-opacity="0.9"/><stop offset="0.6" stop-color="{c["violet"]}" stop-opacity="0.8"/><stop offset="1" stop-color="{c["violet"]}" stop-opacity="0"/></linearGradient></defs>',
           f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="url(#cardg)" stroke="{c["line"]}"/>',
           f'<rect x="20" y="0.2" width="300" height="1.6" rx="0.8" fill="url(#edge)"/>',
           f'<text x="28" y="40" font-family="{MONO}" font-size="12.5" letter-spacing="2" fill="{c["faint"]}">{esc(t["title"])}</text>',
           f'<text x="28" y="62" font-family="{MONO}" font-size="12.5" fill="{c["faint"]}">{t["updated"]} {s["today"]}</text>']
    x0, x1, top, base = 28, W - 28, 84, 176
    slot = (x1 - x0) / WEEKS
    peak = max(s["weeks"]) or 1
    last_month = None
    for i, n in enumerate(s["weeks"]):
        x = x0 + i * slot
        h = max(3, (base - top) * n / peak)
        op = 0.35 + 0.65 * (n / peak) if n else 1
        out.append(f'<rect x="{x+1.5:.1f}" y="{base-h:.1f}" width="{slot-3:.1f}" height="{h:.1f}" rx="2.5" fill="{"url(#barg)" if n else c["empty"]}" fill-opacity="{op:.2f}"/>')
        month = (s["start"] + timedelta(weeks=i)).month
        if month != last_month:
            out.append(f'<text x="{x+1.5:.1f}" y="{base+22}" font-family="{MONO}" font-size="12" fill="{c["faint"]}">{t["months"][month-1]}</text>')
            last_month = month
    items = [(f'{s["total"]:,}' if isinstance(s["total"], int) else s["total"], t["total"]), (str(s["current"]), t["current"]),
             (str(s["best"]), t["best"]), (str(s["active"]), t["active"])]
    cw = (W - 56) / 2
    for i, (num, label) in enumerate(items):
        x = 28 + (i % 2) * cw; y = base + 44 + (i // 2) * 64
        out.append(f'<line x1="{x:.1f}" y1="{y}" x2="{x+cw-14:.1f}" y2="{y}" stroke="{c["line"]}"/>')
        out.append(f'<text x="{x:.1f}" y="{y+32}" font-size="24" font-weight="600" letter-spacing="-0.6" fill="{c["ink"]}">{num}</text>')
        out.append(f'<text x="{x:.1f}" y="{y+52}" font-family="{MONO}" font-size="12" fill="{c["faint"]}">{esc(label)}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'font-family="{SANS}">{"".join(out)}</svg>\n')
    name = "activity-m" + ("" if lang == "en" else "-ko") + f"-{mode}.svg"
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)


def main():
    if "--placeholder" in sys.argv:  # first commit, before the Action fills real numbers
        s = stats([])
        s.update(total="—", current="—", best="—", active="—")
    else:
        s = stats(sample_days() if "--sample" in sys.argv else fetch_days())
    for lang in TEXT:
        for mode in THEMES:
            draw(s, lang, mode)
            draw_phone(s, lang, mode)
    print("activity card:", s["total"], "contributions,", s["current"], "day streak")


if __name__ == "__main__":
    main()
