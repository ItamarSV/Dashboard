import json
from bqconnection import bqdata

def testquery():
    sql = """
        SELECT * FROM `itamarapp.Fraud_detection_example.FD_example_view` LIMIT 10
    """
    df = bqdata(sql)
    jsn = df.to_json(orient='records')
    parsed = json.loads(jsn)

    return parsed

