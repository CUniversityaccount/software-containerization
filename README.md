# Project overview

### Sequence diagram

![Screenshot](Sequence_Diagram_drawio.png)

### Deployment diagram

![Screenshot](Deployment_uml_mk3.png)

# Instructions Local

## To build and run everything Locally

```bash
chmod +x code_to_run_it.sh
./code_to_run_it.sh
```

## the script does:

### inside the dockerfile folder build the images

To build different docker images you will use the following

```bash
docker build -t api-service:latest ./api
docker build -t ui-service:latest ./frontend
```

### Place the images in microk8s registry

tag the images for registry

```bash
docker tag api-service:latest localhost:32000/api-service:latest
docker tag ui-service:latest localhost:32000/ui-service:latest
```

You can push images to registery of microk8s through:

push the images to registry

```bash
docker push localhost:32000/api-service:latest
docker push localhost:32000/ui-service:latest
```

## Deployment Helm

To install the whole project through Helm use:

```bash
helm install <release_name> ./k8s/
```

## Uninstallation with helm

To uninstall a release:

```bash
helm uninstall <release_name>
```

# Instructions Cloud

## Packaging

```bash
helm package k8s-gke/charts/api/
```

## Putting in repo of gcp

```bash
helm push k8s-0.1.0.tgz oci://europe-web1-docker.pkg.dev/subtle-backup-413213/software-containerization-repo
```

## Installation

```bash
helm install k8s-test oci://europe-west1-docker.pkg.dev/subtle-backup
-413213/software-containerization-repo/api-service --version 0.1.0
```

## Uninstallation

```bash
helm uninstall k8s-test
```

# Validation

## HPA

This command is for showing that the autoscaler is applied

```bash
kubectl run -i -n ingress --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.005; do wget -q -O- http://k8s-test-api-service.default.svc.cluster.local:8081/api/; done"
```

## Network policy

### Verify frontend and backend

```bash
kubectl run --rm -i -t --image=alpine test-$RANDOM -n ingress -- sh
\# wget -qO- http://k8s-test-api-service.default.svc.cluster.local:8081/
\# wget -qO- http://k8s-test-ui-service.default.svc.cluster.local:8081/
```

## DEADLINE - TO DO

<!-- - 18 - deadline for frontend otherwise @quarti jumps on it
- unknown - UML @quarti
- 18 - soft deadline for kubernetes oporting supporting api external access, and horizontal scaling
- 16 - 8pm heads up on kubernetes material
- 16 - 8pm heads up on lecture 4 persistant volumes -->

| Deadline | Responsible | Task                             |
| -------- | ----------- | -------------------------------- |
| 28-01    | ?           | Release: Rolling Update & Canary |
| 29-01    | Daniele     | UML                              |
| 2-02     | Daniele     | HTTPS and certmanager            |
| 30-01    | Daniele     | Sketch Generic diagram           |
| 31-01    | Daniele     | Sketch Presentation on google    |

| Section                                                         | Responsible |
| --------------------------------------------------------------- | ----------- |
| 1 Architecture and Artifacts                                    | Daniele     |
| 2 Pre-requisite                                                 | Coen        |
| 3 Container build and first deployment, scaling, uninstallation | Daniele     |
| 4 Application upgrade and re-deployment                         | Coen        |
