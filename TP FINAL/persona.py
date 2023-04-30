class Persona():
    set_dnis=set()
    def __init__(self, nombre, dni, sexo):
            if type(dni)!=str or len(dni)!=8 or not dni.isdigit() or dni in Persona.set_dnis:
                raise ValueError("El DNI no cumple con el formato requerido o ya está registrado.")
            if sexo.upper() !="M" and sexo.upper()!="F":
                raise ValueError("El sexo no cumple con el formato requerido.")
            self.nombre=nombre
            self.dni=int(dni)
            self.sexo=sexo.upper()

    #def __str__(self):
    #    return "{}. DNI: {}, SEXO: {}".format(self.nombre,self.dni,self.sexo)


if __name__ =="__main__":
    p=Persona("josefina geoghegan", 23454532,"M")
    print(p)
