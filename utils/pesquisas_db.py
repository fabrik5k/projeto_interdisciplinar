import pandas as pd

from config.connection_database import get_connection


def retornar_anos_modelo(modelo_carro):
    connection = get_connection()
    cursor = connection.cursor()

    query = f"SELECT ano_modelo FROM carros_fipe WHERE modelo = '{modelo_carro}' GROUP BY ano_modelo"
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

    query = f"SELECT modelo FROM carros_fipe GROUP BY modelo"
    cursor.execute(query)
    dados = cursor.fetchall()

    df = pd.DataFrame(dados, columns=['modelo'])

    cursor.close()
    connection.close()

    json_result = df.to_json(orient='index')

    return json_result
