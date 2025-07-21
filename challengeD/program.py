#!/usr/bin/env python3

import sys

points = (2, 3, 7)


def find_targets(target: int, total: int = 0, total_list=[]):
    if total == target:
        yield sorted(total_list)
    for point in points:
        if total + point <= target:
            yield from find_targets(target, total + point, total_list + [point])


def main():
    for line in sys.stdin:
        items = [v for v in find_targets(int(line))]
        itemset = []
        for item in items:
            if item not in itemset:
                itemset.append(item)
        print(f"There are {len(itemset)} ways to achieve a score of {line.strip()}:")
        if itemset:
            for i in itemset:
                print(" ".join(list(map(str, i))))

if __name__ == "__main__":
    main()
