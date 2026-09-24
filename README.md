# 🛒 BlinkIT Sales Intelligence Engine & Predictive Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![IBM SkillsBuild / AICTE](https://img.shields.io/badge/IBM_SkillsBuild_AICTE-Internship_Project-blue?style=for-the-badge)

---

## 🚀 Executive Summary

In the fast-paced quick-commerce ecosystem, dark stores serve as the operational backbone for rapid deliveries. Maintaining optimal inventory levels is critical to avoiding stockouts, minimizing waste, and maximizing revenue. 

The **BlinkIT Sales Intelligence Engine** is an end-to-end machine learning solution designed to predict item-level sales performance across different retail outlets. By analyzing historical sales metrics and product characteristics, this tool empowers supply chain managers and retail strategists to make data-driven stocking decisions.

---

## 📊 Dataset & Feature Architecture

This project utilizes a simulated retail dataset modeled after BigMart / BlinkIT grocery sales structures.

* **Source:** [BlinkIT Grocery Data (Kaggle)](https://www.kaggle.com/datasets/brijbhushannanda1979/bigmart-sales-data)

| Feature Category | Attribute Name | Description |
| :--- | :--- | :--- |
| **Product Attributes** | `Item_Identifier` / `Item_Weight` | Unique product ID and physical weight |
| **Categorization** | `Item_Fat_Content` / `Item_Type` | Product diet type (Low Fat/Regular) and category classification |
| **Market Metrics** | `Item_Visibility` / `Item_MRP` | Display area percentage allocation and Maximum Retail Price |
| **Outlet Features** | `Outlet_Identifier` / `Outlet_Establishment_Year` | Unique store identifier and year established |
| **Store Profile** | `Outlet_Size` / `Outlet_Location_Type` / `Outlet_Type` | Physical store size, tier of city location, and store format |
| **Target Variable** | `Item_Outlet_Sales` | **(Target)** Total historical sales value of the product at the specific outlet |

---

## 🏗️ System Workflow & Architecture

```mermaid
graph TD
    A[Raw Data Ingestion] --> B[Data Preprocessing & Cleaning]
    B --> C[Missing Value Imputation & Feature Encoding]
    C --> D[Model Training & 5-Fold Cross-Validation]
    D --> E[Model Serialization Pipeline]
    E -->|best_model.pkl| F[Streamlit Interactive Web UI]
    F --> G[Real-Time Sales Forecasting]
