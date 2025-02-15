import sqlalchemy as db
from sqlalchemy.orm import Session
from dominio.modelo import modelProducto
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class Servicio_D_Producto():
    def __init__(self):
        self.engine = db.create_engine("sqlite:///BD_CRUD/tienda.sqlite", echo=True, future=True)
       
    def registro(self, nombre, precio):
        producto = modelProducto()
        producto.nombre = nombre
        producto.precio = precio
        with Session(self.engine) as session:
            session.add(producto)
            session.commit() 
            
    def modificar(self, nombre, precio, id_produto):
        try:
            # Busco el producto en la base de datos
            with Session(self.engine) as sesion:
                producto = sesion.query(modelProducto).filter_by(id = id_produto).one()
               
                # Actualizo los atributos del producto
                producto.nombre = nombre
                producto.precio = precio
                # Confirmo los cambios para la base de datos
                sesion.commit()
                print(f"El producto con el ID {id_produto} se actualizo correctamente ")
               
        except NoResultFound:
            print(f"No se encontro ningun produto con el id {id_produto} no se realizo ninguna modificacion")
            return False
        except Exception as e:
            print(f"Error al actualizar el producto: {e} ") 
            return False
        
        
    def obtener_producto(self) -> List[modelProducto]:
        productos: modelProducto = None
        with Session(self.engine) as session:
            productos = session.query(modelProducto).all()
        return productos
    
    def eliminar_producto(self, id_producto):
        with Session(self.engine) as session:
            producto = session.query(modelProducto).filter_by(id=id_producto).first()
            if producto:
                try:
                    session.delete(producto)
                    session.commit()
                    print(f"El producto con id {id_producto} se elimino correctamente")
                except IntegrityError as e:
                    session.rollback()
                    print(f"No se pudo realizar la eliminacion de el producto con id: {id_producto}, Error: {e}")
            else:
                print(f"No se encontro ningun producto con id {id_producto}") 