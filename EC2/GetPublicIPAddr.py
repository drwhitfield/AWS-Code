#!/usr/bin/python

"""

Script to Obtain Public IP of EC2 Instance
Pass Image-ID of EC2 instance to Function

"""

__author__    = ' Donald R. Whitfield'
__copyright__ = 'S-Box Security, LLC'
__email__     = 'donaldwhitfield@icloud.com'
__status__    = 'Development'


import boto3


def Get_Public_IP(instance_id):
    ec2_client = boto3.client("ec2", region_name="eu-central-1")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))
            
Get_Public_IP('i-0ff9488cd545b8bc3')
