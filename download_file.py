import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define bucket name and file names
bucket_name = 'my-boto3-s3-bucket-syamala'  # Change this to match your bucket
file_name = 'myfile.txt'
download_name = 'downloaded-file.txt'

# Download the file from S3
s3.download_file(bucket_name, file_name, download_name)

print(f'File {file_name} downloaded successfully as {download_name}!')
