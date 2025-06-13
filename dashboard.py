import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned_successful_education.csv')

st.title("Academic Origins of Successful People")

st.subheader("Degree Distribution")
fig, ax = plt.subplots()
sns.countplot(y='Degree', data=df, order=df['Degree'].value_counts().index, ax=ax)
st.pyplot(fig)

st.subheader("Filter by Profession")
profession = st.selectbox("Choose profession", df['Profession'].unique())
filtered = df[df['Profession'] == profession]
st.write(filtered)    
   