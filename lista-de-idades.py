idade1 = 39
idade2 = 40
idade3 = 41
idade4 = 42

print('A idade do primeiro é:', idade1)

print('\n------------------------------------------------------\n')
idades = [40, 41, 42, 43]
print(f'Exitem {len(idades)} pessoas na lista')
print('A idade do primeiro é:', idades[0])

print('\n------------------------------------------------------\n')
print('Adicionando uma nova idade')
idades.insert(0, 39)
print('A idade do primeiro é:', idades[0])

print('\n------------------------------------------------------\n')
print('Removendo a idade do primeiro')
idades.pop(0)
print('A idade do primeiro é:', idades[0])

print('\n------------------------------------------------------\n')
print('Removendo a segunda idade')
idades.pop(1)
print('A idade do segundo agora é:', idades[1])

print('\n------------------------------------------------------\n')
print('Removendo a idade 43')
idades.remove(43)
print('As idades atuais são:', idades)

print('\n------------------------------------------------------\n')
print('Adicionando uma nova idade')
idades.append(43)
print('As idades atuais são:', idades)

print('\n------------------------------------------------------\n')
print('Limpando a lista')
idades.clear()
print('As idades atuais são:', idades)

print('\n------------------------------------------------------\n')
print('Verifica se uma idade existe na lista')
print('A idade 42 existe na lista?')
print('Sim, está na lista!' if 42 in idades else 'Não, não está na lista!')

print('\n------------------------------------------------------\n')
print('Adiciona uma lista de idades a lista atual')
idades.extend([40, 41, 42, 43])
print('As idades atuais são:', idades)

print('\n------------------------------------------------------\n')
print('Adiciona um novo elemento a lista')
idades += [44, 45, 46]
print('As idades atuais são:', idades)

print('\n------------------------------------------------------\n')
print('Cria nova lista com idades ano que vem')
idades_ano_que_vem = [idade + 1 for idade in idades]
print('As idades atuais são:', idades)
print('As idades ano que vem são:', idades_ano_que_vem)

print('\n------------------------------------------------------\n')
print('Seleciona as idades que são maiores que 18')
idades = [15, 16, 17, 18, 19, 20, 21, 22]
idades_maiores_de_18 = [idade for idade in idades if idade > 18]
print('As idades atuais são:', idades)
print('As idades maiores de 18 são:', idades_maiores_de_18)

print('\n------------------------------------------------------\n')
print('Remove idades duplicadas')
idades = [15, 15, 16, 17, 18, 19, 20, 20]
idades.remove(15)
idades.remove(20)
print('As idades atuais são:', idades)

idades = [15, 15, 16, 17, 18, 19, 20, 20]
idades = list(set(idades))
print('As idades atuais são:', idades)

print('\n------------------------------------------------------\n')
print('Imutabilidade da lista')


def faz_processamento_de_visualizacao(lista):
    result = f'O tamanho da lista é: {len(lista)}'
    lista.append(44)
    return result


idades = [15, 16, 17, 18, 19, 20, 21, 22]
print(faz_processamento_de_visualizacao(idades))
print('As idades atuais são:', idades)

print('\n------------------------------------------------------\n')
print('Imutabilidade da lista')


def faz_processamento_de_visualizacao_vazia(lista=None):
    if lista is None:
        lista = list()
    result = f'O tamanho da lista é: {len(lista)}'
    lista.append(44)
    return result


print(faz_processamento_de_visualizacao_vazia())
print(faz_processamento_de_visualizacao_vazia())
