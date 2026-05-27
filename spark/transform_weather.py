from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, col

spark = SparkSession.builder \
    .appName("Weather Transformation") \
    .getOrCreate()

df = spark.read.csv(
    "/opt/airflow/data/raw/weather_raw.csv",
    header=True,
    inferSchema=True
)

# Transformations
df_clean = df.withColumn(
    "weather",
    lower(col("weather"))
)

# Convert Kelvin to Celsius
df_clean = df_clean.withColumn(
    "temperature_celsius",
    col("temperature") - 273.15
)

# Remove original temp column
df_clean = df_clean.drop("temperature")

df_clean.show()

df_clean.write.mode("overwrite").csv(
    "/opt/airflow/data/processed/weather_cleaned.csv",
    header=True
)

spark.stop()