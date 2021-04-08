#!/usr/bin/python

"""

Script to Add New IAM User(s)
Also Attaches User to Existing IAM Security Group 

"""

__author__    = ' Donald R. Whitfield'
__copyright__ = 'S-Box Security, LLC'
__email__     = 'donaldwhitfield@icloud.com'
__status__    = 'Development'


import boto3
import yaml

iam = boto3.client('iam')

def Create_IAM_User():
    User_Name = iam.create_user(UserName = 'dwhitfield')
    User_Key  = iam.create_access_key(UserName = 'dwhitfield')

    Attach_Group = iam.add_user_to_group(
    UserName  = 'dwhitfield',
    GroupName = 'AdminGroup')

    print(yaml.dump(User_Name))
    print(yaml.dump(User_Key['AccessKey']))
    
Create_IAM_User()
