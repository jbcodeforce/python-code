import boto3,os

account_id=os.getenv("AWS_ACCOUNT_ID")
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='MyQueue',QueueOwnerAWSAccountId=account_id)
print("Send a txt messsage")
response = queue.send_message(MessageBody='Hello from client app')
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))