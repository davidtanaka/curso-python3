frase = 'Python é uma boa linguagem'
print('py' not in frase)
print('boa' in frase)

print(frase.lower()) # Isso não mudaa o valor da variável apenas mostra minúscula
frase = frase.lower() # Isso sim altera realmente o valor da variável
print(frase)

print(frase.split()) # Isso separa a frase à partir do carácter desejado 
print(frase.split('o'))
