import streamlit as st
import pandas as pd
import plotly.express as px

# Title and Introduction
st.title("📊 Interactive Data Storyteller")
st.markdown("""
Welcome to the Interactive Data Storyteller!  
Explore trends, patterns, and insights through interactive visualizations and narrative storytelling.
""")

# Load Sample Dataset
@st.cache_data
def load_data():
    return px.data.gapminder()

df = load_data()

# Sidebar for user input
st.sidebar.header("Filter Options")
year = st.sidebar.slider("Select Year", int(df['year'].min()), int(df['year'].max()), 2007)
continent = st.sidebar.multiselect("Select Continents", df['continent'].unique(), default=list(df['continent'].unique()))

# Filter data
filtered_df = df[(df['year'] == year) & (df['continent'].isin(continent))]

# Narrative Section
st.subheader(f"🌍 Global Development in {year}")
st.markdown(f"""
In {year}, countries across {', '.join(continent)} showed diverse trends in life expectancy and GDP per capita.  
Use the chart below to explore how population size, economic output, and health outcomes relate.
""")

# Interactive Bubble Chart
fig = px.scatter(
    filtered_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title=f"Life Expectancy vs GDP per Capita ({year})"
)
st.plotly_chart(fig, use_container_width=True)

# Optional: Add a time-series line chart
country = st.selectbox("Select a country to view its development over time", df['country'].unique())
country_data = df[df['country'] == country]

st.subheader(f"📈 {country}'s Development Over Time")
fig2 = px.line(country_data, x="year", y="lifeExp", title=f"Life Expectancy in {country} Over Time")
st.plotly_chart(fig2, use_container_width=True)
