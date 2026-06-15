import joblib

svd_model = joblib.load(
    "data/processed/svd_model.pkl"
)



def predict_rating(user_id, movie_id):

    prediction = svd_model.predict(
        user_id,
        movie_id
    )

    return prediction.est