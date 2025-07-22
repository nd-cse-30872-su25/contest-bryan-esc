#!/usr/bin/env python3
import sys


def solve(buildings: list[int]) -> int:
    curr_max = float('-inf')
    count = 0
    buildings.reverse()
    for i in range(0, len(buildings)):
        if buildings[i] > curr_max:
            curr_max = buildings[i]
            count += 1
    return count


def main():
    for line in sys.stdin:
        build = [int(x) for x in line.split()]
        print(solve(build))


if __name__ == "__main__":
    main()
