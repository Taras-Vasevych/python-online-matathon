import json
import pickle
from enum import Enum


class FileType(Enum):
    JSON = "JSON"
    BYTE = "BYTE"


class SerializeManager:
    def __init__(self, file_name, type_for_serializing):
        self.file_name = file_name
        self.type_for_serializing = type_for_serializing

    def __enter__(self):
        if self.type_for_serializing == FileType.BYTE:
            self.file = open(self.file_name, 'wb')
        if self.type_for_serializing == FileType.JSON:
            self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


def serialize(object, filename, fileType):
    if  fileType == FileType.BYTE:
        with SerializeManager(filename, fileType) as f:
            pickle.dump(object, f)
    if  fileType == FileType.JSON:
        with SerializeManager(filename, fileType) as f:
            json.dump(object, f)
