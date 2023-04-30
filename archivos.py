#aca lo que hice fue crear un archivo de texto adentro del programa donde genero usuarios
#tomando el nombre y apellido de los empleados y a su vez genero contraseñas para los mismos
# desp escribo en el archivo esos usuarios y contraseñas y desp la idea seria que cuando el 
#empleado ingrese al programa y ponga su usuario y contraseña se busqiue en este archivo 
#y si coinciden los deje entrar y sino pida que reingresen los datos 


def crear_archivo():
    archivo=open("/Users/agust/OneDrive/Desktop/Est de Datos/Tp_Estructura_Datos/usuarios_claves.txt", "w")  #hay que poner la direccion para que todos puedan ingresar
    archivo.close()
    return "listo"
a=crear_archivo()  #esto deberia ir en el main

def escribir(file, datos):  #aca puedo llenar el archivo
    archivo = open(file , 'w')
    info = archivo.write(datos)
    archivo.close()
    return info

def leer_archivo(file):
    archivo=open(file, "r")
    info=archivo.read
    archivo.close()
    return info

def crear_usuario(nombre, apellido, dni, puesto):
    sublista1=[]
    usuario = nombre[0].upper()+apellido[0].upper()+str(dni)
    sublista1.append(usuario)
    return sublista1

def crear_clave(dni):
    sublista2=[]
    clave = str(dni)+"1234"
    sublista2.append(clave)
    return sublista2

sub1=crear_usuario("agus", "corneo", 736953, "sombrillera")
sub2=crear_clave(736953)
lista_usuarios_claves = [sub1, sub2]

#escribir(a,lista_usuarios_claves)  #no puedo pasar la lista, tengo que pasar archivo pot archivo
leer_archivo(a)