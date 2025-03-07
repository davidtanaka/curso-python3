# def tag_bloco(*args, **kwargs):
#     tag = 'span' if kwargs.get('inline') else 'div'
#     html = args[1:] if not callable(args) else args(*args)
    
#     return (
#         f'<{tag} class="{kwargs.get("classe", "")}" '
#         f'id="{kwargs.get("bloco_id", "")}" '
#         f'bloco_accesskey="{kwargs.get("bloco_accesskey", "")}">{html}</{tag}>'
#     )


# def tag_lista(*args):
#     lista = ''.join(f'<li>{item}</li>' for item in args)
#     return f'<ul id="{args[0]}">{lista}</ul>'


# Solução professor
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def filtrar_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) \
        else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {filtrar_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    # print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
    print(
        tag_bloco(tag_lista, 'Sábado', 'Domingo', classe="info", 
        bloco_accesskey='m', bloco_id='conteudo', ul_id='lista')
    )

    print(
        tag_bloco(tag_lista, 'Sábado', 'Domingo', ul_id='lista')
    )
