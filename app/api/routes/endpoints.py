from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends 
from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta,gastoDTORespuesta,gastoDTOPeticion,ingresoDTOPeticion,ingresoDTORespuesta,facturaDTOPeticion,facturaDTORespuesta,categoriaDTOPeticion,categoriaDTORespuesta,MDPDTOPeticion,MDPDTORespuesta
from app.api.models.tablassql import Usuario,Gasto,Factura,Ingreso,Categoria,MDP
from app.database.configuration import sessionLocal, engine

rutas=APIRouter()

def conectarConBd():
    baseDatos=sessionLocal()  #crear el camino de conexion con la bd
    try:
        yield baseDatos
    except Exception as error:
        baseDatos.rollback()  # parar todas las peticiones
        raise error #cuenta que paso (el error)

    finally:
        baseDatos.close()  #cerrar peticion  

    
#   construyendo nuestros servicios

#Cada servicio (operacion o transaccion en BD) debe programarse como una funcion
@rutas.post("/usuario", response_model=UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos") #documentando un servicio 
def guardarUsuario(datosUsuario:UsuarioDTOPeticion,database:Session=Depends(conectarConBd)): # con esto podemos comunicarme con la base de datos
    # debemos filtrar los datos, para que coincidan con la base de datos
    try:
        usuario=Usuario(
            nombres=datosUsuario.nombres,
            edad = datosUsuario.edad,
            telefono=datosUsuario.telefono,
            correo=datosUsuario.correo,
            contraseña=datosUsuario.contraseña,
            fechaRegistro = datosUsuario.fechaRegistro,
            ciudad=datosUsuario.ciudad

        )
        #ordenando a la base de datos
        database.add(usuario) #agregemelo
        database.commit()#tomele foto 
        database.refresh(usuario) #refresquelo
        return usuario  #devuelvamelo

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
@rutas.get("/usuario",response_model=list[UsuarioDTORespuesta],summary="Buscar todos los usuarios en BD")
def buscarUsuarios(database:Session=Depends(conectarConBd)):
    try:
        usuarios = database.query(Usuario).all()
        return usuarios

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")

@rutas.post("/gasto", response_model=gastoDTORespuesta, summary="Registrar un gasto en la base de datos") #documentando un servicio 
def guardarGasto(datosGasto:gastoDTOPeticion,database:Session=Depends(conectarConBd)): # con esto podemos comunicarme con la base de datos
    # debemos filtrar los datos, para que coincidan con la base de datos
    try:
        gasto=Gasto(
            monto=datosGasto.monto,
            fecha=datosGasto.fecha,
            descripcion= datosGasto.descripcion,
            nombre=datosGasto.nombre
        )
        #ordenando a la base de datos
        database.add(gasto) #agregemelo
        database.commit()#tomele foto 
        database.refresh(gasto) #refresquelo
        return gasto  #devuelvamelo

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
@rutas.get("/gasto",response_model=list[gastoDTORespuesta],summary="Buscar todos los gastos en BD")
def buscarGasto(database:Session=Depends(conectarConBd)):
    try:
        gastos = database.query(Gasto).all()
        return gastos

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
#Categoria
@rutas.post("/categoria", response_model=categoriaDTORespuesta, summary="Registrar una categoria en la base de datos") #documentando un servicio 
def guardarCategoria(datosCategoria:categoriaDTOPeticion,database:Session=Depends(conectarConBd)): # con esto podemos comunicarme con la base de datos
    # debemos filtrar los datos, para que coincidan con la base de datos
    try:
        categoria=Categoria(
            nombreCategoria=datosCategoria.nombreCategoria,
            fotoicono=datosCategoria.fotoicono,
            descripcion= datosCategoria.descripcion
        )
        #ordenando a la base de datos
        database.add(categoria) #agregemelo
        database.commit()#tomele foto 
        database.refresh(categoria) #refresquelo
        return categoria  #devuelvamelo

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
@rutas.get("/categoria",response_model=list[categoriaDTORespuesta],summary="Buscar todos las categorias en BD")
def buscarCategoria(database:Session=Depends(conectarConBd)):
    try:
        categoria = database.query(Categoria).all()
        return categoria

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
#Ingreso
@rutas.post("/ingreso", response_model=ingresoDTORespuesta, summary="Registrar un ingreso en la base de datos") #documentando un servicio 
def guardarIngreso(datosIngreso:ingresoDTOPeticion,database:Session=Depends(conectarConBd)): # con esto podemos comunicarme con la base de datos
    # debemos filtrar los datos, para que coincidan con la base de datos
    try:
        ingreso=Ingreso(
            monto=datosIngreso.monto,
            fecha=datosIngreso.fecha,
            descripcion= datosIngreso.descripcion,
            nombre=datosIngreso.nombre
        )
        #ordenando a la base de datos
        database.add(ingreso) #agregemelo
        database.commit()#tomele foto 
        database.refresh(ingreso) #refresquelo
        return ingreso  #devuelvamelo

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
@rutas.get("/ingreso",response_model=list[ingresoDTORespuesta],summary="Buscar todos los ingresos en BD")
def buscarIngreso(database:Session=Depends(conectarConBd)):
    try:
        ingreso = database.query(Ingreso).all()
        return ingreso

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
#Metodo de pago
@rutas.post("/metodoDePago", response_model=MDPDTORespuesta, summary="Registrar un metodo de pago en la base de datos") #documentando un servicio 
def guardarMetodoDePago(datosMetodo:MDPDTOPeticion,database:Session=Depends(conectarConBd)): # con esto podemos comunicarme con la base de datos
    # debemos filtrar los datos, para que coincidan con la base de datos
    try:
        metodoDePago=MDP(
            nombreMetodo=datosMetodo.nombreMetodo,
            descripcion= datosMetodo.descripcion,
        )
        #ordenando a la base de datos
        database.add(metodoDePago) #agregemelo
        database.commit()#tomele foto 
        database.refresh(metodoDePago) #refresquelo
        return metodoDePago  #devuelvamelo

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
@rutas.get("/metodoDePago",response_model=list[MDPDTORespuesta],summary="Buscar todos los ingresos en BD")
def buscarMetodoDePago(database:Session=Depends(conectarConBd)):
    try:
        metodoDePago = database.query(MDP).all()
        return metodoDePago

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
#Factura
@rutas.post("/factura", response_model=facturaDTORespuesta, summary="Registrar una factura en la base de datos") #documentando un servicio 
def guardarFactura(datosFatura:facturaDTOPeticion,database:Session=Depends(conectarConBd)): # con esto podemos comunicarme con la base de datos
    # debemos filtrar los datos, para que coincidan con la base de datos
    try:
        factura=Factura(
            usuario=datosFatura.usuario,
            fecha=datosFatura.fecha,
            metodo= datosFatura.metodo,
            gasto=datosFatura.gasto
        )
        #ordenando a la base de datos
        database.add(factura) #agregemelo
        database.commit()#tomele foto 
        database.refresh(factura) #refresquelo
        return factura  #devuelvamelo

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
@rutas.get("/factura",response_model=list[facturaDTORespuesta],summary="Buscar todos las Facturas en BD")
def buscarFacturas(database:Session=Depends(conectarConBd)):
    try:
        facturas = database.query(Factura).all()
        return facturas

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
