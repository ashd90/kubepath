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
             |  foodrush.local         |
             +------------------------+
                          |
                          v
             +------------------------+
             |      Frontend          |
             |      (Nginx)           |
             +------------------------+
                          |
                          v
             +------------------------+
             |      API Gateway       |
             |      (Flask)           |
             +------------------------+
                |                |
                v                v
   +------------------+  +------------------+
   | Restaurant Svc   |  |   Order Svc      |
   | (Flask)          |  |   (Flask)        |
   +------------------+  +------------------+
           |                     |
           v                     v
   +------------------+  +------------------+
   |   PostgreSQL     |  |     Redis        |
   |   (Database)     |  |     (Cache)      |
   +------------------+  +------------------+
</pre>

---

## 📦 Namespaces

| Namespace | Purpose | Team |
|-----------|---------|------|
| foodrush-frontend | Frontend services | Frontend Team |
| foodrush-backend | Microservices | Backend Team |
| foodrush-data | Databases and Cache | Data Team |
| foodrush-monitoring | Prometheus and Grafana | DevOps Team |

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
foodrush.local/              -> frontend-service (foodrush-frontend)
foodrush.local/api/          -> api-gateway (foodrush-backend)
foodrush.local/restaurants/  -> restaurant-service (foodrush-backend)
foodrush.local/orders/       -> order-service (foodrush-backend)
monitoring.foodrush.local/   -> grafana (foodrush-monitoring)
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

| Service | CPU Request | CPU Limit | Mem Request | Mem Limit |
|---------|-------------|-----------|-------------|-----------|
| frontend | 50m | 100m | 64Mi | 128Mi |
| api-gateway | 100m | 300m | 128Mi | 256Mi |
| restaurant-service | 100m | 300m | 128Mi | 256Mi |
| order-service | 100m | 300m | 128Mi | 256Mi |
| postgres | 200m | 500m | 256Mi | 512Mi |
| redis | 100m | 200m | 64Mi | 128Mi |

---

## 🧪 Kubernetes Concepts Demonstrated

| Concept | Where Used |
|---------|-----------|
| Namespaces | All services isolated by tier |
| Deployments | All services |
| Services | ClusterIP internal, NodePort external |
| ConfigMaps | Non-sensitive configuration |
| Secrets | Database passwords |
| PVC/PV | PostgreSQL persistent storage |
| Ingress | Single entry point routing |
| LimitRange | Per pod resource defaults |
| ResourceQuota | Total namespace resource budget |
| Health Checks | All Flask services |
| RBAC | Team based access control |
| Rolling Updates | Zero downtime deployments |
| Rollback | Instant version revert |
| Prometheus | Metrics collection |
| Grafana | Metrics visualization |
| Kustomize | Single command deployment |

---

## 📁 Folder Structure

<pre>
foodrush/
├── README.md
├── kustomization.yaml          # single command deploy/delete
├── namespaces/
│   └── namespaces.yaml
├── database/
│   ├── database.yaml              # postgres deployment+service+pvc
│   ├── redis.yaml                 # redis deployment+service
│   └── init.sql                   # database initialization
├── restaurant-service/
│   ├── app.py                     # v1 flask microservice
│   ├── app-v2.py                  # v2 with categories endpoint
│   ├── app-v3.py                  # v3 with prometheus metrics
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── Dockerfile-v2
│   ├── Dockerfile-v3
│   └── restaurant-service.yaml
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
├── resource-management/
│   ├── limitrange.yaml
│   └── resourcequota.yaml
├── rolling-updates/
│   └── rolling-update.yaml
└── monitoring/
    ├── servicemonitor.yaml
    └── grafana-dashboard.json
</pre>

---

## 🚀 Deployment Commands

### Prerequisites
<pre>
minikube start
minikube addons enable ingress
minikube addons enable metrics-server
eval $(minikube docker-env)

# Build all images
docker build -t restaurant-service:v1 restaurant-service/
docker build -t order-service:v1 order-service/
docker build -t api-gateway:v1 api-gateway/
docker build -t foodrush-frontend:v1 frontend/
</pre>

### Deploy Everything (Single Command)
<pre>
kubectl apply -k .
</pre>

### Verify Deployment
<pre>
kubectl get all -n foodrush-frontend
kubectl get all -n foodrush-backend
kubectl get all -n foodrush-data
</pre>

### Add Hosts Entry
<pre>
echo "$(minikube ip) foodrush.local" | sudo tee -a /etc/hosts
</pre>

### Access Application
<pre>
http://foodrush.local
</pre>

---

## 🧹 Cleanup Commands

### Delete Everything (Single Command)
<pre>
kubectl delete -k .
</pre>

### Delete Individual Namespaces
<pre>
kubectl delete namespace foodrush-frontend
kubectl delete namespace foodrush-backend
kubectl delete namespace foodrush-data
kubectl delete namespace foodrush-monitoring
</pre>

### Nuclear Option (full minikube reset)
<pre>
minikube delete
minikube start
</pre>

---

## 🔄 Rolling Update Commands

<pre>
# Check rollout status
kubectl rollout status deployment/restaurant-service -n foodrush-backend

# View rollout history
kubectl rollout history deployment/restaurant-service -n foodrush-backend

# Rollback to previous version
kubectl rollout undo deployment/restaurant-service -n foodrush-backend

# Rollback to specific revision
kubectl rollout undo deployment/restaurant-service -n foodrush-backend --to-revision=2
</pre>

---

## 📝 Notes

- Secrets are hardcoded for learning only
- In production use HashiCorp Vault or AWS Secrets Manager
- Images built locally using eval $(minikube docker-env)
- In production images pushed to ECR/ACR/GCR then pulled by cluster
- ResourceQuota set conservatively - increase if test pods hit quota limits
- Kustomize file applies resources in correct dependency order