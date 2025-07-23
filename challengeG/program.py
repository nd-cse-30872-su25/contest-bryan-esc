#!/usr/bin/env python3

import sys
from collections import defaultdict

Graph = dict[int, list[int]]


def find_circuit(graph: Graph, start: int, vertex: int, visited: set[int], path:
                 list[tuple[int,int]], vertices: int)-> list[tuple[int, int]]:
    if path and start == vertex and len(path) == vertices:
        return path

    for neighbor in graph[vertex]:

        if neighbor in visited:
            continue
        
        if neighbor == start and len(path) < vertices - 1:
            continue

        visited.add(graph[vertex][neighbor])

        path.append((vertex, neighbor))

        if find_circuit(graph, start, neighbor, visited, path, vertices):
            return path

        path.pop(-1)

        visited.remove(graph[vertex][neighbor])
    return []

def find_paths(graph: Graph, nvertces: int) -> list[tuple[int, int]]:
    start = sorted(graph.keys())[0]
    visited = set()
    return find_circuit(graph, start, start, visited, [], nvertces)

def main():
    while True:
        try:
            n = int(sys.stdin.readline())
        except ValueError:
            break
        grid = []
        for _ in range(n):
            grid.append(list(map(int, sys.stdin.readline().split())))

        graph: Graph = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    graph[i].append(j)
        print(find_paths(graph, n))


if __name__ == "__main__":
    main()
