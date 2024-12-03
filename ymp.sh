#!/bin/bash

# Get a list of Lambda functions whose name starts with "USDH-"
aws lambda list-functions --query "Functions[?starts_with(FunctionName, 'USDH-')].[FunctionName]" --output text | while read -r function_name
do
  # Get the last invocation time of the function using the CloudWatch metric
  last_invoked=$(aws cloudwatch get-metric-statistics \
    --namespace AWS/Lambda \
    --metric-name Invocations \
    --dimensions Name=FunctionName,Value=$function_name \
    --start-time "1970-01-01T00:00:00Z" \  # Start from epoch to get any available data
    --end-time "$(date --utc +%Y-%m-%dT%H:%M:%SZ)" \
    --period 86400 \
    --statistics Sum \
    --query "Datapoints | sort_by(@, &Timestamp)[-1].Timestamp" \
    --output text)

  # Check if the function has been invoked at least once
  if [ "$last_invoked" != "None" ]; then
    echo "Lambda Function: $function_name was last invoked on $last_invoked"
  else
    echo "Lambda Function: $function_name has never been invoked."
  fi
done