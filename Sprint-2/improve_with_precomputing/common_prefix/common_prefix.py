from typing import List


def find_longest_common_prefix(strings: List[str]):
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """
    seen = set()
    longest = ""
    for string in strings:
        for i in range(1, len(string) + 1):
            prefix = string[:i]
            if prefix in seen and len(prefix) > len(longest):
                longest = prefix

            seen.add(prefix)
    return longest
