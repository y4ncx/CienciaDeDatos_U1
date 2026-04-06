# EJERCICIO 18. --
# 'calificaciones' es una lista o arreglo.
calificaciones = [ 1.0, 4.2, 3.5, 2.8, 4.8 ]

# 'sum' = Suma total del arreglo.
# 'len' = Cantidad de valores en el arreglo.
promedio = sum(calificaciones) / len(calificaciones)

# Valida si el promedio del estudiante aprueba o no.
resultado = "Aprueba." if promedio >= 3.0 else "No aprueba."    


# -- Resultados Impresos --
print("--- 18. Lista de 5 calificaciones ---")
print("Calificaciones:", calificaciones)
print("Promedio:", promedio)
print("¿Aprueba?:", resultado)