import json
from json import JSONEncoder
from typing import List

class Student:
    
    def __init__(self, full_name: str, avg_rank: float, courses: list) -> None:
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses
        
    def __repr__(self):
        return f'{self.full_name} ({self.avg_rank:g}): {self.courses}'
    
    @classmethod    
    def from_json(cls, json_file: str) -> "Student":
        with open(json_file, "r") as f:
            data = json.load(f)
        return cls(**data)
        
    @classmethod
    def from_dict(cls, dct: dict) -> "Student":
        full_name = dct["full_name"]
        avg_rank = dct["avg_rank"]
        courses = dct["courses"]
        return cls(full_name, avg_rank, courses)
        
    
class Group():

    def __init__(self, title: str, students: list) -> None:
        self.title = title
        self.students = students 
        
    def __str__(self):
        return f"{self.title}: {[str(student) for student in self.students]}"

    @classmethod 
    def create_group_from_file(cls, students_file):
        title = students_file.split('.')[0]
        with open(students_file) as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = [data]
        for  d in data:
            students = [Student.from_dict(x) for x in data]
        return cls(title, students)
    
    def serialize_to_json(list_of_groups, filename):
        dump_list = []

        def cond(val, group_s):
            if not isinstance(val, list):
                result = val
            if isinstance(val, list):
                val_list = [student.__dict__ for student in group_s.students]
                result = val_list
            return result

        for group in list_of_groups:
            dump_list.append({key: cond(value, group) for (key, value) in group.__dict__.items()})
        with open(filename,"w") as file:
            json.dump(dump_list, file)
