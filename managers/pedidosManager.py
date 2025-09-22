import psycopg
from models.models import PedidoModel


class PedidosManager:
    def getPedidos(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT producto.nombre, producto.precio, cliente.nombre FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente INNER JOIN producto ON pedido.id_producto = producto.id_producto"
        ).fetchall()
        return [
            {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
        ]

    def getPedidoForId(self, id: int, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT producto.nombre, producto.precio, cliente.nombre FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente INNER JOIN producto ON pedido.id_producto=producto.id_producto WHERE pedido.id_cliente = %s",
            (id,),
        ).fetchall()
        return [
            {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
        ]

    def getPedidoForCliente(self, nombre: str, cursor: psycopg.Cursor) -> list | None:
        idCliente = cursor.execute(
            "SELECT id_cliente FROM cliente WHERE nombre = (%s)", (nombre,)
        ).fetchone()
        if idCliente:
            res = cursor.execute(
                "SELECT producto.nombre, producto.precio, cliente.nombre FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente INNER JOIN producto ON pedido.id_producto = producto.id_producto WHERE pedido.id_cliente = %s",
                (idCliente,),
            ).fetchall()
            return [
                {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
            ]

    def addPedido(self, pedido: PedidoModel, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO pedido (id_producto, id_cliente) VALUES (%s,%s)",
            (pedido.id_producto, pedido.id_cliente),
        )
        return "pedido agregado"
