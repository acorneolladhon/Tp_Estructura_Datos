from clasenodo import *
from persona import Persona

class Listaenlazada():
    def __init__(self):
        self.head=None
        self.len=0

    def __str__(self) -> str:
        if self.len==0:
            return "Lista vacía"
        else:
            devolver=""
            nodo_recorro=self.head
            while nodo_recorro!=None:
                devolver+=str(nodo_recorro)+"\t"
                nodo_recorro=nodo_recorro.prox
            return devolver

#agrega al principio de la lista (como head)
    def agregar_al_inicio(self, nodo:Nodo):
        if len==0:
            self.head=nodo
        else:
            nodo.prox=self.head
            self.head=nodo
        self.len+=1

#EL APPEND TIENE QUE RECIBIR UN VALOR EN FORMATO NODO
#agrega un valor al final de la lista (un append de lista normal)  
    def append(self, nodo:Nodo):
        if self.len==0:
            self.head=nodo
        
        else:
            nodo_recorro=self.head
            while nodo_recorro.prox!=None:
                nodo_recorro=nodo_recorro.prox
            nodo_recorro.prox=nodo
        self.len+=1

#elimina por default el último valor, y si no, elimina el de la posición pedida
#si no está levanta exception
    def pop(self, posicion=None):
        if posicion==None:
            if self.len==0:
                nodo_eliminado=None
            elif self.len==1:
                nodo_eliminado=self.head
                self.head=None
                self.len-=1
            else:
                nodo_recorro=self.head
                while nodo_recorro.prox.prox!=None:
                    nodo_recorro=nodo_recorro.prox
                nodo_eliminado=nodo_recorro.prox
                nodo_recorro.prox=None
                self.len-=1
        else:
            if posicion<self.len: #si la len es 5, no hay posicion 5, hay posicion 4, porque arranca desde 0                
                if posicion==0:
                    nodo_eliminado=self.head
                    self.head=self.head.prox
                else:
                    nodo_recorro=self.head
                    for n in range(posicion-1):
                        nodo_recorro=nodo_recorro.prox
                    nodo_eliminado=nodo_recorro.prox
                    nodo_recorro=nodo_recorro.prox.prox
                self.len-=1
            else:
                raise Exception("El índice indicado excede la longitud de la lista")
        return nodo_eliminado

#elimino la primera aparición del valor
    def eliminar_valor(self,valor_buscado):
        if self.head.dato!=valor_buscado:
            nodo_recorro=self.head
            valor_esta=False
        #si el siguiente a mi nodo es el valor que quiero entonces freno
            while nodo_recorro!=None:
                if nodo_recorro.prox!=None:
                    if nodo_recorro.prox.dato==valor_buscado:
                        valor_esta=True
                        break
                nodo_recorro=nodo_recorro.prox
            
            if valor_esta==True:
                nodo_eliminado=nodo_recorro.prox
                nodo_recorro.prox=nodo_recorro.prox.prox
                self.len-=1
            else:
                nodo_eliminado=None
        
        else:
            nodo_eliminado=self.head
            self.head=self.head.prox
            self.len-=1
        
        return nodo_eliminado

#modificar un valor una vez que lo encuentra
    def modificar_valor(self, valor_buscado, nuevo_valor):
        nodo_recorro=self.head
        while nodo_recorro!=None:
            if nodo_recorro.dato==valor_buscado:
                nodo_recorro.dato=nuevo_valor
            nodo_recorro=nodo_recorro.prox

#chequea si un valor está ya en la lista y devuelve su posicion
    def buscar_valor(self,valor_buscado):
        nodo_recorro=self.head
        recorrido=0
        posicion=None
        while nodo_recorro!=None:
            if nodo_recorro.dato==valor_buscado:
                posicion=recorrido
                break
            nodo_recorro=nodo_recorro.prox
            recorrido+=1    
        return posicion

#le pasas la posicion de un valor y lo elimina
    def eliminar_posicion(self,posicion):
        if posicion<self.len:
            if posicion!=0:
                nodo_recorro=self.head
                for n in range(posicion-1):
                    nodo_recorro=nodo_recorro.prox
                nodo_eliminado=nodo_recorro.prox
                nodo_recorro.prox=nodo_recorro.prox.prox
            else:
                nodo_eliminado=self.head
                self.head=self.head.prox
            self.len-=1
            return nodo_eliminado
        else:
            raise Exception("El índice indicado excede el largo de la lista.")

