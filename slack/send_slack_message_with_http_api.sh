#!/bin/bash
set -euo pipefail

curl -X POST -H 'Authorization: Bearer [your_secret_slack_token]' \
-H 'Content-type: application/json; charset=utf-8' \
--data '{"channel":"general","text":"/remind @here \"Hello world\" in 5 minutes"}' \
https://slack.com/api/chat.postMessage