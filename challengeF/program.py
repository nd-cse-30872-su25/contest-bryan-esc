#!/usr/bin/env python3

import sys

Grid = list[list[int]]


def read_input(rows: int, cols: int):
    grid = [[0 for _ in range(cols + 1)]]

    for _ in range(rows):
        grid.append([0] + list(map(int, sys.stdin.readline().split())))
    return grid


def min_path(grid: Grid, rows: int, cols: int) -> Grid:
    table = [[sys.maxsize for _ in range(cols + 1)] for _ in range(rows + 1)]

    table[0][0] = 0

    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            table[row][col] = (
                min(
                    table[row - 1][(col - 1 + cols) % cols],
                    table[row - 1][col],
                    table[row - 1][(col + 1) % cols],
                )
                + grid[row][col]
            )
    return table


def main():
    while True:
        try:
            rows, cols = list(map(int, sys.stdin.readline().split()))
        except ValueError:
            break
        grid = read_input(rows, cols)
        print(min_path(grid, rows, cols))


if __name__ == "__main__":
    main()
