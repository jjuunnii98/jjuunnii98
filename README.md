<div align="center">

<a href="https://junixion.com">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg" />
  <img src="./assets/header-light.svg" width="100%" alt="Junyeong Song — Founder of JUNIXION, app developer in Seoul" />
</picture>
</a>

<br>

[![junixion.com](https://img.shields.io/badge/junixion.com-0B1F4D?style=flat-square&logo=vercel&logoColor=white)](https://junixion.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0B1F4D?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jun-yeong-song/) [![GitLab](https://img.shields.io/badge/GitLab-0B1F4D?style=flat-square&logo=gitlab&logoColor=white)](https://gitlab.com/jjuunnii98) [![Hugging Face](https://img.shields.io/badge/Hugging_Face-0B1F4D?style=flat-square&logo=huggingface&logoColor=white)](https://huggingface.co/JUNIXION) [![SSRN paper](https://img.shields.io/badge/SSRN_paper-0B1F4D?style=flat-square&logo=ssrn&logoColor=white)](https://papers.ssrn.com/abstract=6656258) [![contact@junixion.com](https://img.shields.io/badge/contact@junixion.com-0B1F4D?style=flat-square&logo=gmail&logoColor=white)](mailto:contact@junixion.com) [![Streak](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjjuunnii98%2Fjjuunnii98%2Fmain%2Fstreak.json&style=flat-square&color=0B1F4D&labelColor=0B1F4D)](https://github.com/jjuunnii98)

</div>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/section-now-dark.svg" />
  <img src="./assets/section-now-light.svg" width="100%" alt="01 Now" />
</picture>

<br>

<a href="https://junixion.com">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/now-dark.svg" />
  <img src="./assets/now-light.svg" width="100%" alt="Nalbom, launching November 2026, and junixion.com, the company website" />
</picture>
</a>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/kpi-dark.svg" />
  <img src="./assets/kpi-light.svg" width="100%" alt="151 countries holidays, 4 platforms, 3 languages, end-to-end encrypted sharing, 745 commits" />
</picture>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/section-nalbom-dark.svg" />
  <img src="./assets/section-nalbom-light.svg" width="100%" alt="02 Nalbom" />
</picture>

> **날마다 봄, 나를 돌아봄. 거꾸로 읽으면 봄날.**  
> *Seeing your days, looking back on yourself. Read backwards: bomnal, spring days.*

Nalbom puts the dates you care about, your calendar, daily notes and everyday work tools into one app, and shows them on the home screen and lock screen. It runs on iPhone, iPad, Mac (Apple silicon) and Android.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/features-dark.svg" />
  <img src="./assets/features-light.svg" width="100%" alt="Nalbom features: calendar, D-days and notes, work tools, widgets and live activities, shared spaces, themes" />
</picture>

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

![React Native 0.81](https://img.shields.io/badge/React_Native_0.81-0B1F4D?style=flat-square&logo=react&logoColor=white) ![Expo SDK 54](https://img.shields.io/badge/Expo_SDK_54-0B1F4D?style=flat-square&logo=expo&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-0B1F4D?style=flat-square&logo=typescript&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-0B1F4D?style=flat-square&logo=sqlite&logoColor=white) ![Swift](https://img.shields.io/badge/Swift-0B1F4D?style=flat-square&logo=swift&logoColor=white) ![Kotlin](https://img.shields.io/badge/Kotlin-0B1F4D?style=flat-square&logo=kotlin&logoColor=white) ![CloudKit](https://img.shields.io/badge/CloudKit-0B1F4D?style=flat-square&logo=icloud&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-0B1F4D?style=flat-square&logo=supabase&logoColor=white) ![RevenueCat](https://img.shields.io/badge/RevenueCat-0B1F4D?style=flat-square) ![Sentry](https://img.shields.io/badge/Sentry-0B1F4D?style=flat-square&logo=sentry&logoColor=white)

[![@nalbom.app](https://img.shields.io/badge/@nalbom.app-2160D4?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/nalbom.app/) [![@nalbomapp](https://img.shields.io/badge/@nalbomapp-2160D4?style=flat-square&logo=x&logoColor=white)](https://x.com/nalbomapp) [![nalbomapp](https://img.shields.io/badge/nalbomapp-2160D4?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/nalbomapp)

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/section-web-dark.svg" />
  <img src="./assets/section-web-light.svg" width="100%" alt="03 junixion.com" />
</picture>

The company website, built and run by me. Private repository, mirrored on GitHub and GitLab.

- **Three languages**: Korean, English and Japanese, with a language menu in the header and Japanese line-breaking and fonts.
- **Nalbom pages**: introduction, real app screenshots (light and dark, three languages), pricing table and FAQ.
- **Legal pages written to match the app**: Nalbom's privacy policy and terms in three languages, updated with each app build. Facts that are unfavorable to users are shown in bold blue, one sentence per line.
- **Invite and D-day links** for Nalbom: the secret key after `#` is only used inside the browser. No analytics, no forms, no referrer, not indexed.
- **Small and quiet**: no database of its own, no visit analytics (Speed Insights only), light and dark modes.
- **Checked on every change**: GitLab CI runs typecheck, lint, build and a Lighthouse gate.
- **Now**: in a review period. The legal pages, app links and press images stay public.

![Next.js 16](https://img.shields.io/badge/Next.js_16-0B1F4D?style=flat-square&logo=nextdotjs&logoColor=white) ![React 19](https://img.shields.io/badge/React_19-0B1F4D?style=flat-square&logo=react&logoColor=white) ![Tailwind v4](https://img.shields.io/badge/Tailwind_v4-0B1F4D?style=flat-square&logo=tailwindcss&logoColor=white) ![Vercel](https://img.shields.io/badge/Vercel-0B1F4D?style=flat-square&logo=vercel&logoColor=white) ![GitLab CI](https://img.shields.io/badge/GitLab_CI-0B1F4D?style=flat-square&logo=gitlab&logoColor=white)

[![@junixion.official](https://img.shields.io/badge/@junixion.official-0B1F4D?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/junixion.official/) [![@junixion](https://img.shields.io/badge/@junixion-0B1F4D?style=flat-square&logo=x&logoColor=white)](https://x.com/junixion) [![junixion.official](https://img.shields.io/badge/junixion.official-0B1F4D?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/junixion.official)

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/section-research-dark.svg" />
  <img src="./assets/section-research-light.svg" width="100%" alt="04 Research" />
</picture>

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

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/section-projects-dark.svg" />
  <img src="./assets/section-projects-light.svg" width="100%" alt="05 Projects" />
</picture>

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

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/section-stack-dark.svg" />
  <img src="./assets/section-stack-light.svg" width="100%" alt="06 Stack" />
</picture>

<div align="center">

![React Native](https://img.shields.io/badge/React_Native-0B1F4D?style=for-the-badge&logo=react&logoColor=white) ![Expo](https://img.shields.io/badge/Expo-0B1F4D?style=for-the-badge&logo=expo&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-0B1F4D?style=for-the-badge&logo=typescript&logoColor=white) ![Swift](https://img.shields.io/badge/Swift-0B1F4D?style=for-the-badge&logo=swift&logoColor=white) ![Kotlin](https://img.shields.io/badge/Kotlin-0B1F4D?style=for-the-badge&logo=kotlin&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-0B1F4D?style=for-the-badge&logo=sqlite&logoColor=white)

![Next.js](https://img.shields.io/badge/Next.js-0B1F4D?style=for-the-badge&logo=nextdotjs&logoColor=white) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-0B1F4D?style=for-the-badge&logo=tailwindcss&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-0B1F4D?style=for-the-badge&logo=supabase&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0B1F4D?style=for-the-badge&logo=postgresql&logoColor=white) ![Deno](https://img.shields.io/badge/Deno-0B1F4D?style=for-the-badge&logo=deno&logoColor=white) ![Vercel](https://img.shields.io/badge/Vercel-0B1F4D?style=for-the-badge&logo=vercel&logoColor=white) ![GitLab CI](https://img.shields.io/badge/GitLab_CI-0B1F4D?style=for-the-badge&logo=gitlab&logoColor=white)

![Python](https://img.shields.io/badge/Python-0B1F4D?style=for-the-badge&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-0B1F4D?style=for-the-badge&logo=pytorch&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-0B1F4D?style=for-the-badge&logo=scikitlearn&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-0B1F4D?style=for-the-badge&logo=pandas&logoColor=white) ![R](https://img.shields.io/badge/R-0B1F4D?style=for-the-badge&logo=r&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-0B1F4D?style=for-the-badge&logo=fastapi&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-0B1F4D?style=for-the-badge&logo=docker&logoColor=white)

</div>

<br>

<div align="center">

![GitHub Stats](./github-metrics.svg)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./github-snake.svg" />
  <img alt="GitHub contribution snake" src="./github-snake-dark.svg" />
</picture>

</div>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/section-about-dark.svg" />
  <img src="./assets/section-about-light.svg" width="100%" alt="07 About" />
</picture>

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

| Area | Open to |
|---|---|
| Apps | Nalbom feedback, bug reports and localization help |
| Research | Survival analysis · LLM / NLP · statistical modeling |
| Roles | App engineer · ML researcher · AI engineer · Quant engineer |
| Academia | Financial Engineering / AI graduate programs (2027 entry) |

<br>

<a href="mailto:contact@junixion.com">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/footer-dark.svg" />
  <img src="./assets/footer-light.svg" width="100%" alt="Software for every day, built and backed to last. JUNIXION, Seoul, contact@junixion.com" />
</picture>
</a>
