from sqlalchemy import Column,Integer,String,Date
from config import Base

class Order(Base):
    __tablename__ = 'restaurante'
    id= Column(Integer,primary_key= True ,index= True)
    nombreRestaurante = Column(String(200))
    identificacionUsuario = Column(Integer)
    menu = Column(String(300))
    valorMenu = Column(Integer)
    fechaPago = Column(Date)
    valorPagado = Column(Integer)

