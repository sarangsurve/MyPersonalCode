import boto3

# Initialize the CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Name of the Glue job
job_name = 'your-glue-job-name'

# Define the CloudWatch log group and log stream names for the Glue job
log_group_name = '/aws-glue/jobs/' + job_name
log_stream_name = job_name

# Retrieve the log events from the specified log group and stream
response = cloudwatch.get_log_events(
    logGroupName=log_group_name,
    logStreamName=log_stream_name,
    startFromHead=True,
    limit=1
)

# Extract the last run datetime from the response
last_run_time = response['events'][0]['timestamp']

# Print the last run datetime in ISO format
print("Glue Job Last Run Datetime: ", last_run_time.isoformat())