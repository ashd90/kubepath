# 🍔 FoodRush — Production Grade Kubernetes Application

A production-grade food delivery platform built to demonstrate real-world Kubernetes patterns.
Inspired by Zomato/Swiggy architecture.

---

## 🏗️ Architecture

<pre>
                    Internet Traffic
                          |
                          v
             +------------------------+
             |    Nginx Ingress        |
             |  myapp.local            |
             +------------------------+
                |              |
                v              v
      +-----------+    +----------------+
      | Frontend  |    |  API Gateway   |
      | (Nginx)   |    |  (Flask)       |
      +-----------+    +----------------+
                            |
              +-------------+-------------+
              |                           |
              v                           v
   +--------------------+    +--------------------+
   | Restaurant Service |    |   Order Service    |
   | (Flask)            |    |   (Flask)          |
   +--------------------+    +--------------------+
              |                           |
              v                           v
   +--------------------+    +--------------------+
   |    PostgreSQL      |    |      Redis         |
   |    (Database)      |    |      (Cache)       |
   +--------------------+    +--------------------+
</pre>

---

## 📦 Namespaces

| Namespace | Purpose | Team |
|-----------|---------|------|
| foodrush-frontend | Frontend services | Frontend Team |
| foodrush-backend | Microservices | Backend Team |
| foodrush-data | Databases & Cache | Data Team |
| foodrush-monitoring | Prometheus & Grafana | DevOps Team |

---

## 🔧 Services

| Service | Namespace | Port | Health Check |
|---------|-----------|------|--------------|
| frontend | foodrush-frontend | 80 | /health/ready |
| api-gateway | foodrush-backend | 5000 | /health/ready |
| restaurant-service | foodrush-backend | 5000 | /health/ready |
| order-service | foodrush-backend | 5000 | /health/ready |
| postgres | foodrush-data | 5432 | TCP |
| redis | foodrush-data | 6379 | TCP |

---

## 🌐 Ingress Routing

<pre>
foodrush.local/              -> frontend-service
foodrush.local/api/          -> api-gateway
foodrush.local/restaurants/  -> restaurant-service
foodrush.local/orders/       -> order-service
monitoring.foodrush.local/   -> grafana
</pre>

---

## 🔑 Environment Variables

### Restaurant Service

| Variable | Source | Description |
|----------|--------|-------------|
| DB_HOST | ConfigMap | PostgreSQL hostname |
| DB_NAME | ConfigMap | Database name |
| DB_USER | ConfigMap | Database user |
| DB_PASSWORD | Secret | Database password |

### Order Service

| Variable | Source | Description |
|----------|--------|-------------|
| DB_HOST | ConfigMap | PostgreSQL hostname |
| DB_NAME | ConfigMap | Database name |
| DB_USER | ConfigMap | Database user |
| DB_PASSWORD | Secret | Database password |
| REDIS_HOST | ConfigMap | Redis hostname |
| REDIS_PORT | ConfigMap | Redis port |

---

## 📊 Resource Limits

| Service | CPU Request | CPU Limit | Memory Request | Memory Limit |
|---------|-------------|-----------|----------------|--------------|
| frontend | 50m | 100m | 64Mi | 128Mi |
| api-gateway | 100m | 300m | 128Mi | 256Mi |
| restaurant-service | 100m | 300m | 128Mi | 256Mi |
| order-service | 100m | 300m | 128Mi | 256Mi |
| postgres | 200m | 500m | 256Mi | 512Mi |
| redis | 100m | 200m | 64Mi | 128Mi |

---

## 📁 Folder Structure

<pre>
foodrush/
├── README.md
├── namespaces/
│   └── namespaces.yaml
├── database/
│   ├── database.yaml          # postgres deployment + service + pvc
│   └── init.sql               # database initialization
├── restaurant-service/
│   ├── app.py                 # flask microservice
│   ├── requirements.txt
│   ├── Dockerfile
│   └── restaurant-service.yaml # deployment + service + configmap
├── order-service/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── order-service.yaml
├── api-gateway/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── api-gateway.yaml
├── frontend/
│   ├── index.html
│   ├── nginx.conf
│   ├── Dockerfile
│   └── frontend.yaml
├── ingress/
│   └── ingress.yaml
├── rbac/
│   └── rbac.yaml
└── monitoring/
    ├── prometheus.yaml
    └── grafana.yaml
</pre>

---

## 🚀 Deployment

### Prerequisites
- Minikube running
- Ingress addon enabled
- Metrics server enabled

### Deploy Everything
<pre>
# Create namespaces first
kubectl apply -f namespaces/namespaces.yaml

# Deploy database
kubectl apply -f database/database.yaml

# Deploy backend services
kubectl apply -f restaurant-service/restaurant-service.yaml
kubectl apply -f order-service/order-service.yaml
kubectl apply -f api-gateway/api-gateway.yaml

# Deploy frontend
kubectl apply -f frontend/frontend.yaml

# Deploy ingress
kubectl apply -f ingress/ingress.yaml
</pre>

### Verify Deployment
<pre>
kubectl get all -n foodrush-frontend
kubectl get all -n foodrush-backend
kubectl get all -n foodrush-data
</pre>

---

## 🧪 Kubernetes Concepts Demonstrated

| Concept | Where Used |
|---------|-----------|
| Namespaces | All services isolated by tier |
| Deployments | All services |
| Services | ClusterIP for internal, NodePort for external |
| ConfigMaps | Non-sensitive configuration |
| Secrets | Database passwords |
| PVC/PV | PostgreSQL persistent storage |
| Ingress | Single entry point routing |
| Resource Limits | All deployments |
| Health Checks | All Flask services |
| RBAC | Team based access control |
| Rolling Updates | Zero downtime deployments |
| HPA | Auto scaling based on CPU |

---

## 📝 Notes

- Secrets are hardcoded for learning purposes only
- In production use HashiCorp Vault or AWS Secrets Manager
- Images built locally using eval $(minikube docker-env)
- In production images pushed to ECR/ACR/GCR