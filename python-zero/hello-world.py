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