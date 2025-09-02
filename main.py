import sqlite3
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from db.db import DBManager
from managers.conexionManager import getCursor, initeDB
from models.models import ClienteModel, PedidoModel, ProductoModel
from routes.clientRouter import router as routerClient
from routes.pedidoRouter import router as routerPedidos
from routes.productsRouter import router as routerProducts


@asynccontextmanager
async def startFunc(app: FastAPI):
    # Arranque de database
    initeDB()
    yield


app = FastAPI(lifespan=startFunc)
dbm = DBManager()
app.include_router(routerClient)
app.include_router(routerProducts)
app.include_router(routerPedidos)


""" @app.get("/obtener_clientes")
def getClientes(cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getClientes(cursor)
    return res


@app.get("/obtener_cliente/{id}")
def getClienteForId(id: int, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getClienteForId(id, cursor)
    return res


@app.post("/crear_cliente")
def postCliente(cliente: ClienteModel, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.addClient(cliente, cursor)
    return {"msg": res} """


""" @app.get("/obtener_productos")
def getProductos(cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getProductos(cursor)
    return res


@app.post("/crear_productos")
def postProductos(producto: ProductoModel, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.addProducto(producto, cursor)
    return {"msg": res} """


""" @app.post("/crear_pedido")
def postPedido(pedido: PedidoModel, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.addPedido(pedido, cursor)
    return {"msg": res}


@app.get("/obtener_pedidos")
def getPedidos(cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getPedidos(cursor)
    return res


@app.get("/obtener_pedido/{id}")
def getPedidoForId(id: int, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getPedidoForId(id, cursor)
    return res


@app.get("/obtener_pedido_por_cliente/{nombre}")
def getPedidoForCliente(nombre: str, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getPedidoForCliente(nombre, cursor)
    return res """
