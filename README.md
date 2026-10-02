# Winning Space Race with Data Science

**IBM Data Science Professional Certificate – Applied Data Science Capstone**

**Author:** Pratiksha Parmeshwar Dharne
**Date:** 2 October 2026

---

## 1. Project Overview

SpaceX advertises Falcon 9 launches at about **$62 million**, compared with **$165 million or more** for other providers. Most of the saving comes from reusing the **first stage**, which can land after launch.

In this project I act as a data scientist for a new rocket company (Space Y) that wants to compete with SpaceX. The goal is to **predict whether a Falcon 9 first stage will land successfully**, so the launch cost can be estimated.

## 2. Questions Answered

- Which factors decide whether the first stage lands?
- How do payload, orbit, launch site and flight number affect success?
- Has the landing success rate improved over time?
- Which launch site performs best?
- Which machine learning model predicts the landing outcome most accurately?

## 3. Repository Structure

| File / Folder | Description |
|---|---|
| `jupyter-labs-spacex-data-collection-api.ipynb` | Data collection using the SpaceX REST API |
| `jupyter-labs-webscraping.ipynb` | Web scraping Falcon 9 launch records from Wikipedia |
| `labs-jupyter-spacex-Data wrangling.ipynb` | Data wrangling and creation of the landing `Class` label |
| `edadataviz.ipynb` | EDA with data visualization (Seaborn / Matplotlib) |
| `jupyter-labs-eda-sql-coursera_sqllite.ipynb` | EDA with SQL (SQLite) |
| `lab_jupyter_launch_site_location.ipynb` | Interactive map with Folium |
| `spacex-dash-app.py` | Interactive dashboard with Plotly Dash |
| `SpaceX_Machine Learning Prediction_Part_5.ipynb` | Predictive analysis (classification models) |
| `All Datasets/` | CSV datasets used in the project |
| `my_data1.db` | SQLite database used for the SQL queries |
| `Graphs/` | Screenshots of charts, maps, dashboard and model results |

## 4. Datasets

| File | Content | Size |
|---|---|---|
| `dataset_part_2.csv` | Wrangled launch data with the `Class` label | 90 rows × 18 columns |
| `dataset_part_3.csv` | One-hot encoded features for machine learning | 90 rows × 80 columns |
| `spacex_web_scraped.csv` | Launch records scraped from Wikipedia | 121 rows × 11 columns |
| `spacex_launch_dash.csv` | Data for the Plotly Dash dashboard | 56 rows × 7 columns |

## 5. Methodology

1. **Data collection:** SpaceX REST API calls and Wikipedia web scraping with BeautifulSoup.
2. **Data wrangling:** handled missing values and created a binary `Class` label (1 = landed, 0 = did not land).
3. **EDA:** seven Seaborn charts and ten SQL queries.
4. **Interactive visual analytics:** Folium launch-site map and Plotly Dash dashboard.
5. **Predictive analysis:** Logistic Regression, SVM, Decision Tree and KNN, tuned with `GridSearchCV` (10-fold cross-validation) on an 80/20 train/test split.

## 6. Key Results

- Overall landing success rate: **66.7%** (60 of 90 launches).
- Yearly success rate rose from **0% (2010–2013)** to **84.2% (2020)**, with a peak of 90% in 2019.
- **KSC LC-39A** is the best launch site (about 77% success).
- **SSO** orbit reached 100% success and **VLEO** 85.7%; **GTO** is the hardest at 51.9%.
- Payloads of **2,000–4,000 kg** had the highest success rate in the dashboard data (61.9%).
- Model test accuracy:

| Model | Cross-validation accuracy | Test accuracy |
|---|---|---|
| Logistic Regression | 84.6% | 83.3% |
| SVM | 84.8% | 83.3% |
| Decision Tree | 87.1% | 77.8% |
| KNN | 84.8% | 83.3% |

Logistic Regression, SVM and KNN tie at **83.3%** test accuracy. Logistic Regression was chosen as the best model because it is the simplest. The Decision Tree overfits: it has the best cross-validation score but the lowest test score.

## 7. Technologies Used

Python, Pandas, NumPy, Requests, BeautifulSoup, Matplotlib, Seaborn, SQLite, Folium, Plotly Dash, Scikit-learn, Jupyter Notebook

## 8. How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. Install the libraries:
   ```bash
   pip install pandas numpy requests beautifulsoup4 matplotlib seaborn folium dash plotly scikit-learn jupyter
   ```
3. Open the notebooks with Jupyter Notebook or JupyterLab.
4. Run the dashboard (keep `spacex_launch_dash.csv` in the same folder as the script):
   ```bash
   python spacex-dash-app.py
   ```
   Then open `http://127.0.0.1:8050` in your browser.

> **Note:** Some notebooks were created in the IBM Skills Network Labs environment (they use `piplite` and `js.fetch` to load data). If they do not run locally, run them in that environment or replace those lines with `pd.read_csv("<file>.csv")`.

## 9. Presentation

The final capstone presentation is included in this repository: `Pratiksha_Dharne_SpaceX_Capstone.pptx`.

## 10. Author

**Pratiksha Parmeshwar Dharne**
IBM Data Science Professional Certificate
