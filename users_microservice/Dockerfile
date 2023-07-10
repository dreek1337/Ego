FROM python:3.10.6
ENV DATABASE_HOST=database
ENV SITE_HOST=0.0.0.0
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
