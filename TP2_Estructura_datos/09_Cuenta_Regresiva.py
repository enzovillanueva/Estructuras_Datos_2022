

class Inverse:

    def __init__(self, iterable: int = None):
        self._lista = []
        if iterable != None:
            self.inverse_append(iterable)

    def inverse_append(self, a):
        self._lista = list(range(a))

    def __iter__(self):
        return Inverse.Iterator(self._lista[::-1], len(self._lista))

    class Iterator():

        def __init__(self, inicio, final):
            self._inicio = inicio
            self._final = final
            self._iterator = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._iterator == self._final:
                self._iterator = 0
                raise StopIteration
            valor = self._inicio[self._iterator]
            self._iterator += 1
            return valor


if __name__ == '__main__':
    for i in Inverse(6):
        print(i, end=' -> ')

    print('\n')
    for i in range(6):
        print(i, end=' -> ')
