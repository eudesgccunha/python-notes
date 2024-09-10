#%%
import requests
import pandas as pd

url = 'hhtps://endereço.com'
resposta = requests.get(url)

#%%
resposta.status_code

#%%
dados = resposta.json()

#%%
for i in dados:
    print(i['lista escolhida'])
    
#%%
df = pd.DataFram(dados) #transformar em um dataframe do pandas
df.to_csv('nome_do_arquivo', sep=',') #exportar o dado extraído com uma api