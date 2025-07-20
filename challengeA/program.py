#!/usr/bin/env python3

import sys

def count_buildings(building: list[int]) -> int:
    total_buildings = 0

    for index in range(len(building) - 1):
        if building[index] > building[index+1]:
            total_buildings += 1

    total_buildings += 1
    return total_buildings


def main():
    for line in sys.stdin:
        build = [int(x) for x in line.split()]
        print(count_buildings(build))

if __name__ == "__main__":
    main()
