cadena = str(input("Ingresa un mensaje: "))
lista = list(cadena)
longitud = 0
contador = 0
minusculas=['b','c','d','f','g','h','j','k','m','n','p','q','r','s','t','v','w','x','y','z']  
mayusculas=['B','C','D','F','G','H','J','K','M','N','P','Q','R','S','T','V','W','X','Y','Z']
for i in range(len(cadena)):
    for i in minusculas:
        if lista[longitud] == i:
            contador += 1  
    for i in mayusculas:
        if lista[longitud] == i:
            contador += 1  
    longitud +=1
print("Las consonantes usadas fueron: ",contador)