class Persona():
    def __init__(self, nombre:str="", dni:str="", sexo:str="F"):
        self.persona_valida = True
        try: 
            self.nombre=nombre
            self.dni=str(dni)
            self.sexo=sexo
            if len(self.dni)!=8:
                raise ValueError("El DNI no cumple no tiene 8 digitos.")
            if self.sexo.upper()!="M" and self.sexo.upper()!="F":
                raise ValueError("El sexo no existe.")
        except ValueError as e:
            print("Error.", e)
            self.persona_valida = False


    def __str__(self):
        if self.persona_valida== True:
            return "Mi nombre es {} y mi DNI es {}".format(self.nombre, self.dni, self.sexo)
        else:
            return "La persona no fue creada"
    

if __name__ =="__main__":
    p=Persona("josefina geoghegan", 23454532,"M")
    print(p)
