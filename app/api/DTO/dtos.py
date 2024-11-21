from pydantic import BaseModel
from datetime import date 

#los DTO son clases que establecen
#el modelo de trasnferencia de datos

class UsuarioDTOPeticion(BaseModel):
    nombre : str
    edad : int
    telefono: str
    correo : str
    contrasena : str
    fechaRegistro : date
    ciudad : str
    class Config:   # trae la informacion de la BD
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id : int
    nombre : str
    correo : str
    contrasena: str
    fechaRegistro: date
    class Config:   
        orm_mode=True


# gastoDTOPeticion
class gastoDTOPeticion(BaseModel):
    monto : int
    descripcion : str
    categoria_id: int
    metodo_id:int
    factura_id:int
    class Config:
        orm_mode=True
class gastoDTORespuesta(BaseModel):
    id : int
    monto : int
    descripcion : str
    categoria_id:int
    metodo_id:int
    factura_id : int
    class Config:
        orm_mode=True

# CategoriaDTOPeticion
class categoriaDTOPeticion(BaseModel):
    nombreCategoria : str
    descripcion : str
    fotoicono : str
    class Config:
        orm_mode=True

class categoriaDTORespuesta(BaseModel):
    id : int
    nombreCategoria : str
    descripcion : str
    fotoicono : str
    class Config:
        orm_mode=True
# IngresoDTOPeticion

class ingresoDTOPeticion(BaseModel):
    descripcion : str
    monto : int
    metodo_id:int
    categoria_id:int
    factura_id : int
    class Config:
        orm_mode=True
class ingresoDTORespuesta(BaseModel):
    id : int
    monto : int
    descripcion : str
    categoria_id:int
    metodo_id:int
    factura_id : int
    class Config:
        orm_mode=True
#Metodo de pago
class MDPDTOPeticion(BaseModel):
    nombreMetodo: str
    descripcion: str
    class Config:
        orm_mode=True
class MDPDTORespuesta(BaseModel):
    id: int
    nombreMetodo: str
    descripcion: str
    class Config:
        orm_mode=True
# FacturaDTOPeticion
class facturaDTORespuesta(BaseModel):
    id: int
    fecha : date
    user_id : int
    total : float
    class Config:
        orm_mode=True
class facturaDTOPeticion(BaseModel):
    fecha : date
    usuario_id : int
    total  : float
    class Config:           
        orm_mode=True
class loginDTOPeticion(BaseModel):
    user: str
    password :str
    