# M2 — JSONL Reader with Bad-Line Tolerance

# JSONL = "JSON Lines" — one JSON object per line. It's the standard
# format for LLM training data, inference logs, and streaming datasets.

# Write data/logs.jsonl containing 6 lines:
# -> 4 valid JSON objects: e.g. {"user": "alice", "action": "click"},
#    {"user": "bob", "action": "purchase"}, etc.
# -> 1 line that's malformed JSON: e.g. {"user": broken
# -> 1 line that's empty (just \n)

# Then write read_jsonl(path) that returns a tuple (records, error_count):
# -> records is a list of parsed dicts from valid lines
# -> error_count is the number of skipped lines (malformed + empty)
# -> Malformed lines should be caught and skipped, not crash the function
# -> Print a warning to stderr for each skipped line, including the line number

# Hint: import sys; print("warning: ...", file=sys.stderr)

# Verification: assert len(records) == 4, assert error_count == 2,
# assert every record in records is a dict.

# Why this matters: real datasets have corrupt lines.
# Every JSONL loader in every ML pipeline you'll ever use
# has to handle this. If your loader crashes on the first
# bad line out of 10 million, you're rewriting it at 3am
# when the training run dies.

import json
import sys

path = "part-6-StructuringRealPrograms/practice-projects-part6/data/logs.jsonl"
with open(path, "w") as logs:
    logs.write('{"user": "alice", "action": "click"}\n')
    logs.write('{"user": "bob", "action": "purchased"}\n')
    logs.write('{"user": "charlie", "action": "seen"}\n')
    logs.write('{"user": "david", "action": "sent"}\n')
    logs.write('{"user": "broken\n')
    logs.write('\n')

def read_jsonl(path):
    records = []
    error_count = 0
    count = 0
    with open(path, "r") as file:
        for line in file:
            count+=1
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"WARNING: Skipped line {count}", file=sys.stderr)
                error_count+=1

        data = (records, error_count)

        return data

data = read_jsonl(path)

assert len(data[0]) == 4
assert data[1] == 2

for item in data[0]:
    assert isinstance(item, dict)

print("All assertions passed!")