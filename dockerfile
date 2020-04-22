FROM python:3.7.4

WORKDIR /service

COPY requirements.txt ./
RUN pip install -r requirements.txt