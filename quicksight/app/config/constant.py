import os

ENV = os.environ.get('ENVIRONMENT', default='local')
REGION = os.environ.get('AWS_REGION', default='eu-west-1')
USER_DYNAMODB_TABLE= os.environ.get('USER_DYNAMODB_TABLE')
DASHBOARD_DYNAMODB_TABLE= os.environ.get('DASHBOARD_DYNAMODB_TABLE')