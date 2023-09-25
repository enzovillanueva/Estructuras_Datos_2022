
import heapq
from collections import deque
from typing import Any


class AdjacentMatrixGraph:

    __slots__ = ['_vertex', '_edges']

    def __init__(self) -> None:
        self._vertex = []
        self._edges = []

    def add_vertex(self, value: Any):
        vertex = len(self._vertex)
        self._vertex.append(value)
        for edge in self._edges:
            edge.append(None)
        self._edges.append([None]*(vertex + 1))
        return vertex

    def add_edge(self, from_: int, _to: int, _weight: int = 1):
        assert 0 <= from_ and _to <= len(self._vertex)
        self._edges[from_][_to] = _weight

    def delete_vertex(self, vertex: int):
        assert 0 <= vertex < len(self._vertex)
        del self._vertex[vertex], self._edges[vertex]
        for edge in self._edges:
            del edge[vertex]

    def delete_edge(self, from_: int, _to: int):
        self._edges[from_][_to] = None

    # Getters y Setters
    def set_vertex(self, vertex: int, value):
        assert 0 <= vertex <= len(self._vertex)
        self._vertex[vertex] = value

    def get_vertex(self, vertex: int):
        assert 0 <= vertex <= len(self._vertex)
        return self._vertex[vertex]

    def set_edge(self, from_, _to, weight):
        assert 0 <= from_ and _to <= len(self._vertex)
        self._edges[from_][_to] = weight

    def get_edge(self, from_, _to):
        assert 0 <= from_ and _to <= len(self._vertex)
        return self._edges[from_][_to]

    # Adyacentes.
    def is_adjacent(self, from_, _to):
        assert 0 <= from_ and _to <= len(self._vertex)
        return self._edges[from_][_to] is not None

    def adjacents(self, from_):
        assert 0 <= from_ <= len(self._vertex)
        result = []
        for i in range(len(self._vertex)):
            result += [i] if self._edges[from_][i] is not None else []
        return result

    def copy(self):
        new_graph = AdjacentMatrixGraph()
        new_graph._vertex = self._vertex.copy()
        for edge in self._edges:
            new_graph._edges.append(edge.copy())
        return new_graph

    def __eq__(self, __graph: object) -> bool:
        return self._vertex == __graph._vertex and self._edges == __graph._edges

    def __len__(self):
        return len(self._vertex)

    def clean(self):
        self._vertex.clear(), self._edges.clear()

    def is_empty(self):
        return len(self._vertex) == len(self._edges) == 0

    # key in dict  -->  dict.__contains__(key)
    def __contains__(self, value):
        return value in self._vertex

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
    def depth_first_search(self, start: int) -> list: # dfs.
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
                # yield current, self.get_vertex(current)

                for conect in self.adjacents(current):
                    if conect not in visit:
                        pending.append(conect), visit.add(conect)
            return _list

    def connected(self, from_: int, _to: int) -> bool:
        if len(self._vertex) != 0:
            assert 0 <= from_ < len(
                self._vertex) and 0 <= _to < len(self._vertex)
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

    def __str__(self) -> str:
        matrix = [[i] + self._edges[i] for i in range(len(self))]
        matrix.insert(0, ['F/T'] + [i for i in range(len(self))])
        print("F: From (first column), T: To (first row)")
        for row in matrix:
            for column in row:
                print(column if column != None else '-', '\t', end='')
            print()
        return ''


if __name__ == '__main__':
    # Pruebas
    matrix_graph = AdjacentMatrixGraph()
    matrix_graph.add_vertex("Pergamino")
    matrix_graph.add_vertex("Junin")
    matrix_graph.add_vertex("Rosario")
    matrix_graph.add_vertex("Buenos Aires")
    matrix_graph.add_vertex("Sarmiento")
    matrix_graph.add_vertex("Ushuaia")
    matrix_graph.add_vertex("Misiones")
    matrix_graph.add_vertex("Montevideo")

    matrix_graph.add_edge(0, 2, 120)
    matrix_graph.add_edge(0, 1, 120)
    matrix_graph.add_edge(0, 3, 400)
    matrix_graph.add_edge(1, 0, 300)
    matrix_graph.add_edge(0, 6, 5000)
    matrix_graph.add_edge(6, 6, 0)
    matrix_graph.add_edge(5, 6, 250)

    # matrix_two
    matrix_two = AdjacentMatrixGraph()
    matrix_two.add_vertex("A")  # 0
    matrix_two.add_vertex("B")  # 1
    matrix_two.add_vertex("C")  # 2
    matrix_two.add_vertex("D")  # 3
    matrix_two.add_vertex("H")  # 4
    matrix_two.add_vertex("R")  # 5
    matrix_two.add_vertex("T")  # 6

    matrix_two.add_edge(4, 0, 60)
    matrix_two.add_edge(4, 6, 200)
    matrix_two.add_edge(5, 4, 600)
    matrix_two.add_edge(1, 4, 320)
    matrix_two.add_edge(4, 3, 123)
    matrix_two.add_edge(2, 5, 90)
    matrix_two.add_edge(3, 2, 110)
    matrix_two.add_edge(3, 1, 510)

    matrix = matrix_graph.copy()
    print(matrix_graph == matrix)
    print("Pergamino" in matrix)
    print(matrix_two)

