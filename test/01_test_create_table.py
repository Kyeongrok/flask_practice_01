from flaskblog.domain.dynamo_table import Table

if __name__ == '__main__':
    t = Table('auction2')
    t.create_table(
        key_schema=[
            {
                'AttributeName': 'date',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'prdcd_whsal_mrkt_new_cd',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        attribute_definitions=[
            {
                'AttributeName': 'date',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'prdcd_whsal_mrkt_new_cd',
                'AttributeType': 'S'
            },
        ],
    )
