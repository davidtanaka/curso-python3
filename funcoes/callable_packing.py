def calcula_preco(preco_bruto, calc_imposto, *params):
    return preco_bruto + preco_bruto * calc_imposto(*params)


def imposto_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, nivel_perigo=1):
    return 0.11 * nivel_perigo if explosivo else 0


if __name__ == '__main__':
    # fone = calcula_preco(20, imposto_x, True)
    # bomba = calcula_preco(200, imposto_y, True, 5)
    # print(bomba)

    preco_bruto = 5000
    preco_final_foguete = calcula_preco(preco_bruto, imposto_x, True)
    preco_final_foguete = calcula_preco(preco_final_foguete, imposto_y, True, 5)
    print(f'Preço final: R$ {preco_final_foguete}')
