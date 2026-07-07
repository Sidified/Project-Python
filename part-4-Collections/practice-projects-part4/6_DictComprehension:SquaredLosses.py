# M3 — Dict Comprehension: Squared Losses
# Hardcode:
# losses_per_epoch = {"epoch_1": 0.9, "epoch_2": 0.6, "epoch_3": 0.4, "epoch_4": 0.25, "epoch_5": 0.15}

# Using a dict comprehension (not a for-loop),
# build a new dict where each value is the square of the
# original (mimics squared-error weighting).Same keys.
# Then, using another dict comprehension with a
# filter, produce a dict containing only epochs where
# the original loss was below 0.5.

# Print both.
# Verification: The squared dict must have the same keys as the original.
# The filtered dict must have exactly 3 entries (epochs 3, 4, 5).

losses_per_epoch = {"epoch_1": 0.9, "epoch_2": 0.6, "epoch_3": 0.4, "epoch_4": 0.25, "epoch_5": 0.15}

newDict = {x: y * y for x, y in losses_per_epoch.items()}
print(newDict)

newDict2 = {x: y for x, y in losses_per_epoch.items() if y < 0.5}
print(newDict2)