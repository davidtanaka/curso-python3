def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de Idade'
    elif idade in range(18, 64 + 1):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Idoso'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade inválida'
    
if __name__ == '__main__':
    # print(faixa_etaria(17))
    for idade in (17, 35, 87, 113, -2, 64):
        print(f'{idade}: {faixa_etaria(idade)}')
