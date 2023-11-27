import base64
import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from config.connection_database import get_connection
from math_model.linear_regression import linear_regression


def plot_unitario(marca, modelo, ano_modelo):
    connection = get_connection()
    cursor = connection.cursor()

    query = f"SELECT * FROM carros_fipe c WHERE c.marca = '{marca}' AND c.modelo = '{modelo}' AND c.ano_modelo = '{ano_modelo}'"
    cursor.execute(query)
    dados = cursor.fetchall()

    cursor.close()
    connection.close()

    dataFrame = pd.DataFrame(dados, columns=['modelo', 'mes_referencia', 'preco_medio'])

    X = dataFrame[['mes_referencia']]
    y = dataFrame['preco_medio']

    xreg = np.arange(X)
    coeficiente_angular, coeficiente_linear = linear_regression(y)

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

    return image_base64, pd.DataFrame(dataFrame, columns=['mes_referencia', 'preco_medio'])
