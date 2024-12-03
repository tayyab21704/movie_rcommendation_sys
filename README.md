# movie_rcommendation_sys

Key Features:
User Input: Users can type in the name of a movie they like.
Recommendation Logic: The app uses a pre-loaded dataset of movies (stored in a DataFrame) and a similarity matrix to find and rank similar titles based on the user's input.
Display Recommendations: Upon clicking the "Recommend" button, the app displays the top 10 similar movie titles to the user.
Technical Details:
The app leverages the difflib library to find close matches for the input movie title.
The similarity scores are calculated based on a matrix that quantifies how similar different movies are to one another.
The app is designed to be run locally via Streamlit, making it accessible through a web browser.
This app is ideal for movie enthusiasts looking for new films to watch based on their preferences.
