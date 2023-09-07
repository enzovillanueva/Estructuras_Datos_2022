

class Stack:

    def __init__(self, iterable=None):
        self._lista = []
        if iterable != None:
            for values in iterable:
                self._lista.append(values)

    @property
    def lista(self):
        return self._lista.copy()

    def lista(self, nuevo):
        self._lista = list(nuevo)

    def push(self, valor):
        self._lista.append(valor)

    def pop(self):
        assert not self.empty(), 'Sin elementos'
        return self._lista.pop()

    def size(self):
        return len(self._lista)

    def empty(self):
        return len(self._lista) == 0

    def inverso(self):  # TP2_Ejercicio_3
        assert not self.empty(), "NO hay elementos en la pila"

        for i in range(len(self._lista)-1, -1, -1):
            print(self._lista[i])

    # TP2_Ejercicio_4
    def palindromo(self):
        if len(self._lista) != 0:
            return self._lista == self._lista[::-1]
         
    # Lo que pedía el ejercicio TP3 (Ej. 4)
    def copy_recursivo(self):
        def do_copy(lista):
            if not lista:
                return []
            else:
                return [lista[0]] + do_copy(lista[1:])

        new_stack = Stack()
        new_stack._lista = do_copy(self._lista)
        return new_stack

    @property
    def tope(self):
        assert not self.empty(), 'Sin elementos'
        return self._lista[-1]

    def clear(self):
        self._lista.clear()

    def copy_iterativo(self):
        new_Stack = Stack()
        new_Stack._lista = self._lista.copy()
        return new_Stack

    def __eq__(self, otraLista):
        return self._lista == otraLista._lista

    def __repr__(self):
        return ('Stack([' + ', '.join(repr(i) for i in self._lista) + '])')


class Cola:

    def __init__(self, cola=None):
        self._lista = []
        if cola is not None:
            for i in cola:
                self._lista.append(i)

    @property
    def lista(self):
        return self._lista.copy()

    def lista(self, elemento):
        self._lista.append(elemento)

    def encolar(self, a):
        self._lista.append(a)

    def desencolar(self):
        self._lista.pop(0)

    def tamaño(self):
        return len(self._lista)

    def emply(self):
        return len(self._lista) == 0

    def __repr__(self):
        return('Cola([' + ', '.join(repr(i) for i in self._lista) + '])')


if __name__ == '__main__':
    pila1 = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    pila2 = Stack("ala")
    print(pila2._lista)
    pila2 = pila1.copy_recursivo()
    print(pila2 == pila1)
