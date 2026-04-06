# EJERCICIO 20. --
# Pedir la edad al usuario.
edad = int(input("Ingresa tu edad: "))


# -- Resultados Impresos --
# Depende del numero suministrado, se tendrá una respuesta.
if edad < 0:
    print("- Edad invalida! -")
elif edad <= 12:
    print("Eres un niño.")
elif edad <= 17:
    print("Eres un joven.")
else:
    print("Eres un adulto.")

