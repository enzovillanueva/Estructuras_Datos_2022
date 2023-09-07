
def es_palindromo(nombre: str) -> str:
    nombre = nombre.replace(" ","")
    return nombre[::-1].lower() == nombre.lower()

print(es_palindromo("a ia"))