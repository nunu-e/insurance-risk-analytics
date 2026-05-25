# Insurance Risk Analytics

## Project Overview

This project analyzes historical auto insurance data to uncover risk patterns, profitability drivers, and customer segments for AlphaCare Insurance Solutions (ACIS).

The objective is to support evidence-based decision-making for:

- Risk-based pricing
- Customer segmentation
- Marketing optimization
- Profitability improvement

The project follows a full data science pipeline including:

- Exploratory Data Analysis (EDA)
- Statistical hypothesis testing
- Data Version Control (DVC)
- Predictive modeling
- Risk-based pricing framework

---

# Objectives

The main objectives of this project are to:

- Understand insurance risk patterns across customer, vehicle, and geographic segments
- Analyze profitability using **Loss Ratio** and **Margin**
- Identify high-risk and low-risk customer groups
- Statistically validate risk differences across segments
- Build predictive models for claims and pricing optimization
- Ensure reproducible and auditable data workflows using DVC

---

# Dataset Description

The dataset contains historical insurance records from **February 2014 to August 2015**, including policy-level, customer-level, and vehicle-level information.

### Included Information

- Customer demographics
- Vehicle characteristics
- Policy and coverage details
- Premium payments
- Claim history

### Key Features

- `TotalPremium`
- `TotalClaims`
- `Province`
- `VehicleType`
- `Make`
- `Model`
- `CustomValueEstimate`
- `TransactionMonth`

---

# Derived Business Metrics

Two key actuarial metrics were engineered:

## 🔹 Loss Ratio

:contentReference[oaicite:0]{index=0}

Measures portfolio profitability and insurance risk exposure.

---

## 🔹 Margin

:contentReference[oaicite:1]{index=1}

Represents the profit contribution per policy.

---

# Exploratory Data Analysis (EDA)

The EDA process included:

- Data summarization and data type validation
- Missing value analysis and handling strategy
- Univariate analysis (distributions of key variables)
- Bivariate and multivariate analysis
- Geographic risk analysis
- Outlier detection using boxplots

---

## Key Insights

- The dataset has **low missing value rates**, indicating high data quality.
- Claim-related variables are **highly right-skewed**, indicating presence of extreme claims.
- Loss ratios vary significantly across:
  - Provinces
  - Vehicle types
- Certain vehicle makes/models are associated with higher claim severity.
- Temporal trends show fluctuations in claim behavior over the observed period.

---

# Visualizations

The project includes the following key visualizations:

- Loss Ratio by Province
- Premium vs Claims Scatter Plot
- Monthly Claims Trend Analysis
- Vehicle Make Risk Comparison
- Correlation Heatmap of Financial Variables

These visualizations provide insights into risk distribution and profitability drivers.

---

# Data Version Control (DVC)

This project uses **DVC (Data Version Control)** to ensure reproducibility and auditability of datasets.

### Features:

- Raw dataset versioning
- Cleaned dataset tracking
- External storage remote setup
- Reproducible pipeline for data loading

### Reproducibility:

To reproduce the dataset:

```bash
dvc pull
```
