#!/usr/bin/env python3

import sys

points = (2, 3, 7)


# def find_targets(target: int, total: int = 0, total_list=[]):
#     if total == target:
#         yield sorted(total_list)
#     for point in points:
#         if total + point <= target:
#              yield from find_targets(target, total + point, total_list + [point])
# def solve(target: int):
#     result = [target + 1] * (target + 1)
#     ways_result = [[] for _ in range(target+1)]
#
#     result[0] = 0
#     for i in range(1, target+1):
#         for point in points:
#             if i >= point and result[i-point]+1  < result[i]:
#                 result[i] = result[i-point]+1
#                 ways_result[i] = ways_result[i-point]+[point]
#     if result[target] == target+1:
#         return []
#
#     print(ways_result)
#     return ways_result[target]


def solve(amount: int):
    res = []

    def backtrack(end, remain, cur_result):
        if end < 0:
            return
        if remain == 0:
            res.append(sorted(cur_result))
            return
        if remain >= points[end]:
            backtrack(end, remain - points[end], cur_result + [points[end]])
        backtrack(end - 1, remain, cur_result)

    backtrack(len(points) - 1, amount, [])
    return res


def main():
    for line in sys.stdin:
        target = int(line)
        result = sorted([v for v in solve(target) if len(v) > 0])
        if len(result) == 1:
            print(f"There is {len(result)} way to achieve a score of {target}:")
        else:
            print(f"There are {len(result)} ways to achieve a score of {target}:")
        for res in result:
            print(" ".join(list(map(str, res))))


if __name__ == "__main__":
    main()
