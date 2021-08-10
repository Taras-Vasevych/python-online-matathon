import json
import jsonschema
from jsonschema import validate
import csv


class InvalidInstanceError(Exception):
    """Raised when schema does not satisfy described json format"""
    def __init__(self, schema):
        self.schema = schema
    
    def __str__(self):
        return f"Error in {self.schema} schema"


class DepartmentName(Exception):
    """Raised when department_id does not found in department.json"""
    def __init__(self, key=None):
        self.key = key
        
    def __str__(self):
        return f"Department with id {self.key} doesn't exists"
    
    
def validate_json(data, schema):
    """Return True if data is valid, False othervise"""
    try:
        validate(data, schema)
    except jsonschema.exceptions.ValidationError:
        return False
    else:
        return True

def user_with_department(csv_file, user_json, department_json):    
    user_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "type": "array",
        "items": {
            "$ref": "#/definitions/WelcomeElement"
        },
        "definitions": {
            "WelcomeElement": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "department_id": {
                        "type": "integer"
                    }
                },
                "required": [
                    "department_id",
                    "id",
                    "name"
                ],
                "title": "WelcomeElement"
            }
        }
    }    
    department_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "type": "array",
        "items": {
            "$ref": "#/definitions/WelcomeElement"
        },
        "definitions": {
            "WelcomeElement": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "name"
                ],
                "title": "WelcomeElement"
            }
        }
    }
    
    with open(user_json, 'r') as users, open(department_json, 'r') as departments:
        users = json.load(users)
        departments = json.load(departments)    
        
    if not validate_json(users, user_schema):
        raise InvalidInstanceError('user')
    if not validate_json(departments, department_schema):
        raise InvalidInstanceError('department')
        
    departments = {
        department['id']: department['name']
        for department in departments
    }
    output = []
    for user in users:
        department_id = user['department_id']
        department = departments.get(department_id)
        if not department:
            raise DepartmentName(department_id) 
        name = user['name']
        output.append({'name': name, 'department': department})
    
    with open(csv_file, 'w') as output_file:
        fieldnames = ['name', 'department']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output)
