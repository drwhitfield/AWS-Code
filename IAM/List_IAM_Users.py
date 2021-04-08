#!/usr/bin/python

"""

Script to Print a Nicely Formatted Listing of IAM Users
Raw Output Resembles JSON But It's Actually A Dictionary
No Secret Access Keys Are Printed 

"""

__author__    = ' Donald R. Whitfield'
__copyright__ = 'S-Box Security, LLC'
__email__     = 'donaldwhitfield@icloud.com'
__status__    = 'Development'


import boto3
import yaml

iam = boto3.client('iam')

def List_IAM_Users():
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        print(yaml.dump(response))

List_IAM_Users()
