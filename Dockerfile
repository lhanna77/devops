FROM bitnami/spark:latest

WORKDIR /app

# Install Python dependencies (using pip)
COPY requirements.txt .  # Copy the requirements file FIRST
RUN pip install -r requirements.txt

COPY load_data.py .
COPY data/ ./data/

CMD [ "spark-submit", "load_data.py" ]

# CMD ["sh", "-c", "spark-submit load_data.py && python process_data2.py"]