#--> validás contraseña y usuario:
    #la contra2wsx y usuario van a estar en un archivo csv que viene del balneario, 
    #pero nosotros se la damos al sistema desde antes,

#-- una vez validado, entrás y subís los archivos.
#ahí ofrecés agregar empleado cliente reserva carpas

#opciones del menú
from balneario import Balneario

bal=Balneario("para cargar archivos")
balneario=bal.leer_archivos("archivobalneario.pkl")  #acá cargo toda la info del balneario

us=input("Ingrese su código de empleado: ")
if balneario.validar_contraseña(us):
    print("Bienvenido al sistema del Balneario")

    comenzar=True
    while comenzar==True:
        #FALTA CHEQUEAR QUE LA CHOICE ESTÉ ENTRE LAS OPCIONES, CREAR FUNCIÓN PARA ESO
        choice=input("""¿Qué desea hacer?
                1- Ingresar un empleado nuevo
                2- Acciones con clientes
                Opción: """)
        if choice=="1":
            nombre=input("Ingrese el nombre del empleado: ")
            dni_ingreso=input("Ingrese el DNI del empleado: ")
            sex=input("Ingrese el sexo del empleado (M o F): ")
            balneario.cargar_empleado(nombre,dni_ingreso,sex)

        elif choice=="2":
            registrado=input("¿El cliente ya está registrado en el sistema?(s o n): ")
            
            #OPCIÓN DE: CLIENTE NO ESTÁ REGISTRADO --> LO REGISTRO
            if registrado.lower().strip()=="n":
                nom=input("Ingrese el nombre del cliente: ")
                dni_cliente=input("Ingrese el DNI del cliente: ")
                sexo_cliente=input("Ingrese el sexo del cliente (M o F): ")
                numero_cliente=input("Ingrese el número de teléfono del cliente (10 dígitos): ")
                tarjeta=input("Ingrese el número de tarjeta del cliente (16 dígitos): ")
                balneario.registrar_cliente(nom,dni_cliente,sexo_cliente.strip(),numero_cliente,tarjeta)

            #OPCIÓN DE: CLIENTE ESTÁ REGISTRADO --> LO VALIDO
            elif registrado.lower().strip()=="s":
                dni_buscado=input("Ingrese el DNI del cliente: ")
                if not(bal.validar_cliente(dni_buscado.strip())):
                    print("El cliente no se encuentra registrado, hágalo ingresando la opción en el menú.")

            #UNA VEZ QUE ENTRÉ CON EL CLIENTE, HAY QUE VER QUÉ QUIERE HACER CON ÉL
            #OFRECER OPCIONES PARA HACER O MODIFICAR RESERVAS

            #ELIGIÓ MAL ENTRE 1 Y 2, LO MANDA A TOMAR LA DECISIÓN
            else:
                print("La opción elegida no estaba entre las posibles.")
    
        #ACÁ VEMOS SI QUIERE CONTINUAR O NO HACIENDO ALGUNA OTRA COSA DESPUÉS DE HACER 
        #LO QUE PEDÍA, ESTO QUIZÁS DEBERÍA IR ADENTRO DE UN WHILE CON LAS OPCIONES PARA
        #EL CLIENTE UNA VEZ DENTRO DEL SISTEMA DEL BALNEARIO
        decision=input("¿Desea continuar? (presione ENTER para salir, y cualquier otra tecla para continuar): ")
        if decision=="":
            break

#UNA VEZ QUE NO QUIERE HACER NADA MÁS, SALE DEL PROGRAMA
print("Ha salido del programa.")



