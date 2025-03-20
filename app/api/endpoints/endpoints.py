from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List 
from fastapi.params import Depends

from app.api.DTO.dtos import ProveedorDTO,ProveedorDTOEnvio,LogisticaDTOEnvio,LogisticaDTO
from app.api.models import Logistica
from app.api.models.Proveedor import Proveedor

from app.database.connection import SessionLocal, engine


rutas=APIRouter()

#Rutina para conectarnos a la BD
def conectarConBd():
    try:
        baseDatos=SessionLocal()
        yield baseDatos

    except Exception as error:
        baseDatos.rollback()
        raise error

    finally:
        baseDatos.close()


#Rutina para construir servicios web
@rutas.post("/proveedor",response_model=ProveedorDTOEnvio,summary="Servicio para guardar un prooveder en la BD")
def guardarProveedor(datosProveedor:ProveedorDTO,database:Session=Depends(conectarConBd)):
    try:
        proveedorAGuardar=Proveedor(
            nombres=datosProveedor.nombres,
            documento=datosProveedor.documento,
            direccion=datosProveedor.direccion,
            ciudad=datosProveedor.ciudad,
            representante=datosProveedor.representante,
            telefonoContacto=datosProveedor.telefonoContacto,
            correo=datosProveedor.correo,
            fechaEnvio=datosProveedor.fechaEnvio,
            costoEnvio=datosProveedor.costoEnvio,
            descripcion=datosProveedor.descripcion
        )
        database.add(proveedorAGuardar) 
        database.commit()
        database.refresh(proveedorAGuardar)
        return proveedorAGuardar

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"tenemos un error {error}")
    



    #Rutina para consultar los proveedores
@rutas.get("/proveedor", response_model=List[ProveedorDTOEnvio], summary="Servicio para consultar todos los")   
def buscarProveedores(database:Session=Depends(conectarConBd)):
    try:
        proveedores=database.query(Proveedor).all()
        return proveedores
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=404, detail=f"tenemos un error {error}")
    


@rutas.post("/logistica",response_model=LogisticaDTOEnvio,summary="Servicio para guardar la logistica en la BD")
def guardarLogistica(datosLogistica:LogisticaDTO,database:Session=Depends(conectarConBd)):
    try:
        guardarLogistica=Logistica(
            nombreProveedor=datosLogistica.nombreProveedor,
            nombreEncargado=datosLogistica.nombreEncargado,
            correoEncargado=datosLogistica.correoEncargado,
            numeroContactoEncargado=datosLogistica.numeroContactoEncargado,
            productos=datosLogistica.productos,
            cantidad=datosLogistica.cantidad,
            numeroRecibo=datosLogistica.numeroRecibo,
            detalles=datosLogistica.detalles,
            transportadora=datosLogistica.transportadora,
            numeroGuia=datosLogistica.numeroGuia,
            fechaRecepcion=datosLogistica.fechaRecepcion
        )
        database.add(guardarLogistica) 
        database.commit()
        database.refresh(guardarLogistica)
        return guardarLogistica

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"tenemos un error {error}")
    


@rutas.get("/logistica", response_model=List[LogisticaDTOEnvio], summary="Servicio para consultar todos los")   
def buscarLogistica(database:Session=Depends(conectarConBd)):
    try:
        proveedores=database.query(Proveedor).all()
        return proveedores
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=404, detail=f"tenemos un error {error}")