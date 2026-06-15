import streamlit as st
import pandas as pd

from src.hybrid import hybrid_recommend

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎥"

    
)

movies = pd.read_parquet(
    "data/processed/movies_features.parquet"
)

st.title("🎬 Movie Recommendation System")

st.markdown(
    """
    This recommendation combines:
        - 🎭Content Based Filtering (Genre Similarity)
        - 👥Collaborative Filtering

        to generate personalised movie recommendations
    """
)


#user input
col1, col2=st.columns(2)

with col1:
    user_id=st.number_input(
        "Enter User ID",
        min_value=1,
        value=1,
        step=1
    )

with col2:
    top_n=st.slider(
        "Number of Recommendations",
        min_value=5,
        max_value=20,
        value=10
    )

#movie Search

movie_search=st.text_input(
    "🔍 Search Movie",
    placeholder="Type a movie name...."
)

filtered_movies=sorted(
    movies[
        movies['title'].str.contains(
            movie_search,
            case=False,
            na=False
        )
    ]['title'].unique()
)

st.caption(f"{len(filtered_movies)} movies found")

if len(filtered_movies)>0:
    movie_title=st.selectbox(
        "Select Movie",
        filtered_movies
    )

    if st.button("Recommend Movies"):
        try:
            recommendations=hybrid_recommend(
                user_id=user_id,
                movie_title=movie_title,
                top_n=top_n
            )

            st.subheader("Recommended Movies")

            for i,(title,genres,score) in enumerate(recommendations,start=1):
                with st.container():
                    st.markdown(
                        f"""
                        ### {i}. {title}

                        **Genres:** {genres}

                        **Predicted Rating:** ⭐ {score:.2f}
                        """
                    )
                    st.divider()

        except Exception as e:
            st.error(f"Error : {str(e)}")


else:
    st.warning("No movies match to your search.Try another movie name")



#Footer

st.markdown("---")

st.caption("Built a Ml project")


