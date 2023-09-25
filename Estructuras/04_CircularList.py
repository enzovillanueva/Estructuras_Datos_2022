
from dataclasses import dataclass
from types import NoneType
from typing import Any


# NO es eficiente, todas sus funciones de agregar y borrar elementos son O(n)
class CircularList:
    @dataclass
    class _Nodo:
        valor: Any
        next: None

    def __init__(self) -> None:
        self._inicio = None

    def agregar_inicio(self, elemento):  # O(n)
        nodo = CircularList._Nodo(elemento, None)
        if self._inicio is None:
            self._inicio = nodo
            self._inicio.next = self._inicio
        else:
            aux = self._inicio
            while aux.next is not self._inicio:  # Siempre "self._inicio", NO "aux"
                aux = aux.next
            nodo.next = self._inicio
            aux.next = nodo
            # En "agregar_inicio", una vez agregado el nodo, SIEMPRE tenemos que asignar el nuevo INICIO
            self._inicio = nodo
            # "self._inicio = nodo"

    def agregar_final(self, elemento):  # O(n)
        nodo = CircularList._Nodo(elemento, None)
        if self._inicio is None:
            self._inicio = nodo
            self._inicio.next = self._inicio
        else:
            aux = self._inicio
            while aux.next is not self._inicio:  # Siempre "self._inicio", NO "aux"
                aux = aux.next
            nodo.next = self._inicio
            aux.next = nodo

    def borrar_primero(self):  # O(n)
        if self._inicio is not None:
            if self._inicio.next is self._inicio:
                self._inicio = None
            else:
                aux = self._inicio
                while aux.next is not self._inicio:
                    aux = aux.next
                self._inicio = self._inicio.next
                aux.next.next = None
                aux.next = self._inicio

    def borrar_ultimo(self):  # O(n)
        if self._inicio is not None:
            if self._inicio.next is self._inicio:
                self._inicio = None
            else:
                aux = self._inicio
                while aux.next.next is not self._inicio:
                    aux = aux.next
                aux.next.next = None
                aux.next = self._inicio

    def mostrar_lista(self):
        if self._inicio is not None:
            aux = self._inicio
            while True:
                print(aux.valor)
                aux = aux.next
                if aux == self._inicio:
                    break


class DoublyCircularList:
    @dataclass  
    class _Nodo:  
        valor: Any
        next: None
        prev: None

    def __init__(self) -> None:
        self._inicio = None

    def agregar_inicio(self, elemento):  # O(1)
        nodo = DoublyCircularList._Nodo(elemento, None, None)
        if self._inicio is None:
            self._inicio = nodo
            self._inicio.prev = self._inicio.next = self._inicio
        else:
            nodo.next = self._inicio
            nodo.prev = self._inicio.prev
            self._inicio.prev = nodo
            nodo.prev.next = nodo
            self._inicio = nodo

    def agregar_final(self, elemento):  # O(1)
        nodo = DoublyCircularList._Nodo(elemento, None, None)
        if self._inicio is None:
            self._inicio = nodo
            self._inicio.prev = self._inicio.next = self._inicio
        else:
            nodo.next = self._inicio
            nodo.prev = self._inicio.prev
            self._inicio.prev = nodo
            nodo.prev.next = nodo

    def borrar_primero(self):  # O(1)
        if self._inicio is not None:
            if self._inicio.next is self._inicio:
                self._inicio = None
            else:
                aux = self._inicio
                self._inicio = self._inicio.next
                self._inicio.prev = aux.prev
                aux.prev.next = aux.next
                aux.next = aux.prev = None

    def borrar_ultimo(self):  # O(1)
        if self._inicio is not None:
            if self._inicio.next is self._inicio:
                self._inicio = None
            else:
                aux = self._inicio.prev
                self._inicio.prev = aux.prev
                aux.prev.next = aux.next
                aux.next = aux.prev = None

    def mostrar_lista(self):
        if self._inicio is not None:
            aux = self._inicio
            while True:
                print(aux.valor)
                aux = aux.next
                if aux == self._inicio:
                    break


if __name__ == '__main__':
    circular = CircularList()
    for i in "Enzo":
        circular.agregar_inicio(i)
    circular.borrar_primero()
    circular.borrar_primero()
    circular.borrar_ultimo()
    circular.borrar_ultimo()
    circular.mostrar_lista()
