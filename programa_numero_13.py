cadena = str(input("Ingrese texto: "))
lista = list(cadena)
lista.pop(0)
print("Resultado: ", end="")
for i in lista:
    print(i, end="")