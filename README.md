# Insurance Risk Analytics

## Project Overview

This project analyzes historical auto insurance data to uncover risk patterns, profitability drivers, and customer segments for AlphaCare Insurance Solutions (ACIS). The analysis supports evidence-based decision making for pricing optimization, risk segmentation, and marketing strategy improvement.

The project covers:

- Exploratory Data Analysis (EDA)
- Statistical hypothesis testing
- Data Version Control (DVC)
- Predictive modeling
- Risk-based pricing analytics

---

# Objectives

The main objectives of this project are to:

- Understand insurance risk patterns across customer and vehicle segments
- Analyze profitability using Loss Ratio and Margin metrics
- Identify high-risk and low-risk groups
- Build predictive models for claims and premium optimization
- Develop reproducible and auditable data workflows

---

# Dataset Description

The dataset contains historical insurance records from February 2014 to August 2015.

### Included Information

- Customer demographics
- Vehicle details
- Policy information
- Premium payments
- Claim history

### Key Features

- `TotalPremium`
- `TotalClaims`
- `Province`
- `VehicleType`
- `AutoMake`
- `CustomValueEstimate`
- `TransactionDate`

---

# Derived Metrics

Two important business metrics were created:

## Loss Ratio

:contentReference[oaicite:0]{index=0}

Measures portfolio profitability and insurance risk.

---

## Margin

:contentReference[oaicite:1]{index=1}

Represents the profit contribution per policy.

---

# Exploratory Data Analysis (EDA)

The EDA process included:

- Data summarization and type inspection
- Missing value analysis
- Univariate analysis
- Bivariate and multivariate analysis
- Geographic trend analysis
- Outlier detection

### Key Findings

- The dataset contains no missing values.
- Claim-related variables are highly right-skewed with significant outliers.
- Loss ratios vary across provinces and vehicle categories.
- Certain vehicle makes are associated with higher average claim amounts.
- Temporal trends suggest fluctuations in claim severity over time.

---

# Visualizations

The project includes several business-focused visualizations:

- Loss Ratio by Province
- Premium vs Claims Scatter Plot
- Monthly Claims Trend
- Vehicle Make Risk Comparison
- Correlation Matrix

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy
- Jupyter Notebook
- DVC
- Git & GitHub

CI/CD pipeline implemented using:

:contentReference[oaicite:2]{index=2}

---

# Project Structure

```text
insurance-risk-analytics/
├── .github/
├── data/
├── notebooks/
├── src/
├── tests/
├── reports/
├── requirements.txt
├── README.md
└── .gitignore
```
