import boto3

def list_glue_jobs_with_connections():
    # Create a Glue client
    glue_client = boto3.client('glue')

    # List all Glue jobs
    response = glue_client.get_jobs()

    # Iterate through the jobs and print job name along with connection name
    for job in response['Jobs']:
        job_name = job['Name']
        connections = job.get('Connections', [])

        print(f"Glue Job Name: {job_name}")
        if connections:
            connection_names = [connection['Name'] for connection in connections]
            print(f"Connection Names: {', '.join(connection_names)}")
        else:
            print("No connections associated with this job.")
        print("\n")

if __name__ == "__main__":
    list_glue_jobs_with_connections()
