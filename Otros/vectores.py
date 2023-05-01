from array import array

vector=array("b", [1,2,3,2,1,4,5,3,5])
vectorfloats=array("d",[2.5,6.5,7,2,1.7])
print(vector)
print(vectorfloats)
print(type(vectorfloats))
lista=[1,-2,3,-1]
vectorenterosconsigno=array("i",lista)
print(vectorenterosconsigno)
for dato in vectorenterosconsigno:
    print(dato, end="\t")
print("\n")
print(len(vectorenterosconsigno))
#ver la ultima posicion del vector
print(vectorfloats[len(vectorfloats)-1])
print(vectorfloats[-1])

print(vector[1:3])

print(vectorenterosconsigno)
vectorenterosconsigno[0]=-10
print(vectorenterosconsigno)

print(vector)
vector[0:3]=array("b",[10,50,50,20,30]) #en vez de los primeros 3 datos, van a estar todos esos
print(vector)

vector.append(17)
vector.append(9)
print(vector)

vector.extend([34,90,21])
print(vector)

#vector.extend([5.5,-2])
#NO SE PUEDE AGREGAR DATOS DE OTRO TIPO EN EL VECTOR DE UN TIPO DE DATOS DIFERENTE


#concatenar dos vectores (solo si son del mismo tipo)
vec1=array("i", [1,2,3,4])
vec2=array("i",[7,8,9])
vecnuevo=vec1+vec2
print(vecnuevo)

#si el index no encuentra el valor devuelve error
vec1.index(3)
print(vec1)

#el pop borra el que elemento que está en la posición que le digo
vec1.pop(vec1.index(3))
print(vec1)
#si no le paso un index al pop, elimina el último

vec1.remove(4)
print(vec1)

#si le pido a remove que elimine un valor que no existe, SALTA ERROR
#vec1.remove(9)

print(vector)
#vect=vector.reverse()   --> ESTO NO FUNCIONA, CUANDO YO INVIERTO EL VECTOR EN CUALQUIER LADO, YA QUEDA REVERTIDO EN TODOS LADOS
#vector.reverse()  #no lo puedo PONER EN UNA VARIANBLE, YA DIRECTAMENTE LO CAMBIA
#print(vect)
print(vector)

hola=sorted(vector)
print(hola)   #el sorted es BUILT IN, se aplica como el len y la funcion normal
#en este caso, no se altera el vector en sí, el vector sigue siendo el original, solo que
# en una variable guardaste ese mismo vector ordenado
print(vector)


#CONVERTIR UN VECTOR EN UNA LISTA
#listanueva=vector.tolist()
listanueva=vector.tolist()
print(listanueva)

#la lista no se va a crear acá, porque en la ejecución no va a mutar el vector, tenes que guar
# darlo en una variabble para crearlo 
# vector.tolist()
# print(vector)
