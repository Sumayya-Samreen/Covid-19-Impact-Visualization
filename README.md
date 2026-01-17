# COVID-19 Impact Visualization

This project visualizes the global impact of the COVID-19 pandemic using multiple datasets. The goal is to provide clear insights into infection trends, deaths, recoveries, and human mobility changes during the pandemic. It includes interactive visualizations (locally in Jupyter) and static plots for GitHub.

## Datasets

1. **Global Time-Series Deaths (`time_series_covid19_deaths_global.csv`)** – Daily COVID-19 deaths by country and region.
2. **Global Time-Series Confirmed Cases (`time_series_covid19_confirmed_global.csv`)** – Daily confirmed COVID-19 cases.
3. **Country Summary (`cases_country.csv`)** – Aggregated COVID-19 statistics by country including confirmed, deaths, recovered, active cases, and mortality rate.
4. **Mobility Changes (`changes-visitors-covid.csv`)** – Google mobility trends showing changes in people’s movement across sectors (retail, parks, workplaces, residential, transit).

## Methods and Analysis

The notebook implements the following steps:

1. **Data Loading and Initial Exploration** – Import libraries, load datasets, and inspect structure and types.
2. **Data Cleaning** – Handle missing values via interpolation, drop unnecessary columns, correct country naming inconsistencies.
3. **Exploratory Data Analysis (EDA)** –

   * Global totals: Confirmed, Deaths, Recovered, Active cases
   * Top 10 worst-affected countries
   * Countries with highest recoveries
   * Deaths and mortality rates by country
4. **Visualization Techniques** –

   * **Interactive Plots (local)**: Plotly and Folium for dynamic exploration of global trends and mobility.
   * **Static Plots (for GitHub)**: PNG exports used since GitHub does not render interactive charts.
   * Choropleth maps of mobility trends across Retail, Parks, Workplaces, Grocery, Transit, and Residential categories.
   * Pie charts for country-level distribution of confirmed, deaths, recovered, and active cases.

## Key Findings

* The United States, India, and Brazil were among the worst-affected countries by confirmed cases.
* Recovery trends were highest in India and Brazil during the studied period.
* Mobility changes reflected widespread lockdowns and reductions in workplace and retail activity.
* Interactive visualizations allow exploration of temporal and spatial trends in COVID-19 impact.

## Project Features

* End-to-end data cleaning, preprocessing, and visualization pipeline
* Comparative country-level and global trend analysis
* Interactive and static visualizations for cases, deaths, recoveries, and mobility
* Choropleth maps for visualizing sector-wise mobility changes

## Dependencies

This project requires the following Python libraries:

```text
pandas==2.3.3
numpy==2.3.3
matplotlib==3.10.6
plotly==5.23.1
ipywidgets==8.2.0
folium==0.16.0
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

## How to Run the Notebook

1. Clone this repository

```bash
git clone https://github.com/Sumayya-Samreen/COVID19-Impact-Visualization.git
cd COVID19-Impact-Visualization
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Launch the notebook

```bash
jupyter notebook covid19_impact_visualization.ipynb
```

> **Note:** GitHub does not render interactive charts (Plotly/Folium). Static PNG versions of key plots are provided for preview. For full interactive experience, run the notebook locally.

## Author

**Sumayya Samreen** — M.Sc. in Artificial Intelligence
Passionate about applied AI, data visualization, and real-world insights from complex datasets.