import boto3
import os


def main(path):
    access_key = 'AKIARJNMNEDDO76DHN7W'
    secret_key = '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'

    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    s3 = session.client('s3')
    s3.upload_file(path, "aws-equitables", "Output.zip")
    return "Sent Successfully"