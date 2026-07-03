# P2 (Easy) — Truthiness Table
# Hardcode these values in your script: 0, 0.0, -1, "", "0", " ", None, True, False.
# For each one, print a line showing the value and whether bool(value) is True or False.
# Format the output so the "Truthy?" column lines up neatly (use f-string width specifiers like {value!r:<10}).

a = 0
b = 0.0
c = -1
d = ""
e = " "
f = None
g = True
h = False
i = "0"

print(f"{'Variable':<10} | {'Value':<10} | {'Truthy?'}")
print("-" * 35)
print(f"{'a':<10} | {a!r:<10} | {bool(a)}")
print(f"{'b':<10} | {b!r:<10} | {bool(b)}")
print(f"{'c':<10} | {c!r:<10} | {bool(c)}")
print(f"{'d':<10} | {d!r:<10} | {bool(d)}")
print(f"{'e':<10} | {e!r:<10} | {bool(e)}")
print(f"{'f':<10} | {f!r:<10} | {bool(f)}")
print(f"{'g':<10} | {g!r:<10} | {bool(g)}")
print(f"{'h':<10} | {h!r:<10} | {bool(h)}")
print(f"{'i':<10} | {i!r:<10} | {bool(i)}")