from listaenlazada import *
import numpy as np 
import matplotlib.pyplot as plt
from persona import *

# lista=Listaenlazada()
# lista.append(Nodo(1))
# lista.append(Nodo(2))
# lista.append(Nodo(3))
# lista.append(Nodo(4))
# lista.append(Nodo(5))

# print(lista)
# print(lista.eliminar_posicion(4))
# print(lista)

listapers=Listaenlazada()
p1=Persona("Josefina","44486117","M")
p2=Persona("Maica","55563777","f")
p3=Persona("Pedro","28817762","m")
p4=Persona("Agustina","30222788", "f")
listapers.append(Nodo(p1))
listapers.append(Nodo(p2))
listapers.append(Nodo(p3))
listapers.append(Nodo(p4))
listapers.append(Nodo(Persona("Juan", "22333776","M")))
listapers.append(Nodo(Persona("Martin", "88822345","M")))

print(listapers)
print(listapers.buscar_caracteristicaobjeto(30222788))
print(listapers.buscar_posicion__dato_objeto(30222788))

print(listapers)
listapers.modificar_dato_objeto(88822345, 23333776)
print("\n")
print(listapers)


#print("Dato eliminado: ")
#print(listapers.eliminar_posicion(3))
#print("\n")
#print("Nueva lista: ")
#print(listapers)

#CREO UN GRÁFICO DE BARRAS
dnis=listapers.recorrer_levantar_datos()
# strings = [str(x) for x in dnis]
# a=[1,2,3,4,5,6]
# plt.title("DNI de las personas por números random")
# plt.ylabel("Números random")
# plt.xlabel("DNIs de las personas")
# plt.bar(strings,a,width=0.5,color="blue")
# plt.show()

vector=np.array(dnis)
print(vector)
print(vector.min())
print(vector.max())
print(vector.mean())
print(vector.reshape([2,3]))
print(vector.size)   #EL SIZE ES UNA PROPERTY, NO UNA FUNCTION, ASÍ Q HAY Q LLAMARLO
print(vector.shape)

