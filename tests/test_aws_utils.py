import os

import boto3
import moto

from pycobertura_test.aws_utils import send_a_message

AWS_SQS_REGION = "us-west-2"
AWS_SQS_NAME = "foobar"


@moto.mock_sqs
def test_send_a_message():
    AWS_ACCOUNT_ID = os.environ["AWS_ACCOUNT_ID"]
    fake_message = "QQ"
    AWS_SQS_URL = (
        f"https://sqs.{AWS_SQS_REGION}.amazonaws.com/{AWS_ACCOUNT_ID}/{AWS_SQS_NAME}"
    )
    sqs = boto3.client(
        "sqs",
        AWS_SQS_REGION,
        endpoint_url=f"https://sqs.{AWS_SQS_REGION}.amazonaws.com",
    )
    sqs.create_queue(QueueName=AWS_SQS_NAME)
    send_a_message(region_name=AWS_SQS_REGION, queue_url=AWS_SQS_URL, message=fake_message)
    assert sqs.receive_message(QueueUrl=AWS_SQS_URL)["Messages"][0]["Body"] == fake_message