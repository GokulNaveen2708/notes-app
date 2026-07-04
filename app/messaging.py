import json
import boto3

from app.config import settings

# One SQS client, reused. boto3 finds the instance's IAM role
# automatically — no keys anywhere.
_sqs = boto3.client("sqs", region_name = "us-west-2")

def publish_note_created(note_id: int, content: str) -> None:

    if not settings.sqs_queue_url:
        return
    message = {"event" : "note_created","note_id": note_id, "content": content}
    _sqs.send_message(QueueUrl =  settings.sqs_queue_url, MessageBody = json.dumps(message)
                      )