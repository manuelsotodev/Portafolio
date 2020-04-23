import math

def media(num):
    suma = 0
    for i in num:
        suma += i
    resultado = suma / len(num)
    return resultado

def moda(num):
    frecuencia = 0                                                                         
    for i in num:                                                                              
        apariciones = num.count(i)                                                             
        if apariciones > frecuencia:                                                       
            frecuencia = apariciones                                                                                                                                              
    modas = []                                                                               
    for i in num:                                                                              
        apariciones = num.count(i)                                                             
        if apariciones == frecuencia and i not in modas:                                   
            modas.append(i) 
    return modas       

def desviacion(num):
    #Definimos el valor de la media en un inicio, para no llamar más de una vez su función
    med = media(num)
    suma = 0
    for i in num:
        suma += (i - med)**2
    resultado = math.sqrt(suma/len(num))
    return resultado
    
def muestra(num):
    #Definimos el valor de la media en un inicio, para no llamar más de una vez su función
    med = media(num)
    suma = 0
    for i in num:
        suma += (i - med)**2
    resultado = math.sqrt(suma/(len(num)-1))
    return resultado

evaluar = True
numeros = []
while evaluar:
    numeros.append(float(input("Ingrese un numero positivo, si desea parar ingrese 0: ")))
    if numeros[len(numeros)-1] == 0:
        numeros.pop(len(numeros)-1)
        evaluar = False
print("La media es: ",media(numeros))
if len(numeros) != len(moda(numeros)):
    print("La moda es: ",moda(numeros))
else:
    print("No hay moda")
print("La desviación estandar en poblacion es ",desviacion(numeros),"y en muestra es ",muestra(numeros))