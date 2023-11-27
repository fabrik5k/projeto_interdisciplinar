import psycopg2


def get_connection():
    connect = psycopg2.connect(
        host='localhost',
        port=5432,
        database='interdisciplinar',
        user='postgres',
        password='1234'
    )

    return connect
