from persona import *
from random import *

def generar_cod():
    cod=""
    for i in range(5):
        cod+=str(randint(0,9))
    # print("Su código de empleado es el siguiente. Guárdelo!!!!: ", cod)
    return cod


class Empleado(Persona):
    set_codemps=set()
    try:
        def __init__(self, nombre, dni, sexo):
                super().__init__(nombre, dni, sexo)
                codemp=generar_cod()
                while codemp in Empleado.set_codemps:
                    codemp=generar_cod()
                self.codemp=codemp
                Empleado.set_codemps.add(codemp)
                print("Este es el código del empleado autogenerado, el empleado deberá guardarlo para ingresar al sistema: {}".format(self.codemp))
                contra=input("A continuación, el empleado debe ingresar su nueva contraseña (5 caracteres mínimo): ")
                while len(contra)<5:
                    contra=input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")
                self.contra=contra
    except ValueError as e:
        print("Error!", e)   

    #acá hace falta cargar esa contraseña y usuario al txt o cs de usuarios

