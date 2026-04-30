import boto3

# Use the local endpoint
dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-west-2',
    endpoint_url='http://localhost:8000',
    aws_access_key_id='dummy',    # Required by boto3, but not used
    aws_secret_access_key='dummy' # Required by boto3, but not used
)

# Create a table
table_name = 'Users'
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print(f"Creating table {table_name}...")
table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
print("Table created.")

# Insert item
table.put_item(
    Item={
        'user_id': 'u123',
        'name': 'Alice',
        'age': 30
    }
)

# Fetch item
response = table.get_item(
    Key={
        'user_id': 'u123'
    }
)

item = response.get('Item')
print("Fetched item:", item)
