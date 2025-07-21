#!/usr/bin/env python3

import sys


def isomorphic(s: str, t: str) -> bool:
    sset = set(s)
    tset = set(t)

    combination = set()
    for index in range(len(s)):
        combination.add((s[index], t[index]))

    return len(sset) == len(combination) == len(tset)


def main():
    for line in sys.stdin:
        items = line.split()
        print("Isomorphic" if isomorphic(items[0], items[1]) else "Not Isomorphic")


if __name__ == "__main__":
    main()
