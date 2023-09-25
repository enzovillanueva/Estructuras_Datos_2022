
from dataclasses import dataclass
from typing import Any


class LinkedList:
    @dataclass
    class _Nodo:
        valor : Any
        next : None
    
    def __init__(self) -> None:
        self._inicio = None
    
    def agregar_inicio(self, elemento): #O(1)
        nodo = LinkedList._Nodo(elemento, None)
        if self._inicio is None:
            self._inicio = nodo
        else:
            nodo.next = self._inicio
            self._inicio = nodo

    def agregar_final(self, elemento):  #O(n)
        nodo = LinkedList._Nodo(elemento, None)
        if self._inicio is None:
            self._inicio = nodo
        else:
            aux = self._inicio
            while aux.next is not None:
                aux = aux.next
            aux.next = nodo

    def borrar_primero(self):   #O(1)
        if self._inicio is not None:
            if self._inicio.next is None:
                self._inicio = None
            else:
                self._inicio = self._inicio.next

    def borrar_ultimo(self):    #O(n)
        if self._inicio is not None:
            if self._inicio.next is None:
                self._inicio = None
            else:
                aux = self._inicio
                while aux.next.next is not None:
                    aux = aux.next
                aux.next = None

    def mostrar_lista(self):
        aux = self._inicio
        while aux is not None:
            print(aux.valor)
            aux = aux.next

class DoublyLinkedList:
    @dataclass
    class _Nodo:
        valor : Any
        next : None
        prev : None
    
    def __init__(self) -> None:
        self._inicio = None
    
    def agregar_inicio(self, elemento): #O(1)
        nodo = DoublyLinkedList._Nodo(elemento, None, None)
        if self._inicio is None:
            self._inicio = nodo
        else:
            nodo.next = self._inicio
            self._inicio.prev = nodo    #Doubly
            self._inicio = nodo

    def agregar_final(self, elemento):  #O(n)
        nodo = DoublyLinkedList._Nodo(elemento, None, None)
        if self._inicio is None:
            self._inicio = nodo
        else:
            aux = self._inicio
            while aux.next is not None:
                aux = aux.next
            aux.next = nodo
            nodo.prev = aux #Doubly

    def borrar_primero(self):   #O(1)
        if self._inicio is not None:
            if self._inicio.next is None:
                self._inicio = None
            else:
                self._inicio = self._inicio.next
                self._inicio.prev.next = None #Doubly
                self._inicio.prev = None #Doubly

    def borrar_ultimo(self):    #O(n)
        if self._inicio is not None:
            if self._inicio.next is None:
                self._inicio = None
            else:
                aux = self._inicio
                while aux.next.next is not None:
                    aux = aux.next
                aux.next.prev = None
                aux.next = None

    def mostrar_lista(self):
        aux = self._inicio
        while aux is not None:
            print(aux.valor)
            aux = aux.next

if __name__ == '__main__':
    l = DoublyLinkedList()

    for i in range(0, 10):
        l.agregar_final(i)
    l.borrar_primero()
    l.borrar_ultimo()
    l.mostrar_lista()