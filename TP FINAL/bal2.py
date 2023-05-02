from carpasomb import Sombrilla
from carpasomb import Carpa
from reserva import Reserva
from empleado import Empleado
from persona import Persona
from cliente import Cliente
import datetime
import pickle
import csv

#PARA ARRANCAR EL PROGRAMA Y PODER PROBARLO, ABRIR EL ARCHIVO USUARIOS CSV (AHÍ ESTÁN ANOTADAS LAS CONTRASEÑAS Y LOS CÓDIGOS DE EMPLEADOS)

def chequear_flotante(numero_en_str):
    try:
        float(numero_en_str)
    except ValueError:
        return False
    else:
        return True

class Balneario():
    def __init__(self, nombre):         
        self.nombre=nombre
        self.dicemp=dict()
        self.dicclientes=dict()
        self.dicusuarios=dict()
        self.reservas_vigentes=dict()
        self.m_carpas=[[Carpa() for i in range(6)] for i in range(4)]
        self.m_sombrillas=[[Sombrilla() for i in range(5)] for i in range(3)]

#imprimo el nombre del Sistema de asignación de reservas
    def __str__(self) -> str:
        return "Bienvenido a {}".format(self.nombre)

#busca info en un pickle, lo carga
    def leer_archivos(self,path):
        try:
            with open(path, "rb") as f:
                infobal=pickle.load(f)
            return infobal
        except FileNotFoundError as e:
            print("Error! El archivo no se encontró.")

