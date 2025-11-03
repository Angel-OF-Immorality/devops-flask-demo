# Builder
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

#Runtime (smaller base image)
FROM python:3.11-slim
WORKDIR /app

#Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
COPY app.py .

#Making sure scripts are in path
ENV PATH = /root/.local/bin:$PATH

CMD ["python", "app.py"]

