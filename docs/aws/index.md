# AWS

## boto3 library

A [unique library](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) to access all AWS services from a python app. 

### Installation

```sh
pip install boto3[crt]
```

Set up authentication credentials for your AWS account using either the IAM Console or the AWS CLI.

```sh
aws configure
# Verify access
aws iam list-users
```

!!! info
    The jbcodeforce/python docker image has the aws cli and goto3.

## Programming samples

### Access S3

```python
import boto3
# declare a client to the service you want
s3 = goto3.service("s3")
# use SDK API for s3.
s3.buckets.all()
```

### Access DynamoDB

The client have can get the table name using the API client: 

```python
import os, boto3

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")

client = boto3.client(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
table = client.list_tables()
tableName=table['TableNames'][0]
```

Then use the dynamoDB API:

```python
orderTable = dynamodb.Table(tableName)

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

orderTable = dynamodb.Table(tableName)
orderTable.put_item(
   Item={
     "orderID": "ORD001",
     "customerID": "C01", 
     "productID": "P01", 
     "quantity": 10,  
     "destinationAddress": { "street": "1st main street", "city": "Santa Clara", "country": "USA", "state": "CA", "zipcode": "95051" }
   })

```

* Run it once the python virtual env is enabled with `python dynamoClient.py`
