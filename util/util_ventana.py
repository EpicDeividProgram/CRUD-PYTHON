# sirve para centrar la ventana al iniciar el programa
def centrar_ventana(ventana, aplicacion_an, aplicacion_la):
    pantalla_an = ventana.winfo_screenwidth()
    pantalla_la = ventana.winfo_screenheight()
    x = int((pantalla_an/2) - (aplicacion_an/2))
    y = int((pantalla_la/2) - (aplicacion_la/2))
    return ventana.geometry(f"{aplicacion_an}x{aplicacion_la}+{x}+{y}")
