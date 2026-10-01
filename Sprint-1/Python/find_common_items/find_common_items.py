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
    second_set = set(second_sequence)
    common = []
    for item in first_sequence:
        if item in second_set:
            common.append(item)

    return common        
