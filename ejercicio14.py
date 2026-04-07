def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

numero = int(input("Ingresa un número: "))
print(es_par_o_impar(numero))