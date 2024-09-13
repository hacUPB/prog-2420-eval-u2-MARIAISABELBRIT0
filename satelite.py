import time 

def main():
    altitud= float(input("ingrese la altitud a la que se envuentre el satilite (en km): "))
    coef_arrastre= float (input("ingrese el coeficiente de arrastre incial del satelite: ")) 
    min_alt= float(input("ingrese la altitud minima de seguridad (en km): "))
    orbitas =0

    while altitud > min_alt:
        perdida_altitud= altitud*coef_arrastre
        if perdida_altitud < 0.02:
            print("el satélite alcanza la altitud mínima de seguridad o se estabiliza")
        else:
            altitud = altitud - perdida_altitud
            coef_arrastre += 0.00001
            orbitas += 1
            print(f"Órbita: {orbitas} Altitud actual = {altitud} km, Coeficiente de arrastre = {coef_arrastre}")
    print(f"numero total de orbitas: {orbitas}")

    pass

if __name__=="__main__":
     main()