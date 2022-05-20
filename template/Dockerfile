FROM python:alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY config.yaml .
COPY main.py .
COPY {{ name }}_bot/ ./{{ name }}_bot

CMD ["python3", "./main.py"]
