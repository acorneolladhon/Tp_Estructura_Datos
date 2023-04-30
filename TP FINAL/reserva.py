import datetime
class Reserva():

    def __init__(self,num_reserva, dias_estadia, tipo_reserva,cliente):
        self.num_reserva=num_reserva
        self.precio=0
        self.fechacomienzo=datetime.datetime.now()
        self.tipo_reserva=tipo_reserva
        self.cliente=cliente
        self.estadia=int(dias_estadia)
        self.vencimiento=datetime.datetime.now()+datetime.timedelta(dias_estadia)
    
    def __str__(self):
        return "Reserva: {}, días de estadía total: {}".format(self.numreserva,self.tiempo_estadia)
    
if __name__=="__main__":
    from datetime import timedelta
    print((datetime.strptime("2025/04/08","%Y/%m/%d")-datetime.now()).days)
    print(datetime.now()+ datetime.timedelta(days=2))
