# 🎬 Project 3: Content-Based Movie Recommendation Engine

<p align="left">
  <img src="https://img.shields.io/badge/AI-NLP%20%26%20RecSys-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Algorithm-Cosine%20Similarity-blue?style=for-the-badge" />
</p>

## 📋 Executive Overview
The **Movie Recommendation Engine** is a full-stack Django web application that provides personalized movie recommendations. Using Natural Language Processing (NLP) and vector space modeling, the engine analyzes movie synopses, genres, cast members, and directors to compute semantic similarities and suggest films tailored to user preferences.

---

## 🗂️ Directory Architecture
```
Project_3_Movie_Recommendation_System/
├── manage.py                  # Django command-line utility
├── movie_recsys/              # Django core application settings & URLs
├── recommendation_engine/     # Recommendation logic and views
├── data/
│   ├── tmdb_5000_movies.csv   # Movie metadata and plot synopses
│   └── tmdb_5000_credits.csv  # Cast and crew information
├── static/                    # Frontend UI stylesheets and scripts
├── templates/                 # HTML UI templates for movie search & results
└── README.md                  # Project documentation
```

---

## 🧠 Algorithmic Methodology
1. **Metadata Construction**: Extracted keywords, top 3 cast members, director names, and genres for over 5,000 films.
2. **Text Vectorization**: Applied **TF-IDF (Term Frequency-Inverse Document Frequency)** and Count Vectorization to transform textual tags into multi-dimensional feature vectors.
3. **Similarity Matrix**: Computed the **Cosine Similarity** score across all movie vectors to measure angular distance between films in feature space.
4. **Real-Time Querying**: When a user selects a movie, the engine retrieves the top $N$ movies with the highest cosine similarity score instantly.

---

## 💻 How to Run Locally

### 1. Install Requirements
```bash
pip install django pandas numpy scikit-learn
```

### 2. Apply Database Migrations & Start Server
```bash
python manage.py migrate
python manage.py runserver
```

### 3. Access the Web App
Open your browser and navigate to: `http://127.0.0.1:8000`
Search for any title (e.g., *Inception*, *The Dark Knight*, *Interstellar*) to discover top recommendation matches.
