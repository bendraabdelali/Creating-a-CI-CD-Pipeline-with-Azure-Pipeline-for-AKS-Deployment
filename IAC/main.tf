
resource "kubernetes_namespace" "monitoring" {
  metadata {

    name = var.namespace
  }
}

resource "helm_release" "prometheus" {
  chart      = "kube-prometheus-stack"
  name       = "prometheus"
  namespace  = var.namespace
  repository = "https://prometheus-community.github.io/helm-charts"

  set {
    name  = "nameOverride"
    value = "prometheus"
  }
  set {
    name  = "namespaceOverride"
    value = var.namespace
  }
  set {
    name  = "grafana.adminPassword"
    value = var.grafana_pass
  }

}


resource "helm_release" "mongo" {
  chart      = "mongodb"
  name       = "mongodb"
  namespace  = var.namespace
  repository = "https://charts.bitnami.com/bitnami"
  depends_on = [
    helm_release.prometheus
  ]

  set{
    name= "nameOverride"
    value="mongodb"
  }
  set {
    name = "metrics.enabled"
    value="true"
  }

  set {
    name="metrics.serviceMonitor.enabled"
    value = true
  }

  set {
    name = "metrics.serviceMonitor.namespace"
    value = var.namespace
  }
  set{
    name="auth.enabled"
    value= false
  }
  set {
    name = "metrics.serviceMonitor.labels.release"
    value = "prometheus"
  }
}
