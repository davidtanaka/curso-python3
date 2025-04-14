from datetime import datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (concluída)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Lavar roupa'))
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Passar pano'))
    casa.append(Tarefa('Lavar prato'))
    casa.append(Tarefa('Lavar carro'))

    # Desafio
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    for tarefa in casa:
        print(f'- {tarefa}')

print(main())
