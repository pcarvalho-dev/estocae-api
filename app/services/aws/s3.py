import base64
import json
import os
import uuid
from mimetypes import guess_extension, guess_type

import boto3
import requests
from flask import request
from werkzeug.utils import secure_filename

from app.services.files.upload import upload_file3
from config import Config

# Creating a client object for the S3 service.
s3 = boto3.client(
    "s3",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
)


def upload_file_s3(image, aws_key, filename=0):
    """
    It takes an image, uploads it to Kraken.io, and then uploads the compressed image to S3
    
    :param image: The image file
    :param aws_key: The folder in the bucket where the images will be stored
    :param filename: The name of the file you want to save it as, defaults to 0 (optional)
    :return: The image_key is being returned.
    """
    try:
        filename_from_image = secure_filename(image.filename)
        os_filename, os_file_extension = os.path.splitext(filename_from_image)
        if filename == 0:
            filename = f"{os_filename}{os_file_extension}"
        else:
            filename = f"{filename}{os_file_extension}"
    except:
        if filename == 0:
            filename = secure_filename(image.filename)

    path = f"{aws_key}/original/{filename}"

    api_endpoint = 'https://api.kraken.io/v1/upload'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'
    }
    files = {
        'file': image
    }
    params = {
        "auth": {
            "api_key": Config.KRAKEN_API_KEY,
            "api_secret": Config.KRAKEN_API_SECRET
        },
        "s3_store": {
            "key": Config.AWS_ACCESS_KEY_ID,
            "secret": Config.AWS_SECRET_ACCESS_KEY,
            "bucket": Config.AWS_BUCKET,
            "region": Config.AWS_BUCKET_LOCATION
        },
        "wait": True,
        "resize": [
            {
                "id": "original",
                "strategy": "none",
                "storage_path": path.lower()
            },
            {
                "id": "small",
                "strategy": "auto",
                "width": 180,
                "height": 180,
                "storage_path": path.replace('original', 'small').lower()
            },
            {
                "id": "medium",
                "strategy": "auto",
                "width": 450,
                "height": 450,
                "storage_path": path.replace('original', 'medium').lower()
            },
            {
                "id": "large",
                "strategy": "auto",
                "width": 850,
                "height": 850,
                "storage_path": path.replace('original', 'large').lower()
            }
        ]
    }

    r = requests.post(url=api_endpoint, headers=headers, files=files, data={
        'data': json.dumps(params)
    })

    r_json = r.json()
    success = r_json['success']

    if success:
        r_json['image_key'] = path.lower()
        return r_json


def delete_file_s3(key):
    """
    It deletes the original file, and the three resized versions of the file
    
    :param key: The name of the file in S3
    :return: True.
    """
    client = s3
    client.delete_object(Bucket=Config.AWS_BUCKET, Key=key)
    client.delete_object(Bucket=Config.AWS_BUCKET,
                         Key=key.replace('original', 'small'))
    client.delete_object(Bucket=Config.AWS_BUCKET,
                         Key=key.replace('original', 'medium'))
    client.delete_object(Bucket=Config.AWS_BUCKET,
                         Key=key.replace('original', 'large'))

    return True


def get_aws_image_keys(key):
    """
    It takes a string, and returns a dictionary with the string as the value for the key "original", and
    the string with "original" replaced with "small", "medium", and "large" as the values for the keys
    "small", "medium", and "large"
    
    :param key: The key of the image in the S3 bucket
    :return: A dictionary with the keys "original", "small", "medium", and "large".
    """
    if key is not None:
        assert isinstance(key, str), "\"key\" must be a string;."

        return {
            "original": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key}",
            "small": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key.replace('original', 'small')}",
            "medium": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key.replace('original', 'medium')}",
            "large": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key.replace('original', 'large')}"
        }
    else:
        return {
            "original": None,
            "small": None,
            "medium": None,
            "large": None
        }


def get_aws_image_keys_private(key):
    """
    It takes a string, and returns a dictionary with four keys, each of which is a string.
    
    :param key: the key of the image in the S3 bucket
    :return: A dictionary with the keys "original", "small", "medium", and "large".
    """
    if key is not None:
        assert isinstance(key, str), "\"key\" must be a string;."

        return {
            "original": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key}",
            "small": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key.replace('original', 'small')}",
            "medium": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key.replace('original', 'medium')}",
            "large": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key.replace('original', 'large')}"
        }
    else:
        return {
            "original": None,
            "small": None,
            "medium": None,
            "large": None
        }


def upload_image_s3_by_item(item, slug):
    """
    It takes a file, uploads it to S3, and returns the URL of the uploaded file
    
    :param item: is the object that I want to save the image
    :param slug: is the name of the folder where the image will be saved
    :return: The upload_image_s3_by_item function is returning the upload variable.
    """
    dict_body = request.get_json()
    name = item.id
    if dict_body:
        file = dict_body['image']

        file_exp = file.split(',')
        image = base64.b64decode(file_exp[1])
        ext = guess_extension(guess_type(file)[0])
        upload = upload_file3(image, f'images/{slug}/{name}',
                              str(uuid.uuid1()) + ext)
    else:
        if 'image' not in request.files:
            return 'Arquivo não Enviado'

        # Upload do Arquivo
        image = request.files['image']
        upload = upload_file3(image, f'images/{slug}/{name}')

    return upload

def get_aws_file(key, type_data=None):
    """
    It takes a string, and returns a dictionary with the string as the value for the key "original", and
    the string with "original" replaced with "small", "medium", and "large" as the values for the keys
    "small", "medium", and "large"

    :param key: The key of the image in the S3 bucket
    :param type_data: File type, can have the values: 'image' or 'file'
    :return: A dictionary with the keys "original", "small", "medium", and "large".
    """
    if key is not None:
        assert isinstance(key, str), "\"key\" must be a string;."

        if type_data == 'image':
            return {
                "original": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key}",
                "small": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key.replace('original', 'small')}",
                "medium": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key.replace('original', 'medium')}",
                "large": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key.replace('original', 'large')}"
            }
        elif type_data == 'file':
            return {
                "original": f"https://{Config.AWS_BUCKET_CLOUDFRONT}/{key}",
            }

    else:
        return {
            "original": None,
            "small": None,
            "medium": None,
            "large": None
        }