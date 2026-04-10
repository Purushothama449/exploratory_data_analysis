import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

print("First 5 rows:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

sns.histplot(df['Age'].dropna(), kde=True)
plt.title("Age Distribution")
plt.show()

sns.histplot(df['Fare'], kde=True)
plt.title("Fare Distribution")
plt.show()

sns.boxplot(x=df['Age'])
plt.title("Age Boxplot")
plt.show()

sns.boxplot(x=df['Fare'])
plt.title("Fare Boxplot")
plt.show()

sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

sns.pairplot(df[['Age', 'Fare', 'Pclass']])
plt.show()

corr = df[['Age', 'Fare', 'Pclass']].corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Matrix")
plt.show()

sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

sns.heatmap(df[['Age','Fare','Pclass']].corr(), annot=True)
plt.title("Correlation Matrix")
plt.show()