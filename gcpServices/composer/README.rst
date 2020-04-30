HandsOn Task

1) Create a composer Environment
2) Create GCS bucket for storing output of from a dataproc service
3) Assig Cloud Composer variables
4) Upload workflow file to DAG folder
5) View Result


Objective:

Create a Dataproc Cluster --> Submit a job --> Send Job Result to Cloud Storage --> Delete the Dataproc Cluster

Todo:

Enable composerapi and dataproc api in your project from ui
Create composer in closest region
Create a Storage bucket


1) Create GCS bucket to output Dataproc results 

gsutil mb -l us-central1 gs://output-gcpdeb001

2) Set our Cloud Composer variables necessary for our workflow.

gcloud composer environments run us-psp-env --location us-central1 variables -- --set gcp_project gcpdeb001

gcloud composer environmensts run us-psp-env --location us-central1 variables -- --set gcs_bucket gs://output-gcpdeb001

gcloud composer environments run us-psp-env --location us-central1 variables -- --set gce_zone us-central1-c

3) Upload the example DAG file to the DAG folder for Cloud Composer. 

gsutil cp gcpServices/composer/quickstart.py gs://us-central1-us-psp-env-6d123432-bucket/dags/quickstart.py

4) Go to the Composer - airflow ui see the output.
