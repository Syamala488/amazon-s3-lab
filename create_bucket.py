import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define a unique bucket name (change "<yourname>" to something unique)
bucket_name = 'my-boto3-s3-bucket-syamala'  # Make sure this name is globally unique

# Create the S3 bucket
response = s3.create_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} created successfully!')
