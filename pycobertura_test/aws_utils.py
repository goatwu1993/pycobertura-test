import boto3


def send_a_message(region_name: str, queue_url: str, message: str):
    sqs = boto3.client("sqs", region_name=region_name)
    sqs.send_message(QueueUrl=queue_url, MessageBody=message)
