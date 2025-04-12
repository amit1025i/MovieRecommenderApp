# importing required libraries
import pickle
import streamlit as st
import requests


# Set custom page configuration
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# --- THEMES: Dark & Light ---
light_theme = """
    <style>
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    h1, h3, h4, p {
        color: #333333 !important;
    }
    .css-1d391kg, .css-1v3fvcr {
        background-color: #f0f2f6 !important;
    }
    </style>
"""

dark_theme = """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    h1, h3, h4, p {
        color: #fafafa !important;
    }
    .css-1d391kg, .css-1v3fvcr {
        background-color: #262730 !important;
    }
    .stTextInput>div>div>input {
        color: #fafafa;
    }
    .stButton>button {
        background-color: #444444;
        color: #fff;
    }
    </style>
"""

# --- Theme Toggle (Positioned in Corner) ---
theme_toggle_css = """
    <style>
    .theme-toggle {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 9999;
        padding: 10px;
        background-color: #f1c40f;
        border-radius: 50%;
        border: none;
        font-size: 20px;
        cursor: pointer;
    }

    .theme-toggle.dark {
        background-color: #2c3e50;
        color: white;
    }

    /* Dark Mode Scroll Issue Fix */
    .stApp {
        overflow-y: auto;
    }

    </style>
"""

# Apply the CSS for positioning the theme toggle
st.markdown(theme_toggle_css, unsafe_allow_html=True)

# --- Theme Selection (Custom Button with Half-Moon) ---
if "theme_choice" not in st.session_state:
    st.session_state.theme_choice = "🌞 Light Mode"

# Apply the current theme choice
if st.session_state.theme_choice == "🌞 Light Mode":
    st.markdown(light_theme, unsafe_allow_html=True)
else:
    st.markdown(dark_theme, unsafe_allow_html=True)

# --- Theme Switch Function ---
def switch_theme():
    if st.session_state.theme_choice == "🌞 Light Mode":
        st.session_state.theme_choice = "🌙 Dark Mode"
    else:
        st.session_state.theme_choice = "🌞 Light Mode"

# Add theme toggle button
if st.button("🌙 / 🌞", key="toggle", on_click=switch_theme):
    pass



# Function to fetch movie poster using TMDB API
def fetch_poster(movie_id):
    try:
        # Construct API URL using movie_id and API key
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

        # Send GET request to TMDB API
        response = requests.get(url, timeout=10)
        response.raise_for_status()              # Raise an exception if the response status is an error

        # Parse JSON response
        data = response.json()

        # Get poster path from response
        poster_path = data.get('poster_path')

        # If a poster exists, return full image URL
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path

        # Return a placeholder if no poster is found
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    # Show warning if request fails
    except requests.exceptions.RequestException as e:
        st.warning(f"⚠️ Could not load poster for movie ID {movie_id}")
        return "https://via.placeholder.com/500x750?text=No+Image"


#  Function to recommend similar movies
def recommend(movie):
    # Get index of selected movie from the dataframe
    index = movies[movies['title'] == movie].index[0]

    # Sort all movies by similarity score in descending order
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    # Create lists to store recommended movie titles and poster URLs
    recommended_movie_names = []
    recommended_movie_posters = []

    # Fetch top 5 similar movies (excluding the first one, which is the movie itself)
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id                       # Get TMDB movie ID
        recommended_movie_posters.append(fetch_poster(movie_id))    # Get poster URL
        recommended_movie_names.append(movies.iloc[i[0]].title)     # Get movie title
    return recommended_movie_names, recommended_movie_posters


# Load saved data: movie details and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))               # Contains movie titles and TMDB IDs
similarity = pickle.load(open('similarity_1.pkl', 'rb'))     # Contains similarity scores between movies

# Extract only movie titles to show in the dropdown
movie_list = movies['title'].values

# -----------------------------
#  UI LAYOUT STARTS HERE
# -----------------------------

#  Main title
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎥 Movie Recommender System 🍿</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown(
    "<h4 style='text-align: center; color: #555;'>Select your favorite movie and discover similar ones you’ll love!</h4>",
    unsafe_allow_html=True)

# Dropdown menu to select a movie
selected_movie = st.selectbox("👇 Choose a movie from the dropdown", movie_list, index=0)


# When user clicks the button
if st.button('🔍 Show Recommendations'):

    # Get 5 recommended movie names and poster URLs
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Separator line
    st.markdown("---")

    # Heading for results
    st.markdown(f"<h3 style='color:#00BFFF;'>🎯 Because you liked <u>{selected_movie}</u>, you might also enjoy:</h3>",
                unsafe_allow_html=True)

    # Create 5 equal-width columns to show recommend movies
    cols = st.columns(5)

    # Loop through each column and display movie poster and title
    for i in range(5):
        with cols[i]:
            st.image(recommended_movie_posters[i],  use_container_width=True)           # Display poster
            st.markdown(
                f"<p style='text-align: center; color: #444; font-weight: bold;'>{recommended_movie_names[i]}</p>",
                unsafe_allow_html=True)            # Display title

# Footer separator
st.markdown("---")

# Footer message
st.markdown(
    "<p style='text-align:center; color:gray;'>💡 Built with love using TMDB API and Streamlit | © 2025 Amit Kumar</p>",
    unsafe_allow_html=True)
