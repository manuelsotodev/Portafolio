numeros = []
primos = []
for x in range(10):
    ingreso = int(input("Ingrese numero: "))
    numeros.append(ingreso)
for i in range(10):
    divisor = 1
    divisores = 0
    while divisor <= numeros[i]:
        if numeros[i] % divisor == 0:
            divisores += 1
        divisor += 1
    if divisores == 2:
        primos.append(numeros[i])
if len(primos) == 0:
    print("No hay numeros primos ingresados :(")
else:
    print("Los siguientes numeros ingresados, son primos:")
    print(primos)