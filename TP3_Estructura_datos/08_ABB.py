
from dataclasses import dataclass
from typing import Any


def _minimum_node(node):
    if node is not None:
        while node.left is not None:
            node = node.left
    return node


def _maximum_node(node):
    if node is not None:
        while node.left is not None:
            node = node.left
    return node


class ABB:
    @dataclass
    class _Node:
        key: Any
        value: Any
        parent: Any
        left: None
        right: None

    # Utilizo un 'Nodo escondido'.
    @dataclass
    class _Root:
        left = None
        right = None
        parent = None

    __slots__ = ['_root', '_len']

    def __init__(self, iterable=None) -> None:
        self._root = ABB._Root()
        self._len = 0
        if iterable is not None:
            for key, values in iterable:
                self.insert(key, values)

    def insert(self, key, value=None) -> None:
        def do_insert(node, parent):
            if node is None:
                node = self._Node(key, value, parent, None, None)
                self._len += 1
            elif key > node.key:
                node.right = do_insert(node.right, node)
            elif key < node.key:
                node.left = do_insert(node.left, node)
            else:  # key == node.key
                node.value = value
            return node

        self._root.left = do_insert(self._root.left, self._root)

    def is_empty(self) -> bool:
        return self._root.left is None

    def __len__(self) -> int:
        return self._len

    def clean(self) -> None:
        self._root, self._len = None, 0

    def find(self, key) -> bool:
        def do_find(node):
            if node is None:
                return False
            elif key > node.key:
                return do_find(node.right)
            elif key < node.key:
                return do_find(node.left)
            else:
                return True
        return do_find(self._root.left)

    def copy(self):
        def do_copy(node, parent):
            if node is None:
                new_node = None
            else:
                new_node = ABB._Node(node.key, node.value, parent, None, None)
                new_node.left = do_copy(node.left, new_node)
                new_node.right = do_copy(node.right, new_node)
            return new_node

        new_tree = ABB()
        new_tree._root.left = do_copy(self._root.left, new_tree._root)
        new_tree._len = self._len
        return new_tree

    def delete(self, key):
        def do_erase(node):
            if node is None:
                result = False
            elif key > node.key:
                result, node.right = do_erase(node.right)
            elif key < node.key:
                result, node.left = do_erase(node.left)
            else:
                node = erase_node(node)
                result = True
            return result, node

        def erase_node(node):
            parent = node.parent
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                node = extract_maximum_node(node)
            assign_parent(node, parent)
            self._len -= 1
            return node

        def extract_maximum_node(node):
            prev = None
            maximum = node.left
            while maximum.right is not None:
                prev = maximum
                maximum = maximum.right

            assign_parent(maximum, node.parent)
            maximum.right = node.right
            assign_parent(maximum.right, maximum)

            if prev is not None:
                prev.right = maximum.left
                assign_parent(prev.right, prev)
                maximum.left = node.left
                assign_parent(maximum.left, maximum)
            return maximum

        def assign_parent(node, parent):
            if node is not None:
                node.parent = parent

        result, self._root.left = do_erase(self._root.left)
        return result

    def begin(self):
        return ABB._Coordinate(_minimum_node(self._root))

    def end(self):
        return ABB._Coordinate(self._root)
    
    def __iter__(self):
        return ABB._Iterator(self.begin(), self.end())

    def __eq__(self, __other: object) -> bool:
        first = self.begin()
        second = __other.begin()

        while first != self.end() and second != __other.end():
            if first.key != second.key or first.value != second.value:
                return False
            first.advance()
            second.advance()

        return first == self.end() and second == __other.end()

    class _Coordinate:
        __slots__ = ['_node']

        def __init__(self, node=None) -> None:
            self._node = node

        @property
        def key(self):
            return self._node.key

        @property
        def value(self):
            return self._node.value

        @value.setter
        def value(self, value):
            self._node.value = value

        def advance(self):
            node = self._node
            if node.right is not None:
                node = _minimum_node(node.right)
            else:
                while node.parent is not None:
                    prev = node
                    node = node.parent
                    if node.right is not prev:
                        break
            self._node = node
            return self

        def retreat(self):
            node = self._node
            if node.left is not None:
                node = _maximum_node(node.left)
            else:
                while node.parent is not None:
                    prev = node
                    node = node.parent
                    if node.left is not prev:
                        break
            self._node = node
            return self

        def prev(self):
            return ABB._Coordinate(self._node).retreat()

        def next(self):
            return ABB._Coordinate(self._node).advance()

        def __eq__(self, __value: object) -> bool:
            return self._node is __value._node

    class _Iterator:
        def __init__(self, node, end):
            self._node = node
            self._end = end
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._node == self._end:
                raise StopIteration
            key, value = self._node.key, self._node.value
            self._node.advance()
            return key, value

    def __str__(self):
        # Es para imprimir el árbol de una manera bonita :-)
        def calculate_placement(node, level):
            if node is None:
                return 0

            nonlocal count
            m1 = calculate_placement(node.left, level + 1)
            placements.append((level, count, node))
            count += 1
            m3 = calculate_placement(node.right, level + 1)
            return max(m1, len(str(node.key)), m3)

        count = 0
        placements = []
        key_len = calculate_placement(self._root.left, 0) + 2

        lines = []
        prev_level = -1
        for level, pos, node in placements:
            i = 2 * level
            while len(lines) <= i:
                lines.append('')

            skip = ' ' * (pos * key_len - len(lines[i]))
            lines[i] += skip + '[{:^{}}]'.format(node.key, key_len - 2)

            if prev_level != -1:
                if prev_level < level:
                    i = 2 * prev_level + 1
                    skip = ' ' * (pos * key_len - len(lines[i]))
                    c = '\\'
                else:
                    i = 2 * level + 1
                    skip = ' ' * (pos * key_len - len(lines[i]) - 1)
                    c = '/'

                lines[i] += skip + '{:>{}}'.format(c,  key_len // 2)

            prev_level = level

        return '\n'.join(lines)


if __name__ == '__main__':
    tree = ABB()
    tree.insert(50)
    tree.insert(20)
    tree.insert(60)
    tree.insert(25)
    tree.insert(40)
    tree.insert(35)
    tree.insert(55)
    tree.insert(70)
    tree.insert(27.5)
    tree.insert(29.5)
    tree.insert(28)

    for i, j in tree:
        print(i, j)
    treeBST = tree.copy()
    print(tree == treeBST)
