from datetime import datetime
from datetime import date
class Reserva():
    def __init__(self, num_reserva, tiempo_estadia, tipo_reserva,fechacomienzo=datetime.now()):
        self.numreserva=num_reserva
        self.tiempo_estadia=tiempo_estadia #en días
        self.fechacomienzo=fechacomienzo #cuando la creás, le pasás la fecha de ese día
        self.precio=0  # el precio lo calcula el empleado al crear la reserva
        self.tipo_reserva=tipo_reserva
    
    def __str__(self):
        return "Reserva: {}, días de estadía total: {}".format(self.numreserva,self.tiempo_estadia)
    
if __name__=="__main__":
    print(type(date.today()))  #--> date today devuelve la fecha tipo "2023-04-05"
    print((datetime.strptime("2025/04/08","%Y/%m/%d")-datetime.now()).days)