# Solicitar al usuario que ingrese 10 números


# numeros = []
# for i in range(10):
#     numero = float(input(F"Ingrese el número {i + 1}: "))
#     numeros.append(numero)

# # Calcular el promedio de la lista
# promedio = sum(numeros) / len(numeros)

# # Mostrar el resultado del promedio al usuario
# print(f"El promedio de los números ingresados es: {promedio}")



numeros = []
for i in range(10):
    numero = float(input("Ingrese el número {}: ".format(i + 1)))
    numeros.append(numero)

promedio = sum(numeros) / len(numeros)

print("El promedio de los números ingresados es: {}".format(promedio))

