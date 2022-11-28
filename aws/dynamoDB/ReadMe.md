# A sample of using DynamoDB with SDK for python and CDK to create resources

## CDK to deploy DynamoDB

* Created with the command:

```sh
cdk init --language python
```

* The add the DynamoDB creation using the [sample approach of this repo](https://github.com/aws-samples/aws-cdk-examples/tree/master/python/dynamodb-lambda):

```python
# file cdk_stack.py
order_table = aws_dynamodb.Table(
            self, "orders",
            partition_key=aws_dynamodb.Attribute(
                name="orderID",
                type=aws_dynamodb.AttributeType.STRING,
            ),
            table_class= aws_dynamodb.TableClass.STANDARD_INFREQUENT_ACCESS,
            billing_mode=aws_dynamodb.BillingMode.PROVISIONED
        )
```

* See [CDK DynamoDB API](https://docs.aws.amazon.com/cdk/api/v1/docs/aws-dynamodb-readme.html)
* Synthetise the CloudFormation generation after the environment setup:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cdk synth
```

* When the CloudFormation generation looks good, deploy to get DynamoDB table created

```sh
cdk deploy
```

* Run the client app locally
* Stop all with... does not see to delete the DynamoDB

```sh
cdk destroy
```

## Client in python

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

## A Flask App to manage Orders

The code is under the folder `flask-order-ms`, and uses the boilerplate template. See the ReadMe file to build it and build the docker image. 

To deploy the image to ECR do the following:

```sh
```

To run it with Fargate do:

```sh
```

## Deeper Dive

Use knowledge from:

* [AWS code sample](https://docs.aws.amazon.com/code-library/latest/ug/python_3_dynamodb_code_examples.html)
* [Dev guide python - dynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.html)