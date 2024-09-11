import random
from random import randint
def main ():
    distancia = 0 
    precio = 0
    
    # datos del usuario 

    usuario= input("ingrese su nombre completo: ")
    titulo= input ("ingrese su titulo (Sr.) o (Sra.): ")
    if titulo not in ["Sr.", "Sra."]:
        print("titulo no valido. Ingrese una de las opciones indicadas")
    elif titulo == ("Sr."):
        print (f"{titulo} {usuario} bienvenido a fast airlines.")
    elif titulo == ("Sra."):
        print (f"{titulo} {usuario} bienvenida a fast airlines.")
    
    # viaje, origen y destino  

    origen = input (input("donde sera el inicio de su vuelo: \nMedellin(1)\nBogota(2)\nCartagena(3)"))
    if origen not in range (1,3):
        print ("seleccione una ciudad entre las opciones disponibles")
    destino = input(input("ingrese su destino: \nMedellin(1)\nBogota(2)\nCartagena(3)"))
    if destino not in range (1,3):
        print ("ingrese un destino dentro de las opciones disponibles") 
    elif origen ==1 and destino == 2:
        distancia== 240
    elif origen==2 and destino ==1:
        distancia ==240
    elif origen == 1 and destino == 3:
        distancia == 461
    elif origen == 3 and destino == 1: 
        distancia == 461
    elif origen == 2 and destino == 3:
        distancia == 657
    elif origen == 3 and destino == 2:
        distancia == 657
    else :
        print ("viaje no disponible.")
        
    # fecha del viaje 

    dia_sem= input(input("ingrese el dia de la semana del viaje: \nlunes(1)\nmartes(2)\nmiercoles(3)\njuenes(4)\nviernes(5)\nsabado(6)\ndomingo(7)"))
    dia_num= input (input("ingrese el numero del dia del mes del viaje: "))
    mes= input(input("ingrese el mes del viaje: "))
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
    asiento = input("ingrese el puesto en el que desea que su silla este ubicada: \nA: ventana(1)\nB: pasillo(2)\nC: sin preferencia(3)")
    fila = randint(1,29)
    # su vuelo 
    print(f"{titulo} {usuario} su vuelo sera el {dia_sem} {dia_num} de {mes} su silla sera {fila} {asiento} y tengra un valor de $ {precio}")

    pass
if __name__=="__main__":
    main()