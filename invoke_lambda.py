import boto3

# Replace with your actual Lambda function name
function_name = 'S3LoggerFunction'  # or your real Lambda name

# Create a Lambda client
client = boto3.client('lambda')

# Invoke the function
response = client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse'
)

# Print the response
print(response['Payload'].read().decode())
