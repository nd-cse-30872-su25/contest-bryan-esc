#!/usr/bin/env python3

import sys
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    name: str
    spouse: str
    children: list["Node"]
    parent: Optional["Node"]

    def add_child(self, child: list["Node"]):
        self.children = child

    def add_parent(self, parent: "Node"):
        self.parent = parent


@dataclass
class Family:
    members = {}

    def add_person(self, person: Node):
        if person.name not in self.members:
            self.members[person.name] = person


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
