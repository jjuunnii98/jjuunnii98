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

<sub>React Native 0.81 · Expo SDK 54 · TypeScript · SQLite · Swift · Kotlin · CloudKit · Supabase · RevenueCat · Sentry</sub>

<sub>[Instagram @nalbom.app](https://www.instagram.com/nalbom.app/) · [X @nalbomapp](https://x.com/nalbomapp) · [Facebook nalbomapp](https://www.facebook.com/nalbomapp)</sub>

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

<sub>Next.js 16 · React 19 · Tailwind v4 · Vercel · GitLab CI</sub>

<sub>[Instagram @junixion.official](https://www.instagram.com/junixion.official/) · [X @junixion](https://x.com/junixion) · [Facebook junixion.official](https://www.facebook.com/junixion.official)</sub>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/section-research-dark.svg" />
  <img src="./assets/section-research-light.svg" width="100%" alt="04 Research" />
</picture>

**Survival Analysis of Corporate Delisting Risk in the Korean Stock Market**  
Cox Proportional Hazards and Accelerated Failure Time Models — KOSPI/KOSDAQ Panel Data (2000–2023)

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
<sub>Python · lifelines · pandas</sub>

**JunixionLM** *(private · personal research)*  
A decoder-only Transformer written from scratch in PyTorch, with no pre-trained weights: RMSNorm, RoPE, Grouped Query Attention, KV cache and a SwiGLU FFN. Three sizes (about 14M, 162M and 489M). The 162M model was trained on 817M tokens (wikitext-103 and Korean/English Wikipedia) to step 50,000, avg loss 1.6946, on Kaggle T4 ×2.  
<sub>PyTorch · Python · Hugging Face</sub>

**[Crypto Drawdown Survival Demo](https://github.com/jjuunnii98/crypto-risk-scoring-demo)** <sub>[live api ↗](https://crypto-risk-scoring-demo.onrender.com/docs)</sub>  
A Cox PH model for 24-hour drawdowns (> 3%) on live Binance data, C-index 0.862. 16 features (RSI, Bollinger, MACD, VWAP gap, ATR, Garman-Klass, Sortino, rolling MDD, funding-rate z-score). 40 passing tests.  
<sub>Python · FastAPI · lifelines</sub>

**[End-to-End ML Analytics System](https://github.com/jjuunnii98/end-to-end-ml-analytics-system)** <sub>[live api ↗](https://ml-churn-api-2z9m.onrender.com/docs)</sub>  
Telco churn prediction as a production ML system. Random Forest (ROC-AUC 0.83) with data validation, feature engineering, artifact-based inference and a Dockerized FastAPI.  
<sub>Python · scikit-learn · Docker</sub>

**[Graduate ML Portfolio](https://github.com/jjuunnii98/grad-portfolio-ml)** <sub>[live api ↗](https://survival-api.onrender.com/docs)</sub>  
Breast cancer survival analysis on METABRIC (1,353 patients). Penalized Cox PH, validation C-index 0.638, deployed as a FastAPI service.  
<sub>Python · lifelines · FastAPI</sub>

</details>

<details>
<summary><b>Data analysis & smaller projects</b></summary>

<br>

**[SQL Analytics Portfolio](https://github.com/jjuunnii98/sql-analytics-portfolio)**  
PostgreSQL 16 on 9 assets × 5 years (13,489 rows): 18 analyses in pure SQL, from window functions to Sharpe ratio, max drawdown, RSI and VWAP. yfinance → CSV → PostgreSQL → Makefile → Python tests.  
<sub>PostgreSQL · SQL</sub>

**[Python Analysis Lab](https://github.com/jjuunnii98/python-analysis-lab)**  
Three domains, each in four notebooks (EDA → features → model → insights): retail segmentation and churn, time-series indicators and backtests, and healthcare risk classification with XGBoost and SHAP.  
<sub>Python · Jupyter</sub>

**[Python Snake Game](https://github.com/jjuunnii98/python-snake-game)**  
Pygame snake with three difficulty modes, speed that grows with the score, saved high scores and a PyInstaller build.  
<sub>Python · Pygame</sub>

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/section-stack-dark.svg" />
  <img src="./assets/section-stack-light.svg" width="100%" alt="06 Stack" />
</picture>

| Area | Tools |
|---|---|
| **Apps** | React Native · Expo · TypeScript · Swift · Kotlin · SQLite · CloudKit |
| **Web & backend** | Next.js · Tailwind CSS · Supabase · PostgreSQL · Deno · Vercel · GitLab CI |
| **ML & statistics** | Python · PyTorch · scikit-learn · pandas · R · SAS · FastAPI · Docker |

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
