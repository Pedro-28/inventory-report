# import csv
# import json
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

# from xml.etree import ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        reports: list
        if path.endswith(".xml"):
            reports = XmlImporter.import_data(path)
        elif path.endswith(".csv"):
            reports = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            reports = JsonImporter.import_data(path)
        if report_type == "simples":
            return SimpleReport.generate(reports)
        # elif report_type == "completo":
        return CompleteReport.generate(reports)
