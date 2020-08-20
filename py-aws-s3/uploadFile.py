import boto3
from botocore.client import Config
import credential

ACCESS_KEY_ID = credential.access_key
ACCESS_SECRET_KEY = credential.secret_key
BUCKET_NAME = 'Your Bucket Name [In S3]'
FILE_NAME_IN_BUCKET = 'upload_Via_Py'

LOCAL_FILE_DATA = open("s3_uploadFile.txt", 'rb')

# S3 Connect
s3_client = boto3.resource('s3',
                    aws_access_key_id=ACCESS_KEY_ID,
                    aws_secret_access_key=ACCESS_SECRET_KEY,
                    config=Config(signature_version='s3v4',
                                  retries={
                                      'max_attempts': 10,
                                      'mode': 'standard'
                                  })
                    )


s3_client.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME_IN_BUCKET,      #This could be folder structure
                                  Body=LOCAL_FILE_DATA,
                                  ACL='authenticated-read')

print("Uploaded to S3")
