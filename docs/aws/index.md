# AWS

## boto3 library

A [unique library](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) to access all AWS services from a python app. 

### Installation

```sh
pip install boto3[crt]
```

Set up authentication credentials for your AWS account using either the IAM Console or the AWS CLI.

```sh
aws configure
# Verify access
aws iam list-users
```

!!! info
    The jbcodeforce/python docker image has the aws cli and goto3.

### Programming samples

```python
inport boto3
# declare a client to the service you want
s3 = goto3.service("s3")
# use SDK API for s3.
s3.buckets.all()
```


