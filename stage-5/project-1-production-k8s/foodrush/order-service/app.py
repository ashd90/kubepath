# order-service/app.py
import os
import time
import json
import uuid
from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras
import redis

app = Flask(__name__)
START_TIME = time.time()

# Redis connection
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True,
)


def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        connect_timeout=5,
    )


@app.route("/orders", methods=["POST"])
def place_order():
    try:
        data = request.get_json()
        order_id = str(uuid.uuid4())[:8]
        order = {
            "order_id": order_id,
            "user_id": data.get("user_id"),
            "restaurant_id": data.get("restaurant_id"),
            "items": data.get("items", []),
            "status": "placed",
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        # Cache order in Redis (expires in 1 hour)
        redis_client.setex(f"order:{order_id}", 3600, json.dumps(order))
        return jsonify(
            {
                "status": "success",
                "message": "Order placed successfully",
                "order": order,
            }
        ), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/orders/<order_id>")
def get_order(order_id):
    try:
        # Check Redis cache first
        cached = redis_client.get(f"order:{order_id}")
        if cached:
            order = json.loads(cached)
            order["source"] = "cache"
            return jsonify({"status": "success", "order": order})
        return jsonify({"status": "error", "message": "Order not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/health/live")
def liveness():
    return jsonify({"status": "alive", "service": "order-service"}), 200


@app.route("/health/ready")
def readiness():
    if time.time() - START_TIME < 10:
        return jsonify({"status": "warming up"}), 503
    try:
        redis_client.ping()
        return jsonify({"status": "ready", "cache": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "not ready", "cache": str(e)}), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
