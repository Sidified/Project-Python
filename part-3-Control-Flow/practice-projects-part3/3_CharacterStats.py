# E3 — Character Stats

# Hardcode: text = "Deep Learning in 2026 is mostly transformers, and some RL."
# Iterate through the string.
# Count:
# vowels (a, e, i, o, u, case-insensitive)
# digits
# spaces
# everything else

#Print all four counts. Also print total = vowels + digits + spaces + others
# and confirm it equals len(text).
#Verification: The total == len(text) check IS the verification — if you miss a category,
# the totals won't match.

text = "Deep Learning in 2026 is mostly transformers, and some RL."

vowels_set = "aeiouAEIOU"
vowels = 0
digits = 0
spaces = 0
evElse = 0
for i in text:
    if i in vowels_set:
        vowels+=1
    elif i.isdigit():
        digits +=1
    elif i.isspace():
        spaces+=1
    else:
        evElse+=1
length = vowels + digits + spaces + evElse
print(f"The total vowels in the string 'text' is -> {vowels}")
print(f"The total digits in the string 'text' is -> {digits}")
print(f"The total spaces in the string 'text' is -> {spaces}")
print(f"Everythin else in the string 'text' is -> {evElse}")
print(f"The length is the string will be {len(text)} which is equal to {length}")