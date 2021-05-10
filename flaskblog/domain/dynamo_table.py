import boto3

class Table():
    def __init__(self):
        self.dynamodb = boto3.client('dynamodb')

    def list_table(self):
        response = self.dynamodb.list_tables()
        return response

    def create_table(self, table_name):
        table = self.dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'stdSpciesNewCode',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'delngDe',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'stdSpciesNewCode',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'delngDe',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'price',
                    'AttributeType': 'N'
                }
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'code_price',
                    'KeySchema': [
                        {
                            'AttributeName': 'stdSpciesNewCode',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'price',
                            'KeyType': 'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        print(table)
        # table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        # print(f'{table_name} has been created')
