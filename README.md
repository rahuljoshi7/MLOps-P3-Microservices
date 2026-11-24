# MLOps P3 - Microservices-Based ML System

## Project Overview
A machine learning application divided into three independent REST API microservices.

## Microservices
1. Preprocessing Service - Handles input data preprocessing.
2. Prediction Service - Loads the trained ML model and generates predictions.
3. Logging Service - Stores application logs.

## Technologies
- Python
- FastAPI
- Scikit-learn
- Docker
- Docker Compose
- Git

## Running the Application
Run all services using:

docker compose up -d --build

## API Documentation
- Preprocessing: http://localhost:8001/docs
- Prediction: http://localhost:8002/docs
- Logging: http://localhost:8003/docs