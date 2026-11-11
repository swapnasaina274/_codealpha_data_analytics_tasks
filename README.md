# CodeAlpha Data Analytics Virtual Training Tasks

This repository contains the completed projects for the CodeAlpha Data Analytics Internship.

---

## 📁 Repository Structure & Task Overview

### 🔹 Task 1: Web Scraping (`task1_web_scraping/`)
- Developed a Python scraper using `BeautifulSoup` and `requests` to extract job listings.
- Parsed job titles, hiring companies, locations, and posting dates into `scraped_job_data.csv`.

### 🔹 Task 2: Exploratory Data Analysis (`task2_eda/`)
- Conducted data validation, missing value profiling, and duplicate checks using `Pandas`.
- Extracted categorical distributions for top job titles, location hubs, and hiring organizations.

### 🔹 Task 3: Data Visualization & Interactive Dashboard (`task3_data_visualization/`)
- Generated distribution plots, market share pie charts, posting timelines, and heatmaps using `Matplotlib` and `Seaborn`.
- Developed an interactive web app (`app.py`) built with `Streamlit` and `Plotly` featuring dynamic keyword search, company/location multiselect filters, real-time KPI metrics, and filtered CSV downloads.

---

## 🚀 How to Run the Interactive Streamlit Dashboard

1. Clone the repository:
   ```bash
   git clone [https://github.com/swapnasaina274/_codealpha_data_analytics_tasks.git](https://github.com/swapnasaina274/_codealpha_data_analytics_tasks.git)
cd _codealpha_data_analytics_tasks/task3_data_visualization
   ```
2. Install required dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
3. Launch the dashboard:
   ```bash
   streamlit run app.py
   ```
