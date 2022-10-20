import boto3

sqs = boto3.resource("sqs")

queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})
# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

for queue in sqs.queues.all():
    print(queue.url)



