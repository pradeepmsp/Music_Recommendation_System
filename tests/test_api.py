from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_recommendations() -> None:
    response = client.get("/recommendations", params={"track_id": 1, "limit": 3})
    assert response.status_code == 200
    payload = response.json()
    assert payload["track_id"] == 1
    assert len(payload["recommendations"]) == 3
    assert all(item["track_id"] != 1 for item in payload["recommendations"])


def test_unknown_track() -> None:
    response = client.get("/recommendations", params={"track_id": 999})
    assert response.status_code == 404
