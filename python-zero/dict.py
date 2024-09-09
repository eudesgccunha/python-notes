# %%

dados = {'nome': 'Eudes', 'sobrenome':'cunha', 'idade':'29'} # 'chave':'valor'

nome = dados['nome']
print(nome)


# %%

dictionary = {'nome': ['eudes', 'gustavo'], 'sobrenome': ['constantino','cunha'], 'idade':'29'} 
print(dictionary)


# %%
dictionary = {'nome': ['eudes', 'gustavo'], 'sobrenome': ['constantino','cunha'], 'idade':'29'} 

nome = dictionary['nome'][1]
print(nome)

# %%
# método keys retorna as chaves do dicionário
dictionary.keys()

# %%
# método vaues retorna os valores do dicionário
dictionary.values()

# %% retorna os pares dos dicionários - chave e valor

dictionary.items()