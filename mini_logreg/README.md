## Mini Logistic Regression Project

In this project, I trained a logistic regression model to classify breast tumors using the scikit-learn breast cancer dataset.

I split the dataset into training and testing sets to check whether the model generalizes well to unseen data. This helps evaluate how well the model performs on new patients.

The model outputs predicted probabilities, which I used to generate an ROC curve.

The AUC value summarizes how well the model separates malignant and benign tumors.
It measures the model's ability to distinguish between classes across all possible thresholds.

For real-world clinical response prediction, external validation datasets and proper confounder control would be necessary.

Top features by |coefficient|: texture error (+), worst concavity (-), mean radius (+), worst symmetry (-), worst compactness (-)

# What I learned today
1. Why use train_test_split?
-> The model could just memorize all training data(overfitting) which may reduce performance on new patients.
2. Why is AUC better than accuracy?
-> Accuracy depends on single threshold(mostly 0.5). In contrast, AUC evaluates the model’s ability to distinguish between classes across all thresholds.
3. What is pandas and why do we use this?
-> A library for working with tabular data (DataFrame), like spreadsheets. It is useful for sorting, filtering, grouping and calculation when analyzing data.

## Background Concept in Korean
1. Logistic regression 직관
- 결과가 0/1일 때 쓰는 모델
- 각 변수는 “확률을 얼마나 올리거나 내리는지” 영향을 준다
- 계수(coefficient)가 +면 확률 ↑, -면 확률 ↓

2. Cancer 
- benign = 양성 종양
- malignant = 악성 종양 (암)
->  0 = benign (암 아님)
    1 = malignant (암)
=> 그래서 우리가 예측한 건:
이 종양이 malignant일 확률; 이미 악성 종양일 확률

3. Concavity : 세포 가장자리의 들어간 정도
- 암세포는 보통 모양이 불규칙적, 울퉁불퉁함, concavity가 큼

4. 과적합(overfitting)
- 직관적 표현: 모델이 데이터를 그냥 외워버린다.

하지만 조금 더 정확히 말하면:
-> 모델이 진짜 질병 패턴(signal) 뿐만 아니라, 우연히 생긴 노이즈(noise)까지 같이 학습해버리는 상태.
=> 일반화(generalization)를 못 하는 문제 발생 가능

5. Regularization
모델이 coefficient를 학습할 때 너무 큰 숫자를 쓰지 못하게 penalty를 주는 것 -> feature selection이 가능해짐
=> 즉; 모델의 복잡도를 인위적으로 제한하는 장치

# Things to think about for building my insight.
1. Why is toy data much easier than real-world clinical prediction?
- Feature dimensionality
- Noise and batch effects
- Confounders
- Class imbalance

# Notes / Limitations
- Coefficient signs/magnitudes can be unstable without feature scaling.
- Highly correlated features (multicollinearity) can lead to counterintuitive coefficients.
- For clinical use, external validation and confounder control are required.

# Next step
- Add feature scaling (StandardScaler) and re-check coefficient stability.