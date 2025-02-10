# Criando um dicionário inicial
# O dicionário armazena diferentes tipos de dados: string, inteiro e lista
dicionario = {'nome': 'Prof. Alison', 'idade': 34, 'cursos': ['Python', 'Js']}
print(dicionario)

# Modificando valores existentes
dicionario['idade'] = 36  # Atualiza a idade para 36
dicionario['cursos'].append('Django')  # Adiciona 'Django' na lista de cursos
print(dicionario)

# Removendo um elemento usando pop()
# .pop() remove a chave especificada e retorna seu valor
nome_removido = dicionario.pop('nome')  # Remove a chave 'nome' e armazena seu valor
print(nome_removido)
print(dicionario)

# Removendo um elemento usando del
# del remove a chave especificada permanentemente, sem retornar o valor
del dicionario['idade']  # Remove a chave 'idade' do dicionário
print(dicionario)

# Atualizando o dicionário com novos valores
dicionario.update({'nome': 'Prof. Leandro', 'idade': 36, 'sexo': 'M'})  # Adiciona novos pares chave-valor
print(dicionario)

# Limpando todo o dicionário
dicionario.clear()  # Remove todos os itens do dicionário, deixando-o vazio
print(dicionario)
