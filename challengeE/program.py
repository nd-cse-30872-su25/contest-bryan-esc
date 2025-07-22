#!/usr/bin/env python3

import sys


def find_paths(
    tree: list[int], target: int, total: int, path: list[int], index: int = 0
):
    left = 2 * index + 1
    right = 2 * index + 2
    leaf = (left >= len(tree) or tree[left] == 0) and (
        right >= len(tree) or tree[right] == 0
    )
    if target == total and leaf:
        yield path

    if left < len(tree) and tree[left] != 0:
        if total + tree[left] <= target:
            yield from find_paths(
                tree, target, total + tree[left], path + [tree[left]], left
            )

    if right < len(tree) and tree[right] != 0:
        if total + tree[right] <= target:
            yield from find_paths(
                tree, target, total + tree[right], path + [tree[right]], right
            )


def main():
    for line in sys.stdin:
        target = int(line)
        tree = list(map(int, sys.stdin.readline().split()))
        res = list(find_paths(tree, target, tree[0], [tree[0]]))
        res = sorted(res)
        if not res:
            print(f"{target}:")
        else:
            for path in res:
                print(f"{target}:", ", ".join(list(map(str, path))))


if __name__ == "__main__":
    main()
