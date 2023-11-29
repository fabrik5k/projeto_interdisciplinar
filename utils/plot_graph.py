import base64
import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from config.connection_database import get_connection
from math_model.linear_regression import linear_regression
from math_model.tendencia_variacao import tendencia
from utils.pesquisas_db import retornar_para_plot


def plot_unitario(marca, modelo, ano_modelo):
    dados = retornar_para_plot(marca, modelo, ano_modelo)

    dataFrame = pd.DataFrame(dados, columns=['modelo', 'mes_referencia', 'preco_medio'])

    X = dataFrame['mes_referencia']
    y = dataFrame['preco_medio']

    xreg = np.arange(len(X))

    coeficiente_angular, coeficiente_linear = linear_regression(y)
    print(coeficiente_angular, coeficiente_linear)

    plt.figure(figsize=(10, 6))
    plt.scatter(xreg, y, color='blue', label='Dados Reais')
    plt.plot(xreg, coeficiente_angular * xreg + coeficiente_linear, color='red', label='Linha de Regressão')
    plt.xlabel('Meses do ano')
    plt.ylabel('Preço Total')
    plt.title('Regressão Linear de Preços medios por mês')
    plt.legend()
    plt.gcf().autofmt_xdate()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    tendencia_porcentagem = tendencia(coeficiente_linear, coeficiente_angular, xreg)

    return image_base64, dataFrame, tendencia_porcentagem


def plot_comparatorio(marca, modelo, ano_modelo):
    dados = retornar_para_plot(marca, modelo[0], ano_modelo[0])
    dados2 = retornar_para_plot(marca, modelo[1], ano_modelo[1])

    dataFrame = pd.DataFrame(dados, columns=['modelo', 'mes_referencia', 'preco_medio'])
    dataFrame2 = pd.DataFrame(dados2, columns=['modelo', 'mes_referencia', 'preco_medio'])

    X = dataFrame['mes_referencia']
    y = dataFrame['preco_medio']

    X2 = dataFrame2['mes_referencia']
    y2 = dataFrame2['preco_medio']

    xreg = np.arange(len(X))

    coeficiente_angular, coeficiente_linear = linear_regression(y)
    coeficiente_angular_2, coeficiente_linear_2 = linear_regression(y2)

    print(coeficiente_angular, coeficiente_linear)

    plt.figure(figsize=(10, 6))
    plt.plot(xreg, y, color='red', label=f'Dados {modelo[0]}')
    plt.plot(xreg, y2, color='blue', label=f'Dados {modelo[1]}')

    plt.xlabel('Meses do ano')
    plt.ylabel('Preço Total')
    plt.title('Preços dos carros')
    plt.legend()
    plt.gcf().autofmt_xdate()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    tendencia_porcentagem = [tendencia(coeficiente_linear, coeficiente_angular, xreg),
                             tendencia(coeficiente_linear_2, coeficiente_angular_2, xreg)]

    return image_base64, dataFrame, dataFrame2, tendencia_porcentagem
