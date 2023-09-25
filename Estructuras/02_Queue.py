
from dataclasses import dataclass
from typing import Any


class QueueLinkedList:
    @dataclass
    class _Nodo:
        valor: Any
        next: None

    def __init__(self) -> None:
        self._inicio = None
        self._ultimo = self._inicio
        self._tamaño = 0

    def encolar(self, elemento):  # O(1)
        nodo = QueueLinkedList._Nodo(elemento, None)
        if self._inicio is None:
            self._inicio = nodo
            self._ultimo = self._inicio
        else:
            self._ultimo.next = nodo
            self._ultimo = self._ultimo.next
        self._tamaño += 1

    def desencolar(self):  # O(1)
        if self._inicio is not None:
            if self._inicio.next is None:
                self._inicio = self._ultimo = None
            else:
                self._inicio = self._inicio.next
            self._tamaño -= 1

    def primero(self):
        return self._inicio

    def ultimo(self):
        return self._ultimo

    def es_vacia(self):
        return self._inicio is None

    def __len__(self):
        return self._tamaño

    def __eq__(self, __o: object) -> bool:  # O(n)
        if self._tamaño == __o._tamaño:
            act1 = self._inicio
            act2 = __o._inicio
            while act1 != None and act2 != None:
                if act1.valor != act2.valor:
                    return False
                act1 = act1.next
                act2 = act2.next

            return True
        else:
            return False

    def mostrar_lista(self):
        aux = self._inicio
        while aux is not None:
            print(aux.valor)
            aux = aux.next


class QueueDoubleList:
    @dataclass
    class _Nodo:
        valor: Any
        next: None
        prev: None

    def __init__(self) -> None:
        self._inicio = None
        self._ultimo = None
        self._tamaño = 0

    def encolar(self, elemento):  # O(1)
        nodo = QueueDoubleList._Nodo(elemento, None, None)
        if self._inicio is None:
            self._inicio = nodo
            self._ultimo = nodo
        else:
            nodo.next = self._inicio
            self._inicio.prev = nodo
            self._inicio = nodo

        self._tamaño += 1

    def desencolar(self):  # O(1)
        if self._inicio is not None:
            if self._inicio.next is None:
                self._inicio = None
                self._ultimo = None
            else:
                self._ultimo = self._ultimo.prev
                self._ultimo.next.prev = None
                self._ultimo.next = None

    def mostrar_lista(self):
        aux = self._ultimo
        while aux is not None:
            print(aux.valor)
            aux = aux.prev


if __name__ == '__main__':
    data = QueueDoubleList()
    data.encolar(1)
    data.encolar(5)
    data.encolar(2)
    data.desencolar()
    data.mostrar_lista()
