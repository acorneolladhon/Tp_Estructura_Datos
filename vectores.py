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
vec1.pop(vec1.index(3))
print(vec1)