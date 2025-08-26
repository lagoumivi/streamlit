import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic_clean.csv")

st.title("Titanic Dashboard")

# Sidebar filters
sex = st.sidebar.selectbox("Select sex:", df['sex'].unique())
pclass = st.sidebar.selectbox("Select class:", sorted(df['pclass'].unique()))

filtered = df[(df['sex'] == sex) & (df['pclass'] == pclass)]

# Columns for plots
col1, col2 = st.columns(2)

with col1:
    st.subheader("Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered['age'].dropna(), kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Fare Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered['fare'], kde=True, ax=ax)
    st.pyplot(fig)

# Table at the bottom
st.subheader("Data Preview")
st.dataframe(filtered.head())
