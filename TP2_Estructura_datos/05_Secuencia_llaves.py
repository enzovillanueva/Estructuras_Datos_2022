

def secuencia_balanceada(secuencia: str) -> bool:
    pila = []
    parentesis = {'{': '}', '(': ')', '[': ']'}

    for i in secuencia:
        if i in parentesis:
            pila.append(i)
        elif len(pila) == 0 or i != parentesis[pila.pop()]:
            return False
    
    return True

print(secuencia_balanceada('[({)}]'))
