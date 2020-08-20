import boto3
from botocore.client import Config
import credential

ACCESS_KEY_ID = credential.access_key
ACCESS_SECRET_KEY = credential.secret_key
BUCKET_NAME = 'Your Bucket Name [In S3]'
FILE_NAME_IN_BUCKET = 'upload_Via_Py'

DOWNLOAD_FILE_PATH = './download/s3_downloadFile.txt'

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


s3_client.Bucket(BUCKET_NAME).download_file(FILE_NAME_IN_BUCKET, DOWNLOAD_FILE_PATH)

print("Downloaded from  S3")