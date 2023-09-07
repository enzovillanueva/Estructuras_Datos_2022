

def inverso():
    limite, lista = 0, []

    while limite != 5:
        number = int(input("Ingrese un numero: "))
        lista.append(number)
        limite +=1
    
    for i in range(len(lista)-1, -1, -1):
        print(lista[i])
    
    return

print()
