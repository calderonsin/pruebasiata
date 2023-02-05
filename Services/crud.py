from sqlalchemy.orm import Session
from Models.Order import Order
from Schemas.Order import OrderSchema

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()

def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def create_order( db: Session, order: OrderSchema):
    _order = Order(nombreRestaurante = order.nombreRestaurante,identificacionUsuario = order.identificacionUsuario, menu = order.menu,
    valorMenu = order.valorMenu, fechaPago = order.fechaPago, valorPagado = order.valorPagado)
    db.add(_order)
    db.commit()
    db.refresh(_order)
    return _order
   

    
    


def update_valor_order(db: Session, order_id: int,order_valorpagado: int, order_valormenu: int):
    _order = get_order_by_id(db=db, order_id=order_id)
    _order.valorPagado = order_valorpagado
    _order.valorMenu = order_valormenu
    db.commit()
    db.refresh(_order)
    return _order