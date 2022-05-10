#!/usr/bin/python

"""
Script to Print a Nicely Formatted Listing of all Security Groups.
The Security Groups have to be provided to the script for it to work properly.
"""

__author__    = ' Donald R. Whitfield'
__copyright__ = 'S-Box Security, LLC'
__email__     = 'donaldwhitfield@icloud.com'
__status__    = 'Development'

import boto3
import yaml


from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

sg_idlist = ["sg-0480cc92206f2106a", "sg-05491b36d633f75ce", "sg-5a09e15e"]

try:
    response = ec2.describe_security_groups(GroupIds=sg_idlist)
    print(yaml.dump(response))
except ClientError as e:
    print(e)
