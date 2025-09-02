import sqlite3

from models.models import ClienteModel


class ClienteManager:
    def addClient(self, cliente: ClienteModel, cursor: sqlite3.Cursor):
        cursor.execute(
            "INSERT INTO cliente (nombre) VALUES (?)",
            (cliente.nombre,),
        )
        return f"cliente creado"

    def getClientes(self, cursor: sqlite3.Cursor) -> list:
        res = cursor.execute("SELECT id_cliente,nombre FROM cliente").fetchall()
        return [{"id": row["id_cliente"], "nombre": row["nombre"]} for row in res]

    def getClienteForId(self, id: int, cursor: sqlite3.Cursor) -> list:
        res = cursor.execute(
            "SELECT id_cliente,nombre FROM cliente WHERE id_cliente = ?", (id,)
        ).fetchall()
        return [{"id": row["id_cliente"], "nombre": row["nombre"]} for row in res]
