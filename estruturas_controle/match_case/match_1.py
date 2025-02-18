# Na época em que o curso foi gravado não existia match case
# no python por isso todas as aulas vão ter soluções
# com e sem match/case

dia_semana = 3

match dia_semana:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sabádo')
    case _:
        print('Dia inválido')


# Solução do professor, sem -> match/case, como explicando no arquivo .txt
def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')
