# M3 — @contextmanager for Reproducible Random State

# Using @contextmanager from contextlib, write random_seed(seed) — a context manager that:
# -> On enter: saves the current random state, then calls random.seed(seed)
# -> On exit: restores the saved state
# -> Uses try/finally so the state is restored even if the block raises

# from contextlib import contextmanager
# import random

# @contextmanager
# def random_seed(seed):
#     ...

# Verification:
# import random

# random.seed(42)
# sequence_1 = [random.random() for _ in range(3)]

# random.seed(42)
# with random_seed(100):
#     inside = [random.random() for _ in range(3)]
# sequence_2 = [random.random() for _ in range(3)]

# # Since we restored state after the block, the outer sequences should match
# assert sequence_1 == sequence_2

# # The inside sequence should be different (used a different seed)
# assert inside != sequence_1

# # Exception inside must still restore state
# random.seed(42)
# try:
#     with random_seed(999):
#         random.random()  # advance
#         raise RuntimeError("boom")
# except RuntimeError:
#     pass
# sequence_3 = [random.random() for _ in range(3)]
# assert sequence_3 == sequence_1  # state restored despite exception

# Why: reproducibility is critical in ML. Every serious experiment runner
# saves and restores random state around specific operations — otherwise
# a debugging log statement in the middle of training changes the entire
# trajectory. This exact pattern generalizes to torch.manual_seed and numpy.random.seed.

from contextlib import contextmanager
import random

@contextmanager
def random_seed(seed):
    current_state = random.getstate()

    random.seed(seed)
    
    try:
        yield 
    finally:
        random.setstate(current_state)

# VERIFICATION

random.seed(42)
sequence_1 = [random.random() for _ in range(3)]

random.seed(42)
with random_seed(100):
    inside = [random.random() for _ in range(3)]
sequence_2 = [random.random() for _ in range(3)]

# Since we restored state after the block, the outer sequences should match
assert sequence_1 == sequence_2

# The inside sequence should be different (used a different seed)
assert inside != sequence_1

# Exception inside must still restore state
random.seed(42)
try:
    with random_seed(999):
        random.random()  # advance
        raise RuntimeError("boom")
except RuntimeError:
    pass
sequence_3 = [random.random() for _ in range(3)]
assert sequence_3 == sequence_1  # state restored despite exception

print("All assertions passed!")