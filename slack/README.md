# Slack integration
- [Python Slack SDK](https://slack.dev/python-slack-sdk/)
- https://pypi.org/project/slack-sdk/#getting-started-tutorial
- [Slack API Authentication](https://api.slack.com/authentication/best-practices)
- https://api.slack.com/authentication/token-types
- https://api.slack.com/methods/chat.postMessage
  - Optional argument: `as_user' (https://api.slack.com/methods/chat.postMessage#authorship)

## Prerequisites
- `poetry install`: to install the required libraries in a virtualenv
- `poetry shell`: to activate the virtualenv


## How to run the example
- `SLACK_TOKEN="[your_secret_slack_token]" python send_slack_message.py`
- I saved the SLACK_TOKEN as a Gist secret (both the Bot and the User)


## Steps I followed
1. I created a Slack app with `chat:write` scope for both the bot and users called "Slack Integration PoC".
   1. If your app has `chat:write.public` scope, your app can post messages without joining a channel as long as the channel is public.
2. I added to my `islomar` Slack workspace.
3. I invited the bot to the `#general` Slack channel with `/invite xx`
