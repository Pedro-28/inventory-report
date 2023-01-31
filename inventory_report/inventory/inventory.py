import csv
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        reports: list
        with open(path) as file:
            file_data = csv.DictReader(file)
            reports = [data for data in file_data]
        if report_type == "simples":
            return SimpleReport.generate(reports)
        elif report_type == "completo":
            return CompleteReport.generate(reports)
