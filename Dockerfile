FROM bitnami/spark:latest

WORKDIR /app

# Install Python dependencies (using pip)
# Copy the requirements file FIRST
COPY requirements.txt .  
RUN pip install -r requirements.txt

COPY main.py .
COPY load_data_lake.py .
COPY load_dwh_silver.py .
COPY load_tests.py .
COPY data/ ./data/
COPY schemas/ ./schemas/

CMD ["sh", "-c", "python main.py && /.local/bin/pytest load_tests.py --junitxml=/app/junit.xml"]

# CMD ["python", "main.py"]
# CMD ["sh", "-c", "spark-submit main.py && load_data_lake.py && python load_dwh_silver.py"]