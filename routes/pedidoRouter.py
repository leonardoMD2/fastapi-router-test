import sqlite3

from fastapi import APIRouter, Depends

from db.db import DBManager
from managers.conexionManager import getCursor
from models.models import PedidoModel

dbm = DBManager()
router = APIRouter(prefix="/pedidos", tags=["Pedidos router"])


@router.post("/crear_pedido")
def postPedido(pedido: PedidoModel, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.addPedido(pedido, cursor)
    return {"msg": res}


@router.get("/obtener_pedidos")
def getPedidos(cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getPedidos(cursor)
    return res


@router.get("/obtener_pedido/{id}")
def getPedidoForId(id: int, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getPedidoForId(id, cursor)
    return res


@router.get("/obtener_pedido_por_cliente/{nombre}")
def getPedidoForCliente(nombre: str, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getPedidoForCliente(nombre, cursor)
    return res
