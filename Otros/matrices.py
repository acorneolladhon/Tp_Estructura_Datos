import numpy as np
#podemos crear vectores o matrices 

#VECTORES --> no hace falta especificar el tipo de dato
hola=np.array([1,2,3])
print(hola)

#MATRICES --> no hace falta especificar datos
matriz=np.array([[1,2,3],[4,5,6]])
print(matriz)

#recorrido matrices por fila
for fila in matriz:
    print(fila)

#recorrido matrices por elemento
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        print(matriz[fila][columna])

#matriz con datos aleatorios
mat=np.empty([2,2])  #le paso cantidad de filas y de columnas que quiero
print(mat) #como no le indico el tipo de dato que quiero automáticamente me lo hace un decimal

mat=np.empty([2,2], "int") 
print(mat)

mat=np.empty([3,4],dtype=int)
print(mat)

#vector con datos aleatorios
vectoraleatorio=np.empty(5, dtype=int)
print(vectoraleatorio)

#CREAR MATRIZ CON CEROS O UNOS
matriz0=np.zeros([2,3],dtype=int)
print(matriz0)
mat1=np.ones([2,4],dtype=int)
print(mat1)

#CREAR VECTORES CON 0 O 1
vec1=np.zeros(3, dtype=int)
vec2=np.ones(2, dtype=int)
print(vec1)
print(vec2)

print("\n")

#METODO ARANGE PARA VECTORES
met=np.arange(0,6,2)
print(met)
met=np.arange(0,6)
print(met)

#METODO RESHAPE PARA MATRICES
matriz=np.arange(4).reshape(2,2)
print(matriz)
matriz=np.arange(8).reshape(4,2)
print(matriz)

#MÉTODO SORT
#método para ordenar por filas 
matriz=np.array([[15,18,3],[5,9,1],[9,17,21]])
print(matriz)
mat=np.sort(matriz)   #vas a ver la matriz ordenada, cada fila individualmente
print(mat)

#ordenar por columna (osea que mirando para abajo, las columnas estén ordenadas)
matriz=np.array([[15,18,3],[5,9,1],[9,17,21]])
print(matriz)
mat=np.sort(matriz,axis=0)   #vas a ver la matriz ordenada, por columna individual
print(mat)

#ordenar todos los datos directamente sin considerar filas 
matriz=np.array([[15,18,3],[5,9,1],[9,17,21]])
print(matriz)
mat=np.sort(matriz,axis=None)   #vas a ver la matriz ordenada, por columna individual
print(mat)

#SUMAR TODOS LOS EELEMENTOS DE LA MATRIZ, CONSEGUIR MAXIMOS Y MINIMOS
print(mat.sum())
print(mat.max())
print(mat.min())

#sumar cada primer elemento de las columnas (osea el 1 y el 3, el 2 y el 4)
mm=np.array([[1,2],[3,4]])
print(mm.sum(axis=0))

#suma los elementos de las filas (osea el 1 con el 2, y el 3 con el 4)
print(mm.sum(axis=1))

print("\n")
adm=np.array([[1,9],[2,3]])
print(adm.max(axis=0)) #devuelve el máximo de cada columna, de la primera es el 2, de la sefunda es el 9)
print(adm.max(axis=1)) #devuelve el máx de cada fila, de la primera el 9, de la segunda el 3
#te devuelve los maximos posicionados en un array 

print(np.ndim(adm)) #devuelve las dimensiones de la matriz (un entero)
print(np.shape(adm)) #devuelve la forma en la que está estructurada, en una tupla (acá es un (2,2))
print(np.size(adm)) #devuelve la cantidad de elementos que tiene, un int (en este caso un 4)