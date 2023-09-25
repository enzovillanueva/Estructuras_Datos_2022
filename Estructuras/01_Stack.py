
from dataclasses import dataclass
from re import S
from typing import Any


class StackLinkedList:
    @dataclass
    class _Nodo:
        valor : Any
        next : None
    
    def __init__(self) -> None:
        self._inicio = None
        self._tope = None
        self._tamaño = 0
    
    def apilar(self, elemento): #O(1)
        nodo = StackLinkedList._Nodo(elemento, None)
        if self._inicio is None:
            self._inicio = nodo
            self._tope = self._inicio
        else:
            self._tope.next = nodo
            self._tope = nodo
        self._tamaño += 1

    def desapilar(self): #O(n)
        if self._inicio is not None:
            if self._inicio.next is None:
                self._inicio = None
                self._tope = None
            else:
                aux = self._inicio
                while aux.next.next is not None:
                    aux = aux.next
                
                aux.next = None
                self._tope = aux
            self._tamaño -= 1

    def tope(self) -> object:
        return self._tope

    def __eq__(self, __o: object) -> bool: #O(n)
        act1 = self._inicio
        act2 = __o._inicio
        while act1 != None and act2 != None:
            if act1.valor != act2.valor:
                return False
            act1 = act1.next
            act2 = act2.next
        return act1 == None and act2 == None

    def copy(self):
        new_copia = StackLinkedList()
        if not self.es_vacia():
            aux = self._inicio
            new_copia._inicio = StackLinkedList._Nodo(aux.valor, None)
            new_copia._tope = new_copia._inicio
            aux = aux.next
            while aux is not None:
                nodo = StackLinkedList._Nodo(aux.valor, None)
                new_copia._tope.next = nodo
                new_copia._tope = nodo
                aux = aux.next
        return new_copia

    def __len__(self) -> int:
        return self._tamaño
    
    def es_vacia(self) -> bool:
        return self._inicio is None

    def mostrar_lista(self):
        aux = self._inicio
        while aux is not None:
            print(aux.valor)
            aux = aux.next

class StackDoubleList:
    @dataclass
    class _Nodo:
        valor : Any
        next : None
        prev : None
    
    def __init__(self) -> None:
        self._inicio = None
        self._tope = None
        self._tamaño = 0
    
    def apilar(self, elemento): #O(1)
        nodo = StackDoubleList._Nodo(elemento, None, None)
        if self._inicio is None:
            self._inicio = nodo
            self._tope = self._inicio
        else:
            self._tope.next = nodo
            nodo.prev = self._tope
            self._tope = nodo

    def desapilar(self): #O(1)
        if self._inicio is not None:
            if self._inicio.next is None:
                self._inicio = None
                self._tope = None
            else:
                self._tope = self._tope.prev
                self._tope.next.prev = None
                self._tope.next = None
                
    def __len__(self):
        def contar(nodo):
            if nodo is None:
                return 0
            else:
                return 1 + contar(nodo.next)
        return contar(self._inicio)

    def mostrar_lista(self):
        aux = self._inicio
        while aux is not None:
            print(aux.valor)
            aux = aux.next

if __name__ == '__main__':
    p = StackLinkedList()
    p.apilar(1)
    p.apilar(2)
    p.apilar(3)
    p.apilar(4)
    p.apilar(5)
    p.desapilar()
    p.mostrar_lista()
