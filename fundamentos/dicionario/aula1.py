dicionario = {'nome': 'Prof(a): Ana.', 'idade': 34, 'cursos': ['Inglês', 'Python']}
print(type(dicionario))
print(dicionario['nome'])
# print(dicionario['idade'])
# print(dicionario['cursos'])

print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

print(dicionario.get('idade'))
print(dicionario.get('tags'))
print(dicionario.get('tags', []))
