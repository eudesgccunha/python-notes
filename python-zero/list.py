lista = ['Eudes', 'Cunha', 'Masculino', 'Casado', 'Magro', 29, 1.82]
print(lista)

len(lista) # retorna o tamanho da lista

# %%
# acessando elementos de uma lista

lista[0] # primeiro elemento

# %%
lista[3] # ultimo elemento


# %%
lista[len(lista)-1] # estou retornando o ultmilo elemento da lista


# %%
lista[len(lista)-2] # estou retornando o peltmilo elemento da lista


# %%
lista[:3] 


# %%
lista[-3] 

# %%
lista[-1] 

# %%
lista[0:2] # recuperar os elementos 0 e 1 [intervalo fechado : intervalo aberto]

# %%
lista[:3] # recuperar os elementos 0 ao 2

# %%
lista[0:-1] # recuperar todos os elementos menos o ultimo

# %%

lista[::2] #start:stop:step - pulando elementos de uma lista - pulando elementos de uma lista - pego o primeiro e pula pro segundo

# %%
lista[::3] #start:stop:step - pulando elementos de uma lista - pego o primeiro e pula a cada tres terceiro

# %%
lista[::-1] # inverte a ordem e salta a cada 1 elemento


# %%
lista[::-2] # inverte a ordem e salta a cada 2 elementos


# %%

lista[-2:] # retonarndo os dois ultimos elementos

# %%

nova_lista = lista[:] #cópia da mesma lista 
print(nova_lista)

# %%

lista_vazia = []
print(lista_vazia)

# %%

notas = []
nota = 7.75

notas.append(nota) # o método append adiciona um elemento no final da lista. Altera a própria lista
# já o método das strings não alteram as strings originais (lower e upper)

notas.append(8.5) # o método append só aceita 1 elemento, neste caso, apenas uma nota

print(notas)
# %%
notas = []
nota = 7.75

notas.append(nota)
notas.append(8.5)
notas.extend([5.6, 7.95, 9.97, 10]) # aceita colocar mais de um elemento na lista. Você deve passar como uma lista e não como uma tupla
print(notas)

# %%
notas = []
nota = 7.75

notas.append(nota)
notas.append(8.5)
notas.extend([5.6, 7.95, 9.97, 10])
notas = notas + [4.0, 3.3, 1.5] # desta maneira também é possível adicionar elementos à lista

print(notas)

# %%
# outros métodos

# notas.remove
# notas.reverse
# notas.sort ...


# %%
# trabalhando com for em listas

names = ['Eudes', "Cunha", "Gustavo"]

for i in names:
    print(i)
    

# %%

nomes = ['eudes', "cunha", "gustavo"]

for nome in nomes:
    print(nome.title()) # .title coloca a primeira letra maiúscula

nomes.extend(['kate','regina'])

print(nomes)

# %%

nomes = ['eudes', "cunha", "gustavo"]

for nome in nomes:
    print(nome.title()) # .title coloca a primeira letra maiúscula

nomes.extend('regina') #extend em forma de tupla vai passar cada letra do elemento pra dentro da lista

print(nomes)
# %%
nomes = ['eudes', "cunha", "gustavo"]

for nome in nomes:
    print(nome.title()) # .title coloca a primeira letra maiúscula

nomes.append('regina')

print(nomes)

# %%
# acessando lista dentro de lista

dados = ['eudes', ['cunha', 'gustavo'], 'regina',['kate']]

dados[1][-1] 

# %%
# acessando lista dentro de lista

dados = ['eudes', ['cunha', 'gustavo'], 'regina',['kate']]

dados[1][0][3] #acessando o h de cunha

# %%

dados = ['eudes', ['cunha', 'gustavo'], 'regina',['kate']]

dados[1][1][:4] #acessando o gus de gustavo


# %%

alturas = []

for i in range(4):
    a = float(input(f'Adicione as alturas de Eudes, Kate, Biu e Ken, respectivamente {i+1}: '))
    alturas.append(a)
    
soma = sum(alturas)
print(soma)

# %%

# unpack de listas

dados = ['eudes', 'cunha']

nome, sobrenome = dados # nesse caso, o primeiro elemento será atribuído à primeira variável e o segundo elemento à segunda variável

print(nome)
print(sobrenome)
# %%

# unpack de listas

dados = ['eudes', 'cunha', 29, 1.82]

nome, sobrenome, *extra = dados # nesse caso, o primeiro elemento será atribuído à primeira variável e o segundo elemento à segunda variável

print(nome)
print(sobrenome)
print(extra) # extra com o * antes compila todo o resto dos itens da lista

# %%

# unpack de listas

dados = ['eudes', 'cunha', 29, 1.82, 'kate']

nome, sobrenome, *_, wife = dados # O *_ representa tudo o que eu não quero extrair da lista. Neste caso, a variável wife vai pegar o ultimo item da lista

print(nome)
print(sobrenome)
print(wife) 
# %%
