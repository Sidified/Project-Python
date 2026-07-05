# Hard1(H1) — Palindrome Cleaner (cumulative — recalls Part II: string immutability + slicing)

#Given: text = "A man, a plan, a canal: Panama" (hardcode it).

#Task:
# Iterate through text character by character.

# Build a new string cleaned containing only lowercase alphanumeric characters.
# (You may use .isalnum() and .lower() — both are string methods.)

# Compare cleaned against its reverse (cleaned[::-1]).

# Print "palindrome" or "not a palindrome".

# At the end, print text again and confirm it's unchanged from the original.
# Print id(text) before step 1 and after step 4 — they must match.

# Part II recall being tested: strings are immutable. You cannot "clean text in place."
# You must build a new string. If you try to write text = text.lower() and
# then loop, you've already mutated the reference and the id check will fail.
# Your loop should read from text and write to a separate cleaned variable.

#Verification:
# - The given input should return "palindrome" (cleaned = "amanaplanacanalpanama").
# - Change to text = "hello world" — expect "not a palindrome".
# - The id(text) before and after must be identical,
# and the printed text must still contain the original commas, colon, and mixed case.

# step 1
text = "A man, a plan, a canal: Panama"
idt = id(text)

# step 2
cleaned = "".join([c for c in text.lower() if c.isalnum()])

# step 3
revCleaned = cleaned[::-1]

# step 4
if cleaned == revCleaned:
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")

print(text)

idtA = id(text)

print(idt)
print(idtA)