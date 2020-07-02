# canary-deployment-using-istio

## Deploy flask-1
```

kubectl apply -f flask-1/gke-deployment.yaml
```

## Deploy flask-2
```
kubectl apply -f flask-2/gke-deployment.yaml
```

## Deploy Istio
```
kubectl apply -f istio-canary-deployment/istio-canary-deployment.yaml
```
