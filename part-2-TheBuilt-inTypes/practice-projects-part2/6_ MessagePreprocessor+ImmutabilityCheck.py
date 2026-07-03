# P6 — Message Preprocessor + Immutability Check
# Hardcode: raw = "   USER: Hello, WORLD. today I love python!   "
# Do the following transformations, each on a separate line,
# storing intermediate results in new variables (step1, step2, …) so you can see each stage:

# 1) Strip leading/trailing whitespace
# 2) Remove the "USER: " prefix (use .removeprefix())
# 3) Lowercase everything
# 4) Replace "python" with "Python"
# 5) Wrap the cleaned result: f"<msg>{cleaned}</msg>"

#Print all intermediate steps and the final wrapped message.
#Then the important part:

# 6) Print raw again at the end. Did it change from its original value?
# 7) Print id(raw) at the very start (before step 1) and again at the end. Same or different?
# 8) Write a one-line comment in your code explaining why raw behaves the way it does,
# referencing what you learned in Part I.

raw = "   USER: Hello, WORLD. today I love python!   "
print(id(raw))

str1 = raw.strip()
print(str1)

str2 = str1.removeprefix("USER: ")
print(str2)

str3 = str2.lower()
print(str3)

str4 = str3.replace("python","Python")
print(str4)

str5 = f"<msg>{str4}</msg>"
print(str5)

print(raw)
print(id(raw)) # -> The Id has not changed because we never changed the 'raw' string. We only made new strings
#and 'raw' only changes if you write raw = raw.strip()