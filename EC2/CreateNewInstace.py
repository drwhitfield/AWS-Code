#!/usr/bin/python

"""

Script to Create New EC2 Instance
Prints Instance ID After Running

"""

__author__    = ' Donald R. Whitfield'
__copyright__ = 'S-Box Security, LLC'
__email__     = 'donaldwhitfield@icloud.com'
__status__    = 'Development'


import boto3

def Create_Instance():
    ec2_client = boto3.client("ec2", 'eu-central-1')
    instances = ec2_client.run_instances(
        ImageId="ami-0db9040eb3ab74509",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ec2-key-pair"
    )

    print(instances["Instances"][0]["InstanceId"])

Create_Instance()
