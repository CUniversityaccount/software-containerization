#?/bin/bash

#AI generated for testing do not submit as it is

kubectl create namespace cert-manager

kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v0.13.1/cert-manager.yaml

kubectl create namespace cert_manager_namespace

kubectl apply -n cert_manager_namespace -f <(echo "
apiVersion: cert-manager.io/v1alpha2
kind: ClusterIssuer
metadata:
  name: I_am_the_issuer
spec:
  selfSigned: {}
")

kubectl apply -n cert_manager_namespace -f <(echo '
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: I_am_the_certificate_name
  namespace: default
spec:
  secretName: I_am_the_secret_name
  duration: 24h
  renewBefore: 12h
  commonName: "127.0.0.1"
  ipAddresses:
  - "127.0.0.1"
  issuerRef:
    name: I_am_the_issuer
    kind: ClusterIssuer
')

kubectl -n cert_manager_namespace get certificate

kubectl -n cert_manager_namespace get secret I_am_the_secret_name
