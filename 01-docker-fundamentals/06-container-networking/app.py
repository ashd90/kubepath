# app.py
import os
from flask import Flask
import redis

app = Flask(__name__)

# Try to connect to Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379)


@app.route("/")
def counter():
    count = r.incr("visits")
    return f"This page has been visited {count} times."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
