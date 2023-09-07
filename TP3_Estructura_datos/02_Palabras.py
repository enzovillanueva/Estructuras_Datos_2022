
def reverse_string(string: str) -> str:  # Ej. 'enzo'
    if len(string) == 0:  # Si la cadena esta vacia, retorna el valor de 'string'
        return string
    else:
        return reverse_string(string[1:]) + string[0]
        # 1. nzo + e, 2.zo + n, 3.o + z, 4. o, 5. "", return


def palindromo_recursivo(string: str) -> bool:
    palabra = string.replace(" ", "").lower()
    cadena = len(palabra)-1

    if palabra[0] != palabra[cadena]:
        return False

    if len(string) < 2:
        return True

    return palindromo_recursivo(palabra[1:cadena])


print(palindromo_recursivo("Anita lava le tina"))
