# Aprendendo mais sobre strings
# strings são imutáveis (Não é possivel mudar o valor)

# print(dir(str))
from pydoc import text


nome = 'Davi Tanaka'
# print(nome)

print(nome[0])
# nome[0] = 'p' # isso gera um erro pois não é possível trocar o valor de uma str

# 'Marca d'água'
print("Dias D'Avila" == 'Dias D\'Avila')

texto = 'Texto entre apostrófos pode ter "aspas"'
print(texto)

doc = """Texto com múltiplas
... linhas"""
print(doc)

doc2 = "Texto com múltiplas \n... linhas"
print(doc2)

doc = '''Texto com múltiplas
... linhas com aspas simples'''
print(doc)
