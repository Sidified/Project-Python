# E1 — Vocabulary Class

# Build a Vocabulary class that encapsulates what you
# built in Part IV's P2 and H1 (token↔id maps), but now as a class instead of loose dicts.

# Requirements:
# -> __init__(self): initialize empty _token_to_id and _id_to_token dicts
#    (leading underscore signals "internal — don't touch from outside")
# -> add(self, token): adds the token if new, returns its id (existing or newly assigned)
# -> encode(self, tokens): takes a list of tokens, returns a list of ids (adds any new tokens)
# -> decode(self, ids): takes a list of ids, returns a list of tokens;
#    raise KeyError with a clear message if any id isn't in the vocab
# -> __len__(self): returns the number of tokens in the vocab (so len(vocab) works)
# -> __contains__(self, token): returns True if the token is in the vocab
#    (so "hello" in vocab works)
# -> __repr__(self): returns something like Vocabulary(size=42)

# Verification (all in code):
# v = Vocabulary()
# ids = v.encode(["hello", "world", "hello"])
# assert ids == [0, 1, 0]
# assert len(v) == 2
# assert "hello" in v
# assert "goodbye" not in v
# assert v.decode([0, 1]) == ["hello", "world"]
# assert repr(v) == "Vocabulary(size=2)"

# decode with unknown id must raise
# try:
#     v.decode([0, 99])
#     raise AssertionError("expected KeyError")
# except KeyError:
#     pass

# Why this matters: this is the shape of every real tokenizer class
# (HuggingFace, sentencepiece, tiktoken). They have the same public interface
# with more sophisticated internals.

class Vocabulary:
    def __init__(self):
        self._token_to_id = {}
        self._id_to_token = {}

    def add(self, token):
        if token not in self._token_to_id:
            self._token_to_id[token] = len(self._token_to_id)
            self._id_to_token[self._token_to_id[token]] = token

        return self._token_to_id[token]
 
    def encode(self, tokens):
        idList = []
        for item in tokens:
           tokenId =  self.add(item)
           idList.append(tokenId)

        return idList
    
    def decode(self, ids):
        tokenList = []
        for item in ids:
            if item not in self._id_to_token:
                raise KeyError(f"Unknown token id: {item}")
            else:
                token = self._id_to_token[item]
                tokenList.append(token)

        return tokenList
    
    def __len__(self):
        return len(self._token_to_id)
    
    def __contains__(self, token):
        return token in self._token_to_id
        
    def __repr__(self):
        return f"Vocabulary(size={len(self._token_to_id)})"
    

v = Vocabulary()
ids = v.encode(["hello", "world", "hello"])
assert ids == [0, 1, 0]
assert len(v) == 2
assert "hello" in v
assert "goodbye" not in v
assert v.decode([0, 1]) == ["hello", "world"]
assert repr(v) == "Vocabulary(size=2)"

# decode with unknown id must raise
try:
    v.decode([0, 99])
    raise AssertionError("expected KeyError")
except KeyError:
    pass

print("All assertions passed!")