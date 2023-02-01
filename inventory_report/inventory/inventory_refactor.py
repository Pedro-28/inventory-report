from inventory_report.importer.importer import Importer


from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer: Importer):
        self.__importer = importer

    def import_data(self, path: str, report_type: str):
        reports = self.__importer.import_data(path)
        if report_type == "simples":
            return SimpleReport.generate(reports)
        elif report_type == "completo":
            return CompleteReport.generate(reports)
