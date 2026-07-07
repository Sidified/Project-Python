# E3 — Set Operations on Model Predictions

# Hardcode:
# pythonpredicted = ["cat", "dog", "bird", "fish", "cat", "cat"]
# actual = ["dog", "bird", "cat", "rabbit", "fish"]

# Convert both to sets. Print:
# -> correct — items predicted AND in actual
# -> hallucinated — predicted but not in actual
# -> missed — in actual but not predicted
# -> union — everything mentioned by either

# Use set operators (&, -, |), not manual loops.
# Verification: For any two sets A and B: |A ∪ B| = |A| + |B| - |A ∩ B|.
# Print all sizes and check this identity holds.

pythonpredicted = ["cat", "dog", "bird", "fish", "cat", "cat"]
actual = ["dog", "bird", "cat", "rabbit", "fish"]

setPred = set(pythonpredicted)
setActual = set(actual)

print(setPred & setActual)  # -> correct
print(setPred - setActual)  # -> hallucinated
print(setActual - setPred)  # -> missed
print(setActual | setPred)  # -> union

aUnionB = len(setPred | setActual)  # -> |A ∪ B|
aLen = len(setPred)  # -> |A|
bLen = len(setActual)  # -> |B|
aInterB = len(setPred & setActual)  # -> |A ∩ B|

print(aUnionB == aLen + bLen - aInterB) # -> |A ∪ B| = |A| + |B| - |A ∩ B|.