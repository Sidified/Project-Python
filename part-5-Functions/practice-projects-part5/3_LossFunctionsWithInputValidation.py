# M1 — Loss Functions with Input Validation

# Write two functions:
# def mean_squared_error(predictions, targets): ...
# def mean_absolute_error(predictions, targets): ...

# Each takes two lists of equal length.
# Both must raise ValueError with a clear message if
# the lists differ in length.
# (You know how to compare len() and raise from Part III's raise?
# If not: raise ValueError("message here").)

# -> MSE = mean of (p - t) ** 2
# -> MAE = mean of abs(p - t)

# Verification: four test cases in code:
# assert mean_squared_error([1, 2, 3], [1, 2, 3]) == 0
# assert mean_absolute_error([1, 2, 3], [1, 2, 3]) == 0
# assert mean_squared_error([1, 2, 3], [2, 3, 4]) == 1.0
# assert mean_absolute_error([1, 2, 3], [2, 3, 4]) == 1.0

# Also test that mismatched-length inputs raise ValueError.
# Since you don't have try/except yet (Part VI), just call it with mismatched lengths,
# observe the error, and comment out that line before running the rest.
# Or wrap it in a small check — your choice.

# Why this matters: these are two of the most-used loss functions in all of ML.
# Every custom loss function you'll write follows this same
# shape: two aligned tensors, elementwise op, reduce to a scalar.

def mean_squared_error(predictions, targets):
    if len(predictions) != len(targets):
        raise ValueError("Lengths of list -> 'predictions' and list -> 'targets' are not equal")
    total = 0
    for pred, targ in zip(predictions, targets):
        total += ((pred - targ) ** 2)
    return total/len(predictions)
    
def mean_absolute_error(predictions, targets):
    if len(predictions) != len(targets):
        raise ValueError("Lengths of list -> 'predictions' and list -> 'targets' are not equal")
    total = 0
    for pred, targ in zip(predictions, targets):
        total += abs(pred - targ)
    return total/len(predictions)
    
assert mean_squared_error([1, 2, 3], [1, 2, 3]) == 0
assert mean_absolute_error([1, 2, 3], [1, 2, 3]) == 0
assert mean_squared_error([1, 2, 3], [2, 3, 4]) == 1.0
assert mean_absolute_error([1, 2, 3], [2, 3, 4]) == 1.0
assert mean_squared_error([1, 2, 3], [1.5, 2.5, 3.5]) == 0.25
assert mean_squared_error([1, 2, 3], [2.5, 3.5, 4.5]) == 2.25

print("All assertions passed!")

# This will raise the -> ValueError: Lengths of list -> 'predictions' and list -> 'targets' are not equal
# mean_squared_error([1, 2, 3], [1, 2])