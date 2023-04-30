class Nodo():
    def __init__(self, dato=None, prox=None):
        self.dato=dato
        self.prox=prox
    
    def __str__(self):
        return str(self.dato)
    
if __name__=="__main__":
    nodo1=Nodo("Jose")
    nodo2=Nodo("Cata")
    nodo3=Nodo("Hugo")
    nodo1.prox=nodo2
    nodo2.prox=nodo3
    print(nodo1,nodo2,nodo3)
    print(nodo1.prox, nodo2.prox,nodo3.prox)