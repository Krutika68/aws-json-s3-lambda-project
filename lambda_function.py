import json
import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    
    bucket = "project-json-bucket-mumbai"
    key = "data/employees.json"

    # Read JSON file from S3
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(obj['Body'].read())

    # Dynamic filter
    department = event.get("department")

    if department:
        filtered = [emp for emp in data if emp["department"] == department]
    else:
        filtered = data

    return {
        "statusCode": 200,
        "body": json.dumps(filtered, indent=4)
    }