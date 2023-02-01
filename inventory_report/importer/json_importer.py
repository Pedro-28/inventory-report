import json


from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            file_data = json.load(file)
            return [data for data in file_data]
