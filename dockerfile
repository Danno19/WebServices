FROM python:3.7.4

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt