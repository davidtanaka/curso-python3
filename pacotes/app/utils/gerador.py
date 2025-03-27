from random import randint


def novo_nome():
    nomes = [
    "Lucas", "Miguel", "Arthur", "Gabriel", "Heitor", "Bernardo",
    "Davi", "João", "Pedro", "Matheus", "Gustavo", "Felipe",
    "Vinícius", "Eduardo", "Henrique", "Rafael", "Daniel", "Enzo"
    ]
    nome_aleatorio = nomes[randint(0, len(nomes))]
    return nome_aleatorio
