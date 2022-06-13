import os
import boto3

ENV = os.environ.get('ENVIRONMENT', default='local')
REGION = os.environ.get('AWS_REGION', default='eu-west-1')

if ENV == 'local':
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb:8000')
else:
    dynamodb = boto3.resource('dynamodb', region_name=REGION)

ssm = boto3.client('ssm')


def db_table(table_name):
    return dynamodb.Table(table_name)