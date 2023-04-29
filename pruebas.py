import datetime
import numpy as np

def hola(capr):
    for fila in range(len(S)):
        for columna in range(len(S[fila])):
            if carpas[fila][columna]==0:
                print("hola")
                return fila, columna 

print(datetime.datetime.now()+datetime.timedelta(days=3))
carpas=[[0 for i in range(6)] for i in range(4)]
S=np.array(carpas)
a,b=hola(carpas)
print(a)
print(b)

#devuelve posicion de la matriz libre
    # def buscar_disponible(self, tipo_reserva):
    #     matriz=self.matrizdetrabajo(tipo_reserva)
    #     for fila in range(len(matriz)):
    #         for columna in range(len(matriz[fila])):
    #             carpasomb=matriz[fila][columna] 
    #             if carpasomb.estado==None:
    #                 espacio=True
    #                 break
    #     if espacio==True:
    #         return fila,columna
    #     else:
    #         return False

#buscar disponible por fila
    # def buscar_filadispo(self, tipo_reserva, num_fila=None):
    #     matriz=self.matrizdetrabajo(tipo_reserva)
    #     if num_fila-1>len(matriz):
    #         raise ValueError("El número de fila no es válido.")
    #     else:    
    #         for columna in range(len(matriz[num_fila-1])):
    #             if matriz[num_fila-1][columna].estado==None:
    #                 espacio=True
    #                 break
    #     if espacio==True:
    #         return num_fila-1, columna
    #     else:
    #         return False
