FROM bitnami/spark:latest

WORKDIR /app

# Install Python dependencies (using pip)
# Copy the requirements file FIRST
COPY requirements.txt .  
RUN pip install -r requirements.txt

COPY load_data_lake.py .
COPY data/ ./data/

# CMD [ "spark-submit", "load_data_lake.py" ]

CMD ["sh", "-c", "spark-submit load_data_lake.py && python load_dwh_silver.py"]