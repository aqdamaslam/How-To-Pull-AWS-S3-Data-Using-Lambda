import boto3
import pandas as pd

s3_file = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    try:
        bucketName = event["Records"][0]["s3"]["bucket"]["name"]
        s3Key = event["Records"][0]["s3"]["object"]["key"]
        print(bucketName)
        print(s3Key)
        resp = s3_file.get_object(Bucket=bucketName, Key=s3Key)
        print(resp['Body'])
        df_s3_data = pd.read_csv(resp['Body'], sep=",")
        print(df_s3_data.head())
    except Exception as err:
        print(err)
