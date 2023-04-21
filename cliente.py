from persona import Persona
class Cliente(Persona):
    #try:
    def __init__(self, nombre, dni, sexo, tel, num_tarjeta):
        if type(tel)!=int or len(str(tel))!=10:
            raise ValueError("El número de teléfono no cumple con el formato adecuado.")
        if type(num_tarjeta)!=int or len(str(num_tarjeta))!=16:
            raise ValueError("El número de tarjeta no cumple con el formato adecuado.")
        super().__init__(nombre, dni, sexo)
        self.tel=tel
        self.num_tarjeta=num_tarjeta
    #except ValueError as e:
    #     print("Error!!", e)

        
    # def __init__(self, nombre, dni, sexo, tel, num_tarjeta):
    #     try:
    #         if type(tel)!=int and len(str(tel))!=10:
    #             raise ValueError("El número de teléfono no cumple con el formato adecuado.")
    #         if type(num_tarjeta)!=int and len(str(num_tarjeta))!=16:
    #             raise ValueError("El número de tarjeta no cumple con el formato adecuado.")
    #         super().__init__(nombre, dni, sexo)
    #         self.tel=tel
    #         self.num_tarjeta=num_tarjeta
    #     except ValueError as e:
    #         print("Error!!", e)

# try:
#         def __init__(self, nombre, dni, sexo):
#                 super().__init__(nombre, dni, sexo)
#                 self.codemp=generar_cod()
#                 contra=input("A continuación, cree su contraseña (5 caracteres mínimo): ")
#                 while len(contra)<5:
#                     contra=input("Vuelva a crear su contraseña (5 caracteres mínimo): ")
#                 self.contra=contra
#     except ValueError as e:
#         print("Error!", e) 

if __name__=="__main__":
    Cliente("juan", 34233564, "M", 1123334321, 1234567890123456)
    
        
