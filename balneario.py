import numpy as np
from carpasomb import Carpa
from  carpasomb import Sombrilla
from reserva import Reserva
from empleado import Empleado
from persona import Persona
from cliente import Cliente
from datetime import datetime
import pickle
import csv


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

    #FUNCIÓN PARA LEER EL PICKLE Y RECUPERAR TODA LA INFO DEL BALNEARIO PARA ARRANCAR
    def leer_archivos(self,path):
        with open(path, "rb") as f:
            infobal=pickle.load(f)
        return infobal

    #FUNCIÓN PARA CARGAR EL ARCHIVO CSV DE CONTRASEÑAS CADA VEZ QUE SE CIERRA EL PROGRAMA
    def cargar_contraseñas(self):
        with open('usuarios.csv', 'w', newline='') as csvfile:
            fieldnames = ['usuario', 'contraseña']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for empleado in self.dicemp.keys():
                writer.writerow({'usuario': empleado.codemp, 'contraseña': empleado.contra})

    def revisar_matrices(self):
        pass
    #con esta función, antes de cerrar el programa revisamos las matrices para ver si están vencidas, si hay algo vencido lo sacamos y ponemos None

    #FUNCIÓN PARA HACER PERSISTIR LA INFO DEL OBJETO BALNEARIO EN UN PICKLE
    def cargar_archivos(self):
        with open("archivobalneario.pkl", "wb") as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    #FUNCIÓN PARA CARGAR UN EMPLEADO A LA LISTA DE EMPLEADOS Y CREARLO
    #HAY QUE VALIDAR LA INFORMACIÓN INGRESADA DESDE LA CLASE EMPLEADO Y PERSONA
    def cargar_empleado(self, nom_cargado, dni_cargado, sexo_cargado):
        try:
            if dni_cargado not in self.dicemp.keys():    
                emp=Empleado(nom_cargado, dni_cargado, sexo_cargado)
                self.dicemp[dni_cargado]=emp
                self.dicusuarios[emp.codemp]=emp.contra
            else:
                raise ValueError("Ese empleado ya fue cargado.")
        except ValueError as e:
            print("Error!", e, "El empleado no fue cargado.")

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
            print("Error !", e, "El cliente no fue registrado.")

    #ESTO VA A PASAR ANTES DE SUBIR LOS ARCHIVOS, ASÍ QUE NO LO VAMOS A USAR
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
    def ver_matriz(self, tipo_reserva):
        matriz_correcta=lambda x: self.m_carpas if x=="C" else self.m_sombrillas
        matriz=matriz_correcta(tipo_reserva)
        for i in matriz:
                if i.estado==None:
                    print(0)
                else:
                    print(i.estado.tiempo_estadia-((datetime.now()-i.fechacomienzo).days()))

    def asignar_reserva(self,matriz, tipo_reserva):
        matriz_correcta=lambda x: self.m_carpas if x=="C" else self.m_sombrillas
        matriz=matriz_correcta(tipo_reserva)
    #según si es sombrilla o carpa, revisamos las matrices para ver si tienen lugares disponibles, y en base a eso asignamos una posicion

    def calcular_precio(): 
        pass
    #este precio despues se lo pasamos a la reserva que creemos

    def modificar_estadia():
        pass
    #viene el cliente y pide modificar su tiempo de estadia


if __name__=="__main__":
    bal=Balneario("Balneario Carilo")
    # for i in bal.m_carpas:
    #     print("\n")
    #     for ax in i:
    #         print(ax.estado, end="\t")
#print("\n")
#bal.cargar_empleado("Juan", 33333333, "m")
#print(bal.dicemp[33333333])

    bal.registrar_cliente("joseidna", 44486117, "m", 1167778764,1111111111111111)

    print(bal.dicclientes[44486117])
    bal.cargar_archivos()
    bl2=Balneario("ca")
    info=bl2.leer_archivos("archivobalneario.pkl")
    bl2=info
    print(bl2)
