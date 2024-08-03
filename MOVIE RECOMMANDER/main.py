import streamlit as st
import recommend

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters

st.header('Movie Recommender System')

movie_list = recommend.movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown",
                              movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend.recommend(selected_movie)
    for recommended_movies_name in recommended_movie_names:
        st.write(recommended_movies_name)
