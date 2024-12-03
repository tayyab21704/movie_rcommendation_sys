import numpy as np
import pandas as pd
import difflib 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data= pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\movie_recommendor\movies.csv")
selected_features=[ 'genres','keywords','tagline','cast','director']

for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')



combined_features = movies_data ['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)

import streamlit as st
import difflib
import pandas as pd

# Assuming movies_data and similarity are already defined
# movies_data = pd.read_csv('path_to_your_movies.csv')  # Uncomment and modify if needed
# similarity = your_similarity_matrix  # Replace with your actual similarity matrix

def recommend_movies(movie_name):
    list_of_all_titles = movies_data['title'].tolist()
    close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    if close_match:
        top_match = close_match[0]
        index_of_the_movie = movies_data[movies_data.title == top_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        recommendations = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        recommended_titles = []
        for i, movie in enumerate(recommendations):
            index = movie[0]
            title_from_index = movies_data[movies_data.index == index]['title'].values[0]
            if i < 10:  # Top 10 recommendations
                recommended_titles.append(title_from_index)
        return recommended_titles
    else:
        return []

# Streamlit web app
st.title('Movie Recommendation System')

movie_name = st.text_input('Enter Your Movie for Recommendation:')
if st.button('Recommend'):
    if movie_name:
        recommendations = recommend_movies(movie_name)
        if recommendations:
            st.write('Movies recommendations:')
            for i, title in enumerate(recommendations, start=1):
                st.write(f"{i}. {title}")
        else:
            st.write("Sorry, no recommendations found.")
    else:
        st.write("Please enter a movie name.")
