import os, joblib
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

st.title("Heart Disease Prediction App")

MODELS_DIR = "models"

