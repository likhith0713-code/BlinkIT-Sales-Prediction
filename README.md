<div align="center">

<h1>🛒 BlinkIT Sales Intelligence Engine & Predictive Dashboard</h1>

<p>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge" alt="Status: Complete"/>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"/>
  <img src="https://img.shields.io/badge/License-Educational-lightgrey?style=for-the-badge" alt="License: Educational"/>
  <img src="https://img.shields.io/badge/IBM%20SkillsBuild-Internship%202026-054ADA?style=for-the-badge&logo=ibm&logoColor=white" alt="IBM SkillsBuild Internship 2026"/>
  <img src="https://img.shields.io/badge/AICTE-Approved-006400?style=for-the-badge" alt="AICTE Approved"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
  <img src="https://img.shields.io/badge/XGBoost-1.7%2B-189AB4?style=flat-square" alt="XGBoost"/>
  <img src="https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Pandas-2.0%2B-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/>
  <img src="https://img.shields.io/badge/Matplotlib%20%2F%20Seaborn-Visualisation-11A9AC?style=flat-square" alt="Matplotlib / Seaborn"/>
</p>

<br/>

> **An end-to-end retail sales forecasting system** — structured across the full **4-Tier Analytics Ladder** (Descriptive → Diagnostic → Predictive → Prescriptive) — with a production-grade Streamlit dashboard for real-time item-outlet sales prediction.

</div>

---

## 📋 Table of Contents

