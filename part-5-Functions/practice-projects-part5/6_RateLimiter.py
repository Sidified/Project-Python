# H1 (Cumulative — recalls Part IV) — Rate Limiter (Closure)

# Write make_rate_limiter(limit) that returns a function.
# The returned function takes no arguments.
# Each call:
# -> Returns True if the call is allowed (under the limit)
# -> Returns False if the limit has been reached
# -> Tracks its own call count using a closure over the enclosing scope

# Example use:
# allow = make_rate_limiter(3)
# print(allow())  # True (1st call)
# print(allow())  # True (2nd call)
# print(allow())  # True (3rd call)
# print(allow())  # False (4th call — over limit)
# print(allow())  # False (5th call — still over limit)

# Two hints:
# -> You can use nonlocal to modify a variable in the enclosing scope
# -> Alternatively, use a mutable container in the
#    enclosing scope (e.g., a list with one element) and
#    mutate it — no nonlocal needed. This works because you're
#    mutating the list, not rebinding the name.

# Do it with whichever approach clicks. If you want to be
# thorough, try both in the same file.

# Part IV recall being tested: the mutable-container
# trick works because lists are mutable — the same lesson from
# Part I & IV. If you had used an int (counter = 0) and tried
# counter += 1 inside the inner function without nonlocal,
# you'd get an UnboundLocalError. Understanding why is the point.

# Verification: create a rate limiter with limit=3.
# Call it 5 times. Assert the sequence of
# returns is [True, True, True, False, False].

# Method_1 -> Using nonlocal to modify a variable in the enclosing scop
def make_rate_limiter(limit):
    lim = limit
   
    def rate_limiter():
        nonlocal lim
        if lim > 0:
            lim-=1
            return True
        else:
            return False
    return rate_limiter


allow = make_rate_limiter(3)
assert allow() == True # True (1st call)
assert allow() == True  # True (2nd call)
assert allow() == True  # True (3rd call)
assert allow() == False  # False (4th call — over limit)
assert allow() == False # False (5th call — still over limit)

print("All assertions passed!")

# Method_2 -> Using a mutable container in the enclosing scope
def make_rate_limiter2(limit):
    lim = [limit]
   
    def rate_limiter2():
        if lim[0] != 0:
            lim[0] = lim[0] - 1
            return True
        else:
            return False
    return rate_limiter2

allow2 = make_rate_limiter2(3)
assert allow2() == True # True (1st call)
assert allow2() == True  # True (2nd call)
assert allow2() == True  # True (3rd call)
assert allow2() == False  # False (4th call — over limit)
assert allow2() == False # False (5th call — still over limit)

print("All assertions passed. Again!")