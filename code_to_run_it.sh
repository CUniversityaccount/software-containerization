#/bin/bash

#build the two images
docker build -t api-service:latest ./api
docker build -t ui-service:latest ./frontend

#enable registry
microk8s enable registry

#tag the images for registry
docker tag api-service:latest localhost:32000/api-service:latest
docker tag ui-service:latest localhost:32000/ui-service:latest

#push the images to registry
docker push localhost:32000/api-service:latest
docker push localhost:32000/ui-service:latest

microk8s.helm install my-release-1 ./k8s-local/
