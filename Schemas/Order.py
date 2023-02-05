from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from datetime import date

T = TypeVar('T')

class OrderSchema(BaseModel):
    id:  Optional[int]
    nombreRestaurante : str
    identificacionUsuario : int
    menu : str
    valorMenu  : float
    fechaPago : date
    valorPagado : float
    

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestOrder(BaseModel):
    parameter: Optional[OrderSchema] = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]