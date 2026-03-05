# app.py
import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
    )


@app.route("/api/messages")
def get_messages():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT message FROM messages;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({"messages": [row[0] for row in rows]})


@app.route("/api/health")
def health():
    return jsonify({"status": "backend is healthy!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
