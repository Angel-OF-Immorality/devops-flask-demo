# This is a single stage dockerfile
# It creates a big image, not recommended to use.
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["python", "app.py"]
