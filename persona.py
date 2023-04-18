class Persona():
    def __init__(self, nombre, dni, sexo):
        self.nombre=nombre
        self.dni=dni
        self.sexo=sexo
    
    def __str__(self):
        return "Mi nombre es {} y mi DNI es {}".format(self.nombre, self.dni)