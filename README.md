# Items API — CI/CD Lab 1

Simple Python FastAPI REST service supporting CRUD operations, JSON responses, OpenAPI/Swagger UI, unit tests, Docker and Azure DevOps CI/CD.

## Stack
Python 3.12, FastAPI, pytest, Docker, Azure DevOps, GitHub, Docker Hub.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Swagger: http://localhost:8000/docs ; OpenAPI: http://localhost:8000/openapi.json

## Run tests
```bash
python -m pytest -v
```

## Build and run Docker image
```bash
docker build -t items-api:latest .
docker run --rm -p 8000:8000 items-api:latest
```

## CI/CD
`azure-pipelines.yml` triggers on push to `main`, installs dependencies, runs tests, builds and pushes the Docker image to Docker Hub. Configure an Azure DevOps Docker Registry service connection named `dockerhub-connection`, create a Docker Hub repository named `items-api`, and set the Azure Pipeline repository to this GitHub repository. The pipeline publishes `latest` and a unique build-ID tag.

## API
- `GET /api/items`
- `GET /api/items/{item_id}`
- `POST /api/items`
- `PUT /api/items/{item_id}`
- `DELETE /api/items/{item_id}`

Data is stored in memory and resets when the service restarts.

CI/CD pipeline автоматично запускається після push у main.

## CI/CD перевірка

Перевірка правила paths-ignore у GitHub Actions.
Зміни лише у README.md не повинні запускати workflow.