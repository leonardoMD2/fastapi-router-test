import sqlite3

from managers.clientesManager import ClienteManager
from managers.pedidosManager import PedidosManager
from managers.productosManager import ProductosManager
from models.models import ClienteModel, PedidoModel, ProductoModel

clienteManager = ClienteManager()
productoManager = ProductosManager()
pedidosManager = PedidosManager()


class DBManager:

    ### Revisar la integridad de los hilos, sqlite y los endpoints
    def __init__(self):
        pass

    ###### Productos #######

    def addProducto(self, producto: ProductoModel, cursor):
        res = productoManager.addProducto(producto, cursor)
        return res

    def getProductos(self, cursor) -> list:
        res = productoManager.getProductos(cursor)
        return res

    ###### Pedidos #######
    def addPedido(self, pedido: PedidoModel, cursor):
        res = pedidosManager.addPedido(pedido, cursor)
        return res

    def getPedidos(self, cursor) -> list:
        res = pedidosManager.getPedidos(cursor)
        return res

    def getPedidoForId(self, id: int, cursor) -> list:
        res = pedidosManager.getPedidoForId(id, cursor)
        return res

    def getPedidoForCliente(self, nombre: str, cursor) -> list | None:
        res = pedidosManager.getPedidoForCliente(nombre, cursor)
        return res

    ###### Clientes #######
    def addClient(self, cliente: ClienteModel, cursor):
        res = clienteManager.addClient(cliente, cursor)
        return res

    def getClientes(self, cursor) -> list:
        res = clienteManager.getClientes(cursor)
        return res

    def getClienteForId(self, id: int, cursor) -> list:
        res = clienteManager.getClienteForId(id, cursor)
        return res
