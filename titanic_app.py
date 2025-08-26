import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned data from your notebook
df = pd.read_csv("titanic_clean.csv")

st.title("Titanic Dashboard")

# Example interactive filter
sex = st.selectbox("Select sex:", df['sex'].unique())
filtered = df[df['sex'] == sex]

st.dataframe(filtered.head())

fig, ax = plt.subplots()
sns.histplot(filtered['age'].dropna(), kde=True, ax=ax)
st.pyplot(fig)
