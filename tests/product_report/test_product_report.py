from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "Leite"
    nome_da_empresa = "Nestle"
    data_de_fabricacao = "31/01/2023"
    data_de_validade = "20/03/2023"
    numero_de_serie = "123456789"
    instrucoes_de_armazenamento = "Manter na geladeira após aberto"

    product_print = (
        "O produto Leite fabricado em 31/01/2023 por Nestle "
        "com validade até 20/03/2023 "
        "precisa ser armazenado Manter na geladeira após aberto."
    )

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )
    assert product.__repr__() == product_print
