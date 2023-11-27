import numpy as np


def variacao_media(dataFrame):
    print(dataFrame['preco_medio'])
    preco_inicial_str = dataFrame['preco_medio'][0]  # Supondo que seja 'R$ 3600,45'
    preco_final_str = dataFrame['preco_medio'][len(dataFrame['preco_medio'])-1]  # Supondo que seja 'R$ 3600,45'

    preco_final = float(preco_final_str.replace('R$', '').replace(',', '.').strip())
    preco_inicial = float(preco_inicial_str.replace('R$', '').replace(',', '.').strip())

    intervalo = np.arange(1, len(dataFrame['preco_medio'])+1)
    return preco_inicial + ((preco_final - preco_inicial) / (intervalo[0] - intervalo[len(intervalo-1)]))*len(intervalo)
