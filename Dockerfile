FROM bitnami/spark:latest

WORKDIR /app

# Install Python dependencies (using pip)
# Copy the requirements file FIRST
COPY requirements.txt .  
RUN pip install -r requirements.txt

COPY main.py .
COPY data/ ./data/

CMD ["python", "main.py"]

# CMD ["sh", "-c", "spark-submit main.py && load_data_lake.py && python load_dwh_silver.py"]