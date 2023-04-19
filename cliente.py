from persona import Persona
class Cliente(Persona):
    def __init__(self, nombre, dni, sexo, tel, num_tarjeta):
        try:
            if type(tel)!=int and len(str(tel))!=10:
                raise ValueError("El número de teléfono no cumple con el formato adecuado. No puede registrarse el cliente.")
            if type(num_tarjeta)!=int and len(str(num_tarjeta))!=16:
                raise ValueError("El número de tarjeta no cumple con el formato adecuado. No puede registrarse el cliente.")
            super().__init__(nombre, dni, sexo)
            self.tel=tel
            self.num_tarjeta=num_tarjeta
            
        except ValueError as e:
            print("Error!!", e)


if __name__=="__main__":
    Cliente("juan", 34233564, "M", 1123334321, 1234567890123456)
    
        
