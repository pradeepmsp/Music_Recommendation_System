from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MusicRecommender:
    def __init__(self, data_path: str | Path) -> None:
        self.tracks = pd.read_csv(data_path)
        required = {"track_id", "title", "artist", "genre", "mood", "energy"}
        missing = required - set(self.tracks.columns)
        if missing:
            raise ValueError(f"Dataset is missing columns: {sorted(missing)}")
        self.tracks["features"] = self.tracks[["artist", "genre", "mood"]].fillna("").agg(" ".join, axis=1)
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(self.tracks["features"])

    def recommend(self, track_id: int, limit: int = 5) -> list[dict]:
        matches = self.tracks.index[self.tracks["track_id"] == track_id].tolist()
        if not matches:
            raise KeyError(track_id)
        index = matches[0]
        scores = cosine_similarity(self.matrix[index], self.matrix).ravel()
        ranked = scores.argsort()[::-1]
        results = []
        for candidate in ranked:
            if candidate == index:
                continue
            row = self.tracks.iloc[candidate]
            results.append({"track_id": int(row.track_id), "title": row.title, "artist": row.artist, "genre": row.genre, "mood": row.mood, "energy": float(row.energy), "similarity": round(float(scores[candidate]), 4)})
            if len(results) == limit:
                break
        return results
