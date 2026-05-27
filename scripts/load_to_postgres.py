import pandas as pd
import glob
from sqlalchemy import create_engine

def load_data():

    engine = create_engine(
        "postgresql://airflow:airflow@postgres:5432/airflow"
    )

    files = glob.glob(
        "/opt/airflow/data/processed/weather_cleaned.csv/part-*.csv"
    )

    if not files:
        raise FileNotFoundError("No processed CSV files found.")

    df = pd.read_csv(files[0])

    df.to_sql(
        "weather_data",
        engine,
        if_exists="append",
        index=False
    )

    print("Data loaded into PostgreSQL.")