from fastapi import APIRouter, HTTPException, Path, Response,status
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from Schemas.Order import OrderSchema, Request, Response, RequestOrder
from controller.orderController import validateDate

import Services.crud as crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/pagos" )
async def create_order_service(request: RequestOrder, db: Session = Depends(get_db)):
    if validateDate(request.parameter.fechaPago):
        
        return Response(status="Bad request",
        status_code=status.HTTP_400_BAD_REQUEST,
                    code="400",
                    message="lo siento pero no se puede recibir el pago por decreto de administración").dict(exclude_none=True)
                    
    else:
        crud.create_order(db, order = request.parameter)
        return Response(status="Success",
        status_code=status.HTTP_200_OK,
                    code="200",
                    message="gracias por pagar").dict(exclude_none=True)
        

    
    

    


@router.get("/pagos")
async def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _orders = crud.get_orders(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_orders)