<div align="center">

# 🛒 BlinkIT Sales Intelligence Engine & Predictive Dashboard

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7%2B-189AB4?style=for-the-badge)](https://xgboost.readthedocs.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![IBM SkillsBuild](https://img.shields.io/badge/IBM%20SkillsBuild-Internship%202026-054ADA?style=for-the-badge&logo=ibm&logoColor=white)](https://skillsbuild.org/)
[![AICTE](https://img.shields.io/badge/AICTE-Approved-006400?style=for-the-badge)](https://www.aicte-india.org/)

**An end-to-end retail sales forecasting system built on the BlinkIT Grocery dataset — structured across the 4-Tier Analytics Ladder (Descriptive → Diagnostic → Predictive → Prescriptive) — featuring a beginner-friendly interactive Streamlit dashboard for real-time sales prediction.**

</div>

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [Official Internship Context](#-official-internship-context)
3. [Project Architecture & Workflow](#-project-architecture--workflow)
4. [Dataset Description & Feature Dictionary](#-dataset-description--feature-dictionary)
5. [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
6. [Model Performance Benchmark](#-model-performance-benchmark)
7. [Prescriptive Analytics — Outlet Scorecard](#-prescriptive-analytics--outlet-scorecard)
8. [Screenshots](#-screenshots)
9. [Local Setup & Execution Guide](#-local-setup--execution-guide)
10. [Project Structure](#-project-structure)
11. [Author & Internship Credentials](#-author--internship-credentials)

---

## 🎯 Executive Summary

The **BlinkIT Sales Intelligence Engine** is a full-stack data analytics and machine learning capstone project that transforms raw grocery retail data into actionable sales intelligence. Built on a real-world item–outlet sales dataset from the Indian quick-commerce grocery chain BlinkIT (formerly Blinkit), the system delivers:

- **Descriptive analytics** — cohort baselines, revenue distribution, and data quality audits
- **Diagnostic analytics** — 6 EDA charts uncovering how outlet type, location tier, store size, and item category influence sales
- **Predictive analytics** — a leakage-aware regression pipeline benchmarking 4 models (Linear Regression, Ridge, Random Forest, XGBoost) with 5-fold cross-validation
- **Prescriptive analytics** — a peer-format outlet scorecard and shelf-visibility restocking priority list
- **Interactive dashboard** — a beginner-friendly Streamlit UI for real-time sales forecasting without any ML knowledge required

> **Disclaimer:** The BlinkIT Grocery dataset is a synthetic/derived item–outlet sales dataset intended for educational and analytical training purposes. Model outputs are statistical estimates and should be used alongside human managerial judgment.

---

## 🏛️ Official Internship Context

| Field | Detail |
|-------|--------|
| **Program** | IBM SkillsBuild Data Analytics with AI Internship 2026 |
| **Collaboration** | Offered in partnership with **AICTE** (All India Council for Technical Education) and **BharatCares** |
| **Internship ID** | `IBMUEDA1448` |
| **Timeline** | 17 August 2026 – 30 September 2026 |
| **Author** | M Y Likhith |
| **Institution** | S JC Institute Of Technology |

This project was developed as the capstone submission for the **IBM SkillsBuild Data Analytics with AI Internship 2026**, a nationally recognised industry–academia programme connecting engineering students with real-world AI/ML use cases under IBM's global learning platform.

---

## 🏗️ Project Architecture & Workflow

```
┌──────────────────────────────────────────────────────────────────┐
│                  BlinkIT Sales Intelligence Engine                │
│                                                                    │
│  ┌─────────────┐    ┌─────────────┐    ┌──────────────────────┐  │
│  │  Raw Data   │───▶│  Cleaning   │───▶│  Feature Engineering │  │
│  │ (8,523 rows)│    │ & Imputation│    │  (Item_Category,      │  │
│  │  12 columns │    │             │    │   Outlet_Age)         │  │
│  └─────────────┘    └─────────────┘    └──────────┬───────────┘  │
│                                                    │               │
│            ┌───────────────────────────────────────┘               │
│            ▼                                                        │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │                  4-TIER ANALYTICS PIPELINE                  │   │
│  │                                                              │   │
│  │  TIER 1 ─ Descriptive   │  TIER 2 ─ Diagnostic             │   │
│  │  • Cohort baselines      │  • 6 EDA visualisations          │   │
│  │  • Revenue stats         │  • Correlation heatmap           │   │
│  │  • Category mix          │  • Outlet/Item breakdowns        │   │
│  │                                                              │   │
│  │  TIER 3 ─ Predictive    │  TIER 4 ─ Prescriptive           │   │
│  │  • 4-model CV benchmark  │  • Peer-format outlet scorecard  │   │
│  │  • Best model: RF (R²    │  • Under-merchandised items list │   │
│  │    0.606, RMSE 38.93)   │  • Visibility restocking alerts  │   │
│  └────────────────────────────────────────────────────────────┘   │
│                                                                    │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              Streamlit Interactive Dashboard                  │  │
│  │  • Product & store parameter sliders/dropdowns               │  │
│  │  • Real-time prediction via best_model.pkl                   │  │
│  │  • Beginner-friendly UI with tips & insights                 │  │
│  └─────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

**Tech Stack:** Python · Pandas · NumPy · Scikit-Learn · XGBoost · Matplotlib · Seaborn · Streamlit · Jupyter Notebooks · Joblib

---

## 📊 Dataset Description & Feature Dictionary

### Overview

| Property | Value |
|----------|-------|
| **Dataset** | BlinkIT Grocery Data (item–outlet level sales) |
| **Records** | 8,523 rows × 12 columns |
| **Grain** | One row = one product sold at one outlet |
| **Target Variable** | `Sales` (continuous, ₹31.29 – ₹266.89) |
| **Outlets** | 10 unique outlets across 3 location tiers |
| **Products** | 1,559 unique item identifiers |

### Feature Dictionary

| Column | Type | Description | Notes |
|--------|------|-------------|-------|
| `Item Identifier` | Categorical | Unique product SKU code | Prefix: `FD`=Food, `DR`=Drinks, `NC`=Non-Consumable |
| `Item Type` | Categorical | Specific product category (16 types) | e.g. Frozen Foods, Dairy, Snack Foods |
| `Item Fat Content` | Categorical | Fat labelling on the product | Raw labels standardised: `LF`/`low fat` → `Low Fat`; `reg` → `Regular` |
| `Item Weight` | Numeric | Package weight in kg | 1,463 missing values — imputed by same-product mean, fallback to Item Type mean |
| `Item Visibility` | Numeric | Shelf visibility score (0–1) | 526 zero-value rows treated as missing; imputed by Item_Category median |
| `Outlet Identifier` | Categorical | Unique store ID (OUT010 – OUT049) | 10 outlets |
| `Outlet Establishment Year` | Numeric | Year the outlet was opened | Converted to `Outlet_Age = 2026 − year` |
| `Outlet Size` | Categorical | Physical store size | Small / Medium / High |
| `Outlet Location Type` | Categorical | City tier classification | Tier 1 (metro) / Tier 2 / Tier 3 |
| `Outlet Type` | Categorical | Store format | Grocery Store / Supermarket Type1/2/3 |
| `Rating` | Numeric | Customer satisfaction rating | Mean: 3.97 / 5 |
| `Sales` | Numeric | **Target** — item-outlet revenue in ₹ | Mean: ₹140.99 · Median: ₹143.01 · Std: ₹62.28 |

### Engineered Features

| Feature | Formula | Purpose |
|---------|---------|---------|
| `Item_Category` | Derived from `Item Identifier` prefix | Low-cardinality grouping (Food / Drinks / Non-Consumable) |
| `Outlet_Age` | `2026 − Outlet Establishment Year` | Captures store maturity effect |

---

## 🔍 Exploratory Data Analysis (EDA)

The notebook (`BlinkITSalesPrediction.ipynb`) contains **6 diagnostic charts** structured as Tier 2 — Diagnostic Analytics:

| Chart | Key Finding |
|-------|-------------|
| **Sales Distribution** | Near-normal distribution centred around ₹140; slight right skew |
| **Average Sales by Outlet Type** | Remarkably flat across all 4 formats (Sup. Type2: ₹141.68 vs Grocery: ₹140.29) |
| **Sales by Location Tier & Store Size** | No single tier/size combination dominates — signal is distributed across interactions |
| **Average Sales by Item Type** | All 16 item types within a tight band; no single category dramatically outperforms |
| **Item Visibility vs Sales & Correlation Heatmap** | All numeric correlations are very weak (max |r| < 0.06) — price/MRP absence is the key data gap |
| **Total Revenue by Outlet** | Grocery Stores (OUT010, OUT019) generate ~40% less total revenue — driven by item count, not per-item sales |

> **Key diagnostic insight:** The absence of an item price / MRP field is the single largest constraint on model accuracy. Price is typically the dominant predictor in retail sales regression; without it, the signal is thin and distributed across categorical interactions — which explains why tree-based models outperform linear ones and why R² remains moderate.

---

## 🏆 Model Performance Benchmark

All models evaluated with **5-fold cross-validation** on an 80/20 train/test split (train: 6,818 rows, test: 1,705 rows).

### Cross-Validation Results (5-Fold CV on Training Set)

| Model | Mean RMSE ↓ | Mean MAE ↓ | Mean R² ↑ |
|-------|------------|-----------|----------|
| 🥇 **Random Forest Regressor** | **38.93** | **29.85** | **0.6064** |
| 🥈 XGBoost | 39.50 | 30.08 | 0.5947 |
| 🥉 Ridge Regression | 61.94 | 52.33 | 0.0038 |
| Linear Regression | 61.94 | 52.33 | 0.0038 |

### Model Selection

**Random Forest Regressor** (100 estimators, `random_state=42`) was selected as the production model based on best cross-validated R² (0.606) and lowest RMSE (38.93). The trained pipeline is serialised as `models/best_model.pkl` and consumed by the Streamlit dashboard.

### Feature Importance (Top 10 — Random Forest)

| Rank | Feature | Importance |
|------|---------|-----------|
| 1 | Item Weight | 0.3464 |
| 2 | Item Visibility | 0.2896 |
| 3 | Rating | 0.0498 |
| 4 | Item Type — Fruits and Vegetables | 0.0202 |
| 5 | Item Type — Dairy | 0.0201 |
| 6 | Item Type — Frozen Foods | 0.0198 |
| 7 | Item Fat Content — Low Fat | 0.0197 |
| 8 | Item Fat Content — Regular | 0.0196 |
| 9 | Item Type — Snack Foods | 0.0188 |
| 10 | Item Type — Canned | 0.0186 |

> **Interpretability note:** `Item Weight` and `Item Visibility` dominate because they are high-cardinality continuous fields that partially allow the forest to distinguish individual products. This reflects variance reduction more than a direct causal effect.

> **Honest limitation:** R² is moderate (≈0.60) because the dataset lacks an item price / MRP field. This is a data-availability constraint, not a modelling error, and is reported transparently.

---

## 📈 Prescriptive Analytics — Outlet Scorecard

A separate **peer-benchmark model** (Random Forest, 300 trees, `max_depth=8`) is trained on outlet format attributes only — excluding `Outlet Identifier` — to estimate what a *typical outlet with this format* should sell. Each real outlet's actual sales are compared against that benchmark:

| Outlet | Format | Tier | Size | Performance vs Peers |
|--------|--------|------|------|---------------------|
| OUT046 | Supermarket Type1 | Tier 1 | Small | **+0.98%** ✅ |
| OUT035 | Supermarket Type1 | Tier 2 | Small | +0.88% ✅ |
| OUT045 | Supermarket Type1 | Tier 2 | Small | +0.39% ✅ |
| OUT018 | Supermarket Type2 | Tier 3 | Medium | +0.23% ✅ |
| OUT013 | Supermarket Type1 | Tier 3 | High | +0.23% ✅ |
| OUT049 | Supermarket Type1 | Tier 1 | Medium | -0.29% ⚠️ |
| OUT010 | Grocery Store | Tier 3 | Small | -0.51% ⚠️ |
| OUT019 | Grocery Store | Tier 1 | Small | -0.77% ⚠️ |
| OUT027 | Supermarket Type3 | Tier 3 | Medium | -0.90% 🔴 |
| OUT017 | Supermarket Type1 | Tier 2 | Small | **-0.95%** 🔴 |

---

## 🖼️ Screenshots

<table>
<tr>
<td align="center"><strong>Dashboard Interface</strong></td>
<td align="center"><strong>Sales Prediction Result</strong></td>
</tr>
<tr>
<td><img src="Screenshots/01_dashboard_interface.png" alt="Dashboard Interface" width="420"/></td>
<td><img src="Screenshots/02_sales_prediction.png" alt="Sales Prediction" width="420"/></td>
</tr>
<tr>
<td align="center"><strong>EDA Distributions</strong></td>
<td align="center"><strong>Feature Importance</strong></td>
</tr>
<tr>
<td><img src="Screenshots/03_eda_distributions.png" alt="EDA Distributions" width="420"/></td>
<td><img src="Screenshots/04_feature_importance.png" alt="Feature Importance" width="420"/></td>
</tr>
</table>

---

## 🚀 Local Setup & Execution Guide

### Prerequisites

- Python 3.10 or higher
- `pip` package manager
- Git

### Step 1 — Clone the Repository

```bash
git clone https://github.com/<your-username>/BlinkIT-Sales-Prediction.git
cd BlinkIT-Sales-Prediction
```

### Step 2 — Create & Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` includes:

```
numpy>=2.0.0
pandas>=2.0.0
scipy>=1.10.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
xgboost>=1.7.0
joblib>=1.3.0
streamlit>=1.30.0
jupyter>=1.0.0
```

### Step 4 — (Optional) Re-train the Model

If you want to regenerate `models/best_model.pkl` from scratch, open and run all cells in the Jupyter notebook:

```bash
jupyter notebook BlinkITSalesPrediction.ipynb
```

The notebook will automatically save the best model to `models/best_model.pkl`.

### Step 5 — Launch the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`.

### Dashboard Usage

| Step | Action |
|------|--------|
| **1** | Select **Product Information** — choose category, item type, weight (kg), and MRP (₹) using the sliders and dropdowns on the left |
| **2** | Select **Store Information** — choose outlet type, store size, location tier, and opening year |
| **3** | Click **🚀 Calculate Expected Sales** to get the real-time prediction |
| **4** | View the **Estimated Total Sales** metric card and read the **Beginner Tips & Insights** panel |

---

## 📁 Project Structure

```
BlinkIT-Sales-Prediction/
│
├── app.py                          # Streamlit dashboard application
├── BlinkITSalesPrediction.ipynb    # Full 4-tier analytics notebook
├── BlinkIT Grocery Data Excel.xlsx # Source dataset (8,523 rows × 12 cols)
├── requirements.txt                # Python dependencies
├── ProjectReport.docx              # Full project report (Word)
│
├── models/
│   └── best_model.pkl              # Serialised Random Forest pipeline
│
└── Screenshots/
    ├── 01_dashboard_interface.png
    ├── 02_sales_prediction.png
    ├── 03_eda_distributions.png
    └── 04_feature_importance.png
```

---

## 👨‍💻 Author & Official Internship Credentials

<table>
<tr>
<td><strong>Name</strong></td>
<td>M Y Likhith</td>
</tr>
<tr>
<td><strong>Institution</strong></td>
<td>S JC Institute Of Technology</td>
</tr>
<tr>
<td><strong>Program</strong></td>
<td>IBM SkillsBuild Data Analytics with AI Internship 2026</td>
</tr>
<tr>
<td><strong>Offered by</strong></td>
<td>IBM, in collaboration with AICTE &amp; BharatCares</td>
</tr>
<tr>
<td><strong>Internship ID</strong></td>
<td><code>IBMUEDA1448</code></td>
</tr>
<tr>
<td><strong>Duration</strong></td>
<td>17 August 2026 – 30 September 2026</td>
</tr>
</table>

---

<div align="center">

**Built with ❤️ as part of the IBM SkillsBuild Data Analytics with AI Internship 2026**

*Empowering the next generation of data scientists through hands-on AI/ML learning*

[![IBM SkillsBuild](https://img.shields.io/badge/IBM%20SkillsBuild-054ADA?style=flat-square&logo=ibm&logoColor=white)](https://skillsbuild.org/)
[![AICTE](https://img.shields.io/badge/AICTE-006400?style=flat-square)](https://www.aicte-india.org/)
[![BharatCares](https://img.shields.io/badge/BharatCares-FF6B35?style=flat-square)](https://www.bharatcares.org/)

</div>
