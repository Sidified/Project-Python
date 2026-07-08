
# H1 Mini Tokenizer + Reverse Lookup
# Hardcode:
# corpus = [
#    "The model is training well.",
#    "Training the model takes time.",
#    "The dataset is large and diverse.",
#    "Large models need diverse data."
#]
# Build a proper mini-tokenizer:

# 1. For each sentence, lowercase it, strip trailing punctuation from
#    each word (., ,, !, ?), and split into tokens.
# 2. Collect all unique tokens into a vocabulary dict {token: id},
#    IDs assigned in order of first appearance.
# 3. Create the reverse dict {id: token}.
# 4. Encode each original sentence into a list of IDs.
#    Store as a list-of-lists called encoded.
# 5. Decode encoded back into sentences using id_to_token and print them.
# 6. Verify: the decoded sentences should match the tokenized-and-cleaned
#    versions of the originals (lowercase, no trailing punctuation).
#    Print match: True/False for each sentence.


# Verification: len(vocab) == number of unique cleaned tokens.
# Every id in every encoded sentence must be a valid key in id_to_token.
# The match: True count must equal 4.

# Why this matters: you've now built the core of what a real tokenizer does.
# Real ones (BPE, WordPiece) are more sophisticated,
# but the encode/decode round-trip logic is identical.

# Part 1 ----------------------------------------------
corpus = [
    "The model is training well.",
    "Training the model takes time.",
    "The dataset is large and diverse.",
    "Large models need diverse data."
]

newCorpus = []
for sent in corpus:
    newCorpus.append((sent.lower()))

print(newCorpus)

tokensList = []

for sent in newCorpus:
    token = []
    for i in sent.split():
        word = i.strip(".,!?")
        token.append(word)
    tokensList.append(token)

print(tokensList)
# -------------------------------------------------------

# Part 2-------------------------------------------------
uniqueTokens = {}
idx = 0
for items in tokensList:
    for i in items:
        if i in uniqueTokens:
            continue
        else:
            uniqueTokens[i] = idx
            idx+=1

print(uniqueTokens)
assert set(uniqueTokens.values()) == set(range(len(uniqueTokens)))
# -------------------------------------------------------

# Part 3-------------------------------------------------
swapUniTok = {value: key for key, value in uniqueTokens.items()}

print(swapUniTok)
# -------------------------------------------------------

# Part 4-------------------------------------------------
encode = []

for item in tokensList:
    container = []
    for words in item:
        container.append(uniqueTokens[words])
    encode.append(container)

print(encode)
# -------------------------------------------------------

# Part 5-------------------------------------------------
decode = []

for item in encode:
    container = []
    for codes in item:
        container.append(swapUniTok[codes])
    decode.append(container)

print(decode)

decodeSent = []

for item in decode:
    sent = " ".join(item)
    decodeSent.append(sent)

print(decodeSent)
# --------------------------------------------------------

# Part 6--------------------------------------------------
clean = []

for item in newCorpus:
    clean.append(item.strip(".,!?"))

i = 0
for item in clean:
    print(item == decodeSent[i])
    i+=1
# --------------------------------------------------------