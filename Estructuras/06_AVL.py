
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


class AVL:
    @dataclass
    class _Node:
        key: Any
        value: Any
        parent: Any
        left: None
        right: None
        height: int

    # Utilizo un 'Nodo escondido'.
    @dataclass
    class _Root:
        left = None
        right = None
        parent = None

    __slots__ = ['_root', '_len']

    def __init__(self, iterable=None) -> None:
        self._root = AVL._Root()
        self._len = 0
        if iterable is not None:
            for key, values in iterable:
                self.insert(key, values)

    def insert(self, key, value=None) -> None:
        def do_insert(node, parent):
            if node is None:
                node = self._Node(key, value, parent, None, None, 1)
                self._len += 1
            elif key == node.key:
                node.value = value
            else:
                if key > node.key:
                    node.right = do_insert(node.right, node)
                else:
                    node.left = do_insert(node.left, node)
                node = self.__balance_avl_tree(node)
            return node

        self._root.left = do_insert(self._root.left, self._root)

    # Funciones para el balanceo del arbol. ######################################
    def __balance_avl_tree(self, node):
        bf = self.__balance_factor(node)
        if bf == 2:
            if self.__balance_factor(node.left) == -1:
                node.left = self.__left_rotation(node.left)
            node = self.__right_rotation(node)
        elif bf == -2:
            if self.__balance_factor(node.right) == 1:
                node.right = self.__right_rotation(node.right)
            node = self.__left_rotation(node)
        else:
            self.__update_height(node)

        return node

    def __balance_factor(self, node):
        factor = 0
        if node is not None:
            if node.left is not None:
                factor += node.left.height
            if node.right is not None:
                factor -= node.right.height
        return factor

    def __right_rotation(self, node):
        left_avl_tree = node.left
        node.left = left_avl_tree.right
        self.__assign_parent(node.left, node)
        left_avl_tree.right = node
        left_avl_tree.parent = node.parent
        node.parent = left_avl_tree
        node = left_avl_tree
        self.__update_height(node.right)
        self.__update_height(node)

        return node

    def __left_rotation(self, node):
        right_avl_tree = node.right
        node.right = right_avl_tree.left
        self.__assign_parent(node.right, node)
        right_avl_tree.left = node
        right_avl_tree.parent = node.parent
        node.parent = right_avl_tree
        node = right_avl_tree
        self.__update_height(node.left)
        self.__update_height(node)

        return node

    def __assign_parent(self, node, parent):
        if node is not None:
            node.parent = parent

    def __update_height(self, node):
        left_height = 0
        if node.left is not None:
            left_height = node.left.height
        right_height = 0
        if node.right is not None:
            right_height = node.right.height
        node.height = 1 + max(left_height, right_height)

    ##############################################################################

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
                node = self.__balance_avl_tree(node)
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
            self.__assign_parent(node, parent)
            self._len -= 1
            return node

        def extract_maximum_node(node):
            prev = None
            maximum = node.left
            while maximum.right is not None:
                prev = maximum
                maximum = maximum.right

            self.__assign_parent(maximum, node.parent)
            maximum.right = node.right
            self.__assign_parent(maximum.right, maximum)

            if prev is not None:
                prev.right = maximum.left
                self.__assign_parent(prev.right, prev)
                maximum.left = node.left
                self.__assign_parent(maximum.left, maximum)
            return maximum

        result, self._root.left = do_erase(self._root.left)
        return result

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
                new_node = AVL._Node(node.key, node.value,
                                     parent, None, None, 1)
                new_node.left = do_copy(node.left, new_node)
                new_node.right = do_copy(node.right, new_node)
            return new_node

        new_tree = AVL()
        new_tree._root.left = do_copy(self._root.left, new_tree._root)
        new_tree._len = self._len
        return new_tree

    def begin(self):
        return AVL._Coordinate(_minimum_node(self._root))

    def end(self):
        return AVL._Coordinate(self._root)

    def __iter__(self):
        return AVL._Iterator(self.begin(), self.end())

    def tree_height(self):
        def do_tree_height(node):
            if node is None:
                return 0
            else:
                return 1 + max(do_tree_height(node.left), do_tree_height(node.right))
        return do_tree_height(self._root.left)

    def __eq__(self, __other: object) -> bool:
        first = self.begin()
        second = __other.begin()

        while first != self.end() and second != __other.end():
            if first.key != second.key or first.value != second.value:
                return False
            first.advance()
            second.advance()

        return first == self.end() and second == __other.end()

    # Recorridos
    def preorder(self):
        def do_preorder(node, orderList):
            if node:
                orderList.append(node.key)
                do_preorder(node.left, orderList)
                do_preorder(node.right, orderList)
            return orderList
        return do_preorder(self._root.left, [])

    def inorder(self):
        def do_inorder(node, orderList):
            if node:
                do_inorder(node.left, orderList)
                orderList.append(node.key)
                do_inorder(node.right, orderList)
            return orderList
        return do_inorder(self._root.left, [])

    def postorder(self):
        def do_postorder(node, orderList):
            if node:
                do_postorder(node.left, orderList)
                do_postorder(node.right, orderList)
                orderList.append(node.key)
            return orderList
        return do_postorder(self._root.left, [])

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
            return AVL._Coordinate(self._node).retreat()

        def next(self):
            return AVL._Coordinate(self._node).advance()

        def __eq__(self, __value: object) -> bool:
            return self._node is __value._node

    class _Iterator:

        __slots__ = ['_node', '_end']

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
    avl_tree = AVL()
    avl_tree.insert(50)
    avl_tree.insert(20)
    avl_tree.insert(60)
    avl_tree.insert(25)
    avl_tree.insert(40)
    avl_tree.insert(35)
    avl_tree.insert(55)
    avl_tree.insert(70)
    avl_tree.insert(27.5)
    avl_tree.insert(29.5)
    avl_tree.insert(28)
    avl_tree.delete(29.5)
    avl = avl_tree.copy()

    print(avl_tree)
    print(avl == avl_tree)
    print(avl_tree.postorder())
