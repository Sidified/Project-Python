# P3 (Easy) — Filename Anatomy via Slicing
# Hardcode this string: filename = "model_v2_final_2026-07-03.safetensors"
# Using only slicing and indexing (no .split(), no .find()), extract and print:
# -> The first 5 characters
# -> The extension including the dot (last 12 characters)
# -> The date substring "2026-07-03" (figure out the indices)
# -> The whole string reversed


filename = "model_v2_final_2026-07-03.safetensors"

f5 = filename[0:5]
print(f5)

ex = filename[-12:]
print(ex)

dt = filename[15:25]
print(dt)

rev = filename[::-1]
print(rev)