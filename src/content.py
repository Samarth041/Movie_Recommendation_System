import pandas as pd
import joblib

movies = pd.read_parquet(
    "data/processed/movies_features.parquet"
)

similarity_matrix = joblib.load(
    "data/processed/content_similarity.pkl"
)

movie_indices = joblib.load(
    "data/processed/movie_indices.pkl"
)


def get_movie_index(title):
    title = title.strip().lower()

    # 1. Exact match first (BEST CASE)
    exact_match = movies[movies["title"].str.lower() == title]

    if len(exact_match) > 0:
        return exact_match.index[0]

    # 2. Fallback: partial match
    matches = movies[movies["title"].str.lower().str.contains(title, regex=False)]

    if len(matches) == 0:
        return None

    return matches.index[0]

def recommend_movies(title, top_n=10):

    idx = get_movie_index(title)

    if idx is None:
        raise ValueError("Movie not found")

    similarity_scores = list(
        enumerate(similarity_matrix[idx])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:top_n+1]

    movie_indices_list = [i[0] for i in similarity_scores]

    return movies.iloc[movie_indices_list][
        ['movie_id','title', 'genres_text']
    ]