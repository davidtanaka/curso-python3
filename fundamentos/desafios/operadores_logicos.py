"""
Este programa simula um cenário onde a família ganha recompensas
(como ir ao shopping) com base no sucesso em duas tarefas.
O resultado de cada tarefa determina o tipo de recompensa
e se a "saúde" da família aumenta ou diminui.

- Confirmando os 2: TV 50' + Sorvete
- Confirmando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""

tarefa_terca = False
tarefa_quinta = True

tv_50 = tarefa_terca and tarefa_quinta
tv_32 = tarefa_terca or tarefa_quinta
sorvete = tarefa_terca or tarefa_quinta
saude = not sorvete

print(f'Tv de 50 polegadas {tv_50}, Tv de 32 polegadas {tv_32}')
print(f'Você tomou sorvete? {sorvete}, sua Saúde esta boa? {saude}')
