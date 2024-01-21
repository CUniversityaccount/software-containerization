# Containerization course vu

A simple application where people can set key and values into the application.

## Ingress Image

For minikube or microk8s enable the addon ingress. They use automatically the NGINX igress controller.

For configuring the local DNS see the tutorial for the minikube:
https://minikube.sigs.k8s.io/docs/handbook/addons/ingress-dns/

Use the command to update the network manager on ubuntu:

```
sudo mv /etc/resolv.conf /etc/resolv.conf.old
systemctl restart NetworkManager.service
```

## Applying the services

## DEADLINE - TO DO

- 18 - deadline for frontend otherwise @quarti jumps on it
- unknown - UML @quarti
- 18 - soft deadline for kubernetes oporting supporting api external access, and horizontal scaling
- 16 - 8pm heads up on kubernetes material
- 16 - 8pm heads up on lecture 4 persistant volumes
