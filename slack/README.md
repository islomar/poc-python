# Slack integration
- [Python Slack SDK](https://slack.dev/python-slack-sdk/)
- https://pypi.org/project/slack-sdk/#getting-started-tutorial
- [Slack API Authentication](https://api.slack.com/authentication/best-practices)
- https://api.slack.com/authentication/token-types


## Prerequisites
- `poetry install`: to install the required libraries in a virtualenv
- `poetry shell`: to activate the virtualenv


## How to run the example
- `SLACK_BOT_TOKEN="[your_secret_slack_bot_token]" python send_slack_message_as_bot.py`
- I saved the SLACK_BOT_TOKEN as Gist secret


## Steps I followed
1. I created a Slack app with `chat:write` scope for both the bot and users called "Slack Integration PoC".
2. I added to my `islomar` Slack workspace.
3. I invited the bot to the `#general` Slack channel with `/invite xx`
