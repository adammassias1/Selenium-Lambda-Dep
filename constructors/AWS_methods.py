import base64
import pandas as pd
import boto3
from io import StringIO
import json

class aws_execution_class:
    
    def pull_S3_files(self, bucket_name, file_name):

        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket = bucket_name, Key = file_name)
        df = obj['Body']
        df_pull_decode  = df.read().decode('utf-8')

        return pd.read_csv(StringIO(df_pull_decode))

    def push_S3_files(self, bucket_name, file_name, dataframe):

        csv_buffer = StringIO()
        dataframe.to_csv(csv_buffer, index = False)
        s3_resource = boto3.resource('s3')
        s3_resource.Object(bucket_name, file_name).put(Body=csv_buffer.getvalue())
    
    def get_sm_secret(self, secret_name, region_name):
        
        client = boto3.client('secretsmanager', region_name=region_name )
        response = client.get_secret_value(
            SecretId=secret_name
        )

        sm_secrets = json.loads(response['SecretString'])

        return sm_secrets
