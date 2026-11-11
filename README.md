# Music Recommendation System

A reproducible content-based music recommendation API built with Python, FastAPI, pandas, and scikit-learn. The service uses TF-IDF vectors and cosine similarity across artist, genre, and mood metadata to return similar tracks.

## Features

- REST API with health and recommendation endpoints
- Content-based recommendation engine using TF-IDF and cosine similarity
- Reproducible sample dataset included in the repository
- Input validation and 404 handling for unknown tracks
- Automated API tests with pytest
- Docker image for portable local or cloud deployment
- GitHub Actions CI for tests and Docker builds

## Project structure

```text
app/                    # FastAPI application and recommendation engine
data/sample_tracks.csv  # Small reproducible track catalogue
tests/                  # API tests
Dockerfile              # Production container definition
requirements.txt        # Pinned Python dependencies
.github/workflows/      # Continuous integration workflow
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the interactive API docs at http://127.0.0.1:8000/docs.

### Example request

```bash
curl "http://127.0.0.1:8000/recommendations?track_id=1&limit=3"
```

## Run tests

```bash
pytest -q
```

## Run with Docker

```bash
docker build -t music-recommendation-system .
docker run --rm -p 8000:8000 music-recommendation-system
```

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/health` | Service health check |
| GET | `/recommendations?track_id=1&limit=5` | Return similar tracks |

## Notes

This reference implementation intentionally uses a small local dataset so it can be tested and deployed without external credentials. It is ready to extend with a larger catalogue, user listening history, persistent storage, authentication, and cloud deployment.
# Music_Recommendation_System
Sportify_Music_Recommendation_System implemented using MLops CI / CD Pipeline 
