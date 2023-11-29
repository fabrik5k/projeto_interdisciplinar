import psycopg2


def get_connection():
    connect = psycopg2.connect(
        host='localhost',
        port=5432,
        database='CPC',
        user='postgres',
        password='Tada-25112003'
    )

    return connect
