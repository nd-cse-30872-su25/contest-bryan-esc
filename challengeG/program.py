#!/usr/bin/env python3

import sys


def solve(grid: list[list[int]], vertices: int) -> int:
    visited = set()

    isolated_nodes = 0
    for vertex in range(vertices):
        if vertex not in visited:
            frontier = [vertex]
            visited.add(vertex)
            while frontier:
                node = frontier.pop()
                for neighbor in range(vertices):
                    if grid[node][neighbor] and neighbor not in visited:
                        visited.add(neighbor)
                        frontier.append(neighbor)
            isolated_nodes += 1
    return isolated_nodes


def main():
    count = 1
    while True:
        try:
            n = int(sys.stdin.readline())
        except ValueError:
            break
        grid = []
        for _ in range(n):
            grid.append(list(map(int, sys.stdin.readline().split())))
        print(f"System {count} isolated circuits: {solve(grid, n)}")
        count += 1


if __name__ == "__main__":
    main()
