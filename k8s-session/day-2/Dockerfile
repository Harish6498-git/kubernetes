# Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY app.py /app/app.py
RUN pip install boto3 requests
CMD ["python3", "app.py"]
