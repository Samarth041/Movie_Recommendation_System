from src.content import recommend_movies
from src.collaborative import predict_rating


def hybrid_recommend(
    user_id,
    movie_title,
    candidate_size=50,
    top_n=10
):

    candidates = recommend_movies(
        movie_title,
        top_n=candidate_size
    )

    if isinstance(candidates, str):
        return candidates

    recommendations = []

    for _, row in candidates.iterrows():

        movie_id = row["movie_id"]

        predicted_rating = predict_rating(
            user_id,
            movie_id
        )

        recommendations.append(
            (
                row["title"],
                row["genres_text"],
                predicted_rating
            )
        )

    recommendations = sorted(
        recommendations,
        key=lambda x: x[2],
        reverse=True
    )

    return recommendations[:top_n]