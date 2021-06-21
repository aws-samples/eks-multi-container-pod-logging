# EKS Multi Container Pod Logging

This demonstration has the pusporse of showing how to use multi-container Pods to export application logs to stdout on Amazon EKS, in that way a log proccessor can collect all the logs and send to a log centralizer.

**This demonstration was tested in us-east-1 region**

## Architecture

## Pre Reqs

- [eksctl](https://eksctl.io/)
- [awscli](https://aws.amazon.com/cli/)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/)

## Provision EKS cluster

We are going to use eksctl to provision our EKS cluster for this demonstration, eksctl will provision the Kubernetes master, nodes and **also the VPC**.

```shell
eksctl create cluster -f kubernetes-cluster-us-east-1.yaml
```

Now we have to configure our `~/.kube/config` file in order to access our cluster using kubectl.

```shell
aws eks --region us-east-1 update-kubeconfig --name kubelogs-cluster
```

This will update your kube config file, now let's test if we can access our cluster.

```shell
kubectl get nodes
```

## Creating our application Docker image

In this step we are going to build our application Docker image and create our ECR repository, after that we are going to push the image to the repository, so we will be able to create our application inside our Amazon EKS cluster.
