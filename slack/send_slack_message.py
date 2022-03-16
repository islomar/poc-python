import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)
slack_token = os.environ["SLACK_TOKEN"]
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel="general",
        text="Hello from your app! :tada:"
    )
    print(response)
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
