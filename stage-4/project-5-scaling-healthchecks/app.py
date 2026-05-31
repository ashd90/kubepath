# app.py
from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

# Simulate app startup delay
start_time = time.time()


@app.route("/")
def home():
    return jsonify({"message": "App is running!", "pid": os.getpid()})


@app.route("/health/live")
def liveness():
    return jsonify({"status": "alive"}), 200


@app.route("/health/ready")
def readiness():
    # App needs 10 seconds to "warm up"
    uptime = time.time() - start_time
    if uptime < 10:
        return jsonify({"status": "not ready", "uptime": uptime}), 503
    return jsonify({"status": "ready", "uptime": uptime}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
