compras = (
    {'Quantidade': 2, 'preço': 10},
    {'Quantidade': 3, 'preço': 20},
    {'Quantidade': 5, 'preço': 14},
)


def calc_preco_total(compra):
    return compra['Quantidade'] * compra['preço']

totais = tuple(map(calc_preco_total, compras))

print('Preço totais:', totais)
print('total geral', sum(totais))