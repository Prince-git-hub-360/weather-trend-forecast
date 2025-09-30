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


## Workflow / Methodology

### 1. Data Cleaning & Preprocessing
- Dropped duplicates
- Handled missing numeric values with **median per location + month**
- Filled missing categorical values with `"Unknown"`
- Removed extreme outliers using **z-score**
- Interpolated remaining numeric missing values
- Saved cleaned dataset to `data/processed/weather_cleaned.csv`

### 2. Exploratory Data Analysis (EDA)
- Generated **summary statistics** for temperature, precipitation, humidity, wind, and cloud coverage
- Plotted **temperature & precipitation distributions**
- Created **scatter plots** for Temperature vs Humidity
- Seasonal trends: **Monthly average temperature**
- Correlation analysis with **heatmap**

### 3. Forecasting Models
- **RandomForestRegressor** used to predict temperature
- Features: `humidity`, `precip_mm`, `wind_kph`, `cloud`
- Model evaluation metrics:
  - MAE and RMSE
- Feature importance visualized

### 4. Advanced Analysis
- **Anomaly Detection** for temperature using IsolationForest
- Seasonal trends analysis by month
- Top 10 hottest countries visualized
- Identified key patterns across locations

### 5. Results & Recommendations
- Forecasting shows reasonable accuracy; ensemble models recommended for improvement
- Extend analysis to all locations and include environmental factors
- Spatial patterns and GIS visualizations suggested
- Climate and seasonal trends highlighted for key insights

## Figures
All figures are saved in `reports/figures/`:
- `temperature_distribution.png`
- `precipitation_distribution.png`
- `temp_vs_humidity.png`
- `avg_temp_by_month.png`
- `feature_importance.png`
- `actual_vs_predicted.png`
- `temperature_anomalies.png`
- `top_countries_temperature.png`
- `correlation_matrix_summary.png`
- `avg_temp_by_month_summary.png`
- `top_countries_summary.png`


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
