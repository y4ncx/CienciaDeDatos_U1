# EJERCICIO 17. --
def clasificar_nota(nota):
    if nota >= 90:
        return "A — Excelente"
    elif nota >= 75:
        return "B — Bueno"
    elif nota >= 60:
        return "C — Aprobado"
    else:
        return "D — Reprobado"

nota = int(input("Ingresa la nota (0-100): "))
print(clasificar_nota(nota))