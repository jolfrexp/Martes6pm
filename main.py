from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.tablassql import Base
from app.api.routes.endpoints import rutas 
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
import os
import uvicorn
#crear las tablas de sql desde python
Base.metadata.create_all(bind = engine)
#Variable para administrar la aplicacion
app = FastAPI()
#Activar el API
# Configurar el protocolo CORS
# Configura los orígenes permitidos
origins = [
    "*", # Cambia esto según necesites
    # Agrega más orígenes si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = ["*"],
#     allow_credentials=True,
#     allow_methods = ["*"],
#     allow_headers=["*"]
# )

@app.get("/")
def main():
    return RedirectResponse(url="/docs")
app.include_router(rutas)
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0",port=port)
    