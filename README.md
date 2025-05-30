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

## Bonus Features


### Continuous Integration (CI)

This project includes a GitHub Actions pipeline that runs automatically on every push or pull request to `main`.

The pipeline performs:

* ✅ Unit tests with `pytest`
* ✅ Docker image build (optional)
* ✅ Quick feedback on API correctness

Workflow file: `.github/workflows/ci.yml`

---

###  Logging

The API includes structured logging using Python’s `logging` module.

Logs include:

* Timestamp
* Log level (INFO, ERROR)
* Message (e.g., input text, prediction output, errors)

These logs appear in the container stdout and are ready for redirection to file or external log services.

---

###  Monitoring with Prometheus & Grafana

Observability is integrated with:

* `/metrics` endpoint exposed by the FastAPI app
* Prometheus scraping metrics every 15s
* Grafana for dashboarding

| Service    | URL                                                  |
| ---------- | ---------------------------------------------------- |
| API        | [http://localhost/predict](http://localhost/predict) |
| Metrics    | [http://localhost/metrics](http://localhost/metrics) |
| Grafana    | [http://localhost:3000](http://localhost:3000)       |
| Prometheus | [http://localhost:9090](http://localhost:9090)       |

