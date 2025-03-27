from app.utils.gerador import novo_nome
from app.negocios.negocio import nome_existente
from app.negocios.backend import add_nome

def main():
    while True:
        nome = novo_nome()
        if not nome_existente(nome):
            add_nome(nome)
            break

    return f'Criando novo nome de testes: "{nome}"'


if __name__ == '__main__':
    print(main())
