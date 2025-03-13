provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "my_ec2" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "my-aws-keypair"  # Replace with your actual key pair name
  tags = {
    Name = "MyEC2Instance"
  }
}
