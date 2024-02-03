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
