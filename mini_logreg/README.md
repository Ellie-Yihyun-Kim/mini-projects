# Mini Logistic Regression Project

## Overview

This project explores how logistic regression can be used to classify breast tumors using the Wisconsin Diagnostic Breast Cancer dataset from scikit-learn.

The goal was to understand the basic machine learning workflow and how statistical models can be applied to biological data.

## Methods

- **Dataset:** Wisconsin Diagnostic Breast Cancer (WDBC)
- **Model:** Logistic Regression (scikit-learn)
- **Train/test split:** 70% training, 30% testing
- **Evaluation:** ROC curve and Area Under the Curve (AUC)
- **Feature analysis:** Examination of model coefficients

The dataset uses the following class labels:

- `0 = malignant` (악성 종양)
- `1 = benign` (양성 종양)

The model uses `predict_proba(X_test)[:, 1]` to estimate the probability of a tumor being benign.

## Results

The logistic regression model achieved an ROC AUC of approximately 1.00 on the test set, rounded to two decimal places.

The ROC curve evaluates how well the model distinguishes benign from malignant tumors across different classification thresholds, treating benign as the positive class.

The five features with the largest absolute coefficients were:

1. Texture error (+)
2. Worst concavity (-)
3. Mean radius (+)
4. Worst symmetry (-)
5. Worst compactness (-)

These coefficients describe the fitted model but should not be interpreted as direct measures of biological importance.

## What I Learned

**1. Why use a train/test split?**

Training and testing on the same data can produce overly optimistic performance estimates. Using a separate test set helps evaluate how well a model generalizes to unseen observations.

**2. Why use ROC AUC instead of accuracy alone?**

Accuracy evaluates predictions at a particular classification threshold, while ROC AUC summarizes how well the model ranks the positive class above the negative class across thresholds.

**3. Why use pandas?**

Pandas provides DataFrames for organizing, sorting, filtering, and analyzing tabular data. In this project, I used pandas to organize and compare model coefficients.

## Background Concepts (Korean Notes)

### 1. Logistic Regression

Logistic Regression은 두 클래스를 구분하는 데 사용할 수 있는 분류 모델입니다.

- 각 feature에 대한 coefficient(계수)를 학습합니다.
- 계수가 양수이면 다른 조건이 같을 때 class 1의 log-odds가 증가합니다.
- 계수가 음수이면 class 1의 log-odds가 감소합니다.
- 이 프로젝트에서 class 1은 benign(양성 종양)입니다.

### 2. Concavity

Concavity는 종양 세포핵 윤곽에서 오목한 부분의 정도를 나타내는 특징입니다.

### 3. Overfitting

과적합은 모델이 실제 패턴뿐 아니라 학습 데이터에만 존재하는 우연한 노이즈까지 학습하여 새로운 데이터에 대한 성능이 저하될 수 있는 현상입니다.

### 4. Regularization

Regularization은 모델의 계수에 제약을 주어 과도하게 복잡한 모델을 방지하는 방법입니다.

- 큰 계수에 penalty를 부여합니다.
- 일반화 성능을 개선하는 데 도움이 될 수 있습니다.
- L1 regularization은 일부 계수를 0으로 만들어 feature selection에 활용될 수 있습니다.
- L2 regularization은 일반적으로 계수를 줄이지만 자동으로 feature selection을 수행하지는 않습니다.

## Limitations

- Feature scaling was not applied, so coefficient magnitudes should not be directly compared as measures of feature importance.
- Correlated features may lead to unstable or counterintuitive coefficients.
- Performance was evaluated using a single random train/test split.
- A high AUC on this dataset does not establish clinical validity.
- Clinical applications would require external validation and careful consideration of confounding factors and dataset differences.

## Next Steps

- Apply `StandardScaler` and re-evaluate model performance.
- Examine coefficient stability after feature scaling.
- Explore cross-validation to assess performance across different data splits.