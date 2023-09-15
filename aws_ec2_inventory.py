#!/usr/bin/python3
import os
import sys
import json
import boto3

# Define the AWS credentials and region.
aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_DEFAULT_REGION')

# Create an AWS session.
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

# Initialize an EC2 client.
ec2 = session.client('ec2')

# Function to fetch EC2 instances with a specific tag.
def get_ansible_nodes():
    instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Type',
                'Values': ['ansible_node']
            }
        ]
    )

    ansible_nodes = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            ansible_nodes.append({
                'ansible_ssh_host': instance['PublicIpAddress'],
                'ansible_ssh_user': 'your_ssh_user',  # Replace with your SSH user
                'ansible_ssh_private_key_file': 'your_private_key.pem'  # Replace with your private key file
            })

    return ansible_nodes

# Main function for generating the dynamic inventory.
def main():
    inventory = {
        '_meta': {
            'hostvars': {}
        },
        'ansible_nodes': get_ansible_nodes()
    }
    print(json.dumps(inventory))

if __name__ == '__main__':
    main()

