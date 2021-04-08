#!/usr/bin/python

"""

Script to Delete AWS IAM User Accounts
Group Membership Must Be Removed Before Deletion
Access Key ID Must Also Be Removed Before Deletion

Note: The Access Key ID Must Be Provided to Script
Consider Providing As Command Line Argument

"""

__author__    = ' Donald R. Whitfield'
__copyright__ = 'S-Box Security, LLC'
__email__     = 'donaldwhitfield@icloud.com'
__status__    = 'Development'


import boto3
import yaml


iam = boto3.client('iam')


def Delete_IAM_User():
    Remove_Group = iam.remove_user_from_group(
        GroupName = 'AdminGroup',
        UserName  = 'dwhitfield')
    print(yaml.dump(Remove_Group))
    
    Remove_Access_Key = iam.delete_access_key(
        AccessKeyId = 'AKIAUPBW3EIM7YPE2FKH',
        UserName    = 'dwhitfield')
    print(yaml.dump(Remove_Access_Key))
    
    Delete_User_Acct = iam.delete_user(
        UserName = 'dwhitfield')
    print(yaml.dump(Delete_User_Acct))
    
Delete_IAM_User()

