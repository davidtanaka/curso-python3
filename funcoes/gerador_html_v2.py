def bloco_tag(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(bloco_tag('bloco'))
    print(bloco_tag('inline e case', 'info', True))
    print(bloco_tag('inline', inline=True))
    print(bloco_tag('falhou', classe='error'))
