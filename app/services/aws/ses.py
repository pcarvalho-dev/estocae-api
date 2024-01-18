# aws simple notification service
import boto3

from config import Config

# aws simple email service
ses = boto3.client(
    "ses",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name="us-east-1"
)
