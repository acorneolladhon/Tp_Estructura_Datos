import json
import pickle

#antes de cargar todo a pickle, lo metemos todo en un diccionario de objetoss/diccionarios
#y lo metemos  pickle, para después tener un diccionario datos[clients]=diccioclientes, datos[emps]
#también hay que armar un archivo csv de usuarios y contraseñas/ y/o un pickle aparte

import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

class Jose():
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        self.diccio={"nuevo":1,"ella":1}
    def __str__(self):
        return "hola"+ str(self.nombre)
    def arch(self):
        with open("C:/Users/Jose/OneDrive/Documentos/ITBA/Estructura de datos y programación/TP BALNEARIO/Tp_Estructura_Datos/nuevo.pkl", "wb") as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

dicc=dict()
p1=Jose(1,2)
p1.arch()

p2=Jose(3,4)
p3=Jose(5,6)
with open("C:/Users/Jose/OneDrive/Documentos/ITBA/Estructura de datos y programación/TP BALNEARIO/Tp_Estructura_Datos/nuevo.pkl", "rb") as f:
    persona=pickle.load(f)
print(persona)
print(persona.diccio)
# dicc["joses"]=[]
# dicc["joses"].append(p1)
# dicc["joses"].append(p2)
# dicc["joses"].append(p3)

# with open("C:/Users/Jose/OneDrive/Documentos/ITBA/Estructura de datos y programación/TP BALNEARIO/Tp_Estructura_Datos/diccioarchi.pkl", "wb") as f:
#     pickle.dump(dicc, f, protocol=pickle.HIGHEST_PROTOCOL)

# with open("C:/Users/Jose/OneDrive/Documentos/ITBA/Estructura de datos y programación/TP BALNEARIO/Tp_Estructura_Datos/diccioarchi.pkl", "rb") as f:
#     reading=pickle.load(f)

# print(reading["joses"][0])
# for i in reading.keys():
#     print(reading[i])

