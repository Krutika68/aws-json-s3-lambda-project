import boto3
import json

# S3 details
BUCKET_NAME = "project-json-bucket-mumbai"
S3_KEY = "data/employees.json"
FILE_NAME = "employees.json"

# Sample employee JSON data
employees = [
    {
        "employee_id": 1,
        "name": "Alice",
        "department": "Engineering",
        "salary": 80000,
        "address": {
            "city": "Mumbai",
            "state": "MH"
        },
        "skills": ["Python", "AWS", "SQL"],
        "active": True,
        "joining_date": "2025-01-15",
        "manager": "Bob",
        "projects": [
            {
                "name": "ProjectX",
                "status": "Ongoing"
            }
        ]
    }
]

# Save JSON locally
with open(FILE_NAME, "w") as f:
    json.dump(employees, f, indent=4)

# Upload to S3
s3 = boto3.client("s3")
s3.upload_file(FILE_NAME, BUCKET_NAME, S3_KEY)

print(f"Uploaded {FILE_NAME} to s3://{BUCKET_NAME}/{S3_KEY}")