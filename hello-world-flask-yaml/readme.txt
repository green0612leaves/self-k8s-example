kubectl apply -f flask-deployment.yaml

kubectl get pods -n hello-flask


kubectl port-forward svc/hello-flask-svc 8080:80 -n hello-flask

127.0.0.1:8080
