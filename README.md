# Medical Healthcare & Research Analyst — Multi-Agent Assistant

A coursework demonstration using FastAPI, Agno Teams, Groq, HTML/CSS/JavaScript, Docker, and Docker Compose. It provides educational information and research-literacy support only; it is not a diagnostic or treatment system.

## Architecture

1. Query Analyzer — classifies the question and identifies research needs.
2. Research Agent — searches the project's local sample reference library.
3. Answer Reviewer — reviews the proposed answer for unsupported claims and safety.
4. Agno Team — coordinates the three agents and synthesizes a response.

The local library is intentionally small and educational. It is not a substitute for validated clinical guidelines or a live medical literature database.

## Requirements

- Python 3.12 for local development
- Docker Desktop with Docker Compose for containerization
- Groq API key for AI requests

## Local setup (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and set your real `GROQ_API_KEY`. Never commit `.env`.

Run:

```powershell
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/`, `http://127.0.0.1:8000/docs`, or `http://127.0.0.1:8000/health`.

## Tests

```powershell
python -m pytest -v
```

The automated tests do not call Groq; they cover basic UI delivery, health metadata, request validation, and local library search.

## Docker

```powershell
docker compose config
docker compose build
docker compose up -d
docker compose ps
docker compose logs -f medical-assistant
```

Open `http://localhost:8000/`. Stop with `docker compose down`.

The Docker image copies application source into the image. Compose intentionally does not bind-mount the source by default; rebuild after code changes using `docker compose up -d --build`.

## Kubernetes and CI/CD

Starter manifests and a GitHub Actions workflow are provided in `k8s/` and `.github/workflows/`. Replace `YOUR_REGISTRY/medical-healthcare-assistant:latest` with an image that exists in a registry accessible to your cluster. Create the Kubernetes Secret in your cluster from a secure source; do not commit actual credentials.

## Medical safety

The assistant is for education and research literacy. It must not be used for diagnosis, medication changes, or emergency triage. Seek a qualified healthcare professional for personal medical decisions; contact local emergency services for possible emergencies.
