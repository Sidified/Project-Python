# E1 — Batch Splitter

# Given a list of items and a batch size, split it into batches of that size.
# Last batch may be smaller.

# items = list(range(23))   # [0, 1, 2, ..., 22]
# batch_size = 5

# Print each batch on its own line, prefixed with its index:

# Use slicing and a loop with range stepping by batch_size.
# Verification: With 23 items and batch_size=5, expect 5 batches (last one has 3 items).
# Total items across all batches must equal len(items) — check this at the end.

# Why this matters: every ML training loop batches its data this way.

items = list(range(23))
batch_size = 5

batches = []

count = 0
startIdx = 0
endIdx = 5

for i in range(0, len(items), batch_size):
    currentBatch = items[startIdx:endIdx]
    batches.append(currentBatch) 
    print(f"batch {count}: {items[startIdx:endIdx]}")
    count+=1
    startIdx+=batch_size
    endIdx+=batch_size

itemLen = 0
for i in range(0, len(batches)):
    itemLen+=len(batches[i])

print(f"Total items in all the batches are -> {itemLen}")