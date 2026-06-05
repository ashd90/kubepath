# app-v3.py - Version 3 with Prometheus metrics
import os
import time
from flask import Flask, jsonify, request, Response
import psycopg2
import psycopg2.extras
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
START_TIME = time.time()
VERSION = "3.0.0"

# Prometheus metrics
REQUEST_COUNT = Counter(
    "restaurant_requests_total",
    "Total requests to restaurant service",
    ["method", "endpoint", "status"],
)
REQUEST_LATENCY = Histogram(
    "restaurant_request_duration_seconds", "Request latency in seconds", ["endpoint"]
)
DB_QUERY_COUNT = Counter(
    "restaurant_db_queries_total", "Total database queries", ["query_type"]
)


def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        connect_timeout=5,
    )


@app.route("/restaurants")
def get_restaurants():
    start = time.time()
    try:
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(
            "SELECT * FROM restaurants WHERE is_open = true ORDER BY rating DESC;"
        )
        restaurants = cur.fetchall()
        cur.close()
        conn.close()
        DB_QUERY_COUNT.labels(query_type="select_all").inc()
        REQUEST_COUNT.labels(method="GET", endpoint="/restaurants", status="200").inc()
        REQUEST_LATENCY.labels(endpoint="/restaurants").observe(time.time() - start)
        return jsonify(
            {
                "status": "success",
                "version": VERSION,
                "count": len(restaurants),
                "restaurants": [dict(r) for r in restaurants],
            }
        )
    except Exception as e:
        REQUEST_COUNT.labels(method="GET", endpoint="/restaurants", status="500").inc()
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/restaurants/<int:restaurant_id>")
def get_restaurant(restaurant_id):
    start = time.time()
    try:
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM restaurants WHERE id = %s;", (restaurant_id,))
        restaurant = cur.fetchone()
        cur.close()
        conn.close()
        DB_QUERY_COUNT.labels(query_type="select_one").inc()
        if not restaurant:
            REQUEST_COUNT.labels(
                method="GET", endpoint="/restaurants/id", status="404"
            ).inc()
            return jsonify({"status": "error", "message": "Restaurant not found"}), 404
        REQUEST_COUNT.labels(
            method="GET", endpoint="/restaurants/id", status="200"
        ).inc()
        REQUEST_LATENCY.labels(endpoint="/restaurants/id").observe(time.time() - start)
        return jsonify({"status": "success", "restaurant": dict(restaurant)})
    except Exception as e:
        REQUEST_COUNT.labels(
            method="GET", endpoint="/restaurants/id", status="500"
        ).inc()
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route("/health/live")
def liveness():
    return jsonify(
        {"status": "alive", "service": "restaurant-service", "version": VERSION}
    ), 200


@app.route("/health/ready")
def readiness():
    if time.time() - START_TIME < 10:
        return jsonify({"status": "warming up"}), 503
    try:
        conn = get_db()
        conn.close()
        return jsonify({"status": "ready", "db": "connected", "version": VERSION}), 200
    except Exception as e:
        return jsonify({"status": "not ready", "db": str(e)}), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
