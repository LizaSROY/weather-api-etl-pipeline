# Weather ETL Pipeline with Apache Airflow, Apache Spark, PostgreSQL, and Streamlit

## Project Overview

This project implements an automated end-to-end ETL (Extract, Transform, Load) pipeline for weather data collection and analytics.

The system automatically extracts real-time weather data from the OpenWeather API for Phnom Penh, processes and transforms the data using Apache Spark, stores cleaned data into PostgreSQL, and visualizes results through a Streamlit dashboard.

The workflow orchestration and scheduling are managed by Apache Airflow.

---

## Project Objectives

The objectives of this project are:

- Collect weather data from an external API
- Process and clean data using distributed computing
- Store transformed data into a relational database
- Automate workflow execution using Airflow
- Visualize weather insights through a dashboard
- Build a scalable and containerized ETL architecture

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Apache Airflow | Workflow orchestration and scheduling |
| Apache Spark (PySpark) | Data transformation |
| PostgreSQL | Data storage |
| Streamlit | Dashboard visualization |
| Docker | Containerization |
| Docker Compose | Service orchestration |
| Python | Development language |
| OpenWeather API | Data source |

---

## System Architecture

```text
OpenWeather API
        ↓
Extract Weather Data
        ↓
Raw CSV Storage
        ↓
Apache Spark Transformation
        ↓
Processed CSV
        ↓
PostgreSQL Database
        ↓
Streamlit Dashboard
        ↓
Apache Airflow Scheduling
```

---

## Project Structure

```text
weather_etl_pipeline/

├── dags/
│   └── weather_etl_dag.py
│
├── scripts/
│   ├── extract_weather.py
│   └── load_to_postgres.py
│
├── spark/
│   └── transform_weather.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ETL Workflow

### Step 1: Extract

Weather data is collected from OpenWeather API.

Extracted attributes include:

- city
- temperature
- feels_like
- humidity
- pressure
- wind_speed
- visibility
- cloudiness
- weather
- timestamp

Raw data is stored as:

```text
data/raw/weather_raw.csv
```

---

### Step 2: Transform

Apache Spark performs several transformation tasks:

- Remove missing values
- Standardize weather text to lowercase
- Convert temperature from Kelvin to Celsius
- Convert "feels_like" temperature to Celsius
- Convert timestamp to datetime
- Create weather categories
- Filter invalid values
- Feature engineering

Output generated:

```text
data/processed/weather_cleaned.csv
```

---

### Step 3: Load

The transformed data is loaded into PostgreSQL.

Target table:

```sql
weather_data
```

Data is inserted automatically using SQLAlchemy.

---

## Airflow Workflow (DAG)

The workflow contains three tasks:

```text
extract_weather
        ↓
transform_weather
        ↓
load_postgres
```

Scheduling:

```python
schedule='@hourly'
```

The pipeline automatically executes every hour.

---

## Docker Services

The project contains the following services:

- PostgreSQL
- Spark Master
- Spark Worker
- Airflow Init
- Airflow Webserver
- Airflow Scheduler
- Streamlit Dashboard

---

## Installation

### Clone Repository

```bash
git clone https://github.com/LizaSROY/weather_api_etl_pipeline.git

cd weather_etl_pipeline
```

---

### Create Environment File

Create:

```text
.env
```

Example:

```env
API_KEY=YOUR_OPENWEATHER_API_KEY
```

---

### Build Containers

```bash
docker compose up -d --build
```

---

## Access Services

### Airflow UI

```text
http://localhost:8080
```

Default credentials:

```text
Username: admin
Password: admin
```

---

### Streamlit Dashboard

```text
http://localhost:8501
```

---

### Spark UI

```text
http://localhost:8081
```

---

## Database Schema

Main table:

```sql
weather_data
```

Columns:

| Column |
|----------|
| city |
| humidity |
| weather |
| temperature_celsius |
| feels_like_celsius |
| pressure |
| wind_speed |
| cloudiness |
| visibility |
| weather_category |
| timestamp |

---

## Sample Dashboard Features

The dashboard includes:

- Total weather records
- Average temperature
- Average humidity
- Temperature trend analysis
- Humidity trend analysis
- Weather distribution
- Interactive filtering

---

## Future Improvements

Potential future enhancements:

- Add weather forecasting
- Add anomaly detection
- Add machine learning prediction models
- Deploy on cloud platforms
- Integrate Kafka for real-time streaming
- Add historical analytics dashboard

---


## License

This project is intended for educational and learning purposes.
