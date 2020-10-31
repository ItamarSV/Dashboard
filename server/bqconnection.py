from google.cloud import bigquery
import pandas as pd
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key/itamarapp.json"
client = bigquery.Client()

def bqdata(querytext):
    sql = querytext
    df = client.query(sql).to_dataframe()
    return df

