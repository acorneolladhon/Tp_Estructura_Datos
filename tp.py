import numpy as np 

class Carpa():
    def __init__(self):
        estado=None

class Sombrilla():
    def __init__(self):
        estado=None

class Balneario():
    def __init__(self, nombre):         
        self.nombre=nombre
        self.dicemp=dict()
        carpas=[[Carpa() for i in range(6)] for i in range(4)]
        self.m_carpas=np.array(carpas)
        sombris=[[Sombrilla() for i in range(5)] for i in range(3)]
        self.m_sombrillas=np.array(sombris)
    
    def registrar_cliente():
        pass
    #acá podemos pedirle los datos al cliente que quiere reservar, preguntarle el tiempo y registrarlo en la lista de clientes (?)
    #también se podría pedir desde el menú --> para no complicar el menú quizas es más facil desde acá 

    def asignar_reserva(matriz, tipo_reserva):
        pass
    #según si es sombrilla o carpa, revisamos las matrices para ver si tienen lugares disponibles, y en base a eso asignamos una posicion

    def calcular_precio(): 
        pass
    #este precio despues se lo pasamos a la reserva que creemos

    def modificar_estadia():
        pass
    #viene el cliente y pide modificar su tiempo de estadia

    def revisar_matrices(self):
        pass
    #chequeamos las fechas al final del programa
    #CHEQUEAMOS LAS MATRICES (ejemplo si ya expiraron las reservas)
    
    def ver_matriz(self):
        pass
    #visualice en pantalla la matriz del balneario

    def cargar_empleado(self):
        pass
    #esta funcion la podemos crear por las dudas para que el empleado se cree y se cargue a la lista por si nos lo piden en el parcial

    def validar_contraseña(self):
        pass
    #podemos hacer un archivo csv con usuarios y contraseñas

    def leer_archivos(self, info_emps, info_matrices):
        pass
    #con esta función, al iniciar el programa desde el main, buscamos toda la información del balneario en los archivos que llamamos y tambien en el archivo de clientes y de empleados

    def cargar_archivos(self, info_emps, info_matrices):
        pass
    #con esta función, al cerrar el programa, guardamos toda la info que recolectamos durante esa utilización del programa 

class Reserva():
    def __init__(self, num_reserva, tiempo_estadia, tipo_reserva):
        self.numreserva=num_reserva
        self.tiempo_estadia=tiempo_estadia #en días
        self.precio=0  # el precio lo calcula el empleado al crear la reserva
        self.tipo_reserva=tipo_reserva

class Empleado():
    def __init__(self, codemp, dni):
        self.codemp=codemp

    
    

    