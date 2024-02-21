import boto3
from datetime import datetime, timedelta

def get_last_run_datetime(glue_job_name, log_group_prefix='/aws-glue/jobs/'):
    # Initialize Boto3 CloudWatch Logs client
    logs_client = boto3.client('logs')

    # Describe CloudWatch Logs groups
    response = logs_client.describe_log_groups(logGroupNamePrefix=log_group_prefix)

    # Find the log group for the specified Glue job
    log_group_name = None
    for log_group in response['logGroups']:
        if glue_job_name in log_group['logGroupName']:
            log_group_name = log_group['logGroupName']
            break

    if log_group_name:
        # Query the CloudWatch Logs for the last event timestamp
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=1)  # Adjust the duration as needed

        response = logs_client.filter_log_events(
            logGroupName=log_group_name,
            startTime=int(start_time.timestamp()) * 1000,
            endTime=int(end_time.timestamp()) * 1000,
            limit=1,
            filterPattern='END RequestId'
        )

        # Extract the timestamp of the last log event
        if 'events' in response and len(response['events']) > 0:
            last_run_timestamp = response['events'][0]['timestamp']
            last_run_datetime = datetime.fromtimestamp(last_run_timestamp / 1000.0)
            return last_run_datetime
        else:
            print(f"No log events found for Glue job '{glue_job_name}'.")
            return None
    else:
        print(f"No log group found for Glue job '{glue_job_name}'.")
        return None

# Example usage
glue_job_name = "YourGlueJobName"
last_run_datetime = get_last_run_datetime(glue_job_name)

if last_run_datetime:
    print(f"The last run datetime for Glue job '{glue_job_name}' is: {last_run_datetime}")
else:
    print("Last run datetime not found.")
