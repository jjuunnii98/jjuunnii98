<div align="center">

# Junyeong Song

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1000&color=58A6FF&center=true&vCenter=true&random=false&width=600&lines=AI+Engineer+%C2%B7+Quantitative+Finance;Survival+Analysis+%C2%B7+Cox+PH+%C2%B7+AFT+Models;Risk+Intelligence+Builder+%40+JUNIXION;Yonsei+University+%C2%B7+Seoul%2C+South+Korea)](https://github.com/jjuunnii98)

<br>

> Financial distress models have not fundamentally changed since Altman (1968).  
> Static scoring. No censoring. No time structure. Fifty years of the same assumption.  
> I'm building the next layer — survival-based, market-aware, production-ready.

<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-jun--yeong--song-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jun-yeong-song/)
[![JUNIXION](https://img.shields.io/badge/junixion.com-000000?style=flat-square&logo=vercel&logoColor=white)](https://junixion.com)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-JUNIXION-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/JUNIXION)
[![Email](https://img.shields.io/badge/jjuunnii98%40yonsei.ac.kr-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:jjuunnii98@yonsei.ac.kr)

![Profile Views](https://komarev.com/ghpvc/?username=jjuunnii98&style=flat-square&color=0d1117&label=views)
![Streak](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/jjuunnii98/jjuunnii98/main/streak.json)

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

---

## Stack

<div align="center">

**Languages & Modeling**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
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

**Analytics & Visualization**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SAS](https://img.shields.io/badge/SAS-003399?style=for-the-badge&logo=sas&logoColor=white)

</div>

---

## JUNIXION

**[junixion.com](https://junixion.com)** — Risk Intelligence AI · FinTech

The research above is not an academic exercise. It is the proof of concept for a broader system.

Financial risk intelligence does not exist as a dedicated AI platform. Bloomberg gives you data. ChatGPT gives you text. Neither gives you a principled, real-time, censoring-aware risk score grounded in the actual statistical structure of financial failure.

That is what JUNIXION builds.

```
Research layer   →  Survival models, stochastic processes, quantitative risk theory
AI layer         →  JunixionLM — custom Transformer, domain SFT pipeline (DART + crypto + code)
Engineering layer →  Real-time inference, scalable pipelines, production deployment
Product layer    →  Domain-specialized Risk Intelligence AI for financial decision-making
```

Proprietary system architecture. IP filing in preparation.

---

## Currently Building

```
Research      →  Continuous-time default models (KRX paper extension)
AI Model      →  JunixionLM — 162M params, Phase 1 ✅, QLoRA SFT prep 🔄
Intelligence  →  Risk pipeline — live 24/7, Supabase accumulating
Mobile        →  SimSage — React Native market intelligence + mock trading
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

**JUNIXION Risk Intelligence Pipeline** *(private · live ✅)*  
4-factor composite score (volatility · liquidity · sentiment · event) running 24/7 via macOS LaunchAgent. 60+ RSS feeds, on-chain metrics (SOPR/MVRV/NVT/hashrate/mempool), stablecoin surveillance (9 assets), derivatives monitoring (funding rate + L/S + OI, Binance/Bybit/OKX), 227-keyword global news routing. Telegram 7-topic dispatch + Streamlit dashboard. Supabase PostgreSQL accumulating risk snapshots continuously.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Telegram Bot API](https://img.shields.io/badge/Telegram_Bot_API-26A5E4?style=flat-square&logo=telegram&logoColor=white)
![Binance API](https://img.shields.io/badge/Binance_API-F0B90B?style=flat-square&logoColor=black)
![DeFi Llama](https://img.shields.io/badge/DeFi_Llama-555555?style=flat-square)
![GNews API](https://img.shields.io/badge/GNews_API-555555?style=flat-square)

**SimSage — JUNIXION Mobile App** *(private · in development 🔄)*  
React Native / Expo SDK 54 frontend to the risk pipeline. AI mock trading (spot/futures/options), Kimchi Premium, Fear & Greed Index, Sector Treemap, liquidation heatmap overlay, live order book, price-target alerts, no-code Strategy Builder, Correlation Matrix + VaR. Shares Telegram bot channel with the intelligence pipeline.  
![React Native](https://img.shields.io/badge/React_Native-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Expo SDK 54](https://img.shields.io/badge/Expo_SDK_54-000020?style=flat-square&logo=expo&logoColor=white)
![Zustand 5](https://img.shields.io/badge/Zustand_5-555555?style=flat-square)
![TanStack Query 5](https://img.shields.io/badge/TanStack_Query_5-FF4154?style=flat-square)

**Research Extension** *(in progress 🔄)*  
Extending the KRX survival paper toward stochastic intensity models — continuous-time hazard rates, market-regime conditioning, time-varying baseline hazard.

---

## Connect

Building the full JUNIXION stack — LLM weights to live intelligence pipeline to mobile app — as a solo researcher and engineer.

| Area | Open to |
|---|---|
| Research | LLM / NLP · survival analysis · stochastic processes · quantitative finance |
| FinTech | JUNIXION partnership · investment |
| Roles | Quant engineer · ML researcher · AI engineer |
| Academia | Financial Engineering / AI graduate programs (2027 entry) |

[![LinkedIn](https://img.shields.io/badge/LinkedIn-jun--yeong--song-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jun-yeong-song/)
[![JUNIXION](https://img.shields.io/badge/JUNIXION-junixion.com-000000?style=flat-square&logo=vercel&logoColor=white)](https://junixion.com)
[![Email](https://img.shields.io/badge/Email-jjuunnii98%40yonsei.ac.kr-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:jjuunnii98@yonsei.ac.kr)

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
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:jjuunnii98@yonsei.ac.kr)

</div>
