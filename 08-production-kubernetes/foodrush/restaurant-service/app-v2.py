# app-v2.py - Version 2 with categories endpoint added
import os
import time
from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras

app = Flask(__name__)
START_TIME = time.time()
VERSION = "2.0.0"


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
    try:
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(
            "SELECT * FROM restaurants WHERE is_open = true ORDER BY rating DESC;"
        )
        restaurants = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(
            {
                "status": "success",
                "version": VERSION,
                "count": len(restaurants),
                "restaurants": [dict(r) for r in restaurants],
            }
        )
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/restaurants/<int:restaurant_id>")
def get_restaurant(restaurant_id):
    try:
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM restaurants WHERE id = %s;", (restaurant_id,))
        restaurant = cur.fetchone()
        cur.close()
        conn.close()
        if not restaurant:
            return jsonify({"status": "error", "message": "Restaurant not found"}), 404
        return jsonify({"status": "success", "restaurant": dict(restaurant)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# NEW in v2: cuisine categories endpoint
@app.route("/restaurants/categories")
def get_categories():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT cuisine FROM restaurants ORDER BY cuisine;")
        categories = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return jsonify(
            {"status": "success", "version": VERSION, "categories": categories}
        )
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


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
