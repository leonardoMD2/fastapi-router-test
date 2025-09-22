import os
from typing import Generator

import psycopg
from dotenv import load_dotenv

load_dotenv()
passwordDB = os.getenv("SUPABASE_PASSWORD")

url = f"postgresql://postgres.qkrdpaiuniqpzgtzsybv:{passwordDB}@aws-1-us-east-2.pooler.supabase.com:5432/postgres"


def getCursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")

    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()


""" def initeDB() -> None:
        connection = sqlite3.connect("comercio.db", check_same_thread=False)
        try:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS cliente (id_cliente INTEGER PRIMARY KEY, nombre TEXT)"
            )
            connection.execute(
                "CREATE TABLE IF NOT EXISTS producto (id_producto INTEGER PRIMARY KEY, nombre TEXT, precio INTEGER, cantidad INTEGER)"
            )
            connection.execute(
                "CREATE TABLE IF NOT EXISTS pedido (id_pedido INTEGER PRIMARY KEY, id_producto INTEGER, id_cliente INTEGER, FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente), FOREIGN KEY (id_producto) REFERENCES producto(id_producto) )"
            )
            connection.commit()
        finally:
            connection.close()
            print("DB Inicializada") """
