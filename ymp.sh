#!/bin/bash

# Set the current date and the date two months ago in seconds since epoch
CURRENT_DATE=$(date +%s)
TWO_MONTHS_AGO=$(date -d '2 months ago' +%s)

# Get a list of Lambda functions whose name starts with "USDH-"
aws lambda list-functions --query "Functions[?starts_with(FunctionName, 'USDH-')].[FunctionName]" --output text | while read -r function_name
do
  # Get the last invocation time of the function using the CloudWatch metric
  last_invoked=$(aws cloudwatch get-metric-statistics \
    --namespace AWS/Lambda \
    --metric-name Invocations \
    --dimensions Name=FunctionName,Value=$function_name \
    --start-time "$(date -d '2 months ago' --utc +%Y-%m-%dT%H:%M:%SZ)" \
    --end-time "$(date --utc +%Y-%m-%dT%H:%M:%SZ)" \
    --period 86400 \
    --statistics Sum \
    --query "Datapoints | sort_by(@, &Timestamp)[-1].Timestamp" \
    --output text)

  # Check if the last invocation is within the last 2 months
  if [ "$last_invoked" != "None" ]; then
    last_invoked_epoch=$(date -d "$last_invoked" +%s)

    if [ $last_invoked_epoch -gt $TWO_MONTHS_AGO ]; then
      echo "Lambda Function: $function_name was last invoked on $last_invoked"
    fi
  fi
done