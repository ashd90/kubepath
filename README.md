# 🚀 My DevOps Journey — Docker to Production Kubernetes

A complete hands-on learning path covering Docker, Kubernetes, Helm, and Istio
from absolute beginner to production-ready deployments.

---

## 👤 About This Repository

This repository documents my personal DevOps learning journey.
Every concept is learned through micro-projects with real problems,
hands-on solutions, and debugging practice.

**Learning Style:**

- Real world analogies before theory
- Feel the problem before learning the solution
- One concept at a time
- Every project committed to Git

---

## 🗺️ Learning Roadmap

### Stage 0 — Environment & Basics ✅
>
> Understand why containers exist by feeling the pain without them

- What is virtualization vs containers
- Why DevOps needs containers
- Running apps manually and hitting dependency problems

### Stage 1 — Docker Fundamentals ✅
>
> Learn Docker from scratch through 5 micro projects

- Project 1: First container
- Project 2: Writing proper Dockerfiles + layer caching
- Project 3: Environment variables
- Project 4: Persistent storage with volumes
- Project 5: Container networking

### Stage 2 — Multi Container Systems ✅
>
> Build a real 3-tier application with Docker Compose

- Project 1: Frontend + Backend + Database
- Docker Compose orchestration
- Named volumes and networks
- Service communication
- Discovering scaling limitations

### Stage 3 — Kubernetes Motivation ✅
>
> Understand why Kubernetes exists through Docker Compose limitations

- Manual scaling problems
- No self healing
- Single machine limitations
- Introduction to Kubernetes concepts

### Stage 4 — Kubernetes Beginner Projects 🔄 (In Progress)
>
> Master Kubernetes fundamentals through hands-on projects

- Project 1: First Pod and Deployment ✅
- Project 2: Service Networking ✅
- Project 3: ConfigMaps and Secrets ✅
- Project 4: Persistent Storage (PV/PVC) ✅
- Project 5: Scaling and Health Checks ⬅️ current

### Stage 5 — Production Kubernetes (Minikube)
>
> Production patterns on local cluster

- Ingress controllers
- Horizontal Pod Autoscaling
- Resource limits and requests
- RBAC and security
- Observability basics

### Stage 5b — Self Managed Kubernetes (kubeadm)
>
> Build a real multi-node cluster from scratch

- Setup 3 VMs with VirtualBox
- Install and configure kubeadm
- Join worker nodes to cluster
- Install networking (Flannel/Calico)
- Install Ingress, Storage, Monitoring

### Stage 5c — Managed Kubernetes (AKS)
>
> Deploy to real cloud managed Kubernetes

- Setup Azure AKS cluster
- Deploy applications to cloud
- Cloud storage and networking
- Cost optimization strategies
- Spot instances and auto scaling

### Stage 6 — Helm
>
> Package and manage Kubernetes applications

- Project 1: Convert YAML to Helm charts
- Templates and values
- Chart dependencies
- Environment specific deployments

### Stage 7 — Istio Service Mesh
>
> Advanced traffic management and security

- Project 1: Traffic routing
- Canary deployments
- mTLS security
- Service observability

### Final Capstone Project
>
> Full production simulation

- CI/CD pipeline
- Multi environment deployments
- Monitoring stack (Prometheus + Grafana)
- Security hardening
- Version rollback
- Microservices architecture

---

## 📁 Repository Structure

---

## 🛠️ Tools & Technologies

| Tool | Purpose | Stage Introduced |
|------|---------|-----------------|
| Docker | Containerization | Stage 1 |
| Docker Compose | Multi-container orchestration | Stage 2 |
| Kubernetes | Container orchestration | Stage 4 |
| Minikube | Local Kubernetes cluster | Stage 4 |
| kubeadm | Self managed cluster setup | Stage 5b |
| AKS | Managed cloud Kubernetes | Stage 5c |
| Helm | Kubernetes package manager | Stage 6 |
| Istio | Service mesh | Stage 7 |

---

## 📚 Key Concepts Learned

| Concept | Description | Stage |
|---------|-------------|-------|
| Containers | Isolated app environments | Stage 1 |
| Dockerfile | Image build instructions | Stage 1 |
| Layer Caching | Faster Docker builds | Stage 1 |
| Volumes | Persistent data storage | Stage 1,4 |
| Networks | Container communication | Stage 1,2 |
| Docker Compose | Multi-container management | Stage 2 |
| Pod | Smallest Kubernetes unit | Stage 4 |
| Deployment | Self healing pod manager | Stage 4 |
| Service | Stable network endpoint | Stage 4 |
| ConfigMap | Non-sensitive configuration | Stage 4 |
| Secret | Sensitive configuration | Stage 4 |
| PV/PVC | Kubernetes persistent storage | Stage 4 |
| HPA | Horizontal Pod Autoscaling | Stage 4 |

---

## 🔗 Resources

- [Docker Documentation](https://docs.docker.com)
- [Kubernetes Documentation](https://kubernetes.io/docs)
- [Minikube Documentation](https://minikube.sigs.k8s.io/docs)
- [Helm Documentation](https://helm.sh/docs)
- [Istio Documentation](https://istio.io/docs)

---

## 📈 Progress

- [x] Stage 0 — Environment & Basics
- [x] Stage 1 — Docker Fundamentals
- [x] Stage 2 — Multi Container Systems
- [x] Stage 3 — Kubernetes Motivation
- [ ] Stage 4 — Kubernetes Beginner Projects (in progress)
- [ ] Stage 5 — Production Kubernetes
- [ ] Stage 5b — Self Managed Kubernetes
- [ ] Stage 5c — Managed Kubernetes (AKS)
- [ ] Stage 6 — Helm
- [ ] Stage 7 — Istio
- [ ] Final Capstone Project
