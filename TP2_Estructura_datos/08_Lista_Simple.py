
from dataclasses import dataclass
from typing import Any


class Lista_Simple:

    @dataclass
    class _Nodo:
        value: Any
        next: None

    class _Head:
        next: None

    def __init__(self, iterable=None) -> None:
        self._head = Lista_Simple._Head()
        self._tope = self._head
        if iterable is not None:
            for values in iterable:
                self.agregar(values)

    def agregar(self, valor):
        nodo = Lista_Simple._Nodo(valor, None)
        self._tope.next = nodo
        self._tope = nodo

    def insertar_despues_de(self, elemento, valor):
        aux = self._head.next
        while aux is not None:
            if aux.value == elemento:
                self.__insert(Lista_Simple._Coordinate(aux), valor)
                break
            aux = aux.next

    def borrar_despues_de(self, elemento):
        aux = self._head.next
        while aux is not None:
            if aux.value == elemento:
                self.__deleted(Lista_Simple._Coordinate(aux))
                break
            aux = aux.next

    def begin(self):
        return Lista_Simple._Coordinate(self._head.next)

    def end(self):
        return Lista_Simple._Coordinate(self._tope)

    def __insert(self, coordenada, valor):
        aux = coordenada._node
        nodo = Lista_Simple._Nodo(valor, None)
        nodo.next = aux.next
        aux.next = nodo

    def __deleted(self, coordenada):
        aux = coordenada._node
        if aux.next is not None:
            delete = aux.next
            aux.next = delete.next
            del delete

    def mostrar_lista(self):
        aux = self._head.next
        while aux != None:
            print(aux.value)
            aux = aux.next

    def borrar_ultimo(self):

        if self._head.next.next is None:
            self._head.next = None
        else:
            aux = self._head.next
            while aux.next.next is not None:
                aux = aux.next

            aux.next = None

    class _Coordinate():

        def __init__(self, coordenada) -> None:
            if isinstance(coordenada, Lista_Simple._Coordinate):
                self._node = coordenada._node
            else:
                self._node = coordenada

        def advance(self):
            self._node = self._node.next
            return self

        def next(self):
            return Lista_Simple._Coordinate(self._node).advance()


if __name__ == '__main__':
    lista = Lista_Simple()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.insertar_despues_de(2, 5)
    lista.borrar_despues_de(3)
    lista.borrar_ultimo()
    lista.borrar_ultimo()
    lista.borrar_ultimo()
    lista.mostrar_lista()
