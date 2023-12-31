import pandas as pd

from config.connection_database import get_connection


def retornar_anos_modelo(modelo_carro):
    connection = get_connection()
    cursor = connection.cursor()

    query = (f"SELECT ano_modelo "
             f"FROM carros_fipe "
             f"WHERE modelo = '{modelo_carro}' GROUP BY ano_modelo")
    cursor.execute(query)
    dados = cursor.fetchall()

    df = pd.DataFrame(dados, columns=['ano_modelo'])

    cursor.close()
    connection.close()

    json_result = df.to_json(orient='index')

    return json_result


def retornar_modelos():
    connection = get_connection()
    cursor = connection.cursor()

    query = (f"SELECT modelo "
             f"FROM carros_fipe "
             f"GROUP BY modelo")
    cursor.execute(query)
    dados = cursor.fetchall()

    df = pd.DataFrame(dados, columns=['modelo'])

    cursor.close()
    connection.close()

    json_result = df.to_json(orient='index')

    return json_result


def retornar_para_plot(marca, modelo, ano_modelo):
    connection = get_connection()
    cursor = connection.cursor()

    query = (f"SELECT c.modelo, c.mes_referencia, c.preco_medio "
             f"FROM carros_fipe c "
             f"WHERE c.marca = '{marca}' AND c.modelo = '{modelo}' AND c.ano_modelo = '{ano_modelo}'")
    cursor.execute(query)
    dados = cursor.fetchall()

    cursor.close()
    connection.close()
    return dados
