from pydantic import BaseModel


class PedidoModel(BaseModel):
    id_producto: int
    id_cliente: int


class ClienteModel(BaseModel):
    nombre: str


class PedidoJoinModel(BaseModel):
    nombre: str
    precio: int
    clienteNombre: str

class ProductoModel(BaseModel):
    nombre: str
    precio: int