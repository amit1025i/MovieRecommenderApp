# 🎬 Movie Recommender System

This is a **Movie Recommendation Web Application** built using **Python**, **Machine Learning**, and **Streamlit**. It suggests similar movies based on the one selected by the user using **content-based filtering**. The app fetches real-time movie posters via the **TMDB API** to create a visually engaging experience.

---

## 🚀 Project Features

- ✅ Recommends **Top 5 Similar Movies** using cosine similarity.
- 🎥 Interactive **dropdown menu** to choose any movie and select Dark/Light Mode also.
- 🔍 Search Bar with Autocomplete **interactive search bar** that suggests movie titles as users type.
    
- 🖼️ Displays **movie posters** fetched in real-time from TMDB.
- ⚡ Fast, responsive, and **easy to use web interface**.
- 🧠 Built with **Scikit-learn**, **Pandas**, and **Streamlit**.
- 🌐 Deployed as a **fully functional web application**.

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend/Logic**: Python, Pandas, Scikit-learn
- **API**: The Movie Database (TMDB) API
- **Deployment**: Localhost or Cloud via Streamlit Sharing

---

## 🧠 How it Works

- Movie data is preprocessed and vectorized using **Bag of Words** model.
- **Cosine similarity** is computed between movies.
- When a user selects a movie, the app fetches the **top 5 most similar movies**.
- Poster images are fetched using the **TMDB API** and displayed in a **card-style layout**.

---

## 📸 Output / Demo

### 🔻 HomePage For Light Mode
<img src="white_h.png" alt="Light Mode" width="1200"/>

### 📍 Recommended Results For Light Mode
<img src="white_m.png" alt="Light Mode" width="1200"/>

### 🔻 HomePage For Dark Mode
<img src="black_h.png" alt="Dark Mode" width="1200"/>

### 📍 Recommended Results For Dark Mode
<img src="black_m.png" alt="Dark Mode" width="1200"/>

## 🚀 Future Enhancements

Here are some exciting ideas to improve this project further:


- 🧠 **Improve Recommendation Algorithm:**  
  Integrate more advanced models like TF-IDF, Word2Vec, or deep learning for better recommendations.

- 🎞️ **Add Movie Trailers and Details:**  
  Fetch and show trailers, genre, rating, release date, and overview using the TMDB API.

- 🌐 **Multi-language Support:**  
  Make the app available in multiple languages for broader accessibility.

- 📱 **Mobile Responsiveness:**  
  Improve UI for mobile devices using responsive design or build a mobile app version.

- 👥 **User Login & History:**  
  Allow users to sign in and view/save their recommendation history.

- 📊 **Analytics Dashboard:**  
  Add admin panel to track user behavior, most recommended movies, etc.

- ☁️ **Deploy on Cloud:**  
  Host the project on platforms like Vercel, Netlify (frontend), and Render or Heroku (backend).


