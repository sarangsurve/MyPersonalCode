import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Get all security groups in the current region
response = ec2_client.describe_security_groups()

# Extract and print security group details
for security_group in response['SecurityGroups']:
    group_id = security_group['GroupId']
    group_arn = f"arn:aws:ec2:{boto3.Session().region_name}:{boto3.Session().client('sts').get_caller_identity()['Account']}:security-group/{group_id}"
    
    print(f"Security Group ID: {group_id}")
    print(f"Security Group ARN: {group_arn}")
    print("Security Group Details:")
    print(security_group)
    print("\n")
