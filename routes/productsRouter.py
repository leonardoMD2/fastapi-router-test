import psycopg
from fastapi import APIRouter, Depends
from managers.conexionManagerSupabase import getCursor
from managers.productosManager import ProductosManager
from models.models import ProductoModel

ProdManager = ProductosManager()
router = APIRouter(prefix="/productos", tags=["Productos router"])


@router.get("/obtener_productos")
def getProductos(producto: ProductoModel, cursor: psycopg.Cursor = Depends(getCursor)):
    res = ProdManager.addProducto(producto, cursor)
    return res


@router.post("/crear_productos")
def postProductos(producto: ProductoModel, cursor: psycopg.Cursor = Depends(getCursor)):
    res = ProdManager.addProducto(producto, cursor)
    return {"msg": res}
