
# Olist Delivery Delay Predictor

An inference service that predicts whether an Olist order will be delivered
late or on time, and returns the probability along with the model version.

> **Status:** Scaffold. The FastAPI service, tests, Docker image, and CI pipeline
> are working end to end with a placeholder model. The real model and
> preprocessor will be wired in from the notebooks in a follow-up commit.

[![CI Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml)

---

## Project Structure

```
olist-delay-service/
├── app/                    # FastAPI application
│   └── main.py             # Routes: /health, /model/info, /predict
├── config/
│   └── config.yaml         # Single source of configuration
├── src/                    # Reusable Python modules
│   ├── data/               # Data loading and cleaning
│   ├── features/           # Label creation and feature engineering
│   ├── models/             # Inference pipeline and evaluation
│   └── utils/              # Config loader and helpers
├── tests/                  # Unit and integration tests
├── .github/workflows/      # CI pipeline
├── Dockerfile              # Container image for the service
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
└── pytest.ini              # Pytest configuration
```

---

## Prerequisites

- Python 3.10+
- Docker Desktop (for containerized runs)
- Git

---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd olist-delay-service
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements-dev.txt
```

### 4. Run the API locally

```bash
fastapi dev app/main.py --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000/docs` for the interactive Swagger UI.

### 5. Or run the API in Docker

```bash
docker build -t olist-delay-api .
docker run -p 8000:8000 olist-delay-api
```

Then visit `http://localhost:8000/docs`.

---

## API Endpoints

| Method | Route         | Description                              |
|--------|---------------|------------------------------------------|
| GET    | `/health`     | Returns `{"status": "ok"}`               |
| GET    | `/model/info` | Returns model name and version           |
| POST   | `/predict`    | Returns prediction, probability, version |

### Example request

```bash
curl.exe -X POST "http://localhost:8000/predict" `
  -H "Content-Type: application/json" `
  -d "@payload.json"
```

Where `payload.json` contains:

```json
{
  "order_id": "test-1",
  "customer_id": "cust-1",
  "order_purchase_timestamp": "2024-01-01"
}
```

### Example response

```json
{
  "prediction": 0,
  "probability": 0.1,
  "model_version": "v0.0.0"
}
```

The current model is a placeholder. Once the real model is wired in, the
`Order` schema will expand to match the training feature set, and the response
will reflect real predictions from the trained Random Forest.

---

## Configuration

All paths, parameters, and settings live in `config/config.yaml`. Nothing is
hardcoded in the source. To change the model path, threshold, or API port,
edit the YAML file — do not edit the Python code.

```yaml
model:
  model_path: "models/final_model.pkl"
  preprocessor_path: "models/preprocessor.pkl"
  feature_names_path: "models/feature_names.pkl"
  threshold: 0.5

api:
  host: "0.0.0.0"
  port: 8000
  version: "v0.0.0"
```

---

## Tests

Run the full test suite with one command:

```bash
pytest -v
```

The scaffold includes:

- `tests/test_features.py` — label and feature engineering behavior
- `tests/test_predict.py` — inference pipeline loads and returns the right shape

As the real model is wired in, tests will compare the pipeline output against
the notebook output on the same input.

---

## CI/CD

Every push and pull request triggers the GitHub Actions pipeline defined in
`.github/workflows/ci.yml`. The pipeline:

1. Checks out the code
2. Sets up Python 3.10
3. Installs `requirements-dev.txt`
4. Runs `flake8` for linting
5. Runs `black --check` for formatting
6. Runs `pytest` for tests

A failing step stops the pipeline. The badge at the top of this README
reflects the current status of `main`.

---

## License

For educational use as part of the MLOps training track.

