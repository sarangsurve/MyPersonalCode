import boto3

# Initialize the Glue client
glue = boto3.client('glue')

# Get a list of all Glue job names
job_names = [job['Name'] for job in glue.get_jobs()['Jobs']]

# Loop through each Glue job and get its connections and associated VPC details
for job_name in job_names:
    # Get the connections of the current Glue job
    connections = glue.get_job(JobName=job_name)['Job']['Connections']['Connections']
    
    # Loop through each connection of the Glue job
    for connection in connections:
        # Get the details of the current connection
        connection_details = glue.get_connection(Name=connection['Name'])['Connection']
        
        # If the connection has a VPC specified, get its details
        if 'JDBC_CONNECTION_URL' in connection_details['ConnectionProperties']:
            if 'vpc-' in connection_details['ConnectionProperties']['JDBC_CONNECTION_URL']:
                # Get the VPC ID from the JDBC connection URL
                vpc_id = connection_details['ConnectionProperties']['JDBC_CONNECTION_URL'].split('/')[2].split(':')[0]
                
                # Get the details of the VPC
                ec2 = boto3.client('ec2')
                vpc_details = ec2.describe_vpcs(VpcIds=[vpc_id])['Vpcs'][0]
                
                # Get the subnet IDs and security group IDs associated with the VPC
                subnet_ids = [subnet['SubnetId'] for subnet in vpc_details['Subnets']]
                security_group_ids = [sg['GroupId'] for sg in vpc_details['SecurityGroups']]
                
                # Print the details of the current connection and associated VPC
                print(f"Connection: {connection_details['Name']}")
                print(f"VPC ID: {vpc_id}")
                print(f"Subnet IDs: {subnet_ids}")
                print(f"Security Group IDs: {security_group_ids}")
                print()