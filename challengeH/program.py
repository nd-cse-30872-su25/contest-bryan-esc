#!/usr/bin/env python3

import sys
from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    parents: set[str] = field(default_factory=set)
    children: set[str] = field(default_factory=set)
    spouses: set[str] = field(default_factory=set)


@dataclass
class FamilyTree:
    members: dict[str, Person] = field(default_factory=dict)

    def get_or_create_person(self, name: str) -> Person:
        if name not in self.members:
            self.members[name] = Person(name=name)
        return self.members[name]

    def add_family_relationship(
        self, parent1_name: str, parent2_name: str, children_names: list[str]
    ):
        parent1 = self.get_or_create_person(parent1_name)
        parent2 = self.get_or_create_person(parent2_name)

        parent1.spouses.add(parent2_name)
        parent2.spouses.add(parent1_name)

        for child_name in children_names:
            child = self.get_or_create_person(child_name)

            parent1.children.add(child_name)
            parent2.children.add(child_name)

            child.parents.add(parent1_name)
            child.parents.add(parent2_name)

    def get_siblings(self, person_name: str) -> set[str]:
        person = self.members[person_name]

        siblings = set()

        for parent_name in person.parents:
            if parent := self.members.get(parent_name):
                for child in parent.children:
                    if child != person_name:
                        siblings.add(child)
        return siblings

    def get_nieces_nephews(self, giver_name: str) -> set[str]:
        giver = self.members[giver_name]

        nieces_nephews = set()

        direct_siblings = self.get_siblings(giver_name)
        for sibling_name in direct_siblings:
            if sibling := self.members[sibling_name]:
                nieces_nephews.update(sibling.children)

        for spouse_name in giver.spouses:
            spouse_siblings = self.get_siblings(spouse_name)
            for spouse_sib_name in spouse_siblings:
                if spouse_sib := self.members.get(spouse_sib_name):
                    nieces_nephews.update(spouse_sib.children)

        return nieces_nephews


def main():
    while True:
        try:
            num_families = int(sys.stdin.readline().strip())
            if num_families == 0:
                break
        except ValueError:
            break

        family_tree = FamilyTree()

        for _ in range(num_families):
            line = sys.stdin.readline().strip()
            parts = line.split(":")
            parents = parts[0].strip()
            children = parts[1].strip()

            parent_names = parents.split()
            children_names = children.split()

            family_tree.add_family_relationship(
                parent_names[0], parent_names[1], children_names
            )

        num_gift_givers = int(sys.stdin.readline().strip())

        for _ in range(num_gift_givers):
            giver_name = sys.stdin.readline().strip()
            nieces_nephews = family_tree.get_nieces_nephews(giver_name)

            if not nieces_nephews:
                print(f"{giver_name} does not need to buy gifts")
            else:
                sorted_gifts = sorted(list(nieces_nephews))
                print(f"{giver_name} needs to buy gifts for: {', '.join(sorted_gifts)}")


if __name__ == "__main__":
    main()
