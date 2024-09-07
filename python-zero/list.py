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