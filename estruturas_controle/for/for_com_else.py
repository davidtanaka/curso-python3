PALAVRAS_PROIBIDAS = ['futebol', 'religião', 'política']

textos = [
    'João gosta de futebol e religião',
    'A praia foi divertida',
    'Paulo não gosta de política',
]

for texto in textos:
    
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui pelo menos uma palavra proíbida: ', palavra)
            break
    else:
        print('Texto aprovado: ', texto)
