# Tabela da verdade do AND
print(True and True)  # True e True resulta em True
print(True and False) # True e False resulta em False
print(False and True) # False e True resulta em False
print(False and False) # False e False resulta em False

# Tabela da verdade do OR
print(True or True)  # True ou True resulta em True
print(True or False) # True ou False resulta em True
print(False or True) # False ou True resulta em True
print(False or False) # False ou False resulta em False

# Tabela da verdade do XOR (Diferente)
print(True != True)  # True é igual a True, então o resultado é False
print(True != False) # True é diferente de False, então o resultado é True
print(False != True) # False é diferente de True, então o resultado é True
print(False != False) # False é igual a False, então o resultado é False

# Operador de negação (not)
print(not True)  # Negação de True é False
print(not False) # Negação de False é True

# Simulação de uma situação real com variáveis
saldo = 1000
salario = 3400
despesas = 1900

# Verifica se o saldo é positivo e se as despesas são menores que 80% do salário
saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

# Verifica se ambas as condições são verdadeiras (meta alcançada)
meta = saldo_positivo and despesas_controladas
print(meta)
