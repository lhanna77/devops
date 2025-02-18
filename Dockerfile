FROM bitnami/spark:latest

WORKDIR /app
COPY load_data.py .
COPY data/DimDate_20250201.txt ./data/DimDate_20250201.txt

CMD [ "spark-submit", "load_data.py" ]
