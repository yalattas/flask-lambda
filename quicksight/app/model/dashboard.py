from config.settings import dynamodb
from config.constant import DASHBOARD_DYNAMODB_TABLE

class Dashboard():
    # def __init__(self):
    #     pass
    def get(dashboard_id):
        return dynamodb.query(
            TableName=DASHBOARD_DYNAMODB_TABLE,
            Select = 'ALL_ATTRIBUTES',
            KeyConditions= {
                'id': {
                    'AttributeValueList': [
                        {
                            'S': dashboard_id
                        }
                    ],
                    # EQ: stands for equal
                    'ComparisonOperator': 'EQ'
                }
            }
        )
    def fetch_all():
        return dynamodb.scan(
            TableName=DASHBOARD_DYNAMODB_TABLE,
            Select = 'ALL_ATTRIBUTES'
        )