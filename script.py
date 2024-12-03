To list AWS Lambda functions that start with the name "USDH-" and were last invoked within the last 2 years, you can use AWS CLI along with some shell scripting. Below is an example script to achieve this:

Prerequisites:

1. AWS CLI must be installed and configured on your system.


2. Ensure you have the necessary permissions to list Lambda functions and get their last invoke time.



Script:

#!/bin/bash

# Set the current date and the date two years ago in seconds since epoch
CURRENT_DATE=$(date +%s)
TWO_YEARS_AGO=$(date -d '2 years ago' +%s)

# Get a list of Lambda functions whose name starts with "USDH-"
aws lambda list-functions --query "Functions[?starts_with(FunctionName, 'USDH-')].[FunctionName]" --output text | while read -r function_name
do
  # Get the last invocation time of the function using the CloudWatch metric
  last_invoked=$(aws cloudwatch get-metric-statistics \
    --namespace AWS/Lambda \
    --metric-name Invocations \
    --dimensions Name=FunctionName,Value=$function_name \
    --start-time "$(date -d '2 years ago' --utc +%Y-%m-%dT%H:%M:%SZ)" \
    --end-time "$(date --utc +%Y-%m-%dT%H:%M:%SZ)" \
    --period 86400 \
    --statistics Sum \
    --query "Datapoints | sort_by(@, &Timestamp)[-1].Timestamp" \
    --output text)

  # Check if the last invocation is within the last 2 years
  if [ "$last_invoked" != "None" ]; then
    last_invoked_epoch=$(date -d "$last_invoked" +%s)

    if [ $last_invoked_epoch -gt $TWO_YEARS_AGO ]; then
      echo "Lambda Function: $function_name was last invoked on $last_invoked"
    fi
  fi
done

Explanation:

1. Get Current and Two-Year-Ago Dates: The script first calculates the current date and the date two years ago in seconds since the epoch.


2. List Lambda Functions: The script uses aws lambda list-functions to list all Lambda functions whose names start with "USDH-".


3. Get Last Invocation Time: For each function, the script uses aws cloudwatch get-metric-statistics to retrieve the last invocation timestamp based on the CloudWatch metrics.


4. Check if Last Invocation is within 2 Years: The script compares the last invocation time with the date two years ago. If the function was invoked within the last two years, the function name and last invoked timestamp are printed.



How to Run:

1. Save the script in a file, e.g., list_usdh_lambda.sh.


2. Give execute permission: chmod +x list_usdh_lambda.sh.


3. Run the script: ./list_usdh_lambda.sh.



This script will print the Lambda function names and their last invocation time if they were invoked in the last two years.

