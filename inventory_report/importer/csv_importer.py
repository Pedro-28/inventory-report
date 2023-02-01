import csv


class CsvImporter:
    @staticmethod
    def import_data(path: str):
        reports = list()
        with open(path) as file:
            file_data = csv.DictReader(file)
            reports = [data for data in file_data]
        return reports
