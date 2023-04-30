from bal2 import *
import pickle
import matplotlib.pyplot as plt


def recorrer_diccionario(diccionario):
    for key in diccionario.keys():
        print(diccionario[key])

try:
    with open("archivobalneario.pkl", "rb") as f:
        balneario=pickle.load(f)
except FileNotFoundError:
        balneario=Balneario("Carpas y sombrillas")
        balneario.cargar_empleado("Mauro Díaz", "21333333", "M")

us=input("Ingrese su código de empleado: ")
validar= balneario.validar_contraseña(us)

while validar==False:
    decision=input("Desea ingresar otro usuario? (presione cualquier tecla, si no, ENTER para salir): ")
    if decision !="":
        us=input("Ingrese su código de empleado: ")
        validar=balneario.validar_contraseña(us)
    else:
        validar=""
  
if validar==True:
    print("Bienvenido al sistema de reservas del Balneario")
    cotizacioncarpa=input("Antes de comenzar, ingrese la cotización de hoy para el precio por día de las carpas: ")
    while not(chequear_flotante(cotizacioncarpa)):
        cotizacioncarpa=input("Formato inválido, ingrése el valor nuevamente: ")
    cotizacionsombrilla=input("Ingrese la cotización de hoy para el precio por día de las sombrillas:")
    while not(chequear_flotante(cotizacionsombrilla)):
        cotizacionsombrilla=input("Formato inválido, ingrése el valor nuevamente: ")

    cotizacionsombrilla=float(cotizacionsombrilla)
    cotizacioncarpa=float(cotizacioncarpa)

    comenzar=True
    while comenzar==True:
        choice=input("""¿Qué desea hacer?
                1- Ingresar un empleado nuevo
                2- Acciones con clientes
                3- Visualizar clientes
                4- Visualizar empleados
                5- Visualizar disponibilidad de sombrillas
                6-Visualizar disponibilidad de carpas
                7-Ver clientes adeudados
                8-Salir: """)

        if choice=="8":
            break
        elif choice=="1":
            nombre=input("Ingrese el nombre del empleado: ")
            dni_ingreso=input("Ingrese el DNI del empleado: ")
            sex=input("Ingrese el sexo del empleado (M o F): ")
            try:
                registro=balneario.cargar_empleado(nombre,dni_ingreso,sex)
            except ValueError as e:
                print("Error!", e)

        elif choice=="2":
            registrado=input("¿El cliente ya está registrado en el sistema?(s o n): ")
            
            #OPCIÓN DE: CLIENTE NO ESTÁ REGISTRADO --> LO REGISTRO
            if registrado.lower().strip()=="n":
                print("Registre al cliente:\n")
                nom=input("Ingrese el nombre del cliente: ")
                dni_cliente=input("Ingrese el DNI del cliente: ")
                sexo_cliente=input("Ingrese el sexo del cliente (M o F): ")
                numero_cliente=input("Ingrese el número de teléfono del cliente (10 dígitos): ")
                tarjeta=input("Ingrese el número de tarjeta del cliente (16 dígitos): ")
                factor=balneario.registrar_cliente(nom,dni_cliente,sexo_cliente.strip(),numero_cliente,tarjeta)
                seguir=lambda x: True if factor==True else False
                continuar=seguir(factor)
                if continuar!=False:
                    dni_trabajado=int(dni_cliente)

            #OPCIÓN DE: CLIENTE ESTÁ REGISTRADO --> LO VALIDO
            elif registrado.lower().strip()=="s":
                dni_cliente=input("Ingrese el DNI del cliente: ")
                if dni_cliente.isdigit():
                    if balneario.validar_cliente(dni_cliente.strip()):
                        continuar=True
                        dni_trabajado=int(dni_cliente)
                    else:
                        continuar=False
                        print("El cliente no se encuentra registrado, hágalo ingresando la opción en el menú.")
                else:
                    continuar=False
                    print("El DNI ingresado no tiene un formato correcto.")

            else:
                continuar=False
                print("La opción elegida no estaba entre las posibles.")

            if continuar==True:
                    print(balneario.dicclientes[dni_trabajado])
                    comenzar2=True
                    while comenzar2==True:
                        choice2=input("""Qué quiere hacer con su cliente?
                        1-Asignar reserva
                        2-Modificar estadía
                        3-Cobrar
                        4-Salir
                        Opción: """)

