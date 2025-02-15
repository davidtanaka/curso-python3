# Esse código foi um desafio passado pelo professor.

# Minha solução
nota = float(input('Digite sua nota: '))

def calcular_nota(nota):
    if nota >= 9.1 and nota <= 10:
        print('Sua nota é: A')

    elif nota >= 8.1 and nota <= 9.0:
        print('Sua nota é: A-')

    elif nota >= 7.1 and nota <= 8.0:
        print('Sua nota é: B')

    elif nota >= 6.1 and nota <= 7.0:
        print('Sua nota é: B-')

    elif nota >= 5.1 and nota <= 6.0:
        print('Sua nota é: C')

    elif nota >= 4.1 and nota <= 5.0:
        print('Sua nota é: C-')

    elif nota >= 3.1 and nota <= 4.0:
        print('Sua nota é: D')

    elif nota >= 2.1 and nota <= 3.0:
        print('Sua nota é: D-')

    elif nota >= 1.1 and nota <= 2.0:
        print('Sua nota é: E')

    elif nota >= 0.0 and nota <= 1.0:
        print('Sua nota é: E-')
    else:
        print('Nota Inválida')

if __name__ == '__main__':
    calcular_nota(nota)



# Solução do professor:
# def nota_conceito(valor):
#     nota = float(valor)

#     if nota > 10:
#         return 'Nota inválida'
#     elif nota >= 9.1:
#         return 'A'
#     elif nota >= 8.1:
#         return 'A-'
#     elif nota >= 7.1:
#         return 'B'
#     elif nota >= 6.1:
#         return 'B-'
#     elif nota >= 5.1:
#         return 'C'
#     elif nota >= 4.1:
#         return 'C-'
#     elif nota >= 3.1:
#         return 'D'
#     elif nota >= 2.1:
#         return 'D-'
#     elif nota >= 1.1:
#         return 'E'
#     elif nota >= 0:
#         return 'E-'
#     else:
#         return 'Nota inválida'


# if __name__ == '__main__':
#     valor_informado = input('Nota do aluno: ')
#     conceito = nota_conceito(valor_informado)
#     print(conceito)
