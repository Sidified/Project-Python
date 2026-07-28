# M2 — @retry Decorator with Arguments

# Write retry(max_attempts=3, on_exception=Exception) as a
# decorator factory — the three-level nested form.

# @retry(max_attempts=3, on_exception=ConnectionError)
# def flaky_call():
#     ...

# Requirements:
# -> Three levels: outer takes args, middle takes the function, inner wraps the call
# -> Uses @wraps
# -> Retries only on the specified exception class (unrelated exceptions should propagate immediately)
# -> Warning to stderr on each failed attempt with attempt number
# -> After max_attempts failures, re-raises the last exception

# Verification:

# attempts = [0]

# @retry(max_attempts=3, on_exception=ConnectionError)
# def flaky():
#     attempts[0] += 1
#     if attempts[0] < 3:
#         raise ConnectionError(f"fail {attempts[0]}")
#     return "ok"

# assert flaky() == "ok"
# assert attempts[0] == 3
# assert flaky.__name__ == "flaky"

# # Always-fails must re-raise
# @retry(max_attempts=2, on_exception=ConnectionError)
# def always_fails():
#     raise ConnectionError("nope")

# try:
#     always_fails()
#     raise AssertionError("expected ConnectionError")
# except ConnectionError:
#     pass

# # Wrong exception type must NOT be caught
# @retry(max_attempts=3, on_exception=ConnectionError)
# def raises_value_error():
#     raise ValueError("wrong type")

# try:
#     raises_value_error()
#     raise AssertionError("expected ValueError to propagate")
# except ValueError:
#     pass  # correct — not caught by retry

# Why: every API client in every AI codebase has some form of this.
# @retry(on_exception=RateLimitError) is what wraps every OpenAI/Anthropic
# SDK call in production.

# Recall from Part VI: you wrote retry(fn, ...) as a wrapper function.
# This is the same logic, restructured as a decorator. Both patterns are
# valid; you'll see decorators far more often in real code.

from functools import wraps
import sys

def retry(max_attempts=3, on_exception=ConnectionError):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except on_exception as e:
                    print(f"Warning: Attempt {attempt} failed: {e}", file=sys.stderr)
                    last_exception = e
            raise last_exception
            
        return wrapper
    
    return decorator


attempts = [0]

@retry(max_attempts=3, on_exception=ConnectionError)
def flaky():
    attempts[0] += 1
    if attempts[0] < 3:
        raise ConnectionError(f"fail {attempts[0]}")
    return "ok"

assert flaky() == "ok"
assert attempts[0] == 3
assert flaky.__name__ == "flaky"

# Always-fails must re-raise
@retry(max_attempts=2, on_exception=ConnectionError)
def always_fails():
    raise ConnectionError("nope")

try:
    always_fails()
    raise AssertionError("expected ConnectionError")
except ConnectionError:
    pass

# Wrong exception type must NOT be caught
@retry(max_attempts=3, on_exception=ConnectionError)
def raises_value_error():
    raise ValueError("wrong type")

try:
    raises_value_error()
    raise AssertionError("expected ValueError to propagate")
except ValueError:
    pass  # correct — not caught by retry

print("All assertions passed!")