# Covid-19 Impact Visualization

An interactive Python dashboard for analyzing the global impact of the COVID-19 pandemic. The project collects, cleans, and visualizes COVID-19 case data, deaths, recoveries, and mobility trends, providing actionable insights over time.

## Datasets

1. **Global Time-Series Deaths (`time_series_covid19_deaths_global.csv`)** – Daily COVID-19 deaths by country.
2. **Global Time-Series Confirmed Cases (`time_series_covid19_confirmed_global.csv`)** – Daily confirmed COVID-19 cases.
3. **Country Summary (`cases_country.csv`)** – Aggregated statistics: confirmed, deaths, recovered, active cases, and mortality rate.
4. **Mobility Trends (`changes-visitors-covid.csv`)** – Sector-wise changes in human movement (retail, workplaces, parks, transit, residential).

## Features

* Interactive and static visualizations of confirmed, deaths, recovered, and active cases.
* Choropleth maps showing global mobility changes across multiple sectors.
* Top-10 country rankings for confirmed cases, deaths, recoveries, and mortality rates.
* Dynamic comparison of countries with the highest impact.
* Real-time trend analysis with interactive Plotly and Folium visualizations.
* Full end-to-end data pipeline: cleaning, preprocessing, visualization.

## Methods and Analysis

1. **Data Loading & Exploration** – Inspect datasets, identify missing values, and ensure data consistency.
2. **Data Cleaning** – Handle missing values via interpolation, remove unnecessary columns, and unify country names.
3. **Exploratory Data Analysis (EDA)** – Identify global trends, worst-affected countries, and recovery statistics.
4. **Visualizations** –

   * Choropleth maps for global COVID-19 and mobility patterns.
   * Pie charts for country-level distribution of confirmed, deaths, recovered, and active cases.
   * Interactive dashboards for deeper exploration of trends over time.

## Key Findings

* The United States, India, and Brazil had the highest confirmed cases.
* India and Brazil showed the highest recovery trends during the studied period.
* Mobility data reflected large-scale lockdowns and reductions in retail and workplace activity.
* Interactive visualizations provide valuable insight into temporal and spatial patterns of the pandemic.

## Dependencies

Install dependencies using the provided requirements file:

```bash
pip install -r requirements.txt
```

Contents of **requirements.txt**:

```text
pandas==2.3.3
numpy==2.3.3
matplotlib==3.10.6
plotly==5.23.1
ipywidgets==8.2.0
folium==0.16.0
pycountry==23.12.11
ipython==8.29.0
jupyter==1.1.1
```

## How to Run the Notebook

1. Clone the repository:

```bash
git clone https://github.com/Sumayya-Samreen/COVID19-Impact-Visualization.git
cd COVID19-Impact-Visualization
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the notebook:

```bash
jupyter notebook covid19_impact_visualization.ipynb
```

> **Note**
>
> * GitHub does not render interactive Plotly/Folium charts. Static PNG versions are provided for preview. For full interactivity, run the notebook locally.
> * Make the notebook trusted in Jupyter (File → Trust Notebook) to properly load maps.
> * `clean_widget.py` is included for GitHub deployment previews and modular static visualization. It is not required to run the notebook locally.

## Pro Tip for Recruiters or Collaborators

This project demonstrates a complete data science workflow from raw data collection to interactive visualization. It highlights skills in:

* Python data analysis and visualization
* Pandas, Plotly, Folium, Matplotlib
* Exploratory Data Analysis (EDA)
* Interactive dashboards
* Data-driven decision support

It is a strong portfolio example for roles in **data science, AI engineering, or analytics**.

## Author
**Sumayya Samreen — M.Sc. in Artificial Intelligence**<br>
Passionate about applied AI, interactive data visualization, and deriving insights from complex datasets.