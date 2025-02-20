import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define bucket name
bucket_name = 'my-boto3-s3-bucket-syamala'  # Change this to match your bucket

# Enable versioning on the S3 bucket
s3.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={'Status': 'Enabled'}
)

print(f'Versioning enabled for bucket {bucket_name}!')
