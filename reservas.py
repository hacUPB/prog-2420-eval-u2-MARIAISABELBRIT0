import random
from random import randint
import datetime
def main ():
    distancia = 0 
    precio = 0
    
    # datos del usuario 

    usuario= input("ingrese su nombre completo: ")
    titulo= input ("ingrese su titulo (Sr) o (Sra): ")

    while titulo not in ["Sr", "Sra"]:
        print("titulo no valido. Ingrese una de las opciones indicadas")
        titulo= input ("ingrese su titulo (Sr) o (Sra): ")
   
    if titulo == "Sr":
        print (f"{titulo} {usuario} bienvenido a fast airlines.")
    elif titulo == "Sra":
        print (f"{titulo} {usuario} bienvenida a fast airlines.")
    
    # viaje, origen y destino  
    
    origen = str(input("donde sera el inicio de su vuelo: "))
    while origen not in ["medellin", "bogota", "cartagena"]:
        print ("seleccione una ciudad entre las opciones disponibles")
        origen = str(input("donde sera el inicio de su vuelo: "))
                     
    destino = str(input("ingrese su destino: "))
    while destino not in ["medellin", "bogota", "cartagena"]:
        print ("ingrese un destino dentro de las opciones disponibles")
        destino = str(input("ingrese su destino: ")) 
   
    if (origen =="medellin" and destino == "bogota") or ( origen=="bogota" and destino =="medellin"): 
        distancia= 240

    elif (origen =="cartagena" and destino == "medellin") or ( origen=="medellin" and destino =="cartagena"):
        distancia = 461

    elif (origen =="cartagena" and destino == "bogota") or ( origen=="bogota" and destino =="cartagena"):
        distancia= 657

    while destino == origen:
        print ("viaje no disponible.")
        origen = str(input("donde sera el inicio de su vuelo: "))
        destino = str(input("ingrese su destino: "))
        
    # fecha del viaje 
    
    fecha= input("ingrese la fecha del viaje en formato dd/mm/aaaa: ")
    fecha_sis =datetime.datetime.strptime(fecha,"%d/%m/%Y")
    print(fecha_sis)
    
    dia_sem= fecha_sis.weekday()
    print(dia_sem)

    if distancia < 400:
        if dia_sem < 5: 
            precio= 79900
        elif dia_sem > 4:
            precio= 119900

    elif distancia > 399:
        if dia_sem < 5:
            precio= 156900
        elif dia_sem > 4:
            precio = 213000
            
    # asignacion de asiento 
    
    asiento=(input("ingrese el puesto en el que desea que su silla este ubicada A(para ventana), B(para el pasillo), C(si no tine preferencia)): "))
    while asiento not in ["A","B","C"]:
        print("selecione una de las categoria de asiento asiento disponible (A,B,C) ")
        asiento=(input("ingrese el puesto en el que desea que su silla este ubicada A(para ventana), B(para el pasillo), C(si no tine preferencia)): "))
    fila = randint(1,29)
    
    # su vuelo 

    print(f"{titulo} {usuario} su vuelo sera en la fecha {fecha} su silla sera {fila} {asiento} y tengra un valor de $ {precio}")

    pass
if __name__=="__main__":
    main()