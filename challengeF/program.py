#!/usr/bin/env python3
import sys

Grid = list[list[int]]


def read_input(rows: int):
    return [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]


def min_path(grid: Grid, rows: int, cols: int) -> Grid:
    table = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        table[row][0] = grid[row][0]
    for col in range(1, cols):
        for row in range(rows):
            table[row][col] = (
                min(
                    table[(row - 1 + rows) % rows][col - 1],
                    table[(row + 1) % rows][col - 1],
                    table[(row) % rows][col - 1],
                )
                + grid[row][col]
            )
    return table


def reconstruct_path(grid: Grid, rows: int, cols: int, table: Grid) -> list[int]:
    end_row = min(range(rows), key=lambda r: table[r][cols - 1])
    path = [end_row + 1]
    r = end_row
    c = cols - 1
    while c > 0:
        curr_cost = table[r][c] - grid[r][c]
        prev_rows = [(r - 1 + rows) % rows, r, (r + 1) % rows]
        prev_rows.sort()
        for prev_r in prev_rows:
            if table[prev_r][c - 1] == curr_cost:
                path.append(prev_r + 1)
                r = prev_r
                break
        c -= 1
    path.reverse()
    return path


def main():
    while True:
        try:
            rows, cols = list(map(int, sys.stdin.readline().split()))
        except ValueError:
            break
        grid = read_input(rows)
        min_table = min_path(grid, rows, cols)
        min_cost = min(min_table[r][cols - 1] for r in range(rows))
        print(min_cost)
        path = reconstruct_path(grid, rows, cols, min_table)
        print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()
