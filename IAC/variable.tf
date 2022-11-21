variable "kube_config" {
  type    = string
  default = "~/.kube/config"
}


variable "namespace" {
  type    = string
}

variable "grafana_pass" {
  type    = string
 
}
