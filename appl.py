import pickle
import pandas as pd
import streamlit as st
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{"
                 "}]?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend (movie):
    movie_index = movies_list[movies_list["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies =[]
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies_list.iloc[i[0]].title)

        #fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


st.title("Movie Recommender System")

movies_list = pickle.load(open("movies.pkl","rb"))
movies = movies_list["title"].values

similarity = pickle.load(open("similarity.pkl","rb"))


selected_movie = st.selectbox(
    "Select a movie",
     movies)
# if st.button("Recommend"):
#     names,posters= recommend(selected_movie_name)
#     for i in names:
#         st.write(i)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
