from persona import *
class Cliente(Persona):
    def __init__(self, nombre, dni, sexo, tel, num_tarjeta):
        super.__init__(nombre, dni, sexo)
        self.tel=tel
        self.num_tarjeta=num_tarjeta
