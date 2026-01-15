# %% [markdown]
# # <center>**Covid-19 and it's Effects**</center>
# 

# %% [markdown]
# ## **Content:**
# 
# 
# 
# 
# > 1. Importing necessary libraries
# 
# > 2. Loading the dataset
# 
# > 3. Basic information about the data
# 
# > 4. Data cleaning
# 
# > 5. Data Visualisation
# 
# 
# 
# 
# 
# 
# 
# 
# 

# %% [markdown]
# #1. Importing necessary libraries

# %%
from IPython.core.display import display, HTML
import plotly.express as px
from ipywidgets import interact
import numpy as np
import folium
from plotly.offline import download_plotlyjs, iplot, init_notebook_mode
import plotly.graph_objects as go
import plotly
import pandas as pd
import ipywidgets as widgets

# %% [markdown]
# #2. Loading the dataset
# 

# %%
from google.colab import drive
drive.mount("/content/drive")

# %%
death=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/DV/Files/Project/time_series_covid19_deaths_global.csv")
confirmed=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/DV/Files/Project/time_series_covid19_confirmed_global.csv")
country=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/DV/Files/Project/cases_country.csv")
df=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/DV/Files/Project/changes-visitors-covid.csv")

# %% [markdown]
# #3. Basic information about the data
# 

# %%
print(death.shape)
print(death.dtypes)
print(death.head())

# %%
print(confirmed.shape)
print(confirmed.dtypes)
print(confirmed.head())

# %%
print(country.shape)
print(country.dtypes)
print(country.head())

# %%
print(df.shape)
print(df.dtypes)
print(df.head())

# %%
death.isnull().sum()

# %%
country.isnull().sum()

# %%
confirmed.isnull().sum()

# %%
df.isnull().sum()

# %% [markdown]
# #4. Data Cleaning
# 

# %%
country.drop("People_Tested", inplace=True, axis=1)

# %%
country.drop("People_Hospitalized", inplace=True, axis=1)

# %%
country.drop("ISO3", inplace=True, axis=1)

# %%
country.head()

# %%
country.isnull().sum()

# %%
is_NaN = country.isnull()
col_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = country[col_has_NaN]
rows_with_NaN

# %%
country[country["Deaths"]==1274.0]

# %%
country.drop([48,104],inplace=True)

# %%
country.interpolate(inplace=True)

# %%
country.isnull().sum()

# %%
death.drop("Province/State", inplace=True, axis=1)

# %%
death['Long'] = death['Long'].replace(np.nan, 106.3468)
death['Lat'] = death['Lat'].replace(np.nan, 56.1304)

# %%
death.isnull().sum()

# %%
is_NaN = death.isnull()
col_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = death[col_has_NaN]
rows_with_NaN

# %%
confirmed.drop("Province/State", inplace=True, axis=1)

# %%
is_NaN = confirmed.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = confirmed[row_has_NaN]
rows_with_NaN

# %%
confirmed['Long'] = confirmed['Long'].replace(np.nan, 106.3468)
confirmed['Lat'] = confirmed['Lat'].replace(np.nan, 56.1304)

# %%
confirmed.isnull().sum()

# %%
country.isnull().sum()

# %%
df.interpolate(inplace=True)

# %%
df.isnull().sum()

# %% [markdown]
# #5. Data Visualisation
# 

# %% [markdown]
# ##5.1 Total Numbers
# 

# %%
confirmed_total = int(country['Confirmed'].sum())
deaths_total = int(country['Deaths'].sum())
recovered_total = int(country['Recovered'].sum())
active_total = int(country['Active'].sum())

# %%
country.head()

# %%
display(HTML("<div style = 'background-color: #504e4e; padding: 20px ; border:solid 2px #414441; box-shadow:0px 2px 2px 0px #888888'>" +
             "<span style='color: #fff; font-size:25px; font-family: monospace;'> Confirmed: "  + str(confirmed_total) +"</span>" +
             "<span style='color: #E84418; font-size:25px; font-family: monospace; margin-left: 20px;'> Deaths: " + str(deaths_total) + "</span>"+
             "<span style='color: #18E703; font-size:25px;  font-family: monospace; margin-left: 20px;'> Recovered: " + str(recovered_total) + "</span>"+
             "<span style='color: red; font-size:25px;  font-family: monospace; margin-left: 20px;'> Active: " + str(active_total) + "</span>"+
             "</div>")
       )

# %% [markdown]
# ## 5.2 Top 10 worst affected countries
# 

# %%
sorted_country = country.sort_values('Confirmed', ascending= False)

# %%
sorted_country.head()

# %%
px.bar(
    sorted_country.head(10),
    x = "Country_Region",
    y = "Confirmed",
    title= "Top 10 worst affected countries", # the axis names
    color_discrete_sequence=["Red"],
    height=500,
    width=1000
)

# %% [markdown]
# ## 5.3 Countries with highest recovery
# 

# %%
sorted_country_rec = country.sort_values('Recovered', ascending= False)

# %%
sorted_country_rec.head()

# %%
def rec(n):
    fig=px.scatter(
      sorted_country_rec.head(n),
      x = "Country_Region",
      y = "Recovered",
      size_max=50,
      size="Recovered",
      color="Country_Region",
      hover_name="Country_Region",

  )
    fig.update_layout(
        title= "Countries with highest recovery",
        height=500,
        width=1000,
    )
    fig.show()
interact(rec, n=10)

# %% [markdown]
# ##5.4 Death and death rates
# 

# %%
sorted_country_deaths = country.sort_values('Deaths', ascending= False)

