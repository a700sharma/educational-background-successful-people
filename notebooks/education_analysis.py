# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Ensure the folder path exists
os.makedirs('images/visualizations', exist_ok=True)
print("Current Working Directory:", os.getcwd())


# 2. Load Dataset
df = pd.read_csv("data/successful_educations.csv")
print(df.head())
print(df.columns)

# 3. Basic Data Overview
print(df.head())
print(df.info())
print(df.describe())  

# 4. Data Cleaning
df.dropna(subset=['Degree', 'Profession'], inplace=True)
df['Degree'] = df['Degree'].fillna("Unknown")

# 5. EDA - Degree Distribution
plt.figure(figsize=(8,6))
df['Degree'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Distribution of Degrees")
plt.xlabel("Degree")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/visualizations/degree_distribution.png")
plt.close()

# 6. Degree vs Profession
plt.figure(figsize=(10,6))
sns.countplot(y='Profession', hue='Degree', data=df, order=df['Profession'].value_counts().index)
plt.title("Degree by Profession")
plt.tight_layout()
plt.savefig("images/visualizations/degree_by_profession.png")
plt.close()

# 7. Education by Country (if 'Country' exists)
if 'Country' in df.columns:
    plt.figure(figsize=(10,5))
    df['Country'].value_counts().head(10).plot(kind='bar', color='orange')
    plt.title("Top 10 Countries by Education Count")
    plt.tight_layout()
    plt.savefig("images/visualizations/top_countries.png")
    plt.close()

# 8. Export cleaned data
df.to_csv("data/cleaned_successful_education.csv", index=False)

# 9. Final message
print("✅ Analysis complete. Cleaned data and visuals are saved.")