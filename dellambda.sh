#!/bin/bash

# Path to the CSV file
CSV_FILE="lambda_functions.csv"

# Check if the CSV file exists
if [ ! -f "$CSV_FILE" ]; then
  echo "Error: CSV file not found!"
  exit 1
fi

# Read the CSV file and extract the Lambda function names
# Assuming the column header is 'Lambda Function' and function names start from the second line
awk -F',' 'NR>1 {print $1}' "$CSV_FILE" | while read -r function_name
do
  # Trim any surrounding whitespace
  function_name=$(echo "$function_name" | xargs)

  # Check if function_name is not empty
  if [ -n "$function_name" ]; then
    # Delete the Lambda function
    echo "Deleting Lambda function: $function_name"
    aws lambda delete-function --function-name "$function_name"

    # Check if the delete command was successful
    if [ $? -eq 0 ]; then
      echo "Successfully deleted: $function_name"
    else
      echo "Failed to delete: $function_name"
    fi
  fi
done