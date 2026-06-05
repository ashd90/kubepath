# app.py
from flask import Flask
import os

app = Flask(__name__)

COUNTER_FILE = "/app/data/counter.txt"


def get_count():
    if not os.path.exists(COUNTER_FILE):
        return 0
    with open(COUNTER_FILE, "r") as f:
        return int(f.read())


def save_count(count):
    os.makedirs("/app/data", exist_ok=True)
    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))


@app.route("/")
def counter():
    count = get_count() + 1
    save_count(count)
    return f"This page has been visited {count} times."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
