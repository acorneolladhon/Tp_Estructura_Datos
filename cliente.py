from persona import Persona

#asumo que los datos que me entran son STR de los inputs
class Cliente(Persona):
    def __init__(self, nombre, dni, sexo, tel, num_tarjeta):
        if type(tel)!=str or len(tel)!=10:
            raise ValueError("El número de teléfono no cumple con el formato adecuado.")
        if type(num_tarjeta)!=str or len(num_tarjeta)!=16:
            raise ValueError("El número de tarjeta no cumple con el formato adecuado.")
        super().__init__(nombre, dni, sexo)
        self.tel=int(tel)
        self.num_tarjeta=int(num_tarjeta)
        self.deuda=0

    def __str__(self):
        return "Datos del cliente:\nNombre: {}, DNI: {}, Sexo: {}, Numtel: {}, Numtarjeta: {}".format(self.nombre,self.dni,self.sexo,self.tel,self.num_tarjeta)

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
    
        
