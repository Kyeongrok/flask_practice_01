import boto3

if __name__ == '__main__':
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='students',
        KeySchema=[
            {
                'AttributeName': 'class',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'no',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'class',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'no',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    print(table)
