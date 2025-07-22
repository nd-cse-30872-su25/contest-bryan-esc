#!/usr/bin/env python3

import sys
import itertools

signs = ("+", "*", "-")


def main():
    for line in sys.stdin:
        target = int(line)
        signs_list = itertools.product(signs, repeat=8)
        eq = "(((9 ? 8) ? 7) ? 6) ? (5 ? (4 ? (3 ? (2 ? 1))))"
        for sign in signs_list:
            result = ""
            index = 0
            for char in eq:
                if char == "?":
                    result += sign[index]
                    index += 1
                else:
                    result += char
            if eval(result) == target:
                print(f"{result} = {target}")
                break


if __name__ == "__main__":
    main()
