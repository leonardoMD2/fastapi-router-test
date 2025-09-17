import sqlite3

from fastapi import APIRouter, Depends
from managers.clientesManager import ClienteManager
from managers.conexionManager import getCursor
from models.models import ClienteModel

# Creación de router
router = APIRouter(prefix="/clientes", tags=["Clientes routes"])
clientManager = ClienteManager()


@router.get("/obtener_clientes")
def getClientes(cursor: sqlite3.Cursor = Depends(getCursor)):
    res = clientManager.getClientes(cursor)
    return res


@router.get("/obtener_cliente/{id}")
def getClienteForId(id: int, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = clientManager.getClienteForId(id, cursor)
    return res


@router.post("/crear_cliente")
def postCliente(cliente: ClienteModel, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = clientManager.addClient(cliente, cursor)
    return {"msg": res}


@router.put("/modificar_cliente/{id}")
def putCliente(
    id: int, clienteUpdated: ClienteModel, cursor: sqlite3.Cursor = Depends(getCursor)
):
    res = clientManager.modifyClient(id, clienteUpdated, cursor)
    return {"msg", res}


@router.delete("/eliminar_cliente/{id}")
def deleteCliente(id: int, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = clientManager.deleteClient(id, cursor)
    return {"msg": res}
