from google.cloud import bigquery


client = bigquery.Client()

bucket_name = 'mils_pubsub'
project = "bigquery-public-data"
dataset_id = "stackoverflow"
table_id = "posts_questions"

destination_uri = "gs://{}/{}".format(bucket_name, "stackoverflow_mils_*.csv")
dataset_ref = bigquery.DatasetReference(project, dataset_id)
table_ref = dataset_ref.table(table_id)

extract_job = client.extract_table(
    table_ref,
    destination_uri,
    # Location must match that of the source table.
    location="US",
)  # API request
extract_job.result()  # Waits for job to complete.

print(
    "Exported {}:{}.{} to {}".format(project, dataset_id, table_id, destination_uri)
)