import boto3

dynamodb = boto3.client('dynamodb')

tables = dynamodb.list_tables()
print(tables)
