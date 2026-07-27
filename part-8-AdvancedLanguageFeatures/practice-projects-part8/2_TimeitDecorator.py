# E2 — @timeit Decorator

# Write @timeit that:
# -> Times how long the wrapped function takes (time.perf_counter())
# -> Prints "<function_name> took X.XXXXs" to sys.stderr after the call
# -> Returns the wrapped function's result unchanged
# -> Uses @functools.wraps to preserve function metadata

# Verification:

# import time
# from functools import wraps

# @timeit
# def slow_square(x):
#     """Returns x squared, slowly."""
#     time.sleep(0.05)
#     return x * x

# assert slow_square(3) == 9
# assert slow_square.__name__ == "slow_square"       # @wraps preserved
# assert "slowly" in slow_square.__doc__             # docstring preserved

# Why: every real ML training script has a timer decorator. Basic profiling.

import time
import sys
from functools import wraps

def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{fn.__name__} took {elapsed:.4f}s", file=sys.stderr)
        return result
    return wrapper

@timeit
def slow_square(x):
    """Returns x squared, slowly."""
    time.sleep(0.05)
    return x * x

assert slow_square(3) == 9
assert slow_square.__name__ == "slow_square"       # @wraps preserved
assert "slowly" in slow_square.__doc__             # docstring preserved

print("All assertions passed!")

