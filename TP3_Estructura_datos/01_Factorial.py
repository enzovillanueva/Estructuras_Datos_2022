
def factorial_iterativa(numero):
    suma = 1

    while numero > 0:
        suma = suma * numero
        numero -= 1

    return suma


def factorial_recursiva(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial_recursiva(numero-1)


def exponente(numero, exp):
    if exp == 0:
        return 1

    return numero * exponente(numero, exp-1)


def digitos_inverse(numero):
    def invertir(number, resultado):
        if number == 0:
            return resultado

        return invertir(number//10, (resultado*10) + number % 10)

    return invertir(numero, 0)


print(digitos_inverse(123456789))
