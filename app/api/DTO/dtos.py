from pydantic import BaseModel, Field
from datetime import date

#Los DTO son objetos d etransferencia de datos
class ProveedorDTO(BaseModel): #EL DTO DE RECEPCION
    nombres:str
    documento:str
    direccion:str
    ciudad:str
    representante:str
    telefonoContacto:str
    correo:str
    fechaEnvio:date
    costoEnvio:int
    descripcion:str

class ProveedorDTOEnvio(BaseModel): #EL DTO DE RESPUESTA
    id:int
    nombres:str
    documento:str
    direccion:str
    ciudad:str
    representante:str
    telefonoContacto:str
    correo:str
    fechaEnvio:date
    costoEnvio:int
    descripcion:str



class LogisticaDTOEnvio(BaseModel): #EL DTO DE RESPUESTA
    id= int
    nombreProveedor=str
    nombreEncargado=str
    correoEncargado= str
    numeroContactoEncargado= str
    productos = str
    cantidad=str
    numeroRecibo=str
    detalles= str
    transportadora=str
    numeroGuia=str
    fechaRecepcion= str


class LogisticaDTO(BaseModel): #EL DTO DE RESPUESTA
    id= int
    nombreProveedor=str
    nombreEncargado=str
    correoEncargado= str
    numeroContactoEncargado= str
    productos = str
    cantidad=str
    numeroRecibo=str
    detalles= str
    transportadora=str
    numeroGuia=str
    fechaRecepcion= str
