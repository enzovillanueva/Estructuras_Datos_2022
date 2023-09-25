
from dataclasses import dataclass


class List:
    @dataclass
    class _Edge:
        _to: None
        _weight: None
        next: None

    @dataclass
    class _Head:
        next = None

    __slots__ = ['_head', '_len']

    def __init__(self) -> None:
        self._head = List._Head()
        self._head.next = self._head
        self._len = 0

    def add(self, _to: int = None, _weight=None):
        node = List._Edge(_to, _weight, None)
        if self._head.next is self._head or node._to < self._head.next._to:
            node.next = self._head.next
            self._head.next = node
        else:
            current = self._head.next
            while current.next != self._head and current.next._to < _to:
                current = current.next

            if current.next != self._head:
                if current.next._to == _to:
                    current.next._weight = _weight
                    return
            node.next = current.next
            current.next = node
        self._len += 1

    def delete(self, _to: int):
        if self._head.next != self._head:
            if self._head.next._to == _to:
                self._head.next = self._head.next.next
            else:
                current = self._head.next
                while current.next != self._head and current.next._to < _to:
                    current = current.next

                if current.next != self._head:
                    if current.next._to == _to:
                        deleted = current.next
                        current.next = deleted.next
            self._len -= 1

    def copy(self):
        new_list = List()
        for i, j in self:
            new_list.add(i, j)
        return new_list

    def __find(self, _to) -> tuple:
        current = self.begin()
        while current != self.end():
            if _to == current.to:
                return True, List._Coordinate(current)
            elif _to < current.to:
                break
            current.advance()
        return False,

    def find_adjacent(self, _to):
        return True if self.__find(_to)[0] else False

    def get_weight(self, _to):
        value = self.__find(_to)
        return value[1].weight if value[0] else False

    def is_empty(self):
        return self._head.next == self._head

    def __len__(self):
        return self._len

    def __iter__(self):
        return List._Iterator(self._head.next, self._head)

    def __eq__(self, __linked: object) -> bool:
        return all(i == j for i, j in zip(self, __linked)) if len(self) == len(__linked) else False

    def clean(self):
        self._head.next, self._len = self._head, 0

    def begin(self):
        return List._Coordinate(self._head.next)

    def end(self):
        return List._Coordinate(self._head)

    class _Coordinate:

        __slots__ = ['_node']

        def __init__(self, node) -> None:
            self._node = node._node if isinstance(
                node, List._Coordinate) else node

        @property
        def to(self):
            return self._node._to

        @property
        def weight(self):
            return self._node._weight

        @weight.setter
        def weight(self, value):
            self._node._weight = value

        def advance(self):
            self._node = self._node.next
            return self

        def next(self):
            return List._Coordinate(self._node).advance()

        def __eq__(self, __value: object) -> bool:
            return self._node == __value._node

    class _Iterator:

        __slots__ = ['_begin', '_end']

        def __init__(self, begin, end) -> None:
            self._begin = begin
            self._end = end

        def __iter__(self):
            return self

        def __next__(self):
            if self._begin == self._end:
                raise StopIteration

            to, weight = self._begin._to, self._begin._weight
            self._begin = self._begin.next
            return to, weight


if __name__ == '__main__':
    list = List()
    list.add(2, 134)
    list.add(5, 44)
    list.add(15, 333)
    list.add(12, 23)
    list.add(10, 42)
    list.add(8, 423)
    list.add(1, 12)
    list.add(17, 43)
    list.add(6, 44)

    list_two = list.copy()
    list_two.add(15,222)
    # list_two.delete(6)
    # list_two.delete(17)
    # list_two.delete(12)
    list_two.mostrar_lista()

    result = [i for i, _ in list_two]
    print(result)
