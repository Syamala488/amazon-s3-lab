import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define bucket name and file name
bucket_name = 'my-boto3-s3-bucket-syamala'  # Change this to match your bucket
file_name = 'myfile.txt'

# Delete the file from S3
s3.delete_object(Bucket=bucket_name, Key=file_name)

print(f'File {file_name} deleted successfully from {bucket_name}!')
