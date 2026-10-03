import os, joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from ucimlrepo import fetch_ucirepo

heart_disease = fetch_ucirepo(id=45)

X = heart_disease.data.features
y = heart_disease.data.targets.rename(
    columns={"num":"target"}
    )
y["target"] = (y["target"]>0).astype(int)
print(heart_disease.metadata)

X.isna().sum()

X = X.dropna()

X["thal"] = X["thal"].astype(int)
y = y.loc[X.index]

df = pd.concat([X, y], axis=1)
df.head()

categorical_cols = ["cp", "restecg", "slope", "thal"]
X[categorical_cols] = X[categorical_cols].astype(str)

X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True, dtype=int)

print("Original Feature Shape:", X.shape)
print("Encoded Feature Shape:", X_encoded.shape)
print(X_encoded.head())

from sklearn.preprocessing import OneHotEncoder

continuous_cols = ["age", "trestbps", "chol", "thalach", "oldpeak", "ca"]
binary_cols = ["sex", "fbs", "exang"]

scaler = StandardScaler()
X_encoded[continuous_cols] = scaler.fit_transform(X_encoded[continuous_cols])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), continuous_cols),
        ("cat", OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore"), categorical_cols),
        ("bin", "passthrough", binary_cols)
    ]
)

## Train Test Split and Modeling
X_train, X_test, y_train, y_test = train_test_split(X, y["target"], test_size=0.2, random_state=42)

X_train_preprocessed = preprocessor.fit_transform(X_train)

## Save preprocessor artifacts
MODELS_DIR = os.path.join("..", "models")
os.makedirs(MODELS_DIR, exist_ok=True)
preprocessor_path = os.path.join(MODELS_DIR, "preprocessor.pkl")
joblib.dump(preprocessor, preprocessor_path)
print(f"Preprocessor saved to {preprocessor_path}")

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

from sklearn.model_selection import GridSearchCV

# ---------------------------------------------------------
# 4. Fit and Save Each Model
# ---------------------------------------------------------
for name, mp in model_params.items():
    clf = GridSearchCV(mp["model"], mp["params"], cv=5, scoring="accuracy", n_jobs=-1)
    clf.fit(X_train_preprocessed, y_train)
    
    best_model = clf.best_estimator_
    model_path = os.path.join(MODELS_DIR, f"model_{name}.pkl")
    joblib.dump(best_model, model_path)
    print(f"Saved {name} model to '{model_path}' (CV Accuracy: {clf.best_score_:.4f})")

from sklearn.metrics import confusion_matrix, classification_report

for name in model_params.keys():
    model = joblib.load(os.path.join(MODELS_DIR, f"model_{name}.pkl"))
    y_pred = model.predict(X_test_preprocessed)

    print(f"Model: {name}")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))