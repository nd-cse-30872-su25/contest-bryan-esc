#!/usr/bin/env python3
import sys


def count_buildings(building: list[int]) -> int:
    total_buildings = 1
    curr = building[0]

    for el in building[1:]:
        if curr >= el:
            total_buildings += 1
        curr = el

    return total_buildings


def main():
    for line in sys.stdin:
        build = [int(x) for x in line.split()]
        print(count_buildings(build))


if __name__ == "__main__":
    main()
