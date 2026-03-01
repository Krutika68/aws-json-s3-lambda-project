# AWS JSON Ingestion Project

## Project Overview
This project demonstrates a serverless workflow for ingesting, storing, and querying JSON data using AWS services. Sample employee JSON data is generated with Python, uploaded to an Amazon S3 bucket, and dynamically filtered using an AWS Lambda function.

## AWS Services Used
- **Amazon S3** – Stores JSON files.
- **AWS Lambda** – Queries JSON files dynamically using Python.
- **IAM** – Grants Lambda permissions to access S3.

## Project Structure

# AWS JSON Ingestion Project

## Project Overview
This project demonstrates a serverless workflow for ingesting, storing, and querying JSON data using AWS services. Sample employee JSON data is generated with Python, uploaded to an Amazon S3 bucket, and dynamically filtered using an AWS Lambda function.

## AWS Services Used
- **Amazon S3** – Stores JSON files.
- **AWS Lambda** – Queries JSON files dynamically using Python.
- **IAM** – Grants Lambda permissions to access S3.

## Project Structure
```

aws-json-ingestion/
├── generate_json.py # Generates sample employee JSON data
├── upload_to_s3.py # Uploads JSON data to S3
├── lambda_function.py # Lambda function to filter JSON data
├── requirements.txt # Python dependencies
├── README.md # Project description
└── screenshots/ # Screenshots of execution and results
```

## Sample Data Structure
The employee dataset contains ~10 fields per record, including nested JSON values:

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

## How it Works
1. `generate_json.py` creates sample JSON data.
2. `upload_to_s3.py` uploads the JSON file to S3.
3. `lambda_function.py` queries the JSON data dynamically based on input parameters (e.g., department).
4. Filtered results are returned as JSON.

## Example Lambda Input Event
```json
{
  "department": "Engineering"
}

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