#cambiar la cabeza de la lista, que arranque desde el segundo nodo
    def comenzar_segundo_nodo(self):
        if self.head is not None and self.head.prox is not None:
            self.head=self.head.prox

#FUNCIONES CON LISTAS ENLAZADAS DE OBJETOS

#le ingresás el dato q buscas, encuentra su posicion (en este caso dni, pero se puede acceder a la característica)
    def buscar_posicion__dato_objeto(self, dato_buscado):
            nodo_recorro=self.head
            recorrido=0
            posicion=None
            while nodo_recorro!=None:
                if nodo_recorro.dato.dni==dato_buscado:
                    posicion=recorrido
                    break
                nodo_recorro=nodo_recorro.prox
                recorrido+=1    
            return posicion

#recorre lista de objetos y accede a la característica de un objeto
    def buscar_caracteristicaobjeto(self,dato_buscado): #ejemplo--> mirar si ya está un dni
        nodo_recorro=self.head
        encontrado=False
        while nodo_recorro!=None:
            if nodo_recorro.dato.dni==dato_buscado:
                encontrado=True
                break
            nodo_recorro=nodo_recorro.prox   
        return encontrado

#recorre una lista enlazada de objetos y devuelve una lista con los valores de los objetos pedidos (lista de dnis)
    def recorrer_levantar_datos(self):
        nodo_recorrido=self.head
        lista_datos=[]
        while nodo_recorrido!=None:
            lista_datos.append(nodo_recorrido.dato.dni)
            nodo_recorrido=nodo_recorrido.prox
        return lista_datos

#modificar un valor una vez que lo encuentra (pero accediendo a una característica particular, acá el DNI)
    def modificar_dato_objeto(self, dato_buscado, nuevo_valor):
        nodo_recorro=self.head
        while nodo_recorro!=None:
            if nodo_recorro.dato.dni==dato_buscado:
                nodo_recorro.dato.dni=nuevo_valor
            nodo_recorro=nodo_recorro.prox

if __name__=="__main__":
    # #print("Imprimo lista instanciada, no tiene elementos todavía:")
    # lista=Listaenlazada()
    # #print(lista)
    
    # #print("Elimino con pop un elemento.")
    # #print("El elemento eliminado de la lista es:", lista.pop())

    # #print("Agrego al inicio un 5:")
    # lista.agregar_al_inicio(Nodo(5))
    # #print(lista)

    # #print("El elemento eliminado de la lista es: ", lista.pop())
    # #print("Longitud",lista.len)
    # #print(lista)

    # #print("Agrego al inicio un 3:")
    # lista.agregar_al_inicio(Nodo(3))
    # #print(lista)

    # #print("Agrego un 10 al final:")
    # lista.append(Nodo(10))
    # #print(lista)

    # #print("Agrego un 2 al principio: ")
    # lista.agregar_al_inicio(Nodo(2))
    # #print(lista)

    # #print("Imprimo la longitud de la lista: ")
    # #print(lista.len)

    # #print("Elimino el último elemento de la lista con pop (debería eliminar el 10)")
    # #elemento_eliminado=lista.pop()
    # #print("El elemento eliminado es: ", elemento_eliminado)
    
    # print("Lista actual: ", lista)
    # print("ELimino el valor: ", lista.pop())
    # print("Lista actual: ",lista)

    # print(lista.eliminar_valor(1))
    # print(lista)

    # lista.modificar_valor(3,7)
    # print(lista)
    
    # print("Posición del valor buscado: ", lista.buscar_valor(8))

    # print(lista.eliminar_posicion(1))

    yo=Persona("Jose", "44444444","M")
    el=Persona("Martin", "44455444","M")
    ella=Persona("Enriqueta", "45644444","F")
    nosotros=Persona("Martinez", "78444444","M")

    listapersonas=Listaenlazada()
    listapersonas.append(Nodo(yo))
    listapersonas.append(Nodo(el))
    listapersonas.append(Nodo(ella))
    listapersonas.append(Nodo(nosotros))
    print(listapersonas)
    #Te devuelve TRUE si encuentra el documento que buscás en la lista
    print(listapersonas.buscar_caracteristicaobjeto(44444444))
    