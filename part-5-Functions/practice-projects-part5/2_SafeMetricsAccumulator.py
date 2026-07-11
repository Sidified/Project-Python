# E2 — Safe Metrics Accumulator (mutable default trap)

# Write add_metric(metric_value, history=None).
# If history is None, create a new empty list.
# Otherwise, append to the passed list.
# Return the resulting list.

# Test:
# add_metric(0.9)                  # expect [0.9]
# add_metric(0.8)                  # expect [0.8] — NOT [0.9, 0.8]
# add_metric(0.5, [0.9, 0.8])      # expect [0.9, 0.8, 0.5]

# Also write a broken version add_metric_broken(metric_value, history=[]) that
# demonstrates the mutable-default trap. Call it 3 times with
# just a value and print the result each time to prove the bug.

# Verification: assert the three good calls match expected outputs.
# Print the broken calls to observe the bug — the third call should
# output [0.9, 0.8, 0.5] instead of [0.5].

def add_metric(metric_value, history=None):
    if history is None:
        history = []
    history.append(metric_value)
    return history

result1 = add_metric(0.9)
result2 = add_metric(0.8)
result3 = add_metric(0.5, [0.9, 0.8])

assert result1 == [0.9]
assert result2 == [0.8]
assert result3 == [0.9, 0.8, 0.5]

print("All assertions passed!")


def add_metric_broken(metric_value, history=[]):
    history.append(metric_value)
    return history

print(add_metric_broken(0.9))
print(add_metric_broken(0.8))
print(add_metric_broken(0.5))


