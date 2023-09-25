#!/usr/bin/env bash


# Sample Call
# ./log_to_slack.sh /opt/iot/slack_endpoint.txt /var/log/water_distance.txt

SLACK_TOKEN=$(cat ${1})
LAST_READ=$(tail -n 1 ${2})
python3 send_to_slack.py --endpoint "${SLACK_TOKEN}" --rawread "${LAST_READ}" ${3}