#hace persistir info del balneario en un pickle
    def cargar_archivos(self):
        try:
            with open("archivobalneario.pkl", "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        except FileNotFoundError:
            print("Error! El arcvhivo no se encontró.")

#carga y crea al emp (corrobora que no esté registrado ya) #LEVANTA ERROR SI NO ESTÁ REGISTRADO
    def cargar_empleado(self, nom_cargado, dni_cargado, sexo_cargado):
        if int(dni_cargado) not in self.dicemp.keys():    
            emp=Empleado(nom_cargado, dni_cargado, sexo_cargado)
            self.dicemp[int(dni_cargado)]=emp
            self.dicusuarios[emp.codemp]=emp.contra
        else:
            raise ValueError("Ese empleado ya fue cargado.")

#crea y registra al cliente
    def registrar_cliente(self, nombre_pedido, dni_pedido, sexo_pedido, numtel, numtarjeta):
        try:
            if (dni_pedido.isdigit()):
                if int(dni_pedido) not in self.dicclientes.keys():
                    cl=Cliente(nombre_pedido,dni_pedido,sexo_pedido,numtel, numtarjeta)
                    self.dicclientes[int(dni_pedido)]=cl
                    return True
                else:
                    raise ValueError("Ese cliente ya se encuentra registrado.")
            else:
                raise ValueError("El DNI ingresado no cumple con el formato requerido.")
        except ValueError as e:
            print("Error !", e, "El cliente no fue registrado.")
            return False

#busca el dni del cliente    
    def validar_cliente(self, dni_cliente):
        buscar_dni=lambda dni:True if dni in self.dicclientes.keys() else False
        return buscar_dni(int(dni_cliente))

#pidey verifica la contraseña del emp
    def validar_contraseña(self, codemp_ingresado):
        if codemp_ingresado in self.dicusuarios.keys():
            contra=input("Ingrese su contraseña: ")
            while self.dicusuarios[codemp_ingresado]!=contra and contra!="0":
                contra=input("Contraseña incorrecta.Vuelva a intentar (o presione 0 para salir): ")
            if contra=="0":
                return False
            else:
                return True
        else:
            print("Ese empleado no está registrado en el sistema.")
            return False

#carga un archivo csv de contraseñas para poder leerlo nosotros y tenerlo de backup
    def crear_backup_contraseñas(self):
        try:
            with open('usuarios.csv', 'w', newline='') as csvfile:
                fieldnames = ['usuario', 'contraseña']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for empleado in self.dicemp.keys():
                    writer.writerow({'usuario': self.dicemp[empleado].codemp, 'contraseña': self.dicemp[empleado].contra})
        except FileNotFoundError:
            print("Error! No se pudo abrir el archivo.")

#acción repetitiva --> busca matriz
    def matrizdetrabajo(self,tipo_reserva):
        if tipo_reserva.lower()=="s" or tipo_reserva.lower()=="c":
            matriz_correcta=lambda x: self.m_carpas if x=="C" else self.m_sombrillas
            return matriz_correcta(tipo_reserva.upper().strip())
        else:
            raise ValueError("Tipo de reserva inválido.")
 
#visualiza la matriz (0 y días restantes)
    def ver_matriz(self, tipo_reserva):
        matriz=self.matrizdetrabajo(tipo_reserva)
        for fila in range(len(matriz)):
            lista=[]
            for columna in range(len(matriz[fila])):
                reser=matriz[fila][columna]
                if reser.estado==None:
                    lista.append("D")
                else:
                    lista.append((reser.estado.vencimiento-datetime.datetime.now()).days)
            print(lista)

#busca lugar en la matriz disponible (asignacion automática o por fila)
    def buscar_posicion_disponible(self, matriz, metodo_busqueda, num_fila=None):
            disponible=None
            if metodo_busqueda.lower()=="f":
                if num_fila!=None and str(num_fila).isdigit():
                    if int(num_fila)>0 and int(num_fila)<=len(matriz):
                        fila=int(num_fila)-1
                        for columna in range(len(matriz[fila])):
                            if matriz[fila][columna].estado==None:
                                return fila,columna
                    else:
                        raise ValueError("La fila pedida no es ubicable en la matriz.")
                else:
                    raise ValueError("No se recibió número de fila o no se recibió en el formato correcto.")
            
            elif metodo_busqueda.lower()=="a":
                for fila in range(len(matriz)):
                    for columna in range(len(matriz[fila])):
                        carpasomb=matriz[fila][columna] 
                        if carpasomb.estado==None:
                            return fila,columna
            else:
                raise ValueError("El método de búsqueda ingresado no es válido.")
            return disponible

#este precio despues se lo pasamos a la reserva que creemos
    def calcular_precio(self,reserva, precioxdia):
        if chequear_flotante(precioxdia):
            precio=reserva.estadia*float(precioxdia)
            return precio
        else:
            raise ValueError("El precio ingresado no cumple con el formato requerido.")

#le pasás el precio, el dni, el número de días, la fila que eligió(si eligió), y hace la reserva     
    def asignar_reserva(self,tipo_reserva,metodo, dias, dni_cliente,cotizacion_dia,fila_elegida=None):
        if str(dni_cliente).isdigit():
            if dni_cliente not in self.reservas_vigentes.keys():
                matriz=self.matrizdetrabajo(tipo_reserva)
                fila,columna=self.buscar_posicion_disponible(matriz,metodo,fila_elegida)
                num_reserva=str(fila)+str(columna)+str(dni_cliente)
                reser=Reserva(num_reserva,dias,tipo_reserva,self.dicclientes[int(dni_cliente)])
                print("El número de reserva asignado es: ", num_reserva)
                try:
                    preciototal=self.calcular_precio(reser,cotizacion_dia)
                except ValueError as e:
                    print("Error!", e)
                print("El precio de su estadía es: $", preciototal)
                matriz[fila][columna].estado=reser
                reser.precio=preciototal
                self.dicclientes[dni_cliente].deuda=preciototal
                print("Fecha de finalización de la reserva (puede modificarse): ", reser.vencimiento)   
                self.reservas_vigentes[reser.cliente.dni]=reser
                return reser
            else:
                raise ValueError("El cliente ya tiene una reserva a su nombre, puede extender su vencimiento con un recargo o reservar nuevamente al finalizar su estadía.")
        else:
            raise ValueError("El DNI ingresado no es válido.")

#viene el cliente y pide modificar su tiempo de estadia
    def modificar_estadia(self,dias_agregados, dni_cliente, precio_actual):
        if dni_cliente in self.reservas_vigentes.keys():
            reserva_modificada=self.reservas_vigentes[dni_cliente]
            reserva_modificada.estadia+=int(dias_agregados)
            reserva_modificada.vencimiento+=datetime.timedelta(days=int(dias_agregados))
            print("El nuevo vencimiento de su estadía es: {}".format(reserva_modificada.vencimiento))
            precioextra=float(precio_actual)*float(dias_agregados)
            reserva_modificada.precio+=precioextra
            self.dicclientes[dni_cliente].deuda+=precioextra
            print("Los días agregados se cobrarán al precio actual por día, el precio agregado es {}$, y la deuda actual del cliente es de {}$".format(precioextra, self.dicclientes[dni_cliente].deuda))
        else:
            raise ValueError("Ese cliente no tiene una reserva vigente a su nombre para modificar.")

#con esta función, antes de cerrar el programa revisamos las matrices para ver si están vencidas, si hay algo vencido lo sacamos y ponemos None
    def revisar_matriz(self,tipo):
       matriz=self.matrizdetrabajo(tipo)
       for fila in range(len(matriz)):
           for columna in range(len(matriz[fila])):
               carpasomb=matriz[fila][columna] 
               if carpasomb.estado!=None:
                    if carpasomb.estado.vencimiento==datetime.datetime.now(): #ya está vencida
                        dnicliente=carpasomb.estado.cliente.dni
                        carpasomb.estado==None
                        self.reservas_vigentes.pop(dnicliente)

#le saca toda o parte de la deuda al cliente
    def cobrar(self, dni_cliente, monto_abonado):
        if int(dni_cliente) in self.dicclientes.keys():
            if self.dicclientes[int((dni_cliente))].deuda!=0:
                if chequear_flotante(monto_abonado):
                    if float(monto_abonado)>0 and float(monto_abonado)<=self.dicclientes[int(dni_cliente)].deuda:
                        self.dicclientes[int(dni_cliente)].deuda-=float(monto_abonado)
                        print("Ahora, la deuda restante es de: {}$".format(self.dicclientes[int(dni_cliente)].deuda))
                    else:
                        raise ValueError("El monto ingresado no es válido.")
                else:
                    raise ValueError("El monto ingresado no cumple con el formato requerido.")
            else:
                raise ValueError("El cliente no tiene una deuda que saldar.")
        else:
            raise KeyError("El cliente no se encuentra registrado.")            

#elimina al empleado que se pida desde el menú (el DNI que llega es un string)
    def eliminar_empleado(self,dni_recibido):
        if dni_recibido.isdigit():
            if int(dni_recibido) in self.dicemp.keys():
                emp_eliminado=self.dicemp.pop(int(dni_recibido))
                return emp_eliminado
            else:
                raise ValueError("El DNI ingresado no se encuentra registrado.")
        else:
            raise ValueError("El DNI ingresado no cumple con el formato requerido.")

#le pasás el tipo de dato que querés cambiar (números asociados a las opciones en el menú) y el valor cargado
#corrobora la info que le llega, si lo cambia devuelve true y si no lo cambia False
    def modificar_datos_cliente(self,dni_cliente,nuevo_dato,tipo_dato):
        if int(dni_cliente) in self.dicclientes.keys():
            if tipo_dato=="1":
                self.dicclientes[int(dni_cliente)].nombre=nuevo_dato
                carga=True
            elif tipo_dato=="2":
                if nuevo_dato.lower().strip() not in ["f","m"]:
                    carga=False
                    raise ValueError("El sexo ingresado no es válido.")
                self.dicclientes[int(dni_cliente)].sexo=nuevo_dato
                carga=True
            elif tipo_dato=="3":
                if not(nuevo_dato.isdigit()) or len(nuevo_dato)!=10:
                    carga=False
                    raise ValueError("El número de teléfono ingresado no cumple con los requerimientos")
                self.dicclientes[int(dni_cliente)].tel=nuevo_dato
                carga=True
            elif tipo_dato=="4":
                if not(nuevo_dato.isdigit()) or len(nuevo_dato)!=16:
                    carga=False
                    raise ValueError("El número de tarjeta no cumple con el formato requerido.")
                self.dicclientes[int(dni_cliente)].num_tarjeta=nuevo_dato
                carga=True
            else:
                raise ValueError("La opción ingresada no es válida.")
            return carga
        else:
            raise ValueError("Ese cliente no se encuentra registrado.")

#para cambiar la contraseña del empleado
    def cambiar_contraseña(self, dni_empleado):
        if int(dni_empleado) not in self.dicemp.keys():
            raise ValueError("El empleado no se encuentra registrado.")
        else:
            contraseña_antigua=input("Ingresar la contraseña anterior: ")
            if self.dicemp[int(dni_empleado)].contra==contraseña_antigua:
                contraseña_nueva=input("Ingresar la nueva contraseña (5 caracteres mínimo): ")
                while len(contraseña_nueva)<5:
                    contraseña_nueva=input("Contraseña inválida, vuelva a ingresarla (5 caracteres mínimo): ")
                print("La nueva contraseña es: ", contraseña_nueva)
                self.dicemp[int(dni_empleado)].contra=contraseña_nueva
                self.dicusuarios[self.dicemp[int(dni_empleado)].codemp]=contraseña_nueva
            else:
                raise ValueError("La contraseña ingresada no coincide con la contraseña actual del empleado. No podrá modificarse.")
                
       

if __name__=="__main__":
    balneario=Balneario("Balneario Carilo")

    #balneario=bal.leer_archivos("archivobalneario.pkl")
    #balneario.crear_backup_contraseñas()
    #balneario.registrar_cliente("Juan Quiroga", "22222222","m","1138338366","1231231231231231")
    balneario.cargar_empleado("Josefina Marta", "22278723", "F")
    for i in balneario.dicemp.keys():
        print(balneario.dicemp[i])
    print("El empleado eliminado es:",balneario.eliminar_empleado("22278723"))
    for i in balneario.dicemp.keys():
        print(balneario.dicemp[i])
    #balneario.cargar_archivos()
    #balneario.crear_backup_contraseñas()
    # for i in balneario.dicclientes.keys():
    #     print(i)
    #     print(type(i))
    #     print(balneario.dicclientes[i])
    # try:
    #    reserva=balneario.asignar_reserva("s",112,3,balneario.dicclientes[22222222])
    # except ValueError as e:
    #    print("Error!", e)

#funciones para ver matrices andan bien !!
    #balneario.ver_matriz("s")
    #balneario.ver_matriz("c")
    
    #print(reserva.vencimiento==datetime.datetime.now())
    # try:
    #     balneario.asignar_reserva("s", "f",8, 22222222,"0")

    #     balneario.ver_matriz("s")
    # except ValueError as e:
    #     print("Error!", e)

