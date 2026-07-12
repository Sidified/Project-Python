# BOSS — Function Composition Pipeline

# Build make_pipeline(*steps) that takes any number of one-argument
# functions and returns a new function. That returned function,
# when called with input x, applies each step in order:
# pipeline = make_pipeline(f, g, h)
# pipeline(x)  # equivalent to h(g(f(x)))

# Note the order: leftmost function runs first, rightmost runs last.
# This is intuitive left-to-right reading.

# Then define these transforms:
# def to_lower(text):
#     return text.lower()

# def strip_punctuation(text):
#     for ch in ".,!?;:":
#         text = text.replace(ch, "")
#     return text
# 
# def tokenize(text):
#     return text.split()

# def filter_short(tokens, min_len=3):
#     return [t for t in tokens if len(t) >= min_len]

# Build this pipeline and test it:
# pipe = make_pipeline(
#     to_lower,
#     strip_punctuation,
#     tokenize,
#     lambda tokens: filter_short(tokens, min_len=4),
# )

# result = pipe("Hello, World! This is a Test of my Pipeline.")

# Verification: decide what the expected output is by tracing
# through each step by hand. Then assert. If you don't want to trace
# by hand, that's a signal that verification is theatrical — do it.
# Expected (I'll give you this one): ["hello", "world", "this", "test", "pipeline"].
# Assert this.

# Then test with different pipelines:
# -> Empty pipeline: make_pipeline() — should return input unchanged.
#    pipeline("test") == "test". Assert.
# -> Single step: make_pipeline(to_lower)("HELLO") == "hello". Assert.

# Concepts used:
# *args (accepting arbitrary functions), closures (the returned function captures steps),
# lambdas (wrapping a multi-arg function into a single-arg one via
# lambda tokens: filter_short(tokens, min_len=4)), higher-order
# functions (functions taking and returning functions).

# Verification (final): three assertions minimum — full pipeline,
# empty pipeline, single-step pipeline.

# Why this problem:
# sklearn.pipeline.Pipeline, LangChain's
# Runnable chains, HuggingFace transforms — all of these are
# compositional pipelines. If you understand this problem, you understand
# the idea underneath all of them. The frameworks add types, error
# handling, and parallelism, but the core is what you're building here.


def make_pipeline(*steps):
    def funct(x):
        for item in steps:
            x = item(x)
        return x
    return funct


def to_lower(text):
    return text.lower()

def strip_punctuation(text):
    for ch in ".,!?;:":
        text = text.replace(ch, "")
    return text

def tokenize(text):
    return text.split()

def filter_short(tokens, min_len=3):
    return [t for t in tokens if len(t) >= min_len]

pipe = make_pipeline(
    to_lower,
    strip_punctuation,
    tokenize,
    lambda tokens: filter_short(tokens, min_len=4),
)

empty_PL = make_pipeline()

result = pipe("Hello, World! This is a Test of my Pipeline.")
assert result == ["hello", "world", "this", "test", "pipeline"]
assert empty_PL("test") == "test"
assert make_pipeline(to_lower)("HELLO") == "hello"

print("All assertions passed!")



