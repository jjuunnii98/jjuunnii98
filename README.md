<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1F4D,55:1E4FB8,100:5B9BFF&height=190&section=header&text=Junyeong%20Song&fontSize=46&fontColor=FFFFFF&fontAlignY=36&desc=Founder%20of%20JUNIXION%20%C2%B7%20App%20Developer%20%C2%B7%20Seoul&descSize=17&descAlignY=58" alt="Junyeong Song — Founder of JUNIXION" width="100%" />

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1100&color=5B9BFF&center=true&vCenter=true&random=false&width=680&lines=Building+Nalbom+%C2%B7+a+widget-first+calendar+app;iPhone+%C2%B7+iPad+%C2%B7+Mac+%C2%B7+Android+%C2%B7+Apple+Watch;On-device+first+%C2%B7+end-to-end+encrypted+sharing;Holidays+for+151+countries+%C2%B7+Korean+%C2%B7+English+%C2%B7+Japanese;Research%3A+survival+analysis+%C2%B7+Cox+PH+%C2%B7+AFT+%C2%B7+C-index+0.738)](https://junixion.com)

> **Software for every day, built and backed to last.**  
> I run JUNIXION, a one-person application software company in Seoul.  
> I design, build, ship and support every part myself: app, widgets, server, website and legal pages.

[![Nalbom](https://img.shields.io/badge/Nalbom-launching_Nov_2026-2160D4?style=flat-square)](#-nalbom-날봄)
[![TestFlight](https://img.shields.io/badge/TestFlight-build_50-0D96F6?style=flat-square&logo=apple&logoColor=white)](#-nalbom-날봄)
[![Google Play](https://img.shields.io/badge/Google_Play-closed_testing-34A853?style=flat-square&logo=googleplay&logoColor=white)](#-nalbom-날봄)
[![Streak](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjjuunnii98%2Fjjuunnii98%2Fmain%2Fstreak.json&style=flat-square)](https://github.com/jjuunnii98)
[![SSRN](https://img.shields.io/badge/SSRN-working_paper-1F4E79?style=flat-square)](https://papers.ssrn.com/abstract=6656258)

[![junixion.com](https://img.shields.io/badge/junixion.com-0B1F4D?style=flat-square&logo=vercel&logoColor=white)](https://junixion.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jun-yeong-song/)
[![GitLab](https://img.shields.io/badge/GitLab-FC6D26?style=flat-square&logo=gitlab&logoColor=white)](https://gitlab.com/jjuunnii98)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/JUNIXION)
[![Email](https://img.shields.io/badge/contact%40junixion.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:contact@junixion.com)

</div>

---

## 🧭 Now

<table>
<tr>
<td width="50%" valign="top">

### 📅 Nalbom (날봄)
**A calendar for seeing your days.**  
D-days, calendar, notes and work tools in one widget-first app.

`iOS` `iPadOS` `macOS` `Android` `watchOS Smart Stack`

**745 commits** · TestFlight build 50 · launching November 2026

</td>
<td width="50%" valign="top">

### 🌐 junixion.com
**The company website.**  
Company story, the Nalbom page, and Nalbom's privacy policy and terms in three languages.

`Next.js 16` `React 19` `Tailwind v4` `Vercel`

**343 commits** · Korean · English · Japanese

</td>
</tr>
</table>

```text
Product    →  Nalbom: final checks before the November launch (iOS, iPadOS, macOS, Android)
Website    →  junixion.com: review period, legal pages and app links stay public
Next       →  App #2 in research, after Nalbom is stable
Research   →  Survival analysis: extending the KRX delisting paper to continuous time
```

---

## 📅 Nalbom (날봄)

> **날마다 봄, 나를 돌아봄. 거꾸로 읽으면 봄날.**  
> *Seeing your days, looking back on yourself. Read backwards: bomnal, spring days.*

Nalbom is JUNIXION's first app. It puts the dates you care about, your calendar, daily notes and everyday work tools into one place, and shows them on the home screen and lock screen.

<table>
<tr>
<td width="33%" valign="top">

**🗓️ Calendar**
- Year, month, week and day views
- Public holidays for **151 countries**
- Lunar dates, per-country rules
- Google and iCloud calendars through the phone's own calendar
- Repeats, multiple alarms, quick add parsed on the device

</td>
<td width="33%" valign="top">

**⏳ D-days & notes**
- D-days, count-ups, anniversaries
- Trip D-days and share cards
- Daily notes with photos, voice, links and places
- One-line journal and mood
- Locked notes with Face ID

</td>
<td width="33%" valign="top">

**💼 Work tools**
- Annual leave under Korean labor law
- Clock-in, 52-hour week, breaks
- Shift-work roster calendar
- Work log → weekly report
- Long-weekend finder, payday countdown

</td>
</tr>
<tr>
<td valign="top">

**📱 Widgets & live**
- Home and lock-screen widgets
- Tap to check or clock in from the widget
- Live Activities and Apple Watch Smart Stack
- Galaxy Live Updates on Android

</td>
<td valign="top">

**👥 Together**
- Shared spaces for couples, family, friends and trips
- **End-to-end encrypted**, keys stay in the invite link
- Key rotation when a member leaves
- iCloud sync between your own Apple devices

</td>
<td valign="top">

**🎨 Look & feel**
- 13 color themes, 19 accent colors
- Matching app icons on iOS
- Text size and full dark mode
- Korean, English and Japanese
- Free, with a one-time lifetime pass

</td>
</tr>
</table>

<details>
<summary><b>How it is built</b> (click to open)</summary>

<br>

| Area | What I did |
|---|---|
| **On-device first** | All records live in SQLite on the phone (54 schema migrations). No account is needed for any basic feature. No ads, no analytics, no AI calls. |
| **Server only where needed** | A small Supabase project (Seoul) for remote holiday tables, shared spaces and D-day web links: Row Level Security, anonymous sign-in, 4 Edge Functions, abuse limits, 7-day soft delete. |
| **Encryption** | Shared records and photos are encrypted on the device with the OS's own AES-GCM before upload, so the server only stores ciphertext. Space keys rotate through an epoch key ring. |
| **iCloud sync** | Native Swift module on `CKSyncEngine` in the user's private CloudKit database. Photos and voice notes sync on Wi-Fi only. |
| **Native code** | 10 native modules and extensions in Swift and Kotlin: widgets, share extension, Live Activities, Android live notifications, CloudKit sync, OS crypto, place search, roster photo reading. |
| **Quality** | 70 test scripts plus typecheck before every build. Each build is checked as a Release build on a simulator, then the archive is inspected before upload. Opt-in crash reports (Sentry) with personal fields scrubbed. |
| **Release** | iOS and Android ship in step: the same build number on TestFlight and Google Play, with release notes in Korean, English and Japanese. |

</details>

![React Native](https://img.shields.io/badge/React_Native_0.81-61DAFB?style=flat-square&logo=react&logoColor=black)
![Expo SDK 54](https://img.shields.io/badge/Expo_SDK_54-000020?style=flat-square&logo=expo&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Swift](https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white)
![CloudKit](https://img.shields.io/badge/CloudKit-3693F3?style=flat-square&logo=icloud&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![RevenueCat](https://img.shields.io/badge/RevenueCat-F25A5A?style=flat-square)
![Sentry](https://img.shields.io/badge/Sentry-362D59?style=flat-square&logo=sentry&logoColor=white)

[![Instagram](https://img.shields.io/badge/@nalbom.app-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/nalbom.app/)
[![X](https://img.shields.io/badge/@nalbomapp-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/nalbomapp)
[![Facebook](https://img.shields.io/badge/nalbomapp-0866FF?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/nalbomapp)

---

## 🌐 junixion.com

The company website, built and run by me. Private repository, mirrored on GitHub and GitLab.

- **Three languages**: Korean, English and Japanese, with a language menu in the header and Japanese line-breaking and fonts.
- **Nalbom pages**: introduction, real app screenshots (light and dark, three languages), pricing table and FAQ.
- **Legal pages written to match the app**: Nalbom's privacy policy and terms in three languages, updated with each app build. Facts that are unfavorable to users are shown in bold blue, one sentence per line.
- **Invite and D-day links** for Nalbom: the secret key after `#` is only used inside the browser. No analytics, no forms, no referrer, not indexed.
- **Small and quiet**: no database of its own, no visit analytics (Speed Insights only), light and dark modes.
- **Checked on every change**: GitLab CI runs typecheck, lint, build and a Lighthouse gate.
- **Now**: in a review period. The legal pages, app links and press images stay public.

![Next.js](https://img.shields.io/badge/Next.js_16-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React_19-61DAFB?style=flat-square&logo=react&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_v4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=flat-square&logo=gitlab&logoColor=white)

[![Instagram](https://img.shields.io/badge/@junixion.official-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/junixion.official/)
[![X](https://img.shields.io/badge/@junixion-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/junixion)
[![Facebook](https://img.shields.io/badge/junixion.official-0866FF?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/junixion.official)

---

## 📊 GitHub

<div align="center">

![GitHub Stats](./github-metrics.svg)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./github-snake.svg" />
  <img alt="GitHub contribution snake" src="./github-snake-dark.svg" />
</picture>

</div>

---

## 🔬 Research

### Survival Analysis of Corporate Delisting Risk in the Korean Stock Market
**Cox Proportional Hazards and Accelerated Failure Time Models — KOSPI/KOSDAQ Panel Data (2000–2023)**

📄 [SSRN Working Paper](https://papers.ssrn.com/abstract=6656258) · Submitted April 2026

> *Static scoring models (Altman Z-score, logistic regression) treat failure as a yes-or-no outcome and drop censored observations. This paper uses event-history methods instead.*

- Builds a KRX survival dataset: 365 firms, 158 delisting events, a 276-month window (DART + FinanceDataReader)
- Compares Kaplan-Meier, Cox PH and Weibull / Log-Normal / Log-Logistic AFT models
- Adds a heteroscedastic AFT extension that captures the variance gap between market segments

| Finding | Result |
|---|---|
| Model discrimination | **C-index = 0.738**, close to the Shumway (2001) US benchmark (C ≈ 0.74) |
| Strongest predictor | 12-month momentum: HR = 0.496, p = 0.001 |
| Volatility | Price volatility: HR = 1.827, p = 0.004 |
| Best specification | Weibull AFT with ancillary scale: AIC = 1620.6, ΔAIC = 318.1 (p < 0.001) |
| Market difference | KOSDAQ vs. KOSPI log-rank χ² = 10.57, p = 0.001 |

`survival analysis` `Cox PH` `AFT` `KRX` `KOSPI` `KOSDAQ` `DART` `empirical research`

**Next**: continuous-time hazard models with time-varying baselines and regime conditioning.

---

## 🧪 Projects

<details open>
<summary><b>Machine learning & statistics</b></summary>

<br>

**[Survival Analysis — KRX](https://github.com/jjuunnii98/survival-analysis-finance)**  
Code for the SSRN paper above. 365 KRX firms, 2000–2023, 43.3% event rate. Kaplan-Meier, Cox PH (C-index 0.738) and AFT models with a heteroscedastic extension. Reproduces every table and figure in the paper.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![lifelines](https://img.shields.io/badge/lifelines-FF6B6B?style=flat-square)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)

**JunixionLM** *(private · personal research)*  
A decoder-only Transformer written from scratch in PyTorch, with no pre-trained weights: RMSNorm, RoPE, Grouped Query Attention, KV cache and a SwiGLU FFN. Three sizes (about 14M, 162M and 489M). The 162M model was trained on 817M tokens (wikitext-103 and Korean/English Wikipedia) to step 50,000, avg loss 1.6946, on Kaggle T4 ×2.  
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

**[Crypto Drawdown Survival Demo](https://github.com/jjuunnii98/crypto-risk-scoring-demo)** [![Live API](https://img.shields.io/badge/Live_API-online-brightgreen?style=flat-square&logo=render&logoColor=white)](https://crypto-risk-scoring-demo.onrender.com/docs)  
A Cox PH model for 24-hour drawdowns (> 3%) on live Binance data, C-index 0.862. 16 features (RSI, Bollinger, MACD, VWAP gap, ATR, Garman-Klass, Sortino, rolling MDD, funding-rate z-score). 40 passing tests.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![lifelines](https://img.shields.io/badge/lifelines-FF6B6B?style=flat-square)

**[End-to-End ML Analytics System](https://github.com/jjuunnii98/end-to-end-ml-analytics-system)** [![Live API](https://img.shields.io/badge/Live_API-online-brightgreen?style=flat-square&logo=render&logoColor=white)](https://ml-churn-api-2z9m.onrender.com/docs)  
Telco churn prediction as a production ML system. Random Forest (ROC-AUC 0.83) with data validation, feature engineering, artifact-based inference and a Dockerized FastAPI.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

**[Graduate ML Portfolio](https://github.com/jjuunnii98/grad-portfolio-ml)** [![Live API](https://img.shields.io/badge/Live_API-online-brightgreen?style=flat-square&logo=render&logoColor=white)](https://survival-api.onrender.com/docs)  
Breast cancer survival analysis on METABRIC (1,353 patients). Penalized Cox PH, validation C-index 0.638, deployed as a FastAPI service.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![lifelines](https://img.shields.io/badge/lifelines-FF6B6B?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)

</details>

<details>
<summary><b>Data analysis & smaller projects</b></summary>

<br>

**[SQL Analytics Portfolio](https://github.com/jjuunnii98/sql-analytics-portfolio)**  
PostgreSQL 16 on 9 assets × 5 years (13,489 rows): 18 analyses in pure SQL, from window functions to Sharpe ratio, max drawdown, RSI and VWAP. yfinance → CSV → PostgreSQL → Makefile → Python tests.  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

**[Python Analysis Lab](https://github.com/jjuunnii98/python-analysis-lab)**  
Three domains, each in four notebooks (EDA → features → model → insights): retail segmentation and churn, time-series indicators and backtests, and healthcare risk classification with XGBoost and SHAP.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

**[Python Snake Game](https://github.com/jjuunnii98/python-snake-game)**  
Pygame snake with three difficulty modes, speed that grows with the score, saved high scores and a PyInstaller build.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-000000?style=flat-square&logo=python&logoColor=white)

</details>

---

## 🛠️ Stack

<div align="center">

**Apps**

![React Native](https://img.shields.io/badge/React_Native-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Expo](https://img.shields.io/badge/Expo-000020?style=for-the-badge&logo=expo&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Swift](https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**Web & backend**

![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Deno](https://img.shields.io/badge/Deno-000000?style=for-the-badge&logo=deno&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)

**ML & statistics**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![SAS](https://img.shields.io/badge/SAS-003399?style=for-the-badge&logo=sas&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</div>

---

## 🎓 Background

**Yonsei University** — Economics × Information Statistics · Expected August 2026  
Undergraduate Research Assistant — Survival Analysis & Healthcare Risk Modeling  
Founder — JUNIXION (application software, opened August 2026)

<details>
<summary><b>Certifications</b></summary>

<br>

**Completed**
- ADsP · SQLD · CDS 빅데이터 전문가 과정
- 2024 제주 스마트관광 빅데이터 해커톤 우수상 — Team Leader

**In progress**
- 투자자산운용사 (Investment Asset Manager)
- 빅데이터분석기사 (Big Data Analytics Engineer) · 정보처리기사 (Engineer Information Processing)

**Planned**
- 리눅스마스터 1급 (Linux Master Level 1) · 정보보안기사 (Engineer Information Security)
- 금융투자분석사 (Financial Investment Analyst)

</details>

---

## 🤝 Connect

| Area | Open to |
|---|---|
| Apps | Nalbom feedback, bug reports and localization help |
| Research | Survival analysis · LLM / NLP · statistical modeling |
| Roles | App engineer · ML researcher · AI engineer · Quant engineer |
| Academia | Financial Engineering / AI graduate programs (2027 entry) |

<div align="center">

[![junixion.com](https://img.shields.io/badge/junixion.com-0B1F4D?style=for-the-badge&logo=vercel&logoColor=white)](https://junixion.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jun-yeong-song/)
[![Email](https://img.shields.io/badge/contact%40junixion.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:contact@junixion.com)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:5B9BFF,45:1E4FB8,100:0B1F4D&height=110&section=footer" alt="" width="100%" />

</div>
