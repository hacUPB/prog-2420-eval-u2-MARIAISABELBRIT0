import time 
def main():
    altitud= float(input("ingrese la altitud a la que se envuentre el satilite: "))
    coef_arrastre= float (input("ingrese el coeficiente de arrastre del satelite: ")) 
    min_alt= float(input("ingrese la altitud minima de seguridad: "))
    perdida_altitud= 0
    orbitas =0
    if coef_arrastre < 0.00001:
        print("satelite estable")
    while altitud>min_alt and coef_arrastre>0:
        perdida_altitud = altitud*coef_arrastre
        altitud= altitud - perdida_altitud
        orbitas = orbitas +1
        coef_arrastre = coef_arrastre + 0.00001
        print(f'en la orbita #{orbitas} la altitud del satelite es: {altitud}')
        time.sleep(0.25)
    
    if altitud<min_alt:
        print(f"se ha perdido conexion con satelite despues de {orbitas} orbitas")
    
    pass
 
if __name__=="__main__":
     main()