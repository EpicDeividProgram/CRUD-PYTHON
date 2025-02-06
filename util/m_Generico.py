import os

def crear_carpeta(ruta, nombre_Car):
    ruta_Com = os.path.join(ruta, nombre_Car)
    
    if not os.path.exists(ruta_Com):
        os.makedirs(ruta_Com)
        return True, f"Se creo la carpeta {nombre_Car} en {ruta}"
    else:
        return False, f"La carpeta {nombre_Car} ya esxiste {ruta}"