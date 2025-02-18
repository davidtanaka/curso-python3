from random import randint

def jogo_da_sorte(numero):
    dado = randint(1, 6)
    for contador in range(1, 7):
        if numero % 2 != 0:
            continue
        if numero % 2 == 0 and numero == dado:
            print('Pensamos no mesmo número. E ele é par' )
            break
    else:
        print('Você errou!')

jogo_da_sorte(4)
