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
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jjuunnii98/jjuunnii98/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/jjuunnii98/jjuunnii98/output/github-snake.svg" />
  <img alt="github contribution snake" src="https://raw.githubusercontent.com/jjuunnii98/jjuunnii98/output/github-snake-dark.svg" />
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
Full implementation of the research above. Cox PH, Weibull/Log-Normal/Log-Logistic AFT, heteroscedastic extension, Kaplan-Meier curves, Schoenfeld residual diagnostics. Reproduces all tables and figures in the working paper.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![lifelines](https://img.shields.io/badge/lifelines-FF6B6B?style=flat-square)

**[Crypto Risk Scoring Demo](https://github.com/jjuunnii98/crypto-risk-scoring-demo)**  
End-to-end crypto market risk scoring pipeline: real-time data ingestion, feature engineering, multi-signal quantitative risk scoring, and FastAPI deployment.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

**[End-to-End ML Analytics System](https://github.com/jjuunnii98/end-to-end-ml-analytics-system)**  
Full ML lifecycle from raw data to Dockerized API serving. Production-oriented architecture: preprocessing → training → evaluation → inference endpoint.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

**[SQL Analytics Portfolio](https://github.com/jjuunnii98/sql-analytics-portfolio)**  
Financial and crypto data analysis with SQL: window functions, time-series aggregation, market data queries.  
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

**[Graduate ML Portfolio](https://github.com/jjuunnii98/grad-portfolio-ml)**  
Penalized Cox regression, statistical modeling experiments, and replication studies from undergraduate research.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)

**[Python Analysis Lab](https://github.com/jjuunnii98/python-analysis-lab)**  
Structured EDA, statistical modeling, and reproducible analysis workflows.  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
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
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
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
Engineering layer →  Real-time inference, scalable pipelines, production deployment
Product layer    →  Domain-specialized Risk Intelligence AI for financial decision-making
```

Proprietary system architecture. IP filing in preparation.

---

## Roadmap

```
2026.08 ──▶  Graduation · Yonsei University
2026    ──▶  Technology IP Filing · JUNIXION proprietary system
2026    ──▶  JUNIXION FinTech company launch preparation
2027.03 ──▶  Graduate School · Financial Engineering / AI (Spring entry)
```

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
