from xml.etree import ElementTree as ET


from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        reports = list()
        file_data = ET.parse(path).getroot().findall("record")
        for report in file_data:
            report_dict = dict()
            for reportInfos in report.getchildren():
                report_dict[reportInfos.tag] = reportInfos.text
            reports.append(report_dict)
        return reports
