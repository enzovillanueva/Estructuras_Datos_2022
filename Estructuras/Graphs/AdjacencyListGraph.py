
import heapq
from collections import deque
from dataclasses import dataclass
from LinkedList import List
from typing import Any


class AdjacencyListGraph:
    @dataclass
    class _Vertex:
        value: Any
        edge: List

    __slots__ = ['_vertex']

    def __init__(self) -> None:
        self._vertex = []

    def add_vertex(self, value):
        vertex = len(self._vertex)
        self._vertex.append(self._Vertex(value, List()))
        return vertex

    def delete_vertex(self, vertex):
        assert 0 <= vertex <= len(self._vertex)
        del self._vertex[vertex]
        for value in len(self._vertex):
            self.delete_edge(value, vertex)

    def add_edge(self, from_, _to, _weight=None):
        assert 0 <= from_ and _to <= len(self._vertex)
        edge = self._vertex[from_].edge
        edge.add(_to, _weight)

    def delete_edge(self, from_, _to):
        assert 0 <= from_ and _to <= len(self._vertex)
        edge = self._vertex[from_].edge
        edge.delete(_to)

    # Getters y setters.
    def set_vertex(self, vertex, value):
        self._vertex[vertex].value = value

    def get_vertex(self, vertex) -> Any:
        assert 0 <= vertex <= len(self._vertex)
        return self._vertex[vertex].value

    def set_edge(self, from_, _to, value):
        assert 0 <= from_ and _to <= len(self._vertex)
        for edge in self._vertex[from_].edge:
            edge.add(_to, value)

    def get_edge(self, from_, _to) -> int:
        assert 0 <= from_ and _to <= len(self._vertex)
        return self._vertex[from_].edge.get_weight(_to)

    # Adyacentes.
    def is_adjacent(self, from_, _to):
        assert 0 <= from_ and _to <= len(self._vertex)
        adjacent = self._vertex.edge
        return adjacent.find_adjacent()

    def adjacents(self, from_) -> list:
        assert 0 <= from_ <= len(self._vertex)
        return [i for i, _ in self._vertex[from_].edge]

    def copy(self):
        new_graph = AdjacencyListGraph()
        for vertex in self._vertex:
            new_graph._vertex.append(self._Vertex(
                vertex.value, vertex.edge.copy()))
        return new_graph

    def __find(self, value):
        for vertex in self._vertex:
            if value == vertex.value:
                return True
        return False

    def __len__(self):
        return len(self._vertex)

    def __eq__(self, __graph: object) -> bool:
        if len(self) != len(__graph):
            return False

        for x, y in zip(self._vertex, __graph._vertex):
            if x.value != y.value or x.edge != y.edge:
                return False

        return True

    def clean(self):
        self._vertex.clear()

    def is_empty(self) -> bool:
        return len(self._vertex) == 0

    # key in dict  -->  dict.__contains__(key)
    def __contains__(self, value):
        return self.__find(value)

    # dict[key]  -->  dict.__getitem__(key)
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            self.add_edge(key[0], key[1], value)
        self.set_vertex(key, value)

    # dict[key] = value -->  dict.__setitem__(key, value)
    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self.get_edge(key[0], key[1])
        return self.get_vertex(key)

    # del dict[key] -->  dict.__delitem__(key)
    def __delitem__(self, key):
        if isinstance(key, tuple):
            self.delete_edge(key[0], key[1])
        self.delete_vertex(key)

    # Recorridos.
    def depth_first_search(self, start: int) -> list: # dfs
        if len(self._vertex) != 0:
            assert 0 <= start < len(self._vertex)
            visit, pending, list_ = set(), list(), list()
            visit.add(start), pending.append(start)
            while pending:
                current = pending.pop()
                list_.append(current)
                # yield current, self.get_vertex(current)

                for conect in self.adjacents(current):
                    if conect not in visit:
                        pending.append(conect), visit.add(conect)
            return list_

    def breadth_first_search(self, start: int) -> list: # bfs
        if len(self._vertex) != 0:
            assert 0 <= start < len(self._vertex)
            visit, pending, _list = set(), deque(), list()
            visit.add(start), pending.append(start)
            while pending:
                current = pending.popleft()
                _list.append(current)

                for conect in self.adjacents(current):
                    if conect not in visit:
                        pending.append(conect), visit.add(conect)
            return _list

    def connected(self, from_: int, _to: int) -> bool:
        if len(self._vertex) != 0:
            assert 0 <= from_ and _to < len(self._vertex)
            visit, pending = set(), deque()
            visit.add(from_), pending.append(from_)
            while pending:
                current = pending.popleft()
                if current == _to:
                    return True
                for conect in self.adjacents(current):
                    if conect not in visit:
                        pending.append(conect), visit.add(conect)
            return False

    def topologic_sort(self):  # bfs
        dict = {vertex : 0 for vertex in range(len(self._vertex))}

        for i in range(len(self._vertex)):
            for j in self.adjacents(i):
                dict[j] += 1

        _list = deque()

        for i in range(len(self._vertex)):
            if dict[i] == 0:
                _list.append(i)

        result = []

        while _list:
            value = _list.popleft()
            result.append(self[value])
            for i in self.adjacents(value):
                dict[i] -= 1
                if dict[i] == 0:
                    _list.append(i)

        return result if len(result) == len(self._vertex) else False

    def shortest_path(self, start: int, max_cost=float('infinity')) -> dict: # Dijkstra 
        assert 0 <= start < len(self._vertex)
        data = {node: [max_cost, []] for node in range(len(self._vertex))}

        data[start] = [0, [start]]

        to_visit = []
        heapq.heappush(to_visit, (0, start))

        while to_visit:
            current_cost, current_node = heapq.heappop(to_visit)
            if data[current_node][0] < current_cost:
                continue
            
            for vertex in self.adjacents(current_node):
                new_cost = current_cost + self.get_edge(current_node, vertex)
                if new_cost < data[vertex][0]:
                    data[vertex][0] = new_cost
                    data[vertex][1] = data[current_node][1] + [vertex]
                    heapq.heappush(to_visit, (new_cost, vertex))
    
        return data


