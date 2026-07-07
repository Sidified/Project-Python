# E2 — Token → ID 

# Hardcode:
# pythontokens = ["hello", "world", "hello", "python", "world", "hello", "ai"]

# Build a dictionary token_to_id where each unique token maps to a unique integer ID,
# assigned in the order they first appear. Then build the reverse mapping id_to_token.
# Print both.

# Expected output:
# token_to_id: {'hello': 0, 'world': 1, 'python': 2, 'ai': 3}
# id_to_token: {0: 'hello', 1: 'world', 2: 'python', 3: 'ai'}

# Do NOT use enumerate(set(tokens)) — sets don't preserve insertion
# order for iteration in the way you need here.
# Build it manually with a loop and an in check.

# Verification: len(token_to_id) == len(id_to_token) == number of unique tokens.
# Every key in one must appear as a value in the other.

# Why this matters: this is how every tokenizer's vocabulary is built. Literally.

pythontokens = ["hello", "world", "hello", "python", "world", "hello", "ai"]

tokens = []
token_to_id = {}
id_to_token = {}

for i in pythontokens:
    if i in tokens:
        continue
    else:
        tokens.append(i)


idx = 0
for i in tokens:
    token_to_id[i] = idx
    idx+=1

print(token_to_id)

k = 0
for t in tokens:
    id_to_token[k] = t
    k+=1

print(id_to_token)




