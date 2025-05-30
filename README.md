# HuggingFace Inference API (Production-Ready Setup)

This project provides a containerized, scalable REST API for serving HuggingFace transformer models using FastAPI, with a robust production setup including:

- **NGINX** (reverse proxy, request routing)
- **Gunicorn** (process manager)
- **Uvicorn** (ASGI server for FastAPI)
- **Docker Compose** (service orchestration)

---




---

## Deployment Steps

### Step 1: Build and Launch the Services

From the root directory:

```bash
docker-compose up --build -d
```

This will:
- Build the FastAPI app container
- Launch a Gunicorn server with Uvicorn workers
- Start an NGINX container as a reverse proxy on port 80

---

### Step 2: Test the API

Send a POST request to the `/predict` endpoint:

```bash
curl -X POST http://localhost/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "This service is awesome!"}'
```

Expected response:

```json
{
  "result": [
    {
      "label": "POSITIVE",
      "score": 0.9998
    }
  ]
}
```

---

### Step 3: Stop and Clean Up

To stop all containers:

```bash
docker-compose down
```

---

## Notes

- Gunicorn is configured with 4 Uvicorn workers for concurrent handling of requests (`gunicorn_conf.py`)
- NGINX forwards requests from port 80 to Gunicorn's internal port 8000
- You can scale workers or add HTTPS in `nginx/default.conf` with Certbot integration
- All configs are lightweight and suitable for cloud deployment

---

## Load Testing

Run `notebook_demo.ipynb` to simulate concurrent user requests via `ThreadPoolExecutor`.

