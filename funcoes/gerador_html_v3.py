def bloco_tag(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'

def tag_list(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'

if __name__ == '__main__':
    lista = tag_list('arroz', 'cebola', 'cenoura', 'couve')
    bloco = bloco_tag(lista, classe="lista-alimentos")
    print(lista)
    print(bloco)
