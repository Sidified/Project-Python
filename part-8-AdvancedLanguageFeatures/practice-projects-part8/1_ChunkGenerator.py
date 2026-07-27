# E1 — Chunk Generator

# Write chunk(iterable, size) that yields lists of size
# elements from any iterable. The last chunk may be smaller.

# list(chunk([1, 2, 3, 4, 5, 6, 7], 3))
# # [[1, 2, 3], [4, 5, 6], [7]]

# Requirements:
# -> Must be a generator (uses yield, doesn't build a list internally)
# -> Must work on any iterable, not just lists — so don't index into it; iterate
# -> Must be lazy — if given an infinite iterable, calling next(chunk(...))
#    should return the first chunk in constant time

# Verification:
# -> assert list(chunk([1, 2, 3, 4, 5, 6, 7], 3)) == [[1, 2, 3], [4, 5, 6], [7]]
# -> assert list(chunk([], 3)) == []
# -> assert list(chunk("abcdef", 2)) == [["a", "b"], ["c", "d"], ["e", "f"]]

# # Laziness check: chunking an infinite generator must not hang
# import itertools
# first_two = list(itertools.islice(chunk(itertools.count(), 5), 2))
# assert first_two == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

# # One-shot exhaustion check
# g = chunk([1, 2, 3, 4], 2)
# list(g)  # consume
# assert list(g) == []  # empty on second pass

# Why: batching is fundamental. Every ML DataLoader batches this way.


def chunk(seq, n):
    itemList = []
    for item in seq:
        itemList.append(item)
        if len(itemList) == n:
            yield itemList
            itemList = []
    if itemList:
        yield itemList


# VERIFICATION

assert list(chunk([1, 2, 3, 4, 5, 6, 7], 3)) == [[1, 2, 3], [4, 5, 6], [7]]
assert list(chunk([], 3)) == []
assert list(chunk("abcdef", 2)) == [["a", "b"], ["c", "d"], ["e", "f"]]

# Laziness check: chunking an infinite generator must not hang
import itertools
first_two = list(itertools.islice(chunk(itertools.count(), 5), 2))
assert first_two == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

# One-shot exhaustion check
g = chunk([1, 2, 3, 4], 2)
list(g)  # consume
assert list(g) == []  # empty on second pass

print("All assertions passed!")