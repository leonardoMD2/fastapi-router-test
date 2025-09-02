import sqlite3

from fastapi import APIRouter, Depends

from db.db import DBManager
from managers.conexionManager import getCursor
from models.models import ProductoModel

dbm = DBManager()
router = APIRouter(prefix="/productos", tags=["Productos router"])


@router.get("/obtener_productos")
def getProductos(cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.getProductos(cursor)
    return res


@router.post("/crear_productos")
def postProductos(producto: ProductoModel, cursor: sqlite3.Cursor = Depends(getCursor)):
    res = dbm.addProducto(producto, cursor)
    return {"msg": res}
