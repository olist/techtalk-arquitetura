import json
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def get_project_package(project_dir):
    return "matches_api"


def sns_publish(endpoint_url, topic_arn, message, dry_run):
    if dry_run:
        msg = f"sns_publish_called, {topic_arn=}, {message=!r}"
        logger.info(msg)
        return

    endpoint_url = endpoint_url if endpoint_url else None
    client = boto3.client("sns", endpoint_url=endpoint_url)

    message = json.dumps({"default": json.dumps(message)})

    try:
        client.publish(
            TopicArn=topic_arn, MessageStructure="json", Message=message,
        )
    except ClientError as exc:
        msg = f"sns_publish_error, {topic_arn=}, {message=!r}, {exc=}"
        logger.error(msg)

    msg = f"sns_publish, {topic_arn=}, {message=!r}"
    logger.info(msg)
