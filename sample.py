from src.hybrid import hybrid_recommend

print("=" * 50)
print("🎬 Movie Recommendation System")
print("=" * 50)

user_id = int(input("Enter User ID: "))

movie_title = input(
    "Enter Movie Name: "
)

recommendations = hybrid_recommend(
    user_id=user_id,
    movie_title=movie_title
)

print("\nRecommended Movies:\n")

for i, (title, genres, score) in enumerate(
    recommendations,
    start=1
):
    print(
        f"{i}. {title}"
    )
    print(
        f"   Genres: {genres}"
    )
    print(
        f"   Predicted Rating: {score:.2f}"
    )
    print("-" * 40)