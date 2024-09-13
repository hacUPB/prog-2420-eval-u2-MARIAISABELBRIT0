from os import system

control = True   #variable de control del bucle inicial

while control == True:
    print("1.calcular primo\n2. factor\n3. salir") #\n es nueva linea
    opcion = int(input("ingrese el numero a probar: "))
    if opcion == 1:
        system("cls")
        print ("calcular el numero primo")
        numero = int(input("ingrese el numero a probar: "))
        cont = 0
        for dividir in range (1,numero +1):
            if (numero % dividir) == 0:
                cont +=1
        if cont > 2:
            print(f"{numero} no es primo")
        else:
             print(f"{numero} es primo") 
    elif opcion == 2:
        system("cls")
        print ("calcular el factorial")
        numero = int(input("ingrese el numero a probar: "))
        fact = 1 
        for i in range(1,numero+1): # este bucle calcula el factorial
            fact *= i               #fact = fact * i
        print(f"{numero}! = {fact}")
    elif opcion == 3: #opccion salir 
        control = False
  
    else:
        print("opcion no valida")