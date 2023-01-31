import csv
import json
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        reports: list
        with open(path) as file:
            if path.endswith('.csv'):
                file_data = csv.DictReader(file)
            elif path.endswith('.json'):
                file_data = json.load(file)
            reports = [data for data in file_data]
        if report_type == "simples":
            return SimpleReport.generate(reports)
        elif report_type == "completo":
            return CompleteReport.generate(reports)
