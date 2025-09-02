import sqlite3

from fastapi import APIRouter, Depends

from db.db import DBManager
from managers.conexionManager import getCursor
from models.models import ClienteModel

# Creación de router
router = APIRouter(prefix="/clientes", tags=["Clientes routes"])
dbm = DBManager()


@router.get("/obtener_clientes")
def getClientes(cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getClientes(cursor)
    return res


@router.get("/obtener_cliente/{id}")
def getClienteForId(id: int, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getClienteForId(id, cursor)
    return res


@router.post("/crear_cliente")
def postCliente(cliente: ClienteModel, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.addClient(cliente, cursor)
    return {"msg": res}
