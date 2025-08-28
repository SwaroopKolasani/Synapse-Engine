import os
from google.cloud import bigquery

# Set up client
client = bigquery.Client()
dataset_id = "synapse_engine"  # Replace with your dataset

data_files = {
    "product_catalog": "data/structured/product_catalog.csv",
    "sales_data": "data/structured/sales_data.csv",
    "return_claims": "data/structured/return_claims.csv",
    "warranty_claims": "data/structured/warranty_claims.csv",
}

def load_csv_to_bq(table_name, file_path):
    table_id = f"{client.project}.{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
    )

    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    
    job.result()
    print(f"✅ Loaded {table_name} from {file_path}")

# Upload all structured CSVs
for table, path in data_files.items():
    load_csv_to_bq(table, path)
