# Containerization course vu

# Docker

### inside the dockerfile folder build the images

To build different docker images you will use the following

```bash
docker build -t <image_name> <location_DockerFile>
```

### Place the images in microk8s registry

The first way to place the image in the registery.

```bash
docker save image_name > myimage.tar
microk8s ctr image import myimage.tar
```

You can push images to registery of microk8s through:

```bash
docker tag <image_name> <registery_host>/<image_name>[:<tag>]
docker push <registery_host>/<image_name>[:<tag>]
```

### List images in microk8s to check that is there

```bash
microk8s ctr images ls
```

# Deployment

## Apply deployment of yaml files

To apply a set of yaml files

```bash
microk8s kubectl apply -f <location>
```

Otherwise for a single file:

```bash
microk8s kubectl apply -f <file_location>
```

## Deployment Helm

To install the whole project through Helm use:

```bash
helm install <release_name> ./k8s/
```

# Uninstallation

## Helm

To uninstall a release:

```bash
helm uninstall <release_name>
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

![Screenshot](Sequence_Diagram_drawio.png)

![Screenshot](Deployment_uml_mk2.drawio.png)

| Section                                                         | Responsible |
| --------------------------------------------------------------- | ----------- |
| 1 Architecture and Artifacts                                    | Daniele     |
| 2 Pre-requisite                                                 | Coen        |
| 3 Container build and first deployment, scaling, uninstallation | Daniele     |
| 4 Application upgrade and re-deployment                         | Coen        |
