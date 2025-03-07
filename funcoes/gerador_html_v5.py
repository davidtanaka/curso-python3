def tag_bloco(*args, **kwargs):
    tag = 'span' if kwargs.get('inline') else 'div'
    html = args[1:] if not callable(args) else args(*args)
    
    return (
        f'<{tag} class="{kwargs.get("classe", "")}" '
        f'id="{kwargs.get("bloco_id", "")}" '
        f'bloco_accesskey="{kwargs.get("bloco_accesskey", "")}">{html}</{tag}>'
    )


def tag_lista(*args):
    lista = ''.join(f'<li>{item}</li>' for item in args)
    return f'<ul id="{args[0]}">{lista}</ul>'


if __name__ == '__main__':
    # print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
    print(
        tag_bloco(tag_lista, 'Sábado', 'Domingo', classe="info", 
        bloco_accesskey='m', bloco_id='conteudo', ul_id='lista')
    )

    print(
        tag_bloco(tag_lista, 'Sábado', 'Domingo', ul_id='lista')
    )
