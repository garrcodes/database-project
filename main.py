import sqlite3
import pandas as pd

# Load data from CSV files
ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

# Create SQLite connection and cursor
conn = sqlite3.connect(':memory:')  # Use in-memory database for demonstration, you can use a file-based database for persistence
cur = conn.cursor()

# Create tables and insert data
cur.execute('''CREATE TABLE ratings (
                user_id INTEGER,
                movie_id INTEGER,
                rating REAL,
                timestamp INTEGER
                )''')

ratings_df.to_sql('ratings', conn, if_exists='append', index=False)

cur.execute('''CREATE TABLE movies (
                movie_id INTEGER,
                title TEXT,
                genres TEXT
                )''')

movies_df.to_sql('movies', conn, if_exists='append', index=False)

# Commit changes
conn.commit()

def calculate_similarity(movie_id1, movie_id2):
    cur.execute('''SELECT AVG(r1.rating), AVG(r2.rating)
                   FROM ratings r1
                   JOIN ratings r2 ON r1.user_id = r2.user_id
                   WHERE r1.movie_id = ? AND r2.movie_id = ?''', (movie_id1, movie_id2))
    row = cur.fetchone()
    if row[0] is None or row[1] is None:
        return 0, 0
    return row[0], row[1]


def recommend_movies(movie_id, num_recommendations=5):
    cur.execute('''SELECT DISTINCT movie_id
                   FROM ratings
                   WHERE movie_id != ?''', (movie_id,))
    all_movies = cur.fetchall()
    
    similarity_scores = []
    for other_movie in all_movies:
        similarity = calculate_similarity(movie_id, other_movie[0])
        similarity_scores.append((other_movie[0], similarity[0] * similarity[1]))
    
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    recommendations = similarity_scores[:num_recommendations]
    
    recommended_movies = []
    for rec in recommendations:
        cur.execute('''SELECT title FROM movies WHERE movie_id = ?''', (rec[0],))
        movie_title = cur.fetchone()[0]
        recommended_movies.append((movie_title, rec[1]))
    
    return recommended_movies

# Example: recommend movies similar to movie with id=1
recommendations = recommend_movies(1)
print("Recommended Movies:")
for movie, score in recommendations:
    print(f"{movie} (Similarity Score: {score}")

# Close connection
conn.close()
