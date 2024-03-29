
# Creating a CI/CD Pipeline with Azure Pipeline for AKS Deployment

In this project we will create :
- 1 - Create a Kubernetes cluster with Azure Kubernetes Service using Terraform
[` Kubernetes cluster with Terraform`](https://github.com/bendraabdelali/K8s-CI-Cd-Azure-Devops-Terraform-#1--create-a-kubernetes-cluster-with-terraform)
- 2 - Create mongodb database and Prometheuse and Grfana using Terraform and helm .  
- 3 - Azure Devops pipeline that continuously build ,test, deploys  our app  to  AKS. the images are pushed to  DockerHub  and the manifests are then deployed to  AKS cluster

<br>


<p align="center">
  <img src="./images/image.png.png" />
</p>

##  Prerequisites

To run this project, you will need:

- [`Azure Account`](https://azure.microsoft.com/) 
- [`Azure Devops Account`](https://azure.microsoft.com/en-us/products/devops/)
- [`Azure CLI`](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [`Terrafrom`](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [`Kubectl`](https://kubernetes.io/docs/tasks/tools/)

## Usage
### 1- Create a Kubernetes cluster with Terraform 
 ```bash
  cd IAC
  az login
  Terraform apply 
```
Verify the health of the cluster
 ```bash
  kubectl get nodes
  kubect get pods 
  kubectl get all -n monitoring
```
#### Access Grafana 

 ```bash
   kubectl get svc prometheus-grafana -n monitoring
```
Copy the  external ip and past it into browser  to use grafana Dashboard
- User: admin
- Password: admin
![grafana](./images/grafana.png)

#### Access Prometheus

 ```bash
 kubectl port-forward prometheus-prometheus-prometheus-0  80:9090 -n monitoring
```
 - ![prometheuse](./images/prometheuse.png)

### 2- Run  the pipeline
To Run the pipeline Just push new Commit in the main branch 
### 3- Check the pipeline 
#### - Azure Pipline 
 ![AzurePipline](./images/check_Azure_Pipline.png)
#### - Docker Hub new Images is pushed 
 ![AzurePipline](./images/check_Docker-Hub.png)
 #### - check the realese Pipeline
 ![AzurePipline](./images/check_realese.png)

## Access to Application 
#### 
 ```bash
 kubectl get svc myapp-svc -n monitoring 
```
copy the  external ip and past it into browser  to use the application
![app](./images/app.png)

## Built With
- Github Action
- Azure Devops
- Terrafrom
- Kubernetes
- Docker
- Grafana
- Prometheus
- MongoDB
- Flask


## Authors
Bendra Abdelali
- [Profile](https://github.com/bendraabdelali)
- [Linkedin](https://www.linkedin.com/in/abdelali-bendra-934755182/)
- [Kaggle](https://www.kaggle.com/bendraabdelali)
