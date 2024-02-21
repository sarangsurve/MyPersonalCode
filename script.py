import boto3

def get_vpc_id_from_connection_name(connection_name):
    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Describe VPC peering connections
    response = ec2_client.describe_vpc_peering_connections(
        Filters=[
            {'Name': 'tag:Name', 'Values': [connection_name]}
        ]
    )

    # Check if any VPC peering connections were found
    if 'VpcPeeringConnections' in response and len(response['VpcPeeringConnections']) > 0:
        # Extract and return the VPC ID
        vpc_id = response['VpcPeeringConnections'][0]['RequesterVpcInfo']['VpcId']
        return vpc_id
    else:
        print(f"No VPC peering connections found with the name '{connection_name}'.")
        return None

# Example usage
connection_name = 'YourConnectionName'
vpc_id = get_vpc_id_from_connection_name(connection_name)

if vpc_id:
    print(f"The VPC ID for the connection '{connection_name}' is: {vpc_id}")
