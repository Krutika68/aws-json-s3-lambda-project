import json

data = [
    {
        "employee_id": 1,
        "name": "Alice",
        "department": "Engineering",
        "salary": 80000,
        "address": {"city": "Mumbai", "state": "MH"},
        "skills": ["Python", "AWS", "SQL"],
        "active": True,
        "joining_date": "2025-01-15",
        "manager": "Bob",
        "projects": [{"name": "ProjectX", "status": "Ongoing"}]
    },
    {
        "employee_id": 2,
        "name": "John",
        "department": "Data",
        "salary": 70000,
        "address": {"city": "Pune", "state": "MH"},
        "skills": ["PySpark", "SQL", "AWS"],
        "active": True,
        "joining_date": "2024-11-01",
        "manager": "Eve",
        "projects": [{"name": "ProjectY", "status": "Completed"}]
    }
]

with open("employees.json", "w") as f:
    json.dump(data, f, indent=4)

print("employees.json file created in project folder!")