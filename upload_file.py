import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define bucket name and file name
bucket_name = 'my-boto3-s3-bucket-syamala'  # Change this to match your created bucket name
file_name = 'myfile.txt'

# Create a sample file
with open(file_name, 'w') as f:
    f.write("Hello S3 - Uploaded via Boto3")

# Upload the file to S3
s3.upload_file(file_name, bucket_name, file_name)

print(f'File {file_name} uploaded successfully to {bucket_name}!')
