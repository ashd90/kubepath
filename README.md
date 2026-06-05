# 🚀 kubepath — Docker to Production Kubernetes

A complete hands-on learning path from Docker basics to production-grade Kubernetes,
ArgoCD GitOps, Helm, and Istio Service Mesh.

---

## 👤 About

Personal DevOps learning journey through real-world micro-projects.
Every concept follows: **Analogy → Problem → Solution → Hands-on → Debug → Challenge**

---

## 🗺️ Learning Path

| # | Directory | Topic | Status |
|---|-----------|-------|--------|
| 01 | 01-docker-fundamentals | Containers, Dockerfiles, Volumes, Networking | ✅ Done |
| 02 | 02-multi-container-docker | Docker Compose, 3-tier app | ✅ Done |
| 03 | 03-kubernetes-basics | Pods, Deployments, Services, ConfigMaps, HPA | ✅ Done |
| 04 | 04-kubernetes-workloads | StatefulSets, DaemonSets, Jobs, CronJobs | ⏳ Upcoming |
| 05 | 05-kubernetes-scheduling | VPA, Node Affinity, Taints, Resource Quotas | ⏳ Upcoming |
| 06 | 06-kubernetes-security | PSS, Image Scanning, Network Policies | ⏳ Upcoming |
| 07 | 07-kubernetes-cluster-admin | Cluster Upgrade, CRDs | ⏳ Upcoming |
| 08 | 08-production-kubernetes | FoodRush production app, Ingress, RBAC, Observability | ✅ Done |
| 09 | 09-self-managed-cluster | kubeadm, multi-node cluster setup | ⏳ Upcoming |
| 10 | 10-managed-cloud-kubernetes | AKS, cloud storage, cost optimization | ⏳ Upcoming |
| 11 | 11-gitops-argocd | ArgoCD, GitOps, App of Apps, multi-env | ⏳ Upcoming |
| 12 | 12-helm | Helm charts, templates, dependencies | ⏳ Upcoming |
| 13 | 13-istio-service-mesh | Traffic management, mTLS, canary, observability | ⏳ Upcoming |
| 14 | 14-capstone-project | Full production simulation | ⏳ Upcoming |

---

## 📁 Repository Structure

<pre>
kubepath/
├── 01-docker-fundamentals/
│   ├── 01-no-docker-problem/          # running apps without docker, dependency hell
│   ├── 02-first-container/            # first docker run, images vs containers
│   ├── 03-dockerfile-basics/          # writing dockerfiles, layer caching
│   ├── 04-env-variables/              # -e flag, .env files, runtime config
│   ├── 05-persistent-storage/         # bind mounts, named volumes
│   └── 06-container-networking/       # docker networks, container DNS
├── 02-multi-container-docker/
│   └── three-tier-app/                # frontend+backend+postgres, docker compose
├── 03-kubernetes-basics/
│   ├── 01-pods-and-deployments/       # pod lifecycle, self healing deployments
│   ├── 02-services-networking/        # clusterIP, nodePort, load balancing
│   ├── 03-configmaps-secrets/         # config injection, secret management
│   ├── 04-persistent-storage/         # PV, PVC, static vs dynamic provisioning
│   └── 05-hpa-healthchecks/           # liveness, readiness, autoscaling
├── 04-kubernetes-workloads/
│   ├── statefulsets/                  # ordered pods, stable network identity
│   ├── daemonsets/                    # one pod per node, log collectors
│   ├── replicasets/                   # how deployments manage pods under hood
│   ├── jobs/                          # batch processing, run to completion
│   └── cronjobs/                      # scheduled tasks, cleanup jobs
├── 05-kubernetes-scheduling/
│   ├── hpa-production/                # real world autoscaling with foodrush
│   ├── vpa/                           # vertical pod autoscaler
│   ├── node-affinity/                 # pod placement rules
│   ├── taints-tolerations/            # node restrictions and exceptions
│   └── resource-quotas/               # namespace level resource budgets
├── 06-kubernetes-security/
│   ├── pod-security-standards/        # restrict pod capabilities
│   ├── image-scanning/                # trivy, vulnerability detection
│   ├── network-policies/              # firewall rules between pods
│   └── secrets-encryption/            # encrypt secrets at rest in etcd
├── 07-kubernetes-cluster-admin/
│   ├── cluster-upgrade/               # rolling upgrades, zero downtime
│   └── crds/                          # extending kubernetes API
├── 08-production-kubernetes/
│   ├── ingress-learning/              # nginx ingress, path and host routing
│   └── foodrush/                      # production grade food delivery app
│       ├── kustomization.yaml         # kubectl apply -k . deploys everything
│       ├── namespaces/
│       ├── database/
│       ├── restaurant-service/
│       ├── order-service/
│       ├── api-gateway/
│       ├── frontend/
│       ├── ingress/
│       ├── rbac/
│       ├── resource-management/
│       ├── rolling-updates/
│       └── monitoring/
├── 09-self-managed-cluster/
│   └── kubeadm-setup/                 # 3 node cluster from scratch
├── 10-managed-cloud-kubernetes/
│   └── aks-deployment/                # azure kubernetes service
├── 11-gitops-argocd/
│   ├── install/                       # argocd setup on minikube
│   ├── applications/                  # deploying apps via argocd
│   ├── app-of-apps/                   # managing multiple apps
│   ├── multi-env/                     # dev staging prod with argocd
│   └── advanced/                      # sync policies, hooks, notifications
├── 12-helm/
│   ├── basics/                        # chart structure, templates, values
│   ├── foodrush-chart/                # convert foodrush to helm chart
│   ├── dependencies/                  # chart dependencies, subcharts
│   └── advanced/                      # hooks, tests, library charts
├── 13-istio-service-mesh/
│   ├── install/                       # istio setup, sidecar injection
│   ├── traffic-management/            # virtual services, destination rules
│   ├── canary/                        # gradual traffic shifting
│   ├── mtls/                          # mutual TLS between services
│   └── observability/                 # kiali, jaeger, prometheus
└── 14-capstone-project/
    ├── ci-cd/                             # github actions pipeline
    ├── multi-env/                         # dev staging prod namespaces
    ├── monitoring/                        # full observability stack
    └── microservices/                     # full microservices architecture
</pre>

---

## 🛠️ Tools and Technologies

| Tool | Purpose | Directory |
|------|---------|-----------|
| Docker | Containerization | 01, 02 |
| Docker Compose | Multi-container orchestration | 02 |
| Kubernetes | Container orchestration | 03-08 |
| Minikube | Local K8s cluster | 03-08 |
| Kustomize | K8s config management | 08 |
| kubeadm | Self managed cluster | 09 |
| AKS | Managed cloud Kubernetes | 10 |
| ArgoCD | GitOps continuous delivery | 11 |
| Helm | Kubernetes package manager | 12 |
| Istio | Service mesh | 13 |
| Prometheus | Metrics collection | 08, 13 |
| Grafana | Metrics visualization | 08, 13 |
| Trivy | Image vulnerability scanning | 06 |

---

## 📚 Key Concepts by Directory

| Concept | Directory |
|---------|-----------|
| Containers, Dockerfiles, Layer Caching | 01 |
| Volumes, Networks, Environment Variables | 01 |
| Docker Compose, Service Communication | 02 |
| Pods, Deployments, Self Healing | 03 |
| Services, ClusterIP, NodePort | 03 |
| ConfigMaps, Secrets | 03 |
| PersistentVolume, PVC, StorageClass | 03 |
| HPA, Liveness, Readiness Probes | 03 |
| StatefulSets, DaemonSets, ReplicaSets | 04 |
| Jobs, CronJobs | 04 |
| VPA, Node Affinity, Taints, Tolerations | 05 |
| Resource Quotas, LimitRange | 05 |
| Pod Security Standards, Image Scanning | 06 |
| Network Policies, Secrets Encryption | 06 |
| Cluster Upgrade, CRDs | 07 |
| Namespaces, RBAC, Ingress, Kustomize | 08 |
| Rolling Updates, Rollback, Observability | 08 |
| FoodRush Production App | 08 |
| kubeadm cluster setup | 09 |
| Managed Kubernetes, Cloud Storage | 10 |
| GitOps, ArgoCD, App of Apps | 11 |
| Helm Charts, Templates, Dependencies | 12 |
| Istio Traffic Management, mTLS, Canary | 13 |

---

## 📈 Progress

- [x] 01 — Docker Fundamentals
- [x] 02 — Multi Container Docker
- [x] 03 — Kubernetes Basics
- [ ] 04 — Kubernetes Workloads
- [ ] 05 — Kubernetes Scheduling
- [ ] 06 — Kubernetes Security
- [ ] 07 — Kubernetes Cluster Admin
- [x] 08 — Production Kubernetes (FoodRush)
- [ ] 09 — Self Managed Cluster (kubeadm)
- [ ] 10 — Managed Cloud Kubernetes (AKS)
- [ ] 11 — GitOps with ArgoCD
- [ ] 12 — Helm
- [ ] 13 — Istio Service Mesh
- [ ] 14 — Capstone Project

---

## 🔗 Resources

- [Docker Docs](https://docs.docker.com)
- [Kubernetes Docs](https://kubernetes.io/docs)
- [Kustomize Docs](https://kustomize.io)
- [ArgoCD Docs](https://argo-cd.readthedocs.io)
- [Helm Docs](https://helm.sh/docs)
- [Istio Docs](https://istio.io/docs)
- [Minikube Docs](https://minikube.sigs.k8s.io/docs)