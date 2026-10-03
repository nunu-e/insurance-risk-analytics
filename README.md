# Insurance Risk Analytics

A Python-based data analysis and machine learning project for exploring insurance risk factors and building predictive models.

## Overview

This project explores insurance-related data through exploratory data analysis, statistical analysis, feature processing, and predictive modeling.

The project also emphasizes reproducibility through version-controlled data workflows and automated testing.

## Objectives

* Explore and understand insurance-related data
* Identify important patterns and relationships
* Perform statistical analysis
* Prepare data for machine learning
* Train predictive models
* Evaluate model performance
* Maintain reproducible data workflows

## Tech Stack

* Python
* Pandas
* NumPy
* SciPy
* scikit-learn
* Jupyter
* DVC
* GitHub Actions
* Pytest

## Project Structure

```text
.
├── .github/
│   └── workflows/
├── notebooks/
├── src/
├── tests/
├── data/
├── README.md
└── ...
```

## Workflow

```text
Raw Data
   |
   v
Data Cleaning
   |
   v
Exploratory Analysis
   |
   v
Feature Processing
   |
   v
Statistical Analysis
   |
   v
Machine Learning
   |
   v
Model Evaluation
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/nunu-e/insurance-risk-analytics.git
cd insurance-risk-analytics
```

Install the project dependencies according to the provided environment configuration.

## Reproducibility

DVC is used to support reproducible data workflows and versioning of data-related artifacts.

## Testing

Run the test suite using:

```bash
pytest
```

## Machine Learning

The project uses scikit-learn for predictive modeling and model evaluation.

Model performance should be interpreted using the evaluation metrics reported in the notebooks and project analysis.

## Future Improvements

* Experiment with additional models
* Improve feature engineering
* Expand model evaluation
* Add model explainability
* Develop a deployable inference service
* Integrate the model into an application

## License

This project is for educational and portfolio purposes.
