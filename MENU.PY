#--> validás contraseña y usuario:
    #la contra y usuario van a estar en un archivo csv que viene del balneario, 
    #pero nosotros se la damos al sistema desde antes,

#-- una vez validado, entrás y subís los archivos.
#ahí ofrecés agregar empleado cliente reserva carpas

#opciones del menú
from balneario import Balneario

bal=Balneario("Balneario Carilo")
balneario=bal.leer_archivos("archivobalneario.pkl")  #acá cargo toda la info del balneario

us=input("Ingrese su nombre de usuario: ")
balneario.validar_contraseña(us)
