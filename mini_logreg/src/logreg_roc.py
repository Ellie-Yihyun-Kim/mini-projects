# Setting before coding:)
# load_breast_cancer loads a public dataset: Wisconsin Diagnostic Breast Cancer dataset (WDBC)
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import pandas as pd

# --- Load Dataset ---
# Load the Wisconsin Diagnostic Breast Cancer dataset.
# X contains tumor features, and y contains class labels.
# Class 0 = malignant, Class 1 = benign.
data = load_breast_cancer()
X = data.data
y = data.target

# --- Train/Test Split ---
# Split the data into training (70%) and testing (30%) sets.
# The test set evaluates performance on unseen data.
# random_state ensures the split is reproducible.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# --- Model Training ---
# LogisticRegression learns coefficients (weights)
# for each feature to estimate the probability of class 1 (benign).
# Class 0 = malignant (악성 종양)
# Class 1 = benign (양성 종양)
#
# A feature is an input variable (a column in X),
# such as tumor radius, texture, or area.
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# --- Predict Probabilities ---
# predict_proba() returns probabilities for both classes.
# [:, 1] selects the probability of class 1 (benign).
y_prob = model.predict_proba(X_test)[:, 1]

# --- ROC Curve and AUC ---
# ROC plots the true positive rate against the false
# positive rate across different classification thresholds.
# AUC measures how well the model distinguishes the classes.
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
print(f"ROC AUC: {roc_auc:.6f}")

# --- Visualization ---
# Making graphs
plt.figure()
plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title(f"ROC Curve (AUC = {roc_auc:.2f})")
plt.show()

# --- Feature Coefficients ---
# Extract feature names and their corresponding coefficients.
feature_names = data.feature_names
coefficients = model.coef_[0]

# Create a DataFrame containing features and coefficients.
coef_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients
})

# Sort coefficients by absolute magnitude.
# Note: Magnitudes are not directly comparable without
# accounting for feature scaling and correlation.
coef_df["Abs_Coefficient"] = coef_df["Coefficient"].abs()
coef_df_sorted = coef_df.sort_values(by="Abs_Coefficient", ascending=False)

# Display the five largest absolute coefficients.
print(coef_df_sorted.head(5))