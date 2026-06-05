# 🚀 My DevOps Journey — Docker to Production Kubernetes

A complete hands-on learning path covering Docker, Kubernetes, ArgoCD, Helm, and Istio
from absolute beginner to production-ready deployments.

---

## 👤 About

Personal DevOps learning journey through micro-projects.
Every concept follows: **Analogy → Problem → Solution → Project → Debug → Challenge**

---

## 🗺️ Roadmap

| Stage | Topic | Status |
|-------|-------|--------|
| 0 | Environment and Basics | ✅ Done |
| 1 | Docker Fundamentals (5 projects) | ✅ Done |
| 2 | Multi Container Systems | ✅ Done |
| 3 | Kubernetes Motivation | ✅ Done |
| 4 | Kubernetes Beginner Projects | ✅ Done |
| 4-ext | Workloads: StatefulSets, DaemonSets, Jobs, CronJobs | ⏳ Upcoming |
| 4-ext | Scheduling: VPA, Node Affinity, Taints, Resource Quotas | ⏳ Upcoming |
| 4-ext | Security: PSS, Image Scanning, Network Policies | ⏳ Upcoming |
| 4-ext | Cluster Admin: Upgrade, CRDs | ⏳ Upcoming |
| 5 | Production Kubernetes - FoodRush App | ✅ Done |
| 5b | Self Managed Kubernetes (kubeadm) | ⏳ Upcoming |
| 5c | Managed Kubernetes (AKS) | ⏳ Upcoming |
| 5d | ArgoCD - GitOps In Depth | ⏳ Upcoming |
| 6 | Helm - In Depth | ⏳ Upcoming |
| 7 | Istio Service Mesh - In Depth | ⏳ Upcoming |
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
│   ├── project-2-first-dockerfile/
│   ├── project-3-env-variables/
│   ├── project-4-persistent-storage/
│   └── project-5-container-networking/
├── stage-2/
│   └── project-1-three-tier-app/
│       ├── docker-compose.yml
│       ├── frontend/
│       ├── backend/
│       └── db/
├── stage-4/
│   ├── project-1-single-container/
│   ├── project-2-service-networking/
│   ├── project-3-config-management/
│   ├── project-4-persistent-storage/
│   ├── project-5-scaling-healthchecks/
│   ├── project-6-workloads/
│   │   ├── statefulsets/
│   │   ├── daemonsets/
│   │   ├── replicasets/
│   │   ├── jobs/
│   │   └── cronjobs/
│   ├── project-7-scheduling/
│   │   ├── hpa-production/
│   │   ├── vpa/
│   │   ├── node-affinity/
│   │   ├── taints-tolerations/
│   │   └── resource-quotas/
│   ├── project-8-security/
│   │   ├── pod-security-standards/
│   │   ├── image-scanning/
│   │   ├── network-policies/
│   │   └── secrets-encryption/
│   └── project-9-cluster-admin/
│       ├── cluster-upgrade/
│       └── crds/
├── stage-5/
│   └── project-1-production-k8s/
│       ├── ingress/                   # ingress learning exercises
│       └── foodrush/                  # production grade app
│           ├── kustomization.yaml     # single command deploy
│           ├── namespaces/
│           ├── database/
│           ├── restaurant-service/
│           ├── order-service/
│           ├── api-gateway/
│           ├── frontend/
│           ├── ingress/
│           ├── rbac/
│           ├── resource-management/
│           ├── rolling-updates/
│           └── monitoring/
├── stage-5b/
│   └── project-1-kubeadm/             # self managed cluster
├── stage-5c/
│   └── project-1-aks/                 # managed cloud k8s
├── stage-5d/
│   └── project-1-argocd/              # gitops in depth
│       ├── install/
│       ├── applications/
│       ├── app-of-apps/
│       ├── multi-env/
│       └── advanced/
├── stage-6/
│   └── project-1-helm-charts/         # helm in depth
│       ├── basics/
│       ├── foodrush-chart/
│       ├── dependencies/
│       └── advanced/
├── stage-7/
│   └── project-1-istio-mesh/          # istio in depth
│       ├── install/
│       ├── traffic-management/
│       ├── canary/
│       ├── mtls/
│       └── observability/
└── capstone/
    ├── ci-cd/
    ├── multi-env/
    ├── monitoring/
    └── microservices/
</pre>

---

## 🛠️ Tools and Technologies

| Tool | Purpose | Stage |
|------|---------|-------|
| Docker | Containerization | 1 |
| Docker Compose | Multi-container orchestration | 2 |
| Kubernetes | Container orchestration | 4 |
| Minikube | Local K8s cluster | 4 |
| Kustomize | K8s config management | 5 |
| kubeadm | Self managed cluster setup | 5b |
| AKS | Managed cloud Kubernetes | 5c |
| ArgoCD | GitOps continuous delivery | 5d |
| Helm | Kubernetes package manager | 6 |
| Istio | Service mesh | 7 |
| Prometheus | Metrics collection | 5 |
| Grafana | Metrics visualization | 5 |

---

## 📚 Key Concepts by Stage

| Concept | Stage |
|---------|-------|
| Containers and Dockerfiles | 1 |
| Layer Caching | 1 |
| Volumes and Networks | 1-2 |
| Docker Compose | 2 |
| Pod and Deployment | 4 |
| Service and Networking | 4 |
| ConfigMap and Secret | 4 |
| PersistentVolume and PVC | 4 |
| HPA and Health Checks | 4 |
| StatefulSets, DaemonSets | 4-ext |
| Jobs and CronJobs | 4-ext |
| VPA, Node Affinity, Taints | 4-ext |
| Network Policies, PSS | 4-ext |
| CRDs, Cluster Upgrade | 4-ext |
| Namespaces and RBAC | 5 |
| Ingress and Annotations | 5 |
| Resource Management | 5 |
| Rolling Updates and Rollback | 5 |
| Observability | 5 |
| Kustomize | 5 |
| GitOps with ArgoCD | 5d |
| Helm Charts | 6 |
| Istio Traffic Management | 7 |
| Istio mTLS and Canary | 7 |

---

## 📈 Progress

- [x] Stage 0 — Environment and Basics
- [x] Stage 1 — Docker Fundamentals
- [x] Stage 2 — Multi Container Systems
- [x] Stage 3 — Kubernetes Motivation
- [x] Stage 4 — Kubernetes Beginner Projects
- [ ] Stage 4-ext — Workloads, Scheduling, Security, Cluster Admin
- [x] Stage 5 — Production Kubernetes (FoodRush)
- [ ] Stage 5b — Self Managed Kubernetes (kubeadm)
- [ ] Stage 5c — Managed Kubernetes (AKS)
- [ ] Stage 5d — ArgoCD GitOps (In Depth)
- [ ] Stage 6 — Helm (In Depth)
- [ ] Stage 7 — Istio (In Depth)
- [ ] Final Capstone Project

---

## 🔗 Resources

- [Docker Docs](https://docs.docker.com)
- [Kubernetes Docs](https://kubernetes.io/docs)
- [Kustomize Docs](https://kustomize.io)
- [ArgoCD Docs](https://argo-cd.readthedocs.io)
- [Helm Docs](https://helm.sh/docs)
- [Istio Docs](https://istio.io/docs)
- [Minikube Docs](https://minikube.sigs.k8s.io/docs)