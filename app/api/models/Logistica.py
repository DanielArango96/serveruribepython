from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Logistica():
    __tablename__ = 'logistica'
    id= Column(Integer, primary_key=True)
    nombreProveedor=Column(String(50))
    nombreEncargado=Column(String(50))
    correoEncargado= Column(String(100))
    numeroContactoEncargado= Column(String(50))
    productos = Column(String(300))
    cantidad=Column(String(50))
    numeroRecibo=Column(String(50))
    detalles= Column(String(200))
    transportadora=Column(String(50))
    numeroGuia=Column(String(50))
    fechaRecepcion= Column(Date)
