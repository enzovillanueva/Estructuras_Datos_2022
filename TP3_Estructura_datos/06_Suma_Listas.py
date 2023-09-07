
def suma_iterativa(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]

    return suma


def suma_recursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_recursiva(lista[1:])


lista = list(range(1, 11))
print(suma_recursiva(lista))
