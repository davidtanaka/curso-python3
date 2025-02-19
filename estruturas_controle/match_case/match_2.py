# Na época em que o curso foi gravado não existia match case
# no python por isso todas as aulas vão ter soluções
# com e sem match/case

# Esse exercício deve retornar: 
# se é um dia de meio de semana ou de fim de semana

# Minha solução (atualizada)
def dia_semana(dia):
    match dia:
        case 'sabado':
            print('Hoje é Fim de semana')
        case 'domingo':
            print('Hoje é Fim de semana')
        case 'segunda':
            print('Hoje é meio de semana')
        case 'terca':
            print('Hoje é meio de semana')
        case 'quarta':
            print('Hoje é meio de semana')
        case 'quinta':
            print('Hoje é meio de semana')
        case 'sexta':
            print('Hoje é meio de semana')
        case _:
            print('Digite um dia válido')

dia_semana(input('Digite o dia da semana: (letras minúsculas e sem acentos): '))


# Solução professor
# Sem match/case
def get_tipo_dia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')
