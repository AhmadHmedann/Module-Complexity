from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


# def find_common_items(
#     first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
# ) -> List[ItemType]:
#     """
#     Find common items between two arrays.

#     Time Complexity:
#     Space Complexity:
#     Optimal time complexity:
#     """
#     common_items: List[ItemType] = []
#     for i in first_sequence:
#         for j in second_sequence:
#             if i == j and i not in common_items:
#                 common_items.append(i)
#     return common_items


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    first_set = set(first_sequence)
    second_set = set(second_sequence)

    common = first_set.intersection(second_set)
    # common = first_set & second_set

    return list(common)
