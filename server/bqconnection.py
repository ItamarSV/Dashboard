from google.cloud import bigquery
import pandas as pd
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key/itamarapp.json"
client = bigquery.Client()

sql = """
    SELECT * FROM `itamarapp.Fraud_detection_example.FD_example_view` LIMIT 10
"""

df = client.query(sql).to_dataframe()

print(df)
