# HuggingFace Sentiment Analysis API

This project provides a containerized REST API for serving HuggingFace models with support for concurrent inference using FastAPI and Gunicorn.

---

## Features

- Scalable inference with Uvicorn workers via Gunicorn
- Based on `distilbert-base-uncased-finetuned-sst-2-english`
- Fast startup and low latency
- Dockerized for easy deployment
- Parallel request demo via Jupyter Notebook

---

## Model Justification

Selected the `distilbert-base-uncased-finetuned-sst-2-english` model due to its balance of performance and speed. It supports accurate sentiment classification while maintaining lightweight resource usage, ideal for real-time inference services.

---

##  Setup

### 🔧Build Docker Image

```bash
docker build -t huggingface-inference-api .
```
###  Run Docker Container

```bash
docker run -p 8000:8000 huggingface-inference-api
```