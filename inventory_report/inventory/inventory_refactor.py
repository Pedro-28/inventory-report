from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator


from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = list()

    def import_data(self, path: str, report_type: str):
        self.data.extend(self.importer.import_data(path))
        if report_type == "simples":
            return SimpleReport.generate(self.data)
        elif report_type == "completo":
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
