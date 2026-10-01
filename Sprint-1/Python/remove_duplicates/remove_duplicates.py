from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


# def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
#     """
#     Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

#     Time complexity:
#     Space complexity:
#     Optimal time complexity:
#     """
#     unique_items = []

#     for value in values:
#         is_duplicate = False
#         for existing in unique_items:
#             if value == existing:
#                 is_duplicate = True
#                 break
#         if not is_duplicate:
#             unique_items.append(value)

#     return unique_items

def remove_duplicates(values):
    seen = set()
    result = []

    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result