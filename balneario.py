import numpy as np
from carpasomb import Carpa
from  carpasomb import Sombrilla
from reserva import Reserva
from empleado import Empleado
from persona import Persona
from cliente import Cliente
from datetime import datetime


class Balneario():

    def __init__(self, nombre):         
        self.nombre=nombre
        self.dicemp=dict()
        self.dicclientes=dict()
        self.dicusuarios=dict()
        carpas=[[Carpa() for i in range(6)] for i in range(4)]
        self.m_carpas=np.array(carpas)
        sombris=[[Sombrilla() for i in range(5)] for i in range(3)]
        self.m_sombrillas=np.array(sombris)

    def leer_archivos(self, arch_emps, arch_clientes, arch_matrices):
        pass
    #con esta función, al iniciar el programa desde el main, buscamos toda la información del balneario en los archivos que llamamos y tambien en el archivo de clientes y de empleados

    def revisar_matrices(self):
        pass
    #con esta función, antes de cerrar el programa revisamos las matrices para ver si están vencidas, si hay algo vencido lo sacamos y ponemos None

    def cargar_archivos(self, info_emps, info_matrices):
        pass
    #con esta función, al cerrar el programa, guardamos toda la info que recolectamos durante esa utilización del programa 

    #FUNCIÓN PARA CARGAR UN EMPLEADO A LA LISTA DE EMPLEADOS Y CREARLO
    #HABRÍA QUE VALIDAR LA INFORMACIÓN INGRESADA DESDE LA CLASE EMPLEADO Y PERSONA
    def cargar_empleado(self, nom_cargado, dni_cargado, sexo_cargado):
        try:
            if dni_cargado not in self.dicemp.keys():    
                emp=Empleado(nom_cargado, dni_cargado, sexo_cargado)
                self.dicemp[dni_cargado]=emp
                self.dicusuarios[emp.codemp]=emp.contra
            else:
                raise ValueError("Ese empleado ya fue cargado.")
        except ValueError as e:
            print("Error!", e)

    #FUNCIÓN PARA REGISTRAR UN CLIENTE Y CREARLO, DIRECTAMENTE SE LE PASA LA INFO
    #IDEM EMPLEADO
    def registrar_cliente(self, nombre_pedido, dni_pedido, sexo_pedido, numtel, numtarjeta):
        try:    
            if dni_pedido not in self.dicclientes.keys():
                cl=Cliente(nombre_pedido,dni_pedido,sexo_pedido,numtel, numtarjeta)
                self.dicclientes[dni_pedido]=cl
            else:
                raise ValueError("Ese cliente ya se encuentra registrado.")
        except ValueError as e:
            print("Error !", e)

    #FUNCIÓN QUE VALIDA LA CONTRASEÑA, DEVUELVE TRUE SI ESTÁ REGISTRADO Y FALSE SI NO
    #HAY QUE CREAR UN ARCHIVO CSV/TXT con contraseñas y usuarios
    def validar_contraseña(self, codemp_ingresado):
        if codemp_ingresado in self.dicemp.keys():
            contra=input("Ingrese su contraseña: ")
            while self.dicusuarios[codemp_ingresado]!=contra and contra!="0":
                contra=input("Contraseña incorrecta.Vuelva a intentar (o presione 0 para salir): ")
            if contra=="0":
                return False
            else:
                return True
        else:
            print("Usted no se encuentra registrado en el sistema.")

    #FUNCIÓN PARA IMPRIMIR LA MATRIZ Y VER LAS OPCIONES SEGÚN CUÁL ESTÁ OCUPADA Y CUÁL NO
    #DICE CUÁNTOS DÍAS LE QUEDA A CADA UNA
    #LO DE S Y C SE PODRÍA HACER CON UN MAP Y FILTER EN MENOS RENGLONES
    def ver_matriz(self, tipo):
        if tipo.lower()=="c":
            for i in self.m_carpas:
                if i==None:
                    print(0)
                else:
                    print(i.tiempo_estadia-((datetime.now()-i.fechacomienzo).days()))
        #al tiempo de estadía le resta lo que ya estuviste
        elif tipo.lower()=="s":
            for i in self.m_sombrillas:
                if i==None:
                    print(0)
                else:
                    print(i.tiempo_estadia-((datetime.now()-i.fechacomienzo).days()))


    def asignar_reserva(matriz, tipo_reserva):
        pass
    #según si es sombrilla o carpa, revisamos las matrices para ver si tienen lugares disponibles, y en base a eso asignamos una posicion

    def calcular_precio(): 
        pass
    #este precio despues se lo pasamos a la reserva que creemos

    def modificar_estadia():
        pass
    #viene el cliente y pide modificar su tiempo de estadia

    