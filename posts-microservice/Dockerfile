FROM python:3.11
ENV SITE_HOST=0.0.0.0
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
