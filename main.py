from contextlib import asynccontextmanager

from fastapi import FastAPI
from managers.conexionManager import initeDB
from routes.clientRouter import router as routerClient
from routes.pedidoRouter import router as routerPedidos
from routes.productsRouter import router as routerProducts

""" @asynccontextmanager
async def startFunc(app: FastAPI):
    # Arranque de database
    initeDB()
    yield """


""" app = FastAPI(lifespan=startFunc) """
app = FastAPI()
app.include_router(routerClient)
app.include_router(routerProducts)
app.include_router(routerPedidos)
