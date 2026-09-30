<div align="center">

# Junyeong Song

**Founder & AI Engineer, [JUNIXION](https://junixion.com)** · Risk Intelligence AI · Seoul

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1000&color=58A6FF&center=true&vCenter=true&random=false&width=620&lines=Risk+Intelligence+AI+for+Financial+Decisions;Building+SimSage+%C2%B7+AI+Mock+Trading+%26+Market+Intelligence;Survival+Analysis+%C2%B7+Cox+PH+%C2%B7+AFT+%C2%B7+C-index+0.738;React+Native+%C2%B7+Supabase+%C2%B7+Next.js+%C2%B7+FastAPI+%C2%B7+PyTorch)](https://junixion.com)

<br>

> Financial distress models have not fundamentally changed since Altman (1968).  
> Static scoring. No censoring. No time structure. Fifty years of the same assumption.  
> I'm building the next layer — survival-based, market-aware, production-ready.

<br>

[![SSRN](https://img.shields.io/badge/SSRN-Working_Paper_%C2%B7_C--index_0.738-1F4E79?style=flat-square)](https://papers.ssrn.com/abstract=6656258)
[![SimSage](https://img.shields.io/badge/SimSage-pre--launch-8B5CF6?style=flat-square)](https://junixion.com)
[![Backend](https://img.shields.io/badge/Backend-33_Edge_Functions_%C2%B7_53_migrations-3ECF8E?style=flat-square&logo=supabase&logoColor=white)](#currently-building)
[![Risk Engine](https://img.shields.io/badge/Risk_Engine-7_factors_%C2%B7_100%2B_collectors-FF4B4B?style=flat-square)](#currently-building)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-jun--yeong--song-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jun-yeong-song/)
[![JUNIXION](https://img.shields.io/badge/junixion.com-000000?style=flat-square&logo=vercel&logoColor=white)](https://junixion.com)
[![GitLab](https://img.shields.io/badge/GitLab-jjuunnii98-FC6D26?style=flat-square&logo=gitlab&logoColor=white)](https://gitlab.com/jjuunnii98)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-JUNIXION-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/JUNIXION)
[![Email](https://img.shields.io/badge/contact%40junixion.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:contact@junixion.com)

<br>

![GitHub Stats](./github-metrics.svg)

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./github-snake.svg" />
  <img alt="github contribution snake" src="./github-snake-dark.svg" />
</picture>

</div>

---

## JUNIXION

**[junixion.com](https://junixion.com)** — Risk Intelligence AI · FinTech

The research below is not an academic exercise. It is the proof of concept for a broader system.

Financial risk intelligence does not exist as a dedicated AI platform. Bloomberg gives you data. ChatGPT gives you text. Neither gives you a principled, real-time, censoring-aware risk score grounded in the actual statistical structure of financial failure.

That is what JUNIXION builds.

```
Research layer    →  Survival models, stochastic processes, quantitative risk theory
AI layer          →  JunixionLM — custom Transformer, domain SFT pipeline (DART + crypto + code)
Engineering layer →  Real-time inference, scalable pipelines, production deployment
Product layer     →  Domain-specialized Risk Intelligence AI for financial decision-making
```

The product stack runs across three private repositories, mirrored on GitHub and GitLab:

| Repository | Role | Stack |
|---|---|---|
| `junixion-app` | **SimSage**, the first consumer product: AI mock trading and global market intelligence | React Native 0.81 · Expo SDK 54 · TypeScript |
| `junixion-server` | Shared backend for the app and website: 53 migrations, 33 Edge Functions, all in production | Supabase (Postgres · Auth · RLS · pg_cron) · Deno |
| `junixion-web` | Monorepo with the public site ([junixion.com](https://junixion.com)) and the risk intelligence engine (`app.` / `api.junixion.com`) | Next.js 16 · Python · FastAPI · Streamlit |

Proprietary system architecture. IP filing in preparation.

---

## Currently Building

```
Research      →  Continuous-time default models (KRX paper extension)
AI Model      →  JunixionLM — 162M params, Phase 1 ✅, QLoRA SFT prep 🔄
Intelligence  →  Risk engine — 7-component composite score, 100+ collectors, FastAPI + Streamlit
Mobile        →  SimSage — server-authoritative mock trading, grounded AI analysis, pre-launch
Backend       →  Supabase — 53 migrations, 33 Edge Functions in production
Web           →  junixion.com — company site, SimSage waitlist, insights blog
```

**JunixionLM** *(private · Phase 1 ✅ · SFT prep 🔄)*  
Decoder-only Transformer from scratch in PyTorch — no pre-trained weights. Architecture: RMSNorm + RoPE + Grouped Query Attention + KV Cache + SwiGLU FFN. Phase 1b complete: 817M tokens (wikitext-103 + Korean/English Wikipedia), step 50,000, avg_loss = 1.6946 on Kaggle T4 ×2. Domain data pipeline ready for Qwen2.5-Coder-7B QLoRA SFT: DART filings + crypto/finance news + finance code (The Stack v2). Phase 6 target: FastAPI serving + Telegram integration → JUNIXION inference layer.  
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Transformer](https://img.shields.io/badge/Transformer-555555?style=flat-square)
![GQA](https://img.shields.io/badge/GQA-555555?style=flat-square)
![RoPE](https://img.shields.io/badge/RoPE-555555?style=flat-square)
![KV Cache](https://img.shields.io/badge/KV_Cache-555555?style=flat-square)
![QLoRA](https://img.shields.io/badge/QLoRA-8B5CF6?style=flat-square)
![SFT](https://img.shields.io/badge/SFT-8B5CF6?style=flat-square)

**SimSage — JUNIXION Mobile App** *(private · pre-launch 🔄)*  
AI mock trading and global market intelligence app built with React Native 0.81 and Expo SDK 54. Supports spot, leveraged futures and options trading. Orders fill against a synthetic order book, with partial fills, slippage, a pre-trade preview and pre-market/after-hours sessions for equities. Balances, positions and liquidations are computed on the server; the client only renders the state the server returns. One 6-factor risk model (volatility · liquidity · sentiment · event · systemic · derivatives) covers crypto, equities, FX and commodities, with CFTC COT positioning feeding the derivatives factor. Tapping a risk factor expands an explanation of it. The AI chat streams its answers, can read the user's mock positions, and grounds its market analysis in measured data passed to the server. Community features include public profiles, follows, @mentions, leagues, a weekly leaderboard and strategy cloning. Other features: Kimchi Premium, Fear & Greed, sector treemap, a monthly-returns heatmap of global indices (incl. Nikkei 225 · Hang Seng · FTSE 100 · Nifty 50), liquidation heatmap, Strategy Builder, Correlation Matrix + VaR, TOTP 2FA, RevenueCat subscriptions, and 5 languages (ko/en/ja/zh/es).  
![React Native](https://img.shields.io/badge/React_Native-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Expo SDK 54](https://img.shields.io/badge/Expo_SDK_54-000020?style=flat-square&logo=expo&logoColor=white)
![Zustand 5](https://img.shields.io/badge/Zustand_5-555555?style=flat-square)
![TanStack Query 5](https://img.shields.io/badge/TanStack_Query_5-FF4154?style=flat-square)
![RevenueCat](https://img.shields.io/badge/RevenueCat-F25A5A?style=flat-square)

**JUNIXION Backend** *(private · production ✅)*  
Shared Supabase backend for SimSage and junixion.com, kept in its own repository so server secrets can never end up in the client bundle. It has 53 SQL migrations and 33 Edge Functions, all active in production. The server-authoritative trading ledger places orders, closes positions and applies rewards through atomic Postgres RPCs, and a pg_cron liquidation, TP/SL and options-expiry batch runs every 2 minutes. The Claude API proxy (chat, market analysis, trade and journal feedback) sits behind a global AI-usage circuit breaker. Subscriptions arrive through a RevenueCat webhook. Account security covers re-authentication, MFA backup codes, device sessions and rate limiting. Market data comes from EODHD prices, SEC EDGAR earnings-tone analysis, and a daily z-score anomaly briefing. The waitlist sends Resend confirmation email and removes bounced addresses automatically.  
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Deno](https://img.shields.io/badge/Deno-000000?style=flat-square&logo=deno&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Claude API](https://img.shields.io/badge/Claude_API-D97757?style=flat-square&logo=anthropic&logoColor=white)

**JUNIXION Risk Intelligence Engine** *(private · live ✅)*  
Real-time multi-factor risk scoring for Upbit-listed crypto assets (2 fixed + a dynamic Top 30 by 24h volume). The composite score (0–1) is a weighted blend of 7 components: volatility 22% · derivatives 18% · sentiment 15% · event 15% · liquidity 12% · on-chain 10% · kimchi premium 8%. It maps to 4 levels: normal, caution ≥ 0.55, warning ≥ 0.75 and critical ≥ 0.90. More than 100 collectors cover markets, derivatives (Deribit options, funding, liquidation maps), on-chain (MVRV, SOPR, exchange reserves, whale flows), macro (M2, DXY, Fed balance sheet), social and news, and ETF/institutional flows. Claude writes the risk explanations (HybridRiskExplainer). Results are served by a Streamlit dashboard and a FastAPI REST API (`app.` / `api.junixion.com`, Docker on a VPS), with Gmail digests and threshold alerts.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

**[junixion.com](https://junixion.com)** *(company site · Vercel ✅)*  
Next.js 16 (App Router) + React 19 + Tailwind v4. Pages include the company story and vision (`/company`), the SimSage launch waitlist with a live counter and one-click unsubscribe, an insights blog (concepts · methodology · market commentary), a glossary, a press kit, a live status page, a changelog and legal pages. The site stays behind a private-preview access gate until launch, with light and dark modes. GitLab CI runs typecheck, lint, build and a Lighthouse quality gate on every change.  
![Next.js](https://img.shields.io/badge/Next.js_16-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React_19-61DAFB?style=flat-square&logo=react&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_v4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=flat-square&logo=gitlab&logoColor=white)

**Research Extension** *(in progress 🔄)*  
Extending the KRX survival paper toward stochastic intensity models — continuous-time hazard rates, market-regime conditioning, time-varying baseline hazard.

---

## Research

### Survival Analysis of Corporate Delisting Risk in the Korean Stock Market
**Cox Proportional Hazards and Accelerated Failure Time Models — KOSPI/KOSDAQ Panel Data (2000–2023)**

📄 [SSRN Working Paper](https://papers.ssrn.com/abstract=6656258) · Submitted April 2026

> *Static scoring models (Altman Z-score, logistic regression) treat failure as a binary outcome and discard censored observations. This paper replaces that assumption with event-history methodology — and it works.*

**What this paper does**
- Constructs a KRX survival dataset: 365 firms, 158 delisting events, 276-month observation window (DART + FinanceDataReader)
- Estimates and compares Kaplan-Meier, Cox PH, Weibull/Log-Normal/Log-Logistic AFT models
- Introduces heteroscedastic AFT extension — captures market-segment variance structure that standard Cox PH ignores

**Key findings**

| Finding | Result |
|---|---|
| Model discrimination | **C-index = 0.738** — competitive with Shumway (2001) US benchmark (C ≈ 0.74) |
| Dominant predictor | 12-month momentum: HR = 0.496, p = 0.001 — markets price distress before accounting statements do |
| Volatility signal | Price volatility: HR = 1.827, p = 0.004 — 82.7% higher delisting hazard per unit increase |
| Best specification | Weibull AFT (ancillary scale): AIC = 1620.6 — ΔAIC = 318.1 over homoscedastic (p < 0.001) |
| Market heterogeneity | KOSDAQ vs. KOSPI log-rank χ² = 10.57, p = 0.001 — fundamentally different survival distributions |

`survival analysis` `Cox PH` `AFT` `financial distress` `KRX` `KOSPI` `KOSDAQ` `DART` `empirical finance`

---

## Projects

**[Survival Analysis — Finance](https://github.com/jjuunnii98/survival-analysis-finance)**  
Full implementation of the SSRN working paper above. 365 KRX firms (KOSPI/KOSDAQ), 2000–2023, 43.3% event rate. Kaplan-Meier, Cox PH (C-index 0.738), and Weibull/Log-Normal/Log-Logistic AFT models with heteroscedastic extension. Data pipeline: DART API + FinanceDataReader → 7 covariates → survival dataset. Reproduces all tables and figures in the working paper.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![lifelines](https://img.shields.io/badge/lifelines-FF6B6B?style=flat-square)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)

**[Crypto Risk Scoring Demo](https://github.com/jjuunnii98/crypto-risk-scoring-demo)**  [![Live API](https://img.shields.io/badge/Live%20API-online-brightgreen?style=flat-square&logo=render&logoColor=white)](https://crypto-risk-scoring-demo.onrender.com/docs)  
Cox PH survival model predicting 24-hour drawdown risk (>3% threshold) on live Binance data — C-index 0.862. 16 engineered features: 9 technical (RSI, Bollinger, MACD, VWAP divergence, ATR) + 7 volatility/tail-risk (Garman-Klass, Sortino, rolling MDD, funding rate z-score). Async multi-symbol scoring. 40 passing tests.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![lifelines](https://img.shields.io/badge/lifelines-FF6B6B?style=flat-square)

**JUNIXION LLM** *(private)*  
Decoder-only Transformer built from scratch in PyTorch — no pre-trained weights. Architecture: RMSNorm + RoPE + Grouped Query Attention + KV Cache + SwiGLU FFN. Three presets: nano (~14M) · small (~162M) · base (~489M). Phase 1b complete: 817M tokens (wikitext-103 + Korean/English Wikipedia), step 50,000, avg_loss = 1.6946 on Kaggle T4 ×2. Phase 4 ready: Qwen2.5-Coder-7B QLoRA SFT on DART filings + crypto/finance news + finance code (The Stack v2). Target: domain-specialized financial risk LLM for the JUNIXION inference layer.  
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

**[End-to-End ML Analytics System](https://github.com/jjuunnii98/end-to-end-ml-analytics-system)**  [![Live API](https://img.shields.io/badge/Live%20API-online-brightgreen?style=flat-square&logo=render&logoColor=white)](https://ml-churn-api-2z9m.onrender.com/docs)  
Telco customer churn prediction as a production ML system. Random Forest (ROC-AUC 0.83, accuracy 0.79) with full pipeline: data validation → numeric/categorical feature engineering → artifact-based inference → Dockerized FastAPI. Modular architecture with config-driven pipeline and 4 test modules.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

**[SQL Analytics Portfolio](https://github.com/jjuunnii98/sql-analytics-portfolio)**  
PostgreSQL 16 analytics on 9 assets × 5 years (13,489 rows): 18 SQL analyses across basics, window functions, financial metrics, and crypto indicators — all implemented from scratch in pure SQL. Sharpe ratio, max drawdown, Bollinger bands, RSI, VWAP, and pairwise correlation across BTC/ETH/SOL/BNB and AAPL/MSFT/NVDA/TSLA/GOOGL. Full pipeline: yfinance → CSV → PostgreSQL → Makefile automation → Python test suite.

> NVDA Sharpe 1.436 · SOL 2021 +11,153% · BTC–ETH correlation 0.817 · BTC max drawdown −76.6%

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

**[Graduate ML Portfolio](https://github.com/jjuunnii98/grad-portfolio-ml)**  [![Live API](https://img.shields.io/badge/Live%20API-online-brightgreen?style=flat-square&logo=render&logoColor=white)](https://survival-api.onrender.com/docs)  
Breast cancer survival analysis on METABRIC clinical dataset (1,353 patients). Penalized Cox PH (L2, penalizer=0.1) vs. baseline — validation C-index 0.638 vs. 0.629. Hazard ratio interpretation: Histologic Grade 3, HER2+, and lymph node positivity as high-risk indicators; ER+ as protective. Deployed as FastAPI inference service.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![lifelines](https://img.shields.io/badge/lifelines-FF6B6B?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

**[Python Analysis Lab](https://github.com/jjuunnii98/python-analysis-lab)**  
Three-domain analysis portfolio, each following a 4-notebook pipeline (EDA → feature engineering → modeling → insights): **(1) Retail** — RFM features, customer segmentation, churn prediction; **(2) Financial** — technical indicators (MA, RSI, Bollinger), volatility clustering, strategy backtesting; **(3) Healthcare** — patient risk classification with XGBoost, SHAP interpretation, SMOTE for class imbalance.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

**[Python Snake Game](https://github.com/jjuunnii98/python-snake-game)**  
Pygame snake game with three difficulty modes (EASY · NORMAL · HARD), progressive FPS acceleration (score-driven speed increase up to 30 FPS), and per-difficulty persistent high scores (JSON). Clean OOP: `Snake` class handles body management, 180° reversal guard, wall and self-collision detection; `Food` class handles collision-aware respawn. WASD + arrow key controls, grid overlay, NEW RECORD indicator. Distributed as standalone executable via PyInstaller.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-000000?style=flat-square&logo=python&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-4B5563?style=flat-square)

---

## Stack

<div align="center">

**Languages & Modeling**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**ML / Statistical Modeling**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**Backend / Deployment**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)

**Product / Full-Stack**

![React Native](https://img.shields.io/badge/React_Native-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Expo](https://img.shields.io/badge/Expo-000020?style=for-the-badge&logo=expo&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Deno](https://img.shields.io/badge/Deno-000000?style=for-the-badge&logo=deno&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

**Analytics & Visualization**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SAS](https://img.shields.io/badge/SAS-003399?style=for-the-badge&logo=sas&logoColor=white)

</div>

---

## Connect

Building the full JUNIXION stack as a solo researcher and engineer: LLM weights, the live risk engine, the Supabase backend, the mobile app and the website.

| Area | Open to |
|---|---|
| Research | LLM / NLP · survival analysis · stochastic processes · quantitative finance |
| FinTech | JUNIXION partnership · investment |
| Roles | Quant engineer · ML researcher · AI engineer |
| Academia | Financial Engineering / AI graduate programs (2027 entry) |

[![LinkedIn](https://img.shields.io/badge/LinkedIn-jun--yeong--song-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jun-yeong-song/)
[![JUNIXION](https://img.shields.io/badge/JUNIXION-junixion.com-000000?style=flat-square&logo=vercel&logoColor=white)](https://junixion.com)
[![Email](https://img.shields.io/badge/Email-contact%40junixion.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:contact@junixion.com)

---

## Background

**Yonsei University** — Economics × Information Statistics · Expected August 2026  
Undergraduate Research Assistant — Survival Analysis & Healthcare Risk Modeling  
Founder — JUNIXION (Risk Intelligence AI · FinTech Startup)

### Certifications

**Completed**
- ADsP · SQLD · CDS 빅데이터 전문가 과정
- 2024 제주 스마트관광 빅데이터 해커톤 우수상 — Team Leader

**In Progress**
- 투자자산운용사 (Investment Asset Manager)
- 빅데이터분석기사 (Big Data Analytics Engineer) · 정보처리기사 (Engineer Information Processing)

**Planned**
- 리눅스마스터 1급 (Linux Master Level 1) · 정보보안기사 (Engineer Information Security)
- 금융투자분석사 (Financial Investment Analyst)

---

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jun-yeong-song/)
[![JUNIXION](https://img.shields.io/badge/JUNIXION-000000?style=flat-square&logo=vercel&logoColor=white)](https://junixion.com)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:contact@junixion.com)

</div>
