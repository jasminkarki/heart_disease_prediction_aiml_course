# Plot target variable distribution
plt.figure(figsize=(12, 12))

# Age vs Heart Disease
plt.subplot(3, 3, 1)
sns.histplot(x='age', hue='target', data=df, multiple="stack")
plt.title("Age")
plt.xlabel("Age")
plt.ylabel("Count")

# Sex vs Heart Disease
plt.subplot(3, 3, 2)
sns.histplot(x='sex', hue='target', data=df, multiple="stack")
plt.title("Sex")
plt.xlabel("Sex (0: Female, 1: Male)")
plt.ylabel("Count")

# Chest Pain vs Heart Disease
plt.subplot(3, 3, 3)
sns.countplot(x='cp', hue='target', data=df)
plt.title("Chest Pain Type (cp)")
plt.xlabel("Chest Pain Type (1: Typical, 2: Atypical, 3: Non-anginal, 4: Asymptomatic)")
plt.ylabel("Count")

# Fasting Blood Sugar vs Heart Disease
plt.subplot(3, 3, 4)
sns.countplot(x='fbs', hue='target', data=df)
plt.title("Target Distribution (0 = No Disease, 1 = Disease)")
plt.xlabel("Fasting Blood Sugar > 120 mg/dl (0: No, 1: Yes)")
plt.ylabel("Count")

# Resting ECG Type vs Heart Disease
plt.subplot(3, 3, 5)
sns.countplot(x='restecg', hue='target', data=df)
plt.title("Resting ECG (restecg)")
plt.xlabel("Resting ECG (0: Normal, 1: ST-T Wave Abnormality, 2: Left Ventricular Hypertrophy)")
plt.ylabel("Count")

# Exercise-Induced Angina vs Heart Disease
plt.subplot(3, 3, 6)
sns.countplot(x='exang', hue='target', data=df)
plt.title("Exercise-Induced Angina (exang)")
plt.xlabel("Exercise-Induced Angina (0: No, 1: Yes)")
plt.ylabel("Count")

# Slope of Peak exercise ST segment vs Heart Disease
plt.subplot(3, 3, 7)
sns.countplot(x='slope', hue='target', data=df)
plt.title("Slope of Peak exercise ST Segment (slope)")
plt.xlabel("Slope of Peak exercise ST Segment (0: Upsloping, 1: Flat, 2: Downsloping)")
plt.ylabel("Count")

# Number of Major Vessels vs Heart Disease
plt.subplot(3, 3, 8)
sns.countplot(x='ca', hue='target', data=df)
plt.title("Number of Major Vessels (ca)")
plt.xlabel("Number of Major Vessels (0-3)")
plt.ylabel("Count")

# Thal Type vs Heart Disease
plt.subplot(3, 3, 9)
sns.countplot(x='thal', hue='target', data=df)
plt.title("Thal Type (thal)")
plt.xlabel("Thal Type (3: Normal, 6: Fixed Defect, 7: Reversible Defect)")
plt.ylabel("Count")

plt.tight_layout()
plt.show()



## Grid Search for Hyperparameter Tuning
model_params = {
    "logistic_regression": {
        "model": LogisticRegression(max_iter=1000, random_state=42),
        "params": {"C": [0.01, 0.1, 1.0, 10.0], "solver": ["liblinear", "lbfgs"]}
    },
    "knn": {
        "model": KNeighborsClassifier(),
        "params": {"n_neighbors": [3, 5, 7, 9, 11], "weights": ["uniform", "distance"]}
    },
    "decision_tree": {
        "model": DecisionTreeClassifier(random_state=42),
        "params": {"max_depth": [3, 5, 7, 10, None], "criterion": ["gini", "entropy"]}
    },
    "random_forest": {
        "model": RandomForestClassifier(random_state=42),
        "params": {"n_estimators": [50, 100, 200], "max_depth": [3, 5, 10, None]}
    },
    "svm": {
        "model": SVC(probability=True, random_state=42),
        "params": {"C": [0.1, 1, 10], "kernel": ["linear", "rbf"]}
    }
}

# Transform test data using the fitted preprocessor
X_test_preprocessed = preprocessor.transform(X_test)


