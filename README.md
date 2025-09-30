# Weather Trend Forecasting Project

## **Project Overview**
This project performs **weather trend forecasting** using a global weather dataset. It covers data cleaning, exploratory data analysis, forecasting with machine learning models, and advanced analysis such as anomaly detection and spatial trends.

**Objective:**  
- Analyze global weather data  
- Forecast temperature and other weather parameters  
- Visualize trends and insights across countries  
- Demonstrate data science and machine learning skills

---

## **Dataset**
- Source: [Global Weather Repository on Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository/code)  
- Description: Daily weather information for cities worldwide.  
- Features: 40+ features including temperature, humidity, wind, precipitation, air quality, and more.

**File structure for data:**
data/
├─ raw/ # Raw CSV data (not included in GitHub)
└─ processed/ # Cleaned and preprocessed data (optional)

---

##  **Project Structure**
weather-trend-forecast/
│
├─ data/ # Raw and processed data
├─ notebooks/ # Step-by-step Jupyter notebooks
│ ├─ 01_data_overview.ipynb
│ ├─ 02_data_cleaning.ipynb
│ ├─ 03_eda_visualization.ipynb
│ ├─ 04_forecasting_models.ipynb
│ ├─ 05_advanced_analysis.ipynb
│ └─ 06_results_summary.ipynb
├─ src/ # Python modules for reusable functions
│ ├─ init.py
│ ├─ data_loader.py
│ └─ preprocess.py
├─ README.md # Project documentation
└─ requirements.txt # Python dependencies

---


---

## **Methodology**

### **1. Data Loading**
- Loaded the dataset using `pandas`  
- Converted `last_updated` column to datetime  
- Ensured essential columns exist (location_name, country)

### **2. Data Cleaning**
- Removed duplicates  
- Handled missing values:
  - Numeric: filled per location and month median
  - Categorical: filled with `"Unknown"`  
- Removed extreme outliers using Z-score  
- Interpolated remaining missing values  

### **3. Exploratory Data Analysis (EDA)**
- Analyzed trends and seasonal patterns  
- Visualized:
  - Temperature and precipitation over time  
  - Correlation between weather features  
  - Geographical differences across countries  

### **4. Forecasting Models**
- Built regression models using **scikit-learn**:  
  - Linear Regression  
  - Random Forest  
  - Gradient Boosting  
- Evaluated using MAE and RMSE  
- Selected best-performing model for prediction  

### **5. Advanced Analysis**
- Detected anomalies in weather patterns  
- Analyzed feature importance  
- Explored climate patterns across regions  
- Optional: spatial and environmental impact analysis  

---

## **Results**
- Cleaned dataset saved to `data/processed/weather_cleaned.csv`  
- Forecast plots saved in `reports/figures/`  
- Notebooks show step-by-step workflow from data cleaning to modeling and results  
- Key insights:
  - Seasonal temperature trends per country  
  - Top features affecting weather parameters  
  - Detected outliers and unusual events  

---

## **How to Run**

1. Clone the repository:  
```bash
git clone https://github.com/Prince-git-hub-360/weather-trend-forecast.git
```
2. Install dependencies:
```bash 
pip install -r requirements.txt
```
3. Open notebooks in order (01 → 06) and run step by step in Jupyter Notebook or VS Code.

## Contact

- **GitHub:** [https://github.com/Prince-git-hub-360](https://github.com/Prince-git-hub-360)  
- **Email:** kumariafprinnce@gmail.com
- **LinkedIn:** [https://www.linkedin.com/in/prince-kumar](https://www.linkedin.com/in/prince-kumar-576544374/) 
