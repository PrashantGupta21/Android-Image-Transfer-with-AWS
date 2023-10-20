import boto3
import os


def main(path):
    access_key = ''
    secret_key = ''

    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    s3 = session.client('s3')
    s3.upload_file(path, "", "")
    return "Sent Successfully"
