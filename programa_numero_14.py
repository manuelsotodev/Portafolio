cadena = str(input("Ingrese texto: "))
lista = list(cadena)
lista.pop(0)
lista.pop(len(lista)-1)
print("Resultado: ")
for i in lista:
    print(i, end="")