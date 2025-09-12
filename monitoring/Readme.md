# 📊 Kubernetes Monitoring with Prometheus & Grafana (Minikube)

This guide sets up **full cluster monitoring** (nodes, pods, deployments, workloads, CPU/memory, and network) on a **Minikube cluster** using the [kube-prometheus-stack](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack) Helm chart.

---

## 🚀 Prerequisites
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) installed  
- [Helm](https://helm.sh/docs/intro/install/) installed  
- `kubectl` configured for Minikube  

---

## 🛠️ Step 1: Start Minikube
Make sure your Minikube cluster has enough resources:
```bash
minikube stop
minikube start --driver=docker 
minikube addons enable metrics-server
```
## 🛠️ Step 2: Add Helm Repos
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

## 🛠️ Step 3: Create Monitoring Namespace
```bash
kubectl create namespace monitoring
```

## 🛠️ Step 4: Install kube-prometheus-stack
```bash
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
```

## 🛠️ Step 5: Verify Pods
Check that all monitoring components are running:
```bash
kubectl get pods -n monitoring
```
## 🛠️ Step 6: Access Grafana
Port-forward Grafana:
```bash
kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80
```
Now open Grafana at: http://localhost:3000

### Get the admin password:
```bash
kubectl get secret -n monitoring monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 --decode; echo
```

## 🛠️ Step 7: Access Prometheus

Find the Prometheus service:
```bash
kubectl get svc -n monitoring | grep prometheus
```

### Port-forward:
```bash
kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-stack-prometheus 9090:9090
```
Now open Prometheus at: http://localhost:9090
