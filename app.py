import streamlit as st
import pickle

# Page Configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

# Load Data
import gdown
import pickle
import os

# Download files only if not already present
if not os.path.exists("movies.pkl"):
    gdown.download("https://drive.google.com/file/d/1E3ojBEuTx4pfE3au1lcfY_3tbXBL8Kam/view?usp=sharing", "movies.pkl", quiet=False)

if not os.path.exists("similarity.pkl"):
    gdown.download("https://drive.google.com/file/d/1MMp5M3y5Z-i7ogXQxhPoXDI87wNFB4z-/view?usp=drive_link", "similarity.pkl", quiet=False)

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation Function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


# UI
st.title("🎬 Movie Recommendation System")

st.write("Select a movie and get 5 similar movie recommendations.")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Choose a Movie",
    movie_list
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.success(recommendations[i])