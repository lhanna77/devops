FROM bitnami/spark:latest

WORKDIR /app
COPY load_data.py .
COPY data/ ./data/

CMD [ "spark-submit", "load_data.py" ]
