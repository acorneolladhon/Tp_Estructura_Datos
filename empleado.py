from persona import *
from random import *

def generar_cod():
    cod=""
    for i in range(5):
        cod+=str(randint(0,9))
    print("Su código de empleado es el siguiente. Guárdelo!!!!: ", cod)
    return cod

class Empleado(Persona):
    try:
        def __init__(self, nombre, dni, sexo):
            super().__init__(nombre, dni, sexo)
            self.codemp=generar_cod()
            contra=input("A continuación, cree su contraseña (5 caracteres mínimo): ")
            while len(contra)<=5:
                contra=contra=input("Vuelva a crear su contraseña (5 caracteres mínimo): ")
            self.contra=contra
    except ValueError as e:
        print("Error!!", e)
        
    #acá hace falta cargar esa contraseña y usuario al txt o cs de usuarios

