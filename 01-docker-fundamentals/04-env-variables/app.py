# app.py
import os
from flask import Flask

app = Flask(__name__)

# Read from environment, use defaults if not set
APP_ENV = os.getenv("APP_ENV", "development")
APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello from Docker!")


@app.route("/")
def home():
    return f"[{APP_ENV}] {APP_MESSAGE}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
