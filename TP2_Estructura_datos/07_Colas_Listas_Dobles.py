
from dataclasses import dataclass
from typing import Any

#Funciona!

class ColaDobleEnlaces:

    @dataclass
    class _Nodo:
        value : Any
        next : None
        prev : None
    
    def __init__(self, iterable=None):
        self._inicio = None
        self._ultimo = None
        if iterable is not None:
            for values in iterable:
                self.encolar(values)

    def encolar(self, value):       # O(1)
        if self._ultimo is None:
            self._inicio = self._Nodo(value, None, self._inicio)
            self._ultimo = self._inicio
        else: 
            self._ultimo.next = self._Nodo(value, None, self._ultimo)
            self._ultimo.prev = self._ultimo 
            self._ultimo = self._ultimo.next

    def desencolar(self):           #O(1)
        if self._inicio is None: 
            return None
        else: 
            aux = self._inicio 
            self._inicio = self._inicio.next
            del aux

    def ultimo(self):
        return self._ultimo.value

    def primero(self):
        return self._inicio.value

    def isEmply(self):
        return self._inicio is None

    def __iter__(self):
        return ColaDobleEnlaces.Iterator(self._inicio)

    def mostrar_lista(self):
        aux = self._inicio
        
        while aux != None:
            print(aux.value, end=" ")
            aux = aux.next

    class Iterator:
        def __init__(self, lista) -> None:
            self._inicio = lista

        def __iter__(self):
            return self

        def __next__(self):
            if self._inicio is None:
                raise StopIteration
            value = self._inicio.value
            self._inicio = self._inicio.next
            return value


if __name__ == '__main__':
    lista = ColaDobleEnlaces()
    lista.encolar(1)
    lista.encolar(2)
    lista.encolar(3)
    lista.encolar("Enzo")
    lista.desencolar()
    lista.mostrar_lista()
    print(lista.primero())

    for i in lista:
        print(i)