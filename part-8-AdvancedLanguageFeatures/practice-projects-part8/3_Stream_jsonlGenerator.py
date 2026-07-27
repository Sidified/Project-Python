# M1 — stream_jsonl Generator

# Write  as a generator that yields records
# one at a time from a JSONL file. This is the streaming version of Part VI's read_jsonl.

# Requirements:stream_jsonl(path)
# -> Yields each parsed record (don't accumulate into a list internally)
# -> Skips empty lines silently
# -> Skips malformed lines with a warning to sys.stderr including the line number
# -> Uses with open(...) correctly — the with block must remain open across yield statements

# Verification:

# import types

# # Create a test file with valid, empty, and malformed lines
# # (5 valid + 1 empty + 1 malformed = 5 records yielded)

# gen = stream_jsonl("data/test_stream.jsonl")
# assert isinstance(gen, types.GeneratorType)     # it's a generator, not a list

# records = list(gen)
# assert len(records) == 5
# assert all(isinstance(r, dict) for r in records)

# # One-shot exhaustion
# assert list(gen) == []

# The with open(...) inside a generator is a subtle point worth pausing on:
# the file stays open as long as the generator is alive. When the generator
# is fully consumed (or garbage collected), the file closes. This is why using
# generators for streaming file reads is safe.

# Why: real ML datasets don't fit in memory. If you built read_jsonl from Part VI
# to return a list, a 200GB training file crashes it. stream_jsonl handles it in constant memory.

import json
import sys
import types

def stream_jsonl(path):
    count = 0
    with open(path, "r") as f:
        for line in f:
            count+=1
            if line.strip() == "":
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                print(f"Warning: malformed JSON on line -> {count}", file=sys.stderr)



# Create a test file with valid, empty, and malformed lines
# (5 valid + 1 empty + 1 malformed = 5 records yielded)

gen = stream_jsonl("part-8-AdvancedLanguageFeatures/practice-projects-part8/data/stream.jsonl")
assert isinstance(gen, types.GeneratorType)     # it's a generator, not a list

records = list(gen)
assert len(records) == 5
assert all(isinstance(r, dict) for r in records)

# One-shot exhaustion
assert list(gen) == []

print("All assertions passed!")