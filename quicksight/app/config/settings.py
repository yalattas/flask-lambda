import os
import boto3
from .constant import *

api_version = 'v1'
# aws - SSM ---------------------------------
ssm = boto3.client('ssm')
# aws - SSM ---------------------------------
# aws - dynamoDB ---------------------------------
if ENV == 'local':
    dynamodb = boto3.client('dynamodb', endpoint_url='http://dynamodb:8000')
else:
    dynamodb = boto3.client('dynamodb', region_name=REGION)
# aws - dynamoDB ---------------------------------
