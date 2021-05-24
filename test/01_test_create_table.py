from flaskblog.domain.dynamo_table import Table

if __name__ == '__main__':
    t = Table('auction_prd_info')
    t.create_table(
        key_schema=[
            {
                'AttributeName': 'prdcd',
                'KeyType': 'HASH'
            }
        ],
        attribute_definitions=[
            {
                'AttributeName': 'date',
                'AttributeType': 'S'
            }
        ],
    )
