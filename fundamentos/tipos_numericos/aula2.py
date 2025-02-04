# Operação com ponto flutuante
print(1.1 + 2.2)  # Pode não ser exatamente 3.3 devido à imprecisão dos floats

from decimal import Decimal, getcontext

# Divisão usando Decimal
print(Decimal(1) / Decimal(7))  # Resultado mais preciso que float padrão

# Definindo a precisão do Decimal para 4 dígitos
getcontext().prec = 4
print(Decimal(1) / Decimal(7))  # Agora limitado a 4 casas decimais

# Obtendo o maior valor entre 1 e 7 usando Decimal
print(Decimal.max(Decimal(1), Decimal(7)))  # Retorna 7

# Listando métodos e atributos disponíveis na classe Decimal
print(dir(Decimal))

# Alterando a precisão para 10 dígitos
getcontext().prec = 10
print(Decimal(1.1) + Decimal(2.2))  # Pode não ser exatamente 3.3 devido à conversão de float para Decimal

# Importando o módulo decimal inteiro
import decimal

# Listando métodos e atributos do módulo decimal
print(dir(decimal))

# Listando todas as variáveis, funções e módulos disponíveis no escopo atual
print(dir())
