class Reserva():
    def __init__(self, num_reserva, tiempo_estadia, tipo_reserva):
        self.numreserva=num_reserva
        self.tiempo_estadia=tiempo_estadia #en días
        self.precio=0  # el precio lo calcula el empleado al crear la reserva
        self.tipo_reserva=tipo_reserva