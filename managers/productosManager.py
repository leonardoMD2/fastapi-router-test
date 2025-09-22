import psycopg
from models.models import ProductoModel


class ProductosManager:
    def addProducto(self, producto: ProductoModel, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO producto (nombre, precio) VALUES (%s,%s)",
            (producto.nombre, producto.precio),
        )
        return "Producto agregado"

    def getProductos(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT * FROM producto").fetchall()
        return [
            {"id_producto": row[0], "nombre": row[1], "precio": row[2]} for row in res
        ]
