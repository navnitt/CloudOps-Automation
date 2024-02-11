#!/bin/bash
#To track resource usage in aws
set -x
#list s3 buckets
aws s3 ls

#list ec2 instance ids only
#aws ec2 describe-instances
aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId'  

#list aws lambda functions
aws lambda list-functions

#list IAM users
aws iam list-users
