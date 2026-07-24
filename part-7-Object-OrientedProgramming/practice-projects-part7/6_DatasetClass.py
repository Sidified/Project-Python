# H1 Dataset Class with __len__, __getitem__, and __iter__

# Build a Dataset class that behaves like a real ML dataset:
# -> __init__(self, path): loads a JSONL file from path
#    (reuse Part VI's read_jsonl pattern — skip malformed
#    lines with a warning). Store the records in a private list.
#    Raise FileNotFoundError if the file doesn't exist
#    (let the built-in exception propagate, don't wrap it).
# -> __len__(self): returns the number of records — enables len(dataset)
# -> __getitem__(self, idx): returns the record at that
#    index — enables dataset[0] and slice dataset[0:3]
#    (slice support: if idx is a slice, return a list of records;
#    else return a single record)
# -> __iter__(self): yields records one at a time — enables for record in dataset:
# -> __repr__(self): Dataset(path='X', size=N)
# -> filter(self, predicate): returns a new Dataset-like object
#    (a plain list of records is acceptable — you don't have to
#    preserve the class) containing only records where predicate(record) is truthy

# Prep step: create a JSONL file at data/dataset.jsonl with 10 records that look like:

# json
# {"text": "sample 1", "label": "positive", "score": 0.87}
# {"text": "sample 2", "label": "negative", "score": 0.42}

# Vary the labels and scores. Include one malformed line and one empty line —
# your Dataset must survive both.

# Verification:

# ds = Dataset("data/dataset.jsonl")
# assert len(ds) == 10                             # 10 valid, malformed/empty skipped
# assert isinstance(ds[0], dict)
# assert isinstance(ds[0:3], list) and len(ds[0:3]) == 3

# count = 0
# for record in ds:
#     assert "text" in record
#     count += 1
# assert count == 10

# positive_only = ds.filter(lambda r: r["label"] == "positive")
# assert all(r["label"] == "positive" for r in positive_only)

# assert repr(ds) == "Dataset(path='data/dataset.jsonl', size=10)"

# # Missing file must raise FileNotFoundError (not something wrapped)
# try:
#     Dataset("data/nonexistent.jsonl")
#     raise AssertionError("expected FileNotFoundError")
# except FileNotFoundError:
#     pass

# Why this matters: PyTorch's Dataset class is exactly this
# shape — __len__ and __getitem__ are the two methods a PyTorch
# Dataset requires. If you can build this cleanly, you already
# understand the core interface of every ML dataset abstraction.
# torch.utils.data.Dataset doesn't require __iter__
# (because DataLoaders iterate by index), but adding it makes
# the class more Pythonic.

import json

class Dataset:
    def __init__(self, path):
        self._data_list = []
        self._path = path
        with open (path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                    self._data_list.append(record)
                except json.JSONDecodeError:
                    print("Skipping a malinformed line")

    def __len__(self):
        return len(self._data_list)

    def __getitem__(self, idx):
        return self._data_list[idx]

    def __iter__(self):
        for record in self._data_list:
            yield record

    def __repr__(self):
        return f"Dataset(path='{self._path}', size={len(self)})"

    def filter(self, predicate):
        filtered_rec = []
        for i in self._data_list:
            if predicate(i):
                filtered_rec.append(i)
        return filtered_rec


path = "part-7-Object-OrientedProgramming/practice-projects-part7/data/dataset.jsonl"
ds = Dataset(path)
assert len(ds) == 10                             # 10 valid, malformed/empty skipped
assert isinstance(ds[0], dict)
assert isinstance(ds[0:3], list) and len(ds[0:3]) == 3

count = 0
for record in ds:
    assert "text" in record
    count += 1
assert count == 10

positive_only = ds.filter(lambda r: r["label"] == "positive")
assert all(r["label"] == "positive" for r in positive_only)

assert repr(ds) == f"Dataset(path='{path}', size=10)"

# Missing file must raise FileNotFoundError (not something wrapped)
try:
    Dataset("data/nonexistent.jsonl")
    raise AssertionError("expected FileNotFoundError")
except FileNotFoundError:
    pass

print("All assertions passed!")