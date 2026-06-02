# 🚀 My DevOps Journey — Docker to Production Kubernetes

A hands-on learning path from containers to production Kubernetes.

---

## 👤 About

Personal DevOps learning journey through micro-projects.
Every concept follows: **Analogy → Problem → Solution → Project → Debug → Challenge**

---

## 🗺️ Roadmap

| Stage | Topic | Status |
|-------|-------|--------|
| 0 | Environment & Basics | ✅ Done |
| 1 | Docker Fundamentals (5 projects) | ✅ Done |
| 2 | Multi Container Systems | ✅ Done |
| 3 | Kubernetes Motivation | ✅ Done |
| 4 | Kubernetes Beginner Projects (extended) | 🔄 In Progress |
| 5 | Production Kubernetes (Minikube) | ⏳ Upcoming |
| 5b | Self Managed Kubernetes (kubeadm) | ⏳ Upcoming |
| 5c | Managed Kubernetes (AKS) | ⏳ Upcoming |
| 6 | Helm | ⏳ Upcoming |
| 7 | Istio Service Mesh | ⏳ Upcoming |
| 🏁 | Capstone Project | ⏳ Upcoming |

---

## 📁 Repository Structure

<pre>
kubepath/
├── README.md
├── stage-0/
│   └── project-1-no-docker/
│       └── app.py
├── stage-1/
│   ├── project-1-first-container/
│   │   ├── Dockerfile
│   │   └── app.py
│   ├── project-2-first-dockerfile/
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   └── requirements.txt
│   ├── project-3-env-variables/
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── .env                  # gitignored
│   │   └── .gitignore
│   ├── project-4-persistent-storage/
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── data/                 # mounted volume
│   └── project-5-container-networking/
│       ├── Dockerfile
│       ├── app.py
│       └── requirements.txt
├── stage-2/
│   └── project-1-three-tier-app/
│       ├── docker-compose.yml
│       ├── frontend/
│       │   ├── Dockerfile
│       │   ├── index.html
│       │   └── nginx.conf
│       ├── backend/
│       │   ├── Dockerfile
│       │   ├── app.py
│       │   └── requirements.txt
│       └── db/
│           └── init.sql
├── stage-4/
│   ├── project-1-single-container/
│   │   ├── pod.yaml
│   │   └── deployment.yaml
│   ├── project-2-service-networking/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── project-3-config-management/
│   │   ├── configmap.yaml
│   │   ├── secret.yaml
│   │   └── deployment.yaml
│   ├── project-4-persistent-storage/
│   │   ├── pv.yaml
│   │   ├── pvc.yaml
│   │   └── deployment.yaml
│   └── project-5-scaling-healthchecks/
│       ├── deployment.yaml
│       └── hpa.yaml
├── stage-5/
│   └── project-1-production-k8s/
├── stage-5b/
│   └── project-1-kubeadm/
│       └── setup-guide.md
├── stage-5c/
│   └── project-1-aks/
│       └── setup-guide.md
├── stage-6/
│   └── project-1-helm-charts/
└── stage-7/
    └── project-1-istio-mesh/
</pre>

---

## 🛠️ Tools

| Tool | Purpose | Stage |
|------|---------|-------|
| Docker | Containerization | 1 |
| Docker Compose | Multi-container orchestration | 2 |
| Kubernetes | Container orchestration | 4 |
| Minikube | Local K8s cluster | 4 |
| kubeadm | Self managed cluster | 5b |
| AKS | Managed cloud K8s | 5c |
| Helm | K8s package manager | 6 |
| Istio | Service mesh | 7 |

---

## 📚 Key Concepts

| Concept | Stage |
|---------|-------|
| Containers & Dockerfiles | 1 |
| Layer Caching | 1 |
| Volumes & Networks | 1-2 |
| Docker Compose | 2 |
| Pod & Deployment | 4 |
| Service & Networking | 4 |
| ConfigMap & Secret | 4 |
| PersistentVolume/Claim | 4 |
| HPA & Health Checks | 4 |
| Ingress & RBAC | 5 |
| Helm Charts | 6 |
| Istio mTLS & Canary | 7 |

---

## 📈 Progress

- [x] Stage 0 — Environment & Basics
- [x] Stage 1 — Docker Fundamentals
- [x] Stage 2 — Multi Container Systems
- [x] Stage 3 — Kubernetes Motivation
- [ ] Stage 4 — Kubernetes Beginner Projects (in progress)
- [ ] Stage 5 — Production Kubernetes
- [ ] Stage 5b — Self Managed Kubernetes (kubeadm)
- [ ] Stage 5c — Managed Kubernetes (AKS)
- [ ] Stage 6 — Helm
- [ ] Stage 7 — Istio
- [ ] Final Capstone Project

---

## 🔗 Resources

- [Docker Docs](https://docs.docker.com)
- [Kubernetes Docs](https://kubernetes.io/docs)
- [Minikube Docs](https://minikube.sigs.k8s.io/docs)
- [Helm Docs](https://helm.sh/docs)
- [Istio Docs](https://istio.io/docs)