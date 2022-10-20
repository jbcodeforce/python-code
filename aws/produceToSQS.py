import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='test')
print("Send a txt messsage")
response = queue.send_message(MessageBody='world')
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))