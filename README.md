# Heart Disease Prediction: AIML Course

This project was conducted with WHIC BIT students as part of the Capstone Project for the AIML Training Course.

The project uses a heart disease dataset sourced from Kaggle. By the end of the course, participants will develop a heart disease prediction system using machine learning techniques.

## Data Source

The heart disease dataset is sourced from [Kaggle — Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).

From ucimlrepo. `!pip install ucimlrepo` [Link](https://archive.ics.uci.edu/dataset/45/heart+disease)

## Setting Up the Project
1. Create a Virtual Environment
First, install virtualenv:
`pip install virtualenv` or `python -m pip install virtualenv`

Create a virtual environment named venv:

`python -m virtualenv venv`

Activate the virtual environment:

`.\venv\Scripts\Activate.ps1`

**PowerShell Execution Policy Issue**

If you encounter the following error:

`.\venv\Scripts\Activate.ps1 : File ...\Activate.ps1 cannot be loaded because running scripts is disabled on this system.`

You can allow locally created PowerShell scripts by running:

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Then activate the virtual environment again:

`.\venv\Scripts\Activate.ps1`

2. Install the Required Packages

Once the virtual environment is activated, install the project dependencies:

`pip install -r requirements.txt`

3. Configure Git

Before making commits, configure your name and email globally in Git:

```shell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

You can verify your Git configuration with:

`git config --global --list`

## Project Goal

The goal of this capstone project is to apply the concepts learned during the AIML training course to build a machine-learning-based heart disease prediction system, from data preparation and exploratory analysis through model training, evaluation, and prediction.


## Feature Importances
### 🔴 Positive Case (Heart Disease Detected)

| Feature | Value | Clinical Meaning (Context for the Model) |
| :--- | :--- | :--- |
| **`cp`** (Chest Pain) | `4` (Asymptomatic) | Paradoxically, asymptomatic chest pain or atypical angina carries high risk in this specific dataset. |
| **`ca`** (Major Vessels) | `2` or `3` | Multiple vessels are blocked or narrowed under fluoroscopy. |
| **`thal`** (Thalassemia) | `3` (Reversible defect) | Indicates temporary blood flow restriction during exercise. |
| **`oldpeak`** (ST Depression) | `2.5` | Significant ST-segment depression, signaling severe cardiac stress. |
| **`thalach`** (Max Heart Rate) | `115` | Low maximum heart rate achieved during physical exertion. |
| **`age` / `sex`** | `61` / `1` (Male) | Older male demographic, statistically increasing base risk. |

### 🟢 Negative Case (No Heart Disease Detected)

| Feature | Value | Clinical Meaning (Context for the Model) |
| :--- | :--- | :--- |
| **`cp`** (Chest Pain) | `1` or `2` | Typical or atypical chest pain that is less correlated with severe blockages. |
| **`ca`** (Major Vessels) | `0` | No major blood vessels show narrowing or blockages. |
| **`thal`** (Thalassemia) | `2` (Normal) | Blood flow to the heart remains normal and steady. |
| **`oldpeak`** (ST Depression) | `0.0` | No abnormal electrical shifts in the heart during exercise. |
| **`thalach`** (Max Heart Rate) | `170` | Excellent cardiac tolerance; heart rate safely peaks high under stress. |
| **`age` / `sex`** | `41` / `0` (Female) | Younger female demographic, statistically lower risk profile in this cohort. |
