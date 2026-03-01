# AWS JSON Ingestion Project

## Project Overview
This project demonstrates a **serverless workflow** for ingesting, storing, and querying JSON data using AWS services. Sample employee JSON data is generated with Python, uploaded to an Amazon S3 bucket, and dynamically filtered using an AWS Lambda function.

---

## AWS Services Used
- **Amazon S3** – Stores JSON files.  
- **AWS Lambda** – Queries JSON files dynamically using Python.  
- **IAM** – Configures permissions for Lambda to access S3.  

---

## Sample Data Structure
The dataset contains employee information with ~10 fields per record, including nested JSON:

- `employee_id`  
- `name`  
- `department`  
- `salary`  
- `address` (nested JSON)  
- `skills`  
- `active`  
- `joining_date`  
- `manager`  
- `projects` (nested JSON)  

**Example JSON Record:**
```json
{
  "employee_id": 1,
  "name": "Alice",
  "department": "Engineering",
  "salary": 80000,
  "address": {"city": "Mumbai", "state": "MH"},
  "skills": ["Python", "AWS", "SQL"],
  "active": true,
  "joining_date": "2025-01-15",
  "manager": "Bob",
  "projects": [{"name": "ProjectX", "status": "Ongoing"}]
}


```
Architecture Flow
Python Script (upload_to_s3.py)
           ↓
   Amazon S3 Bucket
(employees.json stored)
           ↓
  AWS Lambda Function
(reads and processes JSON)
           ↓
 Dynamic JSON Query Result
 ```

 ```
S3 Bucket Details:

Bucket Name: project-json-bucket-mumbai
Region: ap-south-1 (Mumbai)
Bucket Type: General Purpose
Versioning: Disabled
Public Access: Blocked
 ```
---
 ```
## How to Run

1. **Install dependencies:**
```bash
pip install -r requirements.txt

2. **Generate sample JSON data:**
```bash
python generate_json.py

3. **Upload JSON to S3:**
```bash
python upload_to_s3.py

4. Test Lambda Function
Configure the Lambda function in the AWS console using the code in lambda_function.py.
Provide an input event (JSON) and check the filtered output.
 ```
---
Conclusion:

This project demonstrates a serverless architecture where JSON data is generated using Python, stored in Amazon S3, and dynamically queried using AWS Lambda. The solution ensures scalable and efficient data processing while preserving structured and semi-structured data including nested JSON objects and arrays.
---
