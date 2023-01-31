from datetime import datetime
from typing import List, Dict


def convert_in_date(string: str):
    return datetime.strptime(string, "%Y-%m-%d")


class SimpleReport:
    @staticmethod
    def generate(reports: List[Dict]):
        fabrication_list = [
            convert_in_date(report["data_de_fabricacao"]) for report in reports
            ]
        oldest_fabrication = min(fabrication_list).strftime('%Y-%m-%d')
        validity_list = [
            convert_in_date(report["data_de_validade"]) for report in reports
            ]
        now = datetime.now()
        nearest_validity = min(
            validity for validity in validity_list if validity > now
            ).strftime('%Y-%m-%d')
        companies = [report["nome_da_empresa"] for report in reports]
        company_with_more_products = max(set(companies), key=companies.count)

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication}\n"
            f"Data de validade mais próxima: {nearest_validity}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
            )
