# Setting before coding:)
# load_breast_cancer loads a public dataset: Wisconsin Diagnostic Breast Cancer dataset (WDBC)
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Bringing the dataset.
## Setting X as data from load_breast_cancer and y as target from load_breast_cancer dataset.
data = load_breast_cancer()
X = data.data
y = data.target

# train/test split
## Reason for doing this?
## -> If we use all data to train the model then model might just memorize training data(overfitting)
## Therefore, we split the data into train(for training) and test(unseen data) to evaluate how well the model works on new patients => This is called "generalization"

## -> It is a function from scikit-learn. 
## It returns 4 outputs, and we assign them using multiple assignment (unpacking). 
## Random_state is a seed that makes the random split reproducible.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Model Training
## It is not a simulation.
## LogisticRegression fits coefficients (weights) for each feature to estimate the probability of class 1(malignant; 악성 종양일 확률). ; 각 feature가 암일 확률을 얼마나 올리거나 내리는가? 결과적으로 이 환자가 암일 확률을 계산함. => 각 feature에 대해 암일 확률을 계산하기 위한 숫자(계수)를 찾아낸다.
### A feature is an input variable (a column in X). e.g. tumor radius, texture, area etc.
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Predicting Probability
## predict() gives only 0 or 1 but predict_proba() gives the actual probability which is needed for ROC curve.
y_prob = model.predict_proba(X_test)[:, 1]

# Calculating ROC curve
## What does ROC and auc mean? Why are they important?
### ROC : A curve plotting True Positive Rate (TPR) vs False Positive Rate (FPR) across thresholds.
### AUC: Summarizes how well the model distinguish between classes. eg. AUC = 1 : Perfect discrimination. AUC = 0.5: Randomly differentiated.
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# Visualization
## Making graphs
plt.figure()
plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title(f"ROC Curve (AUC = {roc_auc:.2f})")
plt.show()

# Checking Coefficients
## Pandas: A library for working with tabular data (DataFrame), like spreadsheets.
### ; 데이터를 표 형태로 다루는 라이브러리(엑셀 같은 테이블 구조를 코드에서 다루게 해줌)
## Useful for sorting, filtering, grouping and calculation
import pandas as pd

# Extract feature names (column names) from the dataset (X 행렬의 각 열이 무엇을 의미하는지 알려주는 리스트)
feature_names = data.feature_names
# model.coef_ is a 2D array; for binary classification it has shape (1, n_features).
# model.coef_[0] extracts the coefficient vector for the single row.
coefficients = model.coef_[0]

# Making a chart by grouping with feature names and coefficient.
coef_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients
})

# Sort by absolute value (절댓값 기준 정렬)
## Convert data into absolute values and then sort them in descending order
coef_df["Abs_Coefficient"] = coef_df["Coefficient"].abs()
coef_df_sorted = coef_df.sort_values(by="Abs_Coefficient", ascending=False)

# Print the top five feature for cancer
print(coef_df_sorted.head(5))