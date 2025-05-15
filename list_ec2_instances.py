import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Describe instances
response = ec2.describe_instances()

# Loop through the response to print instance IDs and states
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        print(f"Instance ID: {instance_id} - State: {state}")
