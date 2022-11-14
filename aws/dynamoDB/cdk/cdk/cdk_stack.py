from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # create dynamo table
        order_table = aws_dynamodb.Table(
            self, "orders",
            partition_key=aws_dynamodb.Attribute(
                name="orderID",
                type=aws_dynamodb.AttributeType.STRING,
            ),
            table_class= aws_dynamodb.TableClass.STANDARD_INFREQUENT_ACCESS,
            billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
            # make it global
            #replicationRegions= ['us-west-1', 'us-east-1', 'us-west-2'],
        )
        
