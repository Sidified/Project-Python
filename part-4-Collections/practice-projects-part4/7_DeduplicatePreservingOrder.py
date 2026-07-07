# M4 — Deduplicate Preserving Order

# Hardcode:
# sequence = ["a", "b", "a", "c", "b", "d", "e", "a", "f", "c"]
# Return a new list with duplicates removed, preserving the order of first appearance.
# Expected: ["a", "b", "c", "d", "e", "f"].

# Two versions in the same file:
# dedup_v1: uses only a list and in checks (O(n²))
# dedup_v2: uses a set for O(1) lookups + a list for order (O(n))

# Print both results and confirm they're identical.

# Verification: Both outputs must equal ["a", "b", "c", "d", "e", "f"].
# Assert dedup_v1 == dedup_v2.

# Why this matters: set() alone doesn't preserve order
# (well, in modern Python it kind of does by insertion for dicts, but not sets).
# Real-world dedup while preserving order is a common enough
# task that you should know both the naive and efficient way.

sequence = ["a", "b", "a", "c", "b", "d", "e", "a", "f", "c"]

dedup_v1 = []

for i in sequence:
    if i in dedup_v1:
        continue
    else:
        dedup_v1.append(i)
print(dedup_v1)

dedup_v2 = sorted(set(dedup_v1))
print(dedup_v2)

print(dedup_v1 == dedup_v2)