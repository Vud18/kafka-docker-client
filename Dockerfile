FROM python:3.11

WORKDIR /app

COPY main.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "/app/main.py"]
