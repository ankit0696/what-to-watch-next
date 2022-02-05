from urllib import response
from webbrowser import get
import streamlit as st
import pickle
import requests

movies_df = pickle.load(open('movies.pkl','rb'))
similar = pickle.load(open('similar.pkl','rb'))

movies_titles = movies_df['title'].values

def getMovieDetails(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{0}?api_key=8a09c6b846592a7416a55758a52aee3e'.format(movie_id))
    data = response.json()
    return data

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similar[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended = []
    for i in movie_list:
        recommended.append(getMovieDetails(movies_df.iloc[i[0]].movie_id))
    return recommended

st.title('Movie Recommendation System')

option = st.selectbox(
    'Type movie you liked?',
     (movies_titles))

if st.button('Recommend'):
    movies = recommend(option)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.image('https://image.tmdb.org/t/p/w500/' + movies[0]['poster_path'])
        st.text(movies[0]['original_title'])
        st.text('Release date: ' + movies[0]['release_date'])
    with col2:
        st.image('https://image.tmdb.org/t/p/w500/' + movies[1]['poster_path'])
        st.text(movies[1]['original_title'])
        st.text('Release date: ' + movies[1]['release_date'])

    with col3:
        st.image('https://image.tmdb.org/t/p/w500/' + movies[2]['poster_path'])
        st.text(movies[2]['original_title'])
        st.text('Release date: ' + movies[2]['release_date'])
    with col4:
        st.image('https://image.tmdb.org/t/p/w500/' + movies[3]['poster_path'])
        st.text(movies[3]['original_title'])
        st.text('Release date: ' + movies[3]['release_date'])
    with col5:
        st.image('https://image.tmdb.org/t/p/w500/' + movies[4]['poster_path'])
        st.text(movies[4]['original_title'])
        st.text('Release date: ' + movies[4]['release_date'])

