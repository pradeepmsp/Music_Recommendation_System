from pathlib import Path

from fastapi import FastAPI, HTTPException, Query

from app.recommender import MusicRecommender


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "sample_tracks.csv"
recommender = MusicRecommender(DATA_PATH)
app = FastAPI(title="Music Recommendation System", version="1.0.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/recommendations")
def recommendations(track_id: int = Query(..., description="Seed track ID"), limit: int = Query(5, ge=1, le=20)) -> dict:
    try:
        items = recommender.recommend(track_id, limit)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=f"Track {exc.args[0]} was not found") from exc
    return {"track_id": track_id, "recommendations": items}
