# E2 — Input Validation Loop

# Keep asking the user for a positive integer between 1 and 100.
# If they enter something outside that range, print "invalid, try again" and ask again.
# Only exit the loop when they give a valid number, then print "accepted: <n>".

# Verification: Test with -5, 0, 101, 50. The loop must never exit on invalid input.
# Assume the user always enters a number.

num = int(input("Please enter a number between 1 and 100 -> "))

while num < 1 or num > 100 :
    num = int(input("INVALID INPUT. Please enter a number between 1 and 100 -> "))
else:
    print("Accepted")