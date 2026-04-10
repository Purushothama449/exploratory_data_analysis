# Exploratory Data Analysis on Titanic Dataset

## 📌 Objective
The objective of this project is to analyze and understand the Titanic dataset using statistical methods and visualizations before applying machine learning models.

---

## 🛠 Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📂 Dataset
- Titanic Dataset

---

## ⚙️ Steps Performed
1. Loaded dataset using Pandas
2. Displayed first few rows of data
3. Generated summary statistics (mean, std, min, max)
4. Checked missing values
5. Visualized data using:
   - Histograms (Age, Fare)
   - Boxplots (Outlier detection)
   - Countplot (Survival count)
   - Pairplot (Feature relationships)
   - Heatmap (Correlation matrix)

---

## 📊 Output Visualizations

### Age Distribution
![Age Distribution](graph_output/age_distribution.jpg)

### Fare Distribution
![Fare Distribution](graph_output/fare_distribution.jpg)

### Age Boxplot
![Age Boxplot](graph_output/age_boxplot.jpg)

### Fare Boxplot
![Fare Boxplot](graph_output/fare_boxplot.jpg)

### Survival Count
![Survival Count](graph_output/survival_count.jpg)

### Correlation Matrix
![Correlation Matrix](graph_output/correlation_matrix.jpg)

### Pairplot (Feature Relationships)
![Pairplot](graph_output/pairplot.jpg)

---

## 📊 Key Insights
- Most passengers are between age 20–40
- Age feature contains missing values
- Cabin column has many missing values
- Fare shows high variation and contains outliers
- Age distribution is slightly right-skewed
- Weak correlation between Age, Fare, and Pclass
- Pairplot shows no strong linear relationship between features

---

## 🚀 How to Run
```bash
pip install pandas numpy matplotlib seaborn plotly
python exploratory_data_analysis.py
