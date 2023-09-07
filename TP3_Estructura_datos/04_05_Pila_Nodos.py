
from dataclasses import dataclass


class StackLinkedList():

    @dataclass
    class _Node:
        value: None
        next: None
        prev: None

    @dataclass
    class _Head:
        next: None
        prev: None

    def __init__(self) -> None:
        self._head = StackLinkedList._Head(None, None)
        self._apunt = self._head

    def apilar(self, valor) -> None:  # O(1)
        nodo = StackLinkedList._Node(valor, None, None)
        self._apunt.next = nodo
        nodo.prev = self._apunt
        self._apunt = nodo

    def desapilar(self) -> None:  # O(1)
        if self._apunt is None:
            return None
        else:
            self._apunt = self._apunt.prev
            self._apunt.next = None

    def tope(self):
        return self._apunt.value

    def begin(self):
        return self._head

    def end(self):
        aux = self._head
        while aux != None:
            aux = aux.next

        return aux

    # Lo que pedia el ejercicio.

    def __len__(self) -> int:
        def contador(aux):
            if aux.next is None:
                return 0
            return 1 + contador(aux.next)
        return contador(self._head)

    def mostrar_lista(self):
        aux = self._head.next
        while aux != None:
            print(aux.value)
            aux = aux.next


if __name__ == '__main__':
    stack = StackLinkedList()
    stack.apilar(1)
    stack.apilar(2)
    stack.apilar(3)
    stack.apilar(4)
    stack.apilar(5)
    stack.desapilar()
    stack.desapilar()

    print(len(stack))
