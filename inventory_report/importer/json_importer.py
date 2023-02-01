import json


class JsonImporter:
    @staticmethod
    def import_data(path: str):
        reports = list()
        with open(path) as file:
            file_data = json.load(file)
            reports = [data for data in file_data]
        return reports
