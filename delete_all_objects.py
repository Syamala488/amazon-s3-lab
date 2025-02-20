import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define bucket name
bucket_name = 'my-boto3-s3-bucket-syamala'  # Change this to match your bucket

# List all object versions
response = s3.list_object_versions(Bucket=bucket_name)

# Delete all versions and delete markers
if 'Versions' in response:
    for version in response['Versions']:
        s3.delete_object(Bucket=bucket_name, Key=version['Key'], VersionId=version['VersionId'])
        print(f"Deleted {version['Key']} (Version: {version['VersionId']})")

if 'DeleteMarkers' in response:
    for marker in response['DeleteMarkers']:
        s3.delete_object(Bucket=bucket_name, Key=marker['Key'], VersionId=marker['VersionId'])
        print(f"Deleted delete marker {marker['Key']} (Version: {marker['VersionId']})")

print(f"All objects deleted from {bucket_name}!")