if __name__ == '__main__':
    list_graph = AdjacencyListGraph()
    list_graph.add_vertex("Pergamino")
    list_graph.add_vertex("junin")
    list_graph.add_vertex("Buenos Aires")
    list_graph.add_vertex("Rosario")

    list_graph.add_edge(0, 2, 300)
    list_graph.add_edge(2, 0, 100)
    list_graph.add_edge(1, 2, 120)
    list_graph.add_edge(1, 0, 320)
    list_graph.add_edge(0, 3, 100)
    list_graph.add_edge(0, 1, 500)

    # two_graph
    two_graph = AdjacencyListGraph()
    two_graph.add_vertex("A")  # 0
    two_graph.add_vertex("B")  # 1
    two_graph.add_vertex("C")  # 2
    two_graph.add_vertex("D")  # 3
    two_graph.add_vertex("H")  # 4
    two_graph.add_vertex("R")  # 5
    two_graph.add_vertex("T")  # 6

    two_graph.add_edge(4, 0, 60)
    two_graph.add_edge(4, 6, 200)
    two_graph.add_edge(5, 4, 600)
    two_graph.add_edge(1, 4, 320)
    two_graph.add_edge(4, 3, 123)
    two_graph.add_edge(2, 5, 90)
    two_graph.add_edge(3, 2, 110)
    two_graph.add_edge(3, 1, 510)

    # tree_graph
    tree_graph = AdjacencyListGraph()
    tree_graph.add_vertex("AM2")  # 0
    tree_graph.add_vertex("AnNum")  # 1
    tree_graph.add_vertex("Algo1")  # 2
    tree_graph.add_vertex("Algo2")  # 3
    tree_graph.add_vertex("Taller1")  # 4
    tree_graph.add_vertex("EstrCom")  # 5
    tree_graph.add_vertex("Org.Datos")  # 6
    tree_graph.add_vertex("AL2")  # 7
    tree_graph.add_vertex("Proba")  # 8
    tree_graph.add_vertex("F2")  # 9
    tree_graph.add_vertex("F1")  # 10

    tree_graph.add_edge(10, 9, 9)
    tree_graph.add_edge(0, 8, 9)
    tree_graph.add_edge(9, 5, 10)
    tree_graph.add_edge(0, 9, 8)
    tree_graph.add_edge(7, 8, 10)
    tree_graph.add_edge(7, 5, 10)
    tree_graph.add_edge(2, 3, 10)
    tree_graph.add_edge(7, 1, 9)
    tree_graph.add_edge(3, 1, 10)
    tree_graph.add_edge(1, 4, 10)
    tree_graph.add_edge(3, 6, 9)
    tree_graph.add_edge(3, 5, 8)
    tree_graph.add_edge(0, 1, 10)
    tree_graph.add_edge(5, 6, 10)
    tree_graph.add_edge(5, 4, 9)
    
    list_graph[2] = "CABA"
    print(two_graph.breadth_first_search(3))

    print(tree_graph.topologic_sort())
    print(two_graph.shortest_path(4))
