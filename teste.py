import pandas as pd

# Suponha que 'dados' seja uma lista de valores
dados = ['2020', '2021', '2022']

# Criando o DataFrame
df = pd.DataFrame(dados, columns=['ano_modelo'])

# Convertendo o DataFrame para JSON
json_result = df.to_json(orient='records')

print(json_result)
