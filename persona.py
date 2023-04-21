class Persona():
    def __init__(self, nombre, dni, sexo):
        #try:
            if type(dni)!=int or len(str(dni))!=8 or not(str(dni).isdigit()) and dni:
                raise ValueError("El DNI no cumple con el formato requerido.")
            if sexo.upper() !="M" and sexo.upper()!="F":
                raise ValueError("El sexo no cumple con el formato requerido.")
            self.nombre=nombre
            self.dni=dni
            self.sexo=sexo.upper()
        #except ValueError as e:
        #    print("Error!", e)
    def __str__(self):
        return "Mi nombre es {} y mi DNI es {}".format(self.nombre, self.dni)
    

if __name__=="__main__":
    p=Persona("josefina geoghegan", 23454532,"M")
