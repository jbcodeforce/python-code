import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='test')

for message in queue.receive_messages():
    print(message.body)
    message.delete()