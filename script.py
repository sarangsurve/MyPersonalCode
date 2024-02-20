import boto3

# Create a Glue client
glue_client = boto3.client('glue')

# Specify the name of your Glue connection
connection_name = 'your-connection-name'

# Get the Glue connection
response = glue_client.get_connection(
    Name=connection_name
)

# Extract information from the response
connection_details = response['Connection']
print(f"Connection Name: {connection_details['Name']}")
print(f"Connection Type: {connection_details['ConnectionProperties']['CONNECTION_TYPE']}")
print(f"Connection Parameters: {connection_details['ConnectionProperties']['CONNECTOR_CLASS_NAME']}")
