from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(
    host=os.environ.get('DB_HOST'),
    database=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASS')
)

@app.route("/movies", methods=["GET"])
def get_movies():
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    movies = cur.fetchall()
    cur.close()
    return jsonify(movies)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

