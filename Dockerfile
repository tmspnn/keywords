# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt

EXPOSE 8000
CMD ["python3", "src/app.py"]