# %%
sorted_country_deaths.head()

# %%
from folium.plugins import MarkerCluster
world_map2 = folium.Map(location=[11,0], zoom_start=2,tiles='Stamen Terrain', max_zoom =20, min_zoom = 2)

mc = MarkerCluster()
for i in range(len(confirmed)):
  folium.Marker(
        location=[confirmed.iloc[i]['Lat'], confirmed.iloc[i]['Long']],
        popup=str(confirmed.iloc[i]["Country/Region"]),
        tooltip = "<div style='margin: 0px; background-color: gray; color:white;'>"+
                    "<h4 style='text-align:center;font-weight: bold'>"+confirmed.iloc[i]['Country/Region'] + "</h4>"
                    "<hr style='margin:10px;color: white;'>"+
                    "<ul style='color: white;;list-style-type:circle;align-item:left;padding-left:20px;padding-right:20px'>"+

                        "<li>Deaths:   "+str(death.iloc[i,-1])+"</li>"+
                        "<li>Death Rate: "+ str(np.round(death.iloc[i,-1]/(confirmed.iloc[i,-1]+1.00001)*100,2))+ "</li>"+
                    "</ul></div>",
    ).add_to(mc)

world_map2.add_child(mc)

# %% [markdown]
# ##5.5 Total Active, Recovered, Confirmed, Deaths country wise
# 

# %%
country_copy=country.copy(deep=True)
country_copy.set_index("Country_Region", inplace =True)
# country_name=input("Enter country:")
def pie(country_name):
  country_l=country_copy.loc[country_name]
  a=country_l["Confirmed":"Active"]
  a
  b=["Confirmed","Deaths","Recovered","Active"]

  fig = px.pie(values=a, color_discrete_sequence=px.colors.sequential.RdBu, names=b)
  fig.update_traces(textposition='inside', textinfo='label+percent+value',marker=dict(line=dict(color='#000000', width=2)))
  # fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
  return fig.show()

# %%
country_copy.index.unique()

# %%
interact(pie, country_name="India");

# %%
df.head()

# %% [markdown]
# ##5.6 Movement of people during pandemic in different sectors country-wise
# 
# 

# %%
def countr(count):
    country_retail=[]
    country_grocery=[]
    country_parks=[]
    country_transit=[]
    country_work=[]
    country_residential=[]
    DATE=[]
    for i, j in df.iterrows():
        if j['Entity']==count:
            country_retail.append(j["retail_and_recreation"])
            country_grocery.append(j["grocery_and_pharmacy"])
            country_parks.append(j["parks"])
            country_transit.append(j["transit_stations"])
            country_work.append(j["workplaces"])
            country_residential.append(j["residential"])
            DATE.append(j["Date"])
    # from plotly.offline import download_plotlyjs, iplot, init_notebook_mode
    import plotly.graph_objects as go
    import plotly
    one=go.Scatter(
        x=DATE,
        y=country_parks,
        name="Parks",
        opacity=0.8,
        line=dict(color="blue")
    )
    two=go.Scatter(
        x=DATE,
        y=country_retail,
        name="Retail",
        opacity=0.8,
        line=dict(color="green")
    )


    three=go.Scatter(
        x=DATE,
        y=country_grocery,
        name="Grocery",
        opacity=0.8,
        line=dict(color="red")
    )
    four=go.Scatter(
        x=DATE,
        y=country_residential,
        name="Residential",
        opacity=1,
        line=dict(color="darkviolet")
    )
    five=go.Scatter(
        x=DATE,
        y=country_transit,
        name="Transit",
        opacity=0.8,
        line=dict(color="deeppink")
    )
    six=go.Scatter(
        x=DATE,
        y=country_work,
        name="Work",
        opacity=1,
        line=dict(color="chocolate")
    )
    data=[one,two,three,four,five,six]
    layout=dict(
        title="Movement change:"+count,

    )
    fig = go.Figure(
        data=data,
        layout=layout,
    )
    fig.update_layout(
        width=1000,
        height=500,
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    return fig.show()


# %%
interact(countr, count="India");

# %% [markdown]
# ###5.6.1 Movement in Retail & Recreation
# 

# %%
fig=px.choropleth(df,
                   locations="Entity",
                   locationmode="country names",
                   color="retail_and_recreation",
                   animation_frame="Date",
                   color_continuous_scale="Viridis"
                   )
fig.update_layout(title="Change in Retail & Recreation Globally")
fig.show()

# %% [markdown]
# ###5.6.2 Movement in Parks
# 

# %%
fig=px.choropleth(df,
                   locations="Entity",
                   locationmode="country names",
                   color="parks",
                   animation_frame="Date",
                  color_continuous_scale="solar"
                   )
fig.update_layout(title="Change in movement in Parks Globally")
fig.show()

# %% [markdown]
# ###5.6.3 Movement in Grocery & Pharmacy

# %%
fig=px.choropleth(df,
                   locations="Entity",
                   locationmode="country names",
                   color="grocery_and_pharmacy",
                   animation_frame="Date",
                  color_continuous_scale="deep"
                   )
fig.update_layout(title="Change in Grocery & Pharmacy Globally")
fig.show()


# %% [markdown]
# ###5.6.3 Movement in Workplaces

# %%
fig=px.choropleth(df,
                   locations="Entity",
                   locationmode="country names",
                   color="workplaces",
                   animation_frame="Date",
                  color_continuous_scale="delta"
                   )
fig.update_layout(title="Change in Workplaces Globally")
fig.show()

# %% [markdown]
# # **END**