1. [Project Overview & Executive Summary](#-project-overview--executive-summary)
2. [Official Internship Credentials](#-official-internship-credentials)
3. [Repository Structure](#-repository-structure)
4. [Dataset & Feature Engineering](#-dataset--feature-engineering)
5. [EDA Summary & Model Performance](#-eda-summary--model-performance)
6. [Interactive Dashboard UI Preview](#-interactive-dashboard-ui-preview)
7. [Local Installation & Execution Guide](#-local-installation--execution-guide)
8. [Author & Contact](#-author--contact)

---

## 🎯 Project Overview & Executive Summary

The **BlinkIT Sales Intelligence Engine** is a production-ready machine learning system that forecasts item-level sales revenue across BlinkIT's retail outlet network. Built on a real-world grocery dataset of **8,523 item–outlet records**, it transforms raw transactional data into actionable retail intelligence — from shelf-space recommendations to outlet performance scorecards.

### Business Context

Quick-commerce grocery retailers face a critical challenge: knowing *in advance* which product–outlet combinations will generate the most revenue. Without this insight, stores suffer from stockouts on high-velocity SKUs and dead inventory on under-performers. This project addresses that gap by delivering:

| Capability | Description |
|---|---|
| **Real-Time Forecasting** | Predict item outlet sales (₹) for any product–store combination via an interactive dashboard |
| **Outlet Benchmarking** | Compare each outlet's actual performance against a peer-format model to identify under-performers |
| **Feature Intelligence** | Understand which item and outlet attributes drive sales through transparent feature importance analysis |
| **Prescriptive Recommendations** | Actionable shelf-restocking priorities based on visibility-to-sales gaps |

### Key Technical Highlights

| Metric | Value |
|---|---|
| **Dataset** | BlinkIT Grocery Data — 8,523 records × 12 columns |
| **Target Variable** | `Sales` (continuous, ₹31.29 – ₹266.89) |
| **Best Model** | Random Forest Regressor — R² **0.606**, RMSE **38.93** |
| **Runner-Up** | XGBoost Regressor — R² **0.595**, RMSE **39.50** |
| **Validation Strategy** | 5-Fold Cross-Validation on 80/20 train/test split |
| **Deployment** | Streamlit web application with sidebar controls and live prediction |
| **Analytics Framework** | 4-Tier Ladder: Descriptive → Diagnostic → Predictive → Prescriptive |

> **Disclaimer:** The BlinkIT Grocery dataset is a synthetic/derived dataset intended for educational and analytical training purposes. Model outputs are statistical estimates and should be used alongside professional managerial judgment.

---

## 🏛️ Official Internship Credentials

<table>
  <tr>
    <td width="180"><strong>Programme</strong></td>
    <td><strong>IBM SkillsBuild Data Analytics with AI Internship 2026</strong></td>
  </tr>
  <tr>
    <td><strong>Offered by</strong></td>
    <td>IBM, in collaboration with <strong>AICTE</strong> (All India Council for Technical Education) and <strong>BharatCares</strong></td>
  </tr>
  <tr>
    <td><strong>Internship ID</strong></td>
    <td><code>IBMUEDA1448</code></td>
  </tr>
  <tr>
    <td><strong>Timeline</strong></td>
    <td>17 August 2026 – 30 September 2026</td>
  </tr>
  <tr>
    <td><strong>Author</strong></td>
    <td>M Y Likhith</td>
  </tr>
  <tr>
    <td><strong>Institution</strong></td>
    <td>S JC Institute Of Technology</td>
  </tr>
  <tr>
    <td><strong>Project Type</strong></td>
    <td>End-to-End Data Analytics + Machine Learning Capstone</td>
  </tr>
</table>

This project was developed as the capstone submission for the **IBM SkillsBuild Data Analytics with AI Internship 2026**, a nationally recognised industry–academia programme that connects engineering students with real-world AI/ML workflows under IBM's global learning platform.

---

## 📁 Repository Structure

```
BlinkIT-Sales-Prediction/
│
├── 📄 app.py                            # Streamlit dashboard — sidebar controls,
│                                        # parsed DataFrame view, live prediction,
│                                        # and Retail Strategy Insights panel
│
├── 📓 BlinkITSalesPrediction.ipynb      # End-to-end 4-tier analytics notebook
│                                        # (EDA → Cleaning → Training → Evaluation
│                                        #  → Prescriptive Outlet Scorecard)
│
├── 📊 BlinkIT Grocery Data Excel.xlsx   # Source dataset (8,523 rows × 12 columns)
│
├── 📋 requirements.txt                  # Pinned Python package dependencies
│
├── 📝 ProjectReport.docx                # Full internship project report (Word)
│
├── models/
│   └── 🤖 best_model.pkl               # Serialised Random Forest sklearn pipeline
│                                        # (ColumnTransformer + RandomForestRegressor)
│
└── Screenshots/
    ├── 🖼️ 01_dashboard_interface.png    # Default dashboard state (no prediction)
    ├── 🖼️ 02_sales_prediction.png       # Active prediction result (₹181.85)
    ├── 🖼️ 03_eda_distributions.png      # Sales distribution histogram with KDE
    └── 🖼️ 04_feature_importance.png     # Top 12 Random Forest feature importances
```

---

## 📊 Dataset & Feature Engineering

### Raw Dataset Overview

| Property | Value |
|---|---|
| **Source** | BlinkIT Grocery Data (synthetic/derived, for educational use) |
| **Shape** | 8,523 rows × 12 columns |
| **Grain** | One row = one product SKU sold at one specific outlet |
| **Target** | `Sales` — item-outlet revenue in ₹ |
| **Unique Products** | 1,559 item identifiers |
| **Unique Outlets** | 10 outlets across Tier 1, Tier 2, and Tier 3 cities |
| **Total Verified Revenue** | ₹1,201,681.49 |
| **Mean Sales / Record** | ₹140.99 (Median: ₹143.01, Std: ₹62.28) |

### Feature Dictionary

| Feature | Type | Range / Values | Description |
|---|---|---|---|
| `Item Identifier` | Categorical | 1,559 unique codes | Product SKU. Prefix encodes category: `FD`=Food, `DR`=Drinks, `NC`=Non-Consumable |
| `Item Type` | Categorical | 16 types | Specific product sub-category (Dairy, Frozen Foods, Snack Foods, etc.) |
| `Item Fat Content` | Categorical | Low Fat · Regular · Non-Edible | Fat classification. Raw dataset contains 5 inconsistent labels; standardised during cleaning |
| `Item Weight` | Numeric | ~4.0 – 22.0 kg | Package weight. **1,463 missing values** — imputed by same-product mean, fallback to Item Type mean |
| `Item Visibility` | Numeric | 0.001 – 0.35 | Fraction of total display area allocated to this product. **526 zero-value rows** treated as missing and imputed by Item_Category median |
| `Outlet Identifier` | Categorical | OUT010 – OUT049 (10 outlets) | Unique store code. Excluded from the benchmark model to avoid identity leakage |
| `Outlet Establishment Year` | Numeric | 1985 – 2022 | Year the outlet was founded. Converted to `Outlet_Age` (see below) |
| `Outlet Size` | Categorical | Small · Medium · High | Physical floor area classification |
| `Outlet Location Type` | Categorical | Tier 1 · Tier 2 · Tier 3 | City tier. Tier 1 = major metropolitan cities |
| `Outlet Type` | Categorical | Grocery Store · Supermarket Type1/2/3 | Retail format. Supermarket Type 3 shows highest volume |
| `Rating` | Numeric | 1.0 – 5.0 | Customer satisfaction score. Dataset mean: 3.97/5 |
| `Sales` | Numeric | ₹31.29 – ₹266.89 | **Target variable** — item-outlet revenue |

### Engineered Features

| Derived Feature | Formula | Rationale |
|---|---|---|
| `Item_Category` | Extracted from `Item Identifier` prefix (`FD`/`DR`/`NC`) | Reduces 1,559-level cardinality to 3 meaningful groups (Food / Drinks / Non-Consumable), eliminating train/test leakage risk |
| `Outlet_Age` | `2026 − Outlet Establishment Year` | Continuous measure of store maturity. Older outlets have established customer bases |

### Data Cleaning Pipeline

Three data-quality issues were systematically resolved before modelling:

1. **Fat Content Label Standardisation** — Five inconsistent labels (`Low Fat`, `low fat`, `LF`, `Regular`, `reg`) mapped to two canonical values. Non-Consumable items reassigned as `Non-Edible`.
2. **Item Weight Imputation** — Same-product mean weight across outlets applied first (a product's physical weight doesn't change by outlet); Item Type mean used as fallback. Zero missing values remain after cleaning.
3. **Item Visibility Zero-Value Correction** — 526 records with `Item Visibility = 0.0` are not physically meaningful for a stocked item. Replaced with the per-`Item_Category` median visibility.

---

## 🔬 EDA Summary & Model Performance

### Tier 1 — Descriptive Analytics (Cohort Baseline)

| Statistic | Value |
|---|---|
| Total Records | 8,523 |
| Total Verified Revenue | ₹1,201,681.49 |
| Mean Sales / Record | ₹140.99 |
| Median Sales / Record | ₹143.01 |
| Std Dev of Sales | ₹62.28 |
| Outlet Type with Most Records | Supermarket Type1 (5,577 records) |
| Dominant Item Category | Food (6,125 records — 71.9%) |

### Tier 2 — Diagnostic Analytics (EDA Findings)

| Chart | Key Diagnostic Finding |
|---|---|
| **Sales Distribution** | Bimodal-like distribution with peaks ~₹100–120 and ~₹170–190; Sales range ₹31–₹267 *(see Screenshot 3)* |
| **Average Sales by Outlet Type** | Remarkably flat across all 4 formats (Supermarket Type2: ₹141.68 vs Grocery Store: ₹140.29 — only 1% spread) |
| **Sales by Location Tier & Outlet Size** | No dominant tier/size interaction; signal distributed thinly across categorical combinations |
| **Average Sales by Item Type** | All 16 item types within a tight ±10% band around the mean — no single category dramatically outperforms |
| **Correlation Heatmap** | Maximum absolute numeric correlation with Sales = 0.026 (Item Weight). No linear predictor is strong in isolation |
| **Total Revenue by Outlet** | Grocery Stores generate ~40% less total revenue — driven by lower item count per outlet, not lower per-item sales |

> **Core diagnostic insight:** The absence of an **Item MRP / price field** in this dataset is the primary constraint on model accuracy. Retail price is universally the dominant sales predictor; without it, predictive signal is thin and distributed across categorical interactions — this is why tree-based ensembles substantially outperform linear models and why R² is moderate rather than high. This limitation is documented transparently in the notebook.

### Tier 3 — Predictive Analytics (Model Benchmark)

All models evaluated with **5-fold cross-validation** on an 80/20 train/test split (Train: 6,818 rows · Test: 1,705 rows). The full preprocessing pipeline (imputation + scaling + one-hot encoding) is fitted only on training folds to guarantee zero leakage.

#### 5-Fold Cross-Validation Results

| Rank | Model | Mean RMSE ↓ | Mean MAE ↓ | Mean R² ↑ |
|:---:|---|:---:|:---:|:---:|
| 🥇 | **Random Forest Regressor** *(selected)* | **38.93** | **29.85** | **0.6064** |
| 🥈 | XGBoost Regressor | 39.50 | 30.08 | 0.5947 |
| 🥉 | Ridge Regression | 61.94 | 52.33 | 0.0038 |
| 4 | Linear Regression | 61.94 | 52.33 | 0.0038 |

**Why tree ensembles win:** The sharp performance cliff between tree-based and linear models confirms that the predictive signal lives in non-linear interactions between outlet type, location tier, item category, and visibility — relationships that linear models cannot represent.

#### Top 12 Feature Importances — Random Forest *(see Screenshot 4)*

| Rank | Feature | Importance Score |
|:---:|---|:---:|
| 1 | `Item Weight` | 0.3464 |
| 2 | `Item Visibility` | 0.2896 |
| 3 | `Rating` | 0.0498 |
| 4 | `Item Fat Content` — Low Fat | 0.0197 |
| 5 | `Item Fat Content` — Regular | 0.0196 |
| 6 | `Item Type` — Frozen Foods | 0.0198 |
| 7 | `Item Type` — Fruits and Vegetables | 0.0202 |
| 8 | `Item Type` — Canned | 0.0186 |
| 9 | `Item Type` — Snack Foods | 0.0188 |
| 10 | `Item Type` — Dairy | 0.0201 |
| 11 | `Outlet_Age` | ~0.013 |
| 12 | `Item Type` — Meat | ~0.011 |

> **Interpretability caveat:** `Item Weight` and `Item Visibility` dominate the importance chart because they are continuous, high-cardinality fields that partially allow the forest to implicitly distinguish individual products — variance reduction, not necessarily causal effect. This is documented in the notebook.

#### Tier 4 — Prescriptive Analytics (Outlet Scorecard)

A separate **peer-benchmark model** (Random Forest, 300 trees, `max_depth=8`) is trained on outlet format attributes only — deliberately excluding `Outlet Identifier` — to estimate what a *typical outlet of this format* should sell. Each store's actual revenue is compared against that peer baseline:

| Outlet | Format | Location | Size | Performance vs Peers |
|---|---|---|---|---|
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

## 🖥️ Interactive Dashboard UI Preview

The Streamlit dashboard features a **dark-themed, wide-layout design** with a fixed sidebar for parameter input and a two-column main area displaying the parsed feature DataFrame alongside live retail strategy insights.

---

### 1 · Dashboard Interface — Default State

The sidebar exposes all 10 model input controls. The main panel renders the parsed input as a live DataFrame (including the derived `Outlet_Age`) so users can verify exactly what the model receives before prediction.

![Dashboard Interface](Screenshots/01_dashboard_interface.png)

*Sidebar controls: Item Category · Item Weight (slider) · Item Fat Content · Item Visibility (slider) · Item Type · Item MRP (reference only, not in model) · Outlet Establishment Year · Outlet Size · Outlet Location Tier · Outlet Type*

---

### 2 · Sales Prediction — Active Result

After clicking **🚀 Predict Expected Sales**, the model loads `models/best_model.pkl`, constructs the feature vector from the sidebar inputs, and renders the predicted revenue in a prominent green success banner.

![Sales Prediction Result](Screenshots/02_sales_prediction.png)

*Example: Baking Goods · 12.5 kg · Low Fat · Visibility 0.06 · Outlet established 1985 (Age: 41) → **Predicted Item Outlet Sales: ₹181.85***

---

### 3 · EDA — Sales Distribution

The notebook's Tier 2 diagnostic analysis includes a histogram with KDE curve showing the distribution of all 8,523 item-outlet sales records, revealing a bimodal-like structure with two broad peaks (₹100–120 and ₹170–190) and a near-uniform plateau between them.

![EDA Sales Distribution](Screenshots/03_eda_distributions.png)

*Sales range: ₹31 – ₹267 · Mean: ₹140.99 · The distribution motivates tree-based models (non-linear decision boundaries) over linear regression*

---

### 4 · Feature Importance — Random Forest (Top 12)

The feature importance analysis from the production Random Forest model confirms that `Item Weight` (0.346) and `Item Visibility` (0.290) are the two strongest individual predictors, together accounting for ~63% of total tree-split information gain.

![Feature Importance](Screenshots/04_feature_importance.png)

*Item Weight and Item Visibility dominate; all categorical features contribute smaller, individually similar importance scores — consistent with the diagnostic finding that signal is distributed across many feature interactions*

---

## 🚀 Local Installation & Execution Guide

### Prerequisites

- Python **3.10 or higher**
- `pip` package manager
- Git

### Step 1 — Clone the Repository

```bash
git clone https://github.com/<your-username>/BlinkIT-Sales-Prediction.git
cd BlinkIT-Sales-Prediction
```

### Step 2 — Create and Activate a Virtual Environment

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

### Step 3 — Install All Dependencies

```bash
pip install -r requirements.txt
```

Full `requirements.txt`:
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

`models/best_model.pkl` is included in the repository. If you want to regenerate it from scratch, run all cells in the notebook:

```bash
jupyter notebook BlinkITSalesPrediction.ipynb
```

The notebook will clean the data, train all four models with 5-fold CV, select the best, and serialise it to `models/best_model.pkl`.

### Step 5 — Launch the Streamlit Dashboard

```bash
streamlit run app.py
```

The app opens automatically at **`http://localhost:8501`**.

### Dashboard Walkthrough

| Step | Action |
|---|---|
| **Configure Product** | Use the sidebar to set **Item Category**, **Item Weight**, **Item Fat Content**, **Item Visibility**, **Item Type**, and **Item MRP** (reference display only — not used by the model) |
| **Configure Outlet** | Set **Outlet Establishment Year**, **Outlet Size**, **Outlet Location Tier**, and **Outlet Type** |
| **Review Inputs** | The **Parsed Input DataFrame** in the main panel shows the exact feature vector — including the derived `Outlet_Age` — that will be passed to the model |
| **Predict** | Click **🚀 Predict Expected Sales** to get the predicted item-outlet revenue (₹) rendered as a green success banner |
| **Interpret** | The **Retail Strategy Insights** panel on the right provides context on how Outlet Type and Item MRP influence sales patterns |

> **Note:** `Item MRP` appears in the sidebar and the display DataFrame for reference, but is accompanied by a clear caption stating it is *not used by the prediction model* (it was not present in the original training data). This ensures the UI is honest about the model's inputs.

---

## 👨‍💻 Author & Contact

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
    <td><strong>Programme</strong></td>
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

*Empowering the next generation of data professionals through hands-on AI/ML practice*

<br/>

<img src="https://img.shields.io/badge/IBM%20SkillsBuild-054ADA?style=flat-square&logo=ibm&logoColor=white" alt="IBM SkillsBuild"/>
&nbsp;
<img src="https://img.shields.io/badge/AICTE-Approved-006400?style=flat-square" alt="AICTE"/>
&nbsp;
<img src="https://img.shields.io/badge/BharatCares-FF6B35?style=flat-square" alt="BharatCares"/>

</div>
