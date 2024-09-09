# %%

# a grosso modo, tuplas são listas imutáveis

tupla = ('Eudes', 'Cunha', 29, 1.82)

print(tupla)

# as tuplas são úteis para garantir dados que não devem ser alterados 

# set não pode ter elementos repetidos, as tuplas podem
# %%
# número da sorte com 3 tentativas

numero_sorte = 7


for i in range(3): # range de 3 tentativas
    numero = int(input('Entre com um número de 1 a 15:'))
    if numero == numero_sorte:
        print('Você acertou!')
        break
    else: 
        print('Você errou. Tente novamente!')
   

# %%


try:
    numero = int(input('Entre com um número de 1 a 15:'))

except: ValueError as err:
    print('Escreva um número/algarismo!')
    
    