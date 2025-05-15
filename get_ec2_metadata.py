import requests

# AWS EC2 instance metadata URL
url = "http://169.254.169.254/latest/meta-data/"

# Make the request
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print("EC2 Metadata:")
        print(response.text)
    else:
        print("Failed to retrieve metadata.")
except Exception as e:
    print(f"Error: {e}")
