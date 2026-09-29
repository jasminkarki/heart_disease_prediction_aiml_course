# Heart Disease Prediction — AIML Course

This project was conducted with WHIC BIT students as part of the Capstone Project for the AIML Training Course.

The project uses a heart disease dataset sourced from Kaggle. By the end of the course, participants will develop a heart disease prediction system using machine learning techniques.

## Data Source

The heart disease dataset is sourced from Kaggle: [Kaggle — Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

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