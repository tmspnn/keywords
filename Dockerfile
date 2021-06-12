# syntax=docker/dockerfile:1
FROM python:latest

WORKDIR /app
COPY . .
RUN bash install.sh

EXPOSE 8000
CMD ["python", "src/app.py"]
