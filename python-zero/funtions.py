#%%

# def é a palabra usada para definir uma função

def function(x): # o nome da função é function
    variavel = x + 10 # essa variável só existe dentro da funcao
    return variavel

#%%
# chamando a função

function(7)

# %%

y = function(18)
print(y)

# %%

# também pode definir uma função vazia

def func():
    print('Função vazia')
    
func()
# %%

# função para somar

def soma(a, b): # dentro do parêntesis estão os argumentos da função. Como foram passados dois elementos, eles são obrigatórios
    return a + b

soma(10, 12)
# %%

# tornando um dos argumentos opcionais ao chamar a função

def soma(a, b=0): # quando coloco um valor default para o argumento, retira-se a obrigatoriedade de passar os dois argumentos. Os valores obrigatórios devem vir antes dos opcionais!
    return a + b

soma(10)

# %%
soma(5,11)


# %%
def soma(a=0, b=0): # os dois podem ser opcionais
    return a + b # o devolve pra fora da função

soma()
# %%
soma(a=2, b=7)
# %%
soma(b=30)
# %%
# passando valores indefinidos para a função com *args

def sum(*args):
    total = 0
    
    for i in args:
        total += i
        
    return total


sum(1, 5, 7, 11,12)
# %%
sum()

# %%
sum(5,78,9)
# %%

def operacao(op, *num): #não necessariamente precisa estar escrito args. Basta ter o * antes do elemento. O primeiro elemento será obrigatório e único. O segundo em diante é opcional e posso adicionar quantos achar necessários. O num é uma lista.
    total = 0
    
    if op == 'soma':
        
        for i in num:
            total += i
    elif op == 'multi':
        total = 1
        for i in num:
            total *= i
               
    return total

operacao('multi',2,20)
# %%
operacao('soma', 5,1,2,45,2)
# %%
operacao('soma')


# %%

# inversão de variáveis

a = 10
b = 20
print(a,b)


a, b = b, a

print(a, b)
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
