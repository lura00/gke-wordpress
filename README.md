# Wordpress kubernetes configuration and GKE deplyment

### Project to deploy a wordpress site to your GCP GKE cluster.
    - You need a GKE cluster up and running to run the pipeline.

## To run locally

    - Clone this repository.
    
### Apply and Verify
    
    - kubectl apply -k ./

    To verify that secrets exists:

    - kubectl get secrets

    Verify that a PersistentVolume got dynamically provisioned.

    - kubectl get pvc

    Verify that the Pod is running by running the following command:

    - kubectl get pods

    Verify that the Service is running by running the following command:

    - kubectl get services wordpress

    Run the following command to get the IP Address for the WordPress Service:

    - minikube service wordpress --url

### Cleaning up

    - kubectl delete -k ./


If you have a GCP account you need to fork this repo and add following secrets to your repo:

    - TOKEN_GITHUB (Personal access token)
    - GKE_EMAIL
    - GKE_KEY
    - GKE_PROJECT_ID