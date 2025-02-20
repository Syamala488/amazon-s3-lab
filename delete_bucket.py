import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define bucket name
bucket_name = 'my-boto3-s3-bucket-syamala'  # Change this to match your bucket

# Delete the S3 bucket
s3.delete_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} deleted successfully!')