<<<<<<< HEAD
                        if choice2=="1":
                            tipo_reserva=input("Qué va a reservar? (Sombrilla: s, Carpa: c): ")
                            if tipo_reserva.lower()=="s" or tipo_reserva.lower()=="c":
                                print("Actualmente, estas son las opciones (los números representan los días por los cuales permanecerá ocupada, los 0 representan disponibilidad): ")
                                balneario.ver_matriz(tipo_reserva)
                                metodo_eleccion=input("Desea elegir una fila? O prefiere una asignación automática de lugar? (Fila: F, Automático: A): ")
                                if metodo_eleccion.lower().strip()!="f" and metodo_eleccion.lower().strip()!="a":
                                    print("El método elegido no es válido.")
                                else:
                                    if metodo_eleccion.lower()=="f":
                                        fila_requerida=input("Elija la fila que desea: ")
                                    else:
                                        fila_requerida=None
                                    dias=input("Ingrese la cantidad de días de hospedaje: ")
                                    if dias.isdigit():
                                        try:
                                            precio_dia=lambda tipo_reserva:cotizacioncarpa if tipo_reserva.lower().strip()=="c" else cotizacionsombrilla
                                            precio=precio_dia(tipo_reserva)
                                            reserva_realizada=balneario.asignar_reserva(tipo_reserva,metodo_eleccion,int(dias), int(dni_trabajado),precio,fila_requerida)
                                            balneario.ver_matriz(tipo_reserva)
                                        except ValueError as e:
                                            print("Error!", e)
                                    else:
                                        print("El formato de los días ingresados no es correcto, deberá volver a comenzar la operación.")
                            else:
                                print("La opción ingresada no es válida.")

                        elif choice2=="2":
                            try:
                                d_extra=input("Ingrese días que se desea agregar a la estadía: ")
                                if d_extra.isdigit():
                                    try:
                                        if dni_trabajado in balneario.reservas_vigentes.keys():
                                            tipo=balneario.reservas_vigentes[dni_trabajado].tipo_reserva
                                            precio=precio_dia(tipo)
                                            print(precio)
                                            balneario.modificar_estadia(d_extra,dni_trabajado, precio)
                                        else:
                                            print("Ese cliente no tiene una reserva vigente a su nombre para modificar.")

                                    except ValueError as e:
                                        print("Error!!", e)
                                else:
                                    raise ValueError("El número de días ingresado no cumple con el formato válido.La modificación no puede ser llevada a cabo.")
                            except ValueError as e:
                                print("Error!", e)
                        
                        elif choice2=="3":
                            try:
                                print("La deuda actual del cliente es de ${}".format(balneario.dicclientes[dni_trabajado].deuda))
                                monto_abonado=input("¿Cuánto abonará el cliente? ")
                                balneario.cobrar(dni_trabajado, monto_abonado)
                            except ValueError as e:
                                print("Error!", e)
                            except KeyError as e:
                                print("Error!", e)
                        elif choice2=="4":
                            break
                        
                        else:
                            print("La elección no era una opción.")
        
                        finalización=input("Desea hacer algo más con este cliente? (ENTER para salir, cualquier tecla para continuar): ")
                        if finalización=="":
                            break

        elif choice=="3":
            recorrer_diccionario(balneario.dicclientes)
                        
        elif choice=="4":
            recorrer_diccionario(balneario.dicemp)

        elif choice=="5":
            balneario.ver_matriz("s")
                        
        elif choice=="6":
            balneario.ver_matriz("c")
                        
        elif choice=="7":
            print("Los DNI de los clientes deudores son los siguientes: \n")
            for cliente in balneario.dicclientes.keys():
                if balneario.dicclientes[cliente].deuda!=0:
                    print(cliente)
                                
        decision=input("¿Desea continuar? (presione ENTER para salir, y cualquier otra tecla para continuar): ")
        if decision=="":
=======
                    finalización=input("Desea hacer algo más con este cliente? (ENTER para continuar, cualquier tecla para salir): ")
                    if finalización!="":
                        break
        #ACÁ VEMOS SI QUIERE CONTINUAR O NO HACIENDO ALGUNA OTRA COSA DESPUÉS DE HACER 
        #LO QUE PEDÍA, ESTO QUIZÁS DEBERÍA IR ADENTRO DE UN WHILE CON LAS OPCIONES PARA
        #EL CLIENTE UNA VEZ DENTRO DEL SISTEMA DEL BALNEARIO
        decision=input("¿Desea continuar? (presione ENTER para continuar, y cualquier otra tecla para salir): ")
        if decision!="":
>>>>>>> a823c47b2c8181ca8ecd1d6a3d67c73a504fa0ec
            break

balneario.revisar_matriz("c")
balneario.revisar_matriz("s")
balneario.cargar_archivos()
balneario.crear_backup_contraseñas()
print("Ha salido del programa.")



