print('Hello World!')

# %%
print('Eudes')
print('Cunha')
# %%

# %%
name = "Eudes"
print(name)

# %%
print('Seja bem-vindo,', name)

# %%
# pedindo um input para o usuário
nome = input('Entre com seu nome: \n Esperando...')
print(nome)

# %%
# um programa que pergunta seu nome e dá bom-dia
program_nome = input('Olá, bom-dia! Qual o seu nome? \n')
print('Seja bem-vindo,', program_nome)

# %%
print('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eget justo orci. Donec mollis tincidunt massa quis lobortis. Nullam placerat urna vitae scelerisque placerat. Nam condimentum quis felis sed convallis. Quisque efficitur odio eu orci fermentum, a blandit diam varius. Praesent nec elementum quam. Nam finibus mollis vestibulum. Donec volutpat nulla eu nisl elementum, at gravida lorem faucibus. Nullam sit amet maximus urna, malesuada sagittis magna. Aliquam ut ante eget leo facilisis efficitur. Integer convallis vel nisl nec blandit. Nulla ut leo magna. Praesent sit amet ullamcorper ex. Cras sagittis et massa vel euismod. Phasellus non dui posuere, varius ante finibus, dapibus felis.')
input('Para saber a continuação da história, digite enter')

print('Maecenas tristique, purus id scelerisque sollicitudin, dui nulla sollicitudin est, non ullamcorper augue sem eu nibh. Integer eu mauris aliquam arcu tristique fringilla ac quis tellus. Proin iaculis dui eros, vel placerat nibh porta quis. Vestibulum vulputate magna sit amet risus varius tempus. Ut ut imperdiet lectus. Phasellus facilisis ultrices ex quis iaculis. Quisque feugiat rhoncus massa eget semper.')
input('Para saber a continuação da história, digite enter')

print('Vestibulum tristique pharetra enim, et fermentum metus pretium sed. Pellentesque imperdiet mauris imperdiet augue pulvinar, ut dapibus mauris lacinia. In id dictum risus. Nunc malesuada sit amet purus ut molestie. Duis justo turpis, maximus eu velit id, sagittis iaculis tellus. Aenean accumsan, est vel rhoncus iaculis, ex diam accumsan eros, quis fermentum erat mi at libero. Suspendisse potenti.')

# %%
# condicionais

idade = int(input('Digite a sua idade:'))

if idade >= 18:
    print('Você é maior de idade.')
        
# %%

age = int(input('Digite a sua idade:'))

if age >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')    
        
# %%

how_old = int(input('Digite a sua idade:'))

if how_old < 18:
    print('Você é menor de idade.')

elif how_old > 65:
    print('Você é idoso(a).')
    
else:
    print('Você é maior de idade.') 

    
# %%
your_age = int(input('Digite a sua idade:'))

if your_age < 18:
    print('Você tem', your_age,'anos. Você é menor de idade.')

elif your_age == 18:
    print('Você tem', your_age,'anos. Você é maior de idade. Já se alistou no serviço militar?')
    
else:
    print('Você tem', your_age,'anos. Você é maior de idade!')
# %%

# estrutura de repetição

count = 1
while count <= 10:
    print('Contando')
    count += 1 # count = count + 1
    
# %%

qtd = int(input('Quantas repetições você deseja?'))
count = 1

while count <= qtd:
    print(count)
    count += 2 # count = count + 1
    
# %%

while True:
    
    user_pass = input('Digite a sua senha aqui:')
    
    if user_pass == '1234':
        break
        
    elif user_pass == 'senha':
        print('Espertinho. Ainda não acertou. Tente outra vez')
        
    else:
        print('Tente outra vez')
        continue
        
print('Senha correta!')


# %%

# for

for i in "Eudes Cunha":
    print(i)
# %%
for i in "10":
    print(i)
# %%
for i in "Eudes Cunha":
    
    if i == 'C':
        continue
    elif i == ' ':
        break
    
    print(i)
# %%
for i in "Eudes Cunha":
    
    if i == 'C':
        continue
    elif i == ' ':
        continue
    
    print(i)
# %%
range(10)

