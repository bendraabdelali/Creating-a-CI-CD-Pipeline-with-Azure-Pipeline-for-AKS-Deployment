[![Python application](https://github.com/bendraabdelali/Sentiment-Analysis/actions/workflows/python-app.yml/badge.svg?branch=main&event=push)](https://github.com/bendraabdelali/Sentiment-Analysis/actions/workflows/python-app.yml)

# K8S-APP-CI-CD 

In this project we will create :
- 1 Create a Kubernetes cluster with Azure Kubernetes Service using Terraform
[` Kubernetes cluster with Terraform`](https://github.com/bendraabdelali/K8s-CI-Cd-Azure-Devops-Terraform-#1--create-a-kubernetes-cluster-with-terraform)
- 2  Create mongodb database and Prometheuse and Grfana using Terraform and helm .  
- 3 Github Action pipeline that continuously build ,test  our app using  github actions . and trriger  Azure Devops  Pipelines.
- 4 Azure Devops pipeline that continuously  deploys to  AKS.  the images are pushed to your DockerHu  and the manifests are then deployed to  AKS cluster.
<br>
![image](./images/image.png.png)


##  Prerequisites

To run this project, you will need to install 

- [`Azure Account`](https://azure.microsoft.com/en-us/free/?WT.mc_id=A261C142F) 
- [`Azure Devops Account`](https://azure.microsoft.com/en-us/products/devops/)
- [`Azure Cli`](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [`Terrafrom`](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [`Kubectl`](https://kubernetes.io/docs/tasks/tools/)



## Usage
### 1- Create a Kubernetes cluster with Terraform 
first go and run House_predict_.ipynb to create model.joblib 
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
Acces Grafana user:admin password: admin
 ```bash
  kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80
```

Acces Prometheus
 ```bash
 kubectl port-forward prometheus-prometheus-prometheus-0  80:9090 -n monitoring
```


### 2- Run  the pipeline
To Run the pipeline Just push new Commit in the main branch 
### 3- Check the pipline 




## Access to Application 
#### 
acces th app 
 ```bash
 kubectl get svc myapp-svc -n monitoring 
```
copy the  external ip to use the application
![image](./image/Aks.png)






## Built With
- Github Action
- Azure Devops
- Terrafrom
- Kubernetes
- Azure
- Docker
- Grafana
- Prometheus
- Mongo DB
- Flask


## Authors
Bendra Abdelali
- [Profile](https://github.com/bendraabdelali)
- [Linkedin](https://www.linkedin.com/in/abdelali-bendra-934755182/)
- [Kaggle](https://www.kaggle.com/bendraabdelali)