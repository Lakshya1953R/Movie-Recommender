import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ── Load data & build similarity matrix ───────────
movies = pd.read_csv("movies.csv")
cv = CountVectorizer()
vectors = cv.fit_transform(movies["genres"])
similarity = cosine_similarity(vectors)

# ── Recommendation function (same as before) ──────
def recommend(movie_title):
    index = movies[movies["title"] == movie_title].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top5 = scores[1:6]
    
    recommendations = []
    for idx, score in top5:
        recommendations.append(movies["title"][idx])
    return recommendations

# ── Web UI starts here ─────────────────────────────

# Page title
st.title("🎬 Movie Recommendation System")
st.write("Select a movie you like and we'll recommend similar ones!")

# Dropdown menu of all movies
selected_movie = st.selectbox(
    "Choose a movie:",
    movies["title"].tolist()
)

# Button
if st.button("Recommend 🎯"):
    results = recommend(selected_movie)
    
    st.subheader(f"Because you liked **{selected_movie}**, watch these:")
    
    for i, movie in enumerate(results):
        st.success(f"{i+1}. {movie}")
