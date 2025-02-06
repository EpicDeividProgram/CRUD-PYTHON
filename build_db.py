import sqlalchemy as db # Importamos SQLAchemy para poder interactuar con la base de datos
import dominio.modelo as modelo # Importamos el modelo de la base de datos
import util.m_Generico as gen # Importamos un modulo personalizado para funionalidades generiacas

# nombre de la carpeta que se creara para los datos de la base de datos
nombre_Car = "BD_CRUD"

# Ruta donde se creara la carpeta de la base de datos
ruta = "./"

# Crecion de la carpeta si no existe
gen.crear_carpeta(ruta, nombre_Car)

engine = db.create_engine("sqlite:///BD_CRUD/tienda.sqlite", echo=True, future=True)

modelo.Base.metadata.create_all(engine)
