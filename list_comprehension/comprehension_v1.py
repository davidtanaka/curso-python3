# [ exepressão for item in list if condicional ]
dobros = [i * 2 for i in range(10)]
print(dobros)

# Sem list comprehension
dobros = []
for i in range(10):
    dobros.append(i * 2)
print(dobros)