# %%
range(0, 10) # (start, stop); quantidade = stop - start
# %%
range(2, 10) # (start, stop); quantidade = stop - start
# %%
seq = range(0, 10)
for i in seq:
    print(i)
# %%
seq = range(3, 10)
for i in seq:
    print(i)
# %%
seq = int(input("quantos 'olás' você quer?"))
for i in range(seq):
    print('olá')
# %%
seq = int(input("quantos 'olás' você quer?"))
for i in range(seq):
    print(i)
    
# %%
for i in range(1,16):
    if i % 2 == 0: # aqui solicitamos que a sobra seja igual a zero; isto vai retornar os números pares
        print(i)


# %%
for i in range(1,16):
    if i % 2 == 1: # aqui solicitamos que a sobra seja igual a 1; isto vai retornar os números ímpares
        print(i)


# %%
bebida = 'refri, suco, água'

item = str(input('Escreva qual bebida você deseja.'))

if item in bebida:
    print('Ok. Pode se dirigir ao caixa.')

else:
    print('Infelizmente não dispomos desta bebida')
    

# %%
# programa para contar a quantidade de letras numa frase
word = input('Digite a palavra/frase aqui') # por padrão o input retorna uma string
quantity = 0 # para fazer contas eu preciso passar o valor inicial

for i in word:
    if i == 'a':
        quantity += 1
print('A palavra/frase', word, 'contém', quantity, 'vezes a letra a.')

# %%
# outra forma de contar letras ou palavras utilizando o método .count
palavra = "carro"
palavra.count('r')

# %%
# método .lower
# O método lower() em Python transforma todas as letras de uma string em minúsculas

plvr = "Carro, BIKE, TriCiclo".lower()
print(plvr)
plvr.count('c') # aqui tem que ser uma letra minúscula, já que foi utilizado o método .lower

# %%
# método .upper
# O método upper() em Python transforma todas as letras de uma string em minúsculas

plvr = "Carro, BIKE, TriCiclo".upper()
print(plvr)
plvr.count('C') # aqui tem que ser uma letra minúscula, já que foi utilizado o método .lower


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

except ValueError as err:
    print('Escreva um número/algarismo!')
    
# %%


numero_sorte = 7


for i in range(3): # range de 3 tentativas
    try:
        numero = int(input('Entre com um número de 1 a 15:'))

    except ValueError:
        print('Escreva um número/algarismo!')
        continue

    if numero == numero_sorte:
        print('Você acertou!')
        break
    
    else: 
        print('Você errou. Tente novamente!')
# %%
numero_sorte = 7


for i in range(3): # range de 3 tentativas
    
    while True:
        try:
            numero = int(input('Entre com um número de 1 a 15:'))
            break
        
        except ValueError:
            print('Escreva um número/algarismo!')
            numero_sorte = 7


for i in range(3): # range de 3 tentativas
    try:
        numero = int(input('Entre com um número de 1 a 15:'))

    except ValueError:
        print('Escreva um número/algarismo!')
        # continue

    if numero == numero_sorte:
        print('Você acertou!')
        break
    
    else: 
        print('Você errou. Tente novamente!')

    if numero == numero_sorte:
        print('Você acertou!')
        break
    
    else: 
        print('Você errou. Tente novamente!')
# %%

# ler arquivos e sobrescrever

arquivo = open('arquivo.txt', 'w') # o w significa escrever (sobrescrevendo)
arquivo.write('Notas de python')
arquivo.close()
# %%
# para adicionar linhas, use o 'a'
archive = open('archive.txt', 'a')
archive.write('Python notes')
archive.close()
# %%
# para ler o arquivo , use o 'r' de read
archive = open('archive.txt', 'r')
content = archive.read()
archive.close()

print(content)
# %%
# para ler linhas 
archive = open('archive.txt', 'r')
line = archive.readlines()
archive.close()

print(line)

# %%
# é preferível usar o with para abrir arquivos, conexão com banco de dados ou qualquer coisa para garantir que no final da execução o arquivo seja fechado

with open('arquivo.txt', 'r') as file:
    info = file.read()
    
print(info)
# %%
