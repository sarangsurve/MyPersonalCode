import boto3

# Replace 'your_lambda_function_name' with your actual Lambda function name
lambda_function_name = 'your_lambda_function_name'

# Create a Lambda client
lambda_client = boto3.client('lambda')

# Get the function configuration to retrieve triggers
function_config = lambda_client.get_function_configuration(FunctionName=lambda_function_name)

# Extract triggers from the response
triggers = function_config.get('Triggers', [])

# Print the triggers
for trigger in triggers:
    print(trigger)
