import sqlite3

from models.models import ProductoModel


class ProductosManager:
    def addProducto(self, producto: ProductoModel, cursor: sqlite3.Cursor):
        cursor.execute(
            "INSERT INTO producto (nombre, precio) VALUES (?,?)",
            (producto.nombre, producto.precio),
        )
        return "Producto agregado"

    def getProductos(self, cursor: sqlite3.Cursor) -> list:
        res = cursor.execute("SELECT * FROM producto").fetchall()
        return [
            {"id_producto": row[0], "nombre": row[1], "precio": row[2]} for row in res
        ]
