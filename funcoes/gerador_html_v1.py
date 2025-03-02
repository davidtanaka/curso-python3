def bloco_tag(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions)
    assert bloco_tag('Qualquer coisa') == \
        '<div class="success">Qualquer coisa</div>'
    assert bloco_tag('Não foi possível excluir', 'error') == \
        '<div class="error">Não foi possível excluir</div>'
