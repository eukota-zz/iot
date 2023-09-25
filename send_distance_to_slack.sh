#!/usr/bin/env bash

SLACK_TOKEN=$(cat /opt/iot/slack_endpoint.txt)
LAST_READ=$(tail -n 1 /var/log/water_distance.txt)
PAYLOAD="{\"text\":\"Distance Read: $LAST_READ\"}"
COMMAND="curl -X POST -H 'Content-type: application/json' --data '${PAYLOAD}' ${SLACK_TOKEN}"
#echo "COMMAND: ${COMMAND}"
eval $COMMAND
