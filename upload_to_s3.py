import boto3

# Replace with your actual bucket name
bucket_name = 'mys3bucket '

# File you want to upload
file_name = 'file.txt'

# Create an S3 client
s3 = boto3.client('s3')

# Upload the file
s3.upload_file(file_name, bucket_name, file_name)

print(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'")
