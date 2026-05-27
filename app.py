import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Weather ETL Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("🌦️ Weather ETL Dashboard")
st.markdown(
    "Real-time weather analytics from Apache Airflow + Apache Spark + PostgreSQL"
)

# -----------------------------
# PostgreSQL Connection
# -----------------------------
engine = create_engine(
    "postgresql://airflow:airflow@postgres:5432/airflow"
)

# -----------------------------
# Load Data Safely
# -----------------------------
try:
    query = """
    SELECT *
    FROM weather_data
    ORDER BY timestamp DESC
    """

    df = pd.read_sql(query, engine)

    if df.empty:
        st.warning("No data found in weather_data table.")
        st.stop()

except Exception as e:
    st.error(f"Database Error: {e}")
    st.stop()

# -----------------------------
# Data Cleaning / Transformation
# -----------------------------
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Lowercase weather text
df['weather'] = df['weather'].str.lower()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Dashboard Filters")

weather_filter = st.sidebar.multiselect(
    "Weather Type",
    options=df['weather'].unique(),
    default=df['weather'].unique()
)

filtered_df = df[df['weather'].isin(weather_filter)]

# -----------------------------
# Metrics Section
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Records",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Average Temperature (°C)",
        round(filtered_df['temperature_celsius'].mean(), 2)
    )

with col3:
    st.metric(
        "Average Humidity (%)",
        round(filtered_df['humidity'].mean(), 2)
    )

# -----------------------------
# Temperature Trend Chart
# -----------------------------
st.subheader("🌡️ Temperature Trend")

fig_temp = px.line(
    filtered_df,
    x='timestamp',
    y='temperature_celsius',
    title='Temperature Over Time',
    markers=True
)

st.plotly_chart(fig_temp, use_container_width=True)

# -----------------------------
# Humidity Trend Chart
# -----------------------------
st.subheader("💧 Humidity Trend")

fig_humidity = px.bar(
    filtered_df,
    x='timestamp',
    y='humidity',
    title='Humidity Over Time'
)

st.plotly_chart(fig_humidity, use_container_width=True)

# -----------------------------
# Weather Distribution Chart
# -----------------------------
st.subheader("☁️ Weather Distribution")

weather_counts = (
    filtered_df['weather']
    .value_counts()
    .reset_index()
)

weather_counts.columns = ['weather', 'count']

fig_weather = px.pie(
    weather_counts,
    names='weather',
    values='count',
    title='Weather Conditions Distribution'
)

st.plotly_chart(fig_weather, use_container_width=True)

# -----------------------------
# Raw Data Table
# -----------------------------
st.subheader("📋 Raw Weather Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)