import boto3

def get_vpc_id_by_connection_name(connection_name):
    # Initialize the Boto3 EC2 client
    ec2_client = boto3.client('ec2')

    # Describe VPN connections
    response = ec2_client.describe_vpn_connections(Filters=[{'Name': 'tag:Name', 'Values': [connection_name]}])

    # Check if any VPN connections were found
    if 'VpnConnections' in response and len(response['VpnConnections']) > 0:
        # Extract the VPC ID from the first matching connection
        vpc_id = response['VpnConnections'][0]['VpcId']
        return vpc_id
    else:
        print(f"No VPN connection found with the name: {connection_name}")
        return None

# Example usage
connection_name = "YourConnectionName"
vpc_id = get_vpc_id_by_connection_name(connection_name)

if vpc_id:
    print(f"The VPC ID for the VPN connection '{connection_name}' is: {vpc_id}")
else:
    print("VPC ID not found.")
