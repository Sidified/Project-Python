# H2 (Cumulative — recalls Parts III + IV) — Recursive Nested Config Key Counter

# Given an arbitrarily nested dict:
# config = {
#    "model": {
#        "architecture": "transformer",
#        "layers": {"n": 12, "hidden": 768}
#    },
#    "training": {
#        "optimizer": {"name": "adam", "lr": 0.001},
#        "schedule": {"warmup": 100, "decay": 0.99}
#    },
#    "data": {
#        "splits": {
#            "train": {"size": 10000, "shuffle": True},
#            "val": {"size": 1000, "shuffle": False}
#        }
#    }
# }

# Write count_all_keys(obj) that recursively counts every key
# at every level of nesting. If a value is itself a dict,
# recurse into it and add its key count too. If it's not a dict, don't recurse.

# Expected for the above: count them by hand first.
# Then run your function. If they don't match, either your
# count-by-hand was wrong or your recursion is wrong. Either way, useful.

# Verification: count by hand first, then assert your
# function returns that number. Also test on count_all_keys({}) — should return 0.
# Test on count_all_keys({"a": 1}) — should return 1. Test on
# count_all_keys({"a": {"b": 1}}) — should return 2.

# Why this matters: recursive walking of nested structures
# is how every JSON/YAML config parser works, how PyTorch's
# state_dict traversal works, how you inspect nested
# model architectures. This is the pattern.


config = {
    "model": {
        "architecture": "transformer",
        "layers": {"n": 12, "hidden": 768}
    },
    "training": {
        "optimizer": {"name": "adam", "lr": 0.001},
        "schedule": {"warmup": 100, "decay": 0.99}
    },
    "data": {
        "splits": {
            "train": {"size": 10000, "shuffle": True},
            "val": {"size": 1000, "shuffle": False}
        }
    }
}

def count_all_keys(obj):
    count = 0
    if isinstance(obj, dict):
        for key in obj:
            count+=1
            count+= count_all_keys(obj[key])
    
    return count

assert count_all_keys(config) == 20
assert count_all_keys({}) == 0
assert count_all_keys({"a": 1}) == 1
assert count_all_keys({"a": {"b": 1}}) == 2

print("All assertions passed. Again!")