#!/usr/bin/env python3

import sys
from dataclasses import dataclass


@dataclass
class Node:
    dad: str
    mom: str
    children: list["Node"]


def main():
    while True:
        try:
            families = int(sys.stdin.readline())
        except ValueError:
            break

        for _ in range(families):
            parents, children = sys.stdin.readline().strip().split(":")
            print(parents, children.strip())

        ngift_givers = int(sys.stdin.readline())

        for _ in range(ngift_givers):
            print(sys.stdin.readline().strip())


if __name__ == "__main__":
    main()
