# H1 (Cumulative — recalls Part V) — Retry Wrapper for Flaky Calls

# Write retry(fn, max_attempts=3, on_exception=Exception):
# -> Calls fn() (a no-argument function)
# -> If it raises on_exception, catches it and retries — up to max_attempts total attempts
# -> If any attempt succeeds, return the result
# -> If all attempts fail, re-raise the last exception
# -> Print a warning to stderr on each failed attempt including the attempt number

# Test with a flaky function:
# attempts = [0]  # mutable counter

# def flaky_api_call():
#     attempts[0] += 1
#     if attempts[0] < 3:
#         raise ConnectionError(f"simulated network fail on attempt {attempts[0]}")
#     return {"status": "ok", "data": [1, 2, 3]}

# Call retry(flaky_api_call, max_attempts=3, on_exception=ConnectionError).
# Should succeed on the 3rd attempt.

# Also test the "always fails" case:
# def always_fails():
#     raise ConnectionError("this always fails")

# Wrap this in retry with max_attempts=3. Verify it raises ConnectionError after 3 attempts.

# Part V recall: you're passing a function as an argument (first-class functions) and
# using the closure-style mutable counter trick you learned in P6 to simulate
# state across attempts.

# Verification: assert the successful call returns {"status": "ok", "data": [1, 2, 3]}.
# For the always-fails case, use try/except ConnectionError and assert the
# exception was raised. Also assert attempts[0] == 3 at the end of the success
# test — proving it actually retried the right number of times.

# Why this matters: every real API call needs retry logic. HTTP errors, rate limits,
# transient network failures. You'll write this shape of code hundreds of times.

import sys

def retry(fn, max_attempts=3, on_exception=Exception):
    count = 0
    while count < max_attempts:
        count+=1
        try:
            ans = fn()
            return ans
        except on_exception as e:
            print(f"WARNING: Attempt number {count} failed: {e}", file=sys.stderr)
            if count == max_attempts:
                raise


attempts = [0]

def flaky_api_call():
    attempts[0] += 1
    if attempts[0] < 3:
        raise ConnectionError(f"simulated network fail on attempt {attempts[0]}")
    return {"status": "ok", "data": [1, 2, 3]}

print("")
print("--------------CALLING THE FLAKY_API_CALL()--------------")
statement = retry(flaky_api_call, max_attempts=3, on_exception=ConnectionError)

assert statement == {"status": "ok", "data": [1, 2, 3]}
assert attempts[0] == 3

print("")
print("---------------CALLING THE ALWAYS_FAILS()---------------")
def always_fails():
    raise ConnectionError("this always fails")

try:
    retry(always_fails, max_attempts=3, on_exception=ConnectionError)

    assert False, "Expected ConnectionError"

except ConnectionError:
    pass

print("")
print("--------------------------------------------------------")
print("All assertions passed!")
print("--------------------------------------------------------")
