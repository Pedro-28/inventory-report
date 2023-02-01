import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    sys_values = sys.argv
    # print(f"SDSADSADS {sys_values}")
    if len(sys_values) != 3:
        return print("Verifique os argumentos", file=sys.stderr)

    if sys_values[1].endswith(".csv"):
        importer = CsvImporter
    elif sys_values[1].endswith(".json"):
        importer = JsonImporter
    elif sys_values[1].endswith(".xml"):
        importer = XmlImporter

    inventory_refactor = InventoryRefactor(importer)
    print(inventory_refactor.import_data(sys_values[1], sys_values[2]), end="")


if __name__ == "__main__":
    main()
