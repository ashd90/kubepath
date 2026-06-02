# api-gateway/app.py
import os
import time
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
START_TIME = time.time()

# Service URLs from environment
RESTAURANT_SERVICE = os.getenv("RESTAURANT_SERVICE_URL")
ORDER_SERVICE = os.getenv("ORDER_SERVICE_URL")


def forward_request(url, method="GET", data=None, headers=None):
    try:
        if method == "GET":
            response = requests.get(url, timeout=5)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=5)
        return response.json(), response.status_code
    except requests.exceptions.ConnectionError:
        return {"status": "error", "message": "Service unavailable"}, 503
    except requests.exceptions.Timeout:
        return {"status": "error", "message": "Service timeout"}, 504
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500


# Restaurant routes
@app.route("/api/restaurants")
def get_restaurants():
    data, status = forward_request(f"{RESTAURANT_SERVICE}/restaurants")
    return jsonify(data), status


@app.route("/api/restaurants/<int:restaurant_id>")
def get_restaurant(restaurant_id):
    data, status = forward_request(f"{RESTAURANT_SERVICE}/restaurants/{restaurant_id}")
    return jsonify(data), status


# Order routes
@app.route("/api/orders", methods=["POST"])
def place_order():
    data, status = forward_request(
        f"{ORDER_SERVICE}/orders", method="POST", data=request.get_json()
    )
    return jsonify(data), status


@app.route("/api/orders/<order_id>")
def get_order(order_id):
    data, status = forward_request(f"{ORDER_SERVICE}/orders/{order_id}")
    return jsonify(data), status


@app.route("/api/health")
def health():
    services = {}
    # Check restaurant service
    try:
        r = requests.get(f"{RESTAURANT_SERVICE}/health/live", timeout=3)
        services["restaurant-service"] = (
            "healthy" if r.status_code == 200 else "unhealthy"
        )
    except:
        services["restaurant-service"] = "unreachable"
    # Check order service
    try:
        r = requests.get(f"{ORDER_SERVICE}/health/live", timeout=3)
        services["order-service"] = "healthy" if r.status_code == 200 else "unhealthy"
    except:
        services["order-service"] = "unreachable"
    return jsonify({"status": "success", "services": services})


@app.route("/health/live")
def liveness():
    return jsonify({"status": "alive", "service": "api-gateway"}), 200


@app.route("/health/ready")
def readiness():
    if time.time() - START_TIME < 10:
        return jsonify({"status": "warming up"}), 503
    return jsonify({"status": "ready"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
