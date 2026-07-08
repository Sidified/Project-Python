# Part IV — Collections

## What this part covered

- **Lists:** mutable, ordered, indexable. Common methods: `.append()`, `.extend()`, `.pop()`, `.sort()`, `.reverse()`. Slicing works the same as strings.
- **Tuples:** immutable, ordered. Useful for fixed records and as dict keys (strings and tuples are hashable; lists are not).
- **Dictionaries:** key-value pairs, insertion order preserved (Python 3.7+). O(1) lookup by key. `.get(k, default)` avoids `KeyError`. `.setdefault(k, [])` is the one-liner for dict-of-lists.
- **Sets:** unordered collections of unique items. O(1) membership checks. Operators: `&` (intersection), `|` (union), `-` (difference), `^` (symmetric difference).
- **Iteration helpers:**
  - `range(start, stop, step)` — numeric sequence
  - `enumerate(x)` — `(index, value)` pairs
  - `zip(a, b, c)` — parallel iteration over multiple iterables
  - `sorted(x, key=..., reverse=...)` — returns a new sorted list
  - `reversed(x)` — reversed iterator
- **Comprehensions:** `[expr for x in iter if cond]` (list), `{k: v for ...}` (dict), `{expr for ...}` (set). Cleaner than for-loops for simple transformations.

## What I built

- Fixed-size batch splitter (like every ML training loop)
- Token → ID vocabulary and reverse mapping (core of every tokenizer)
- Set operations on predicted vs actual labels (correct / hallucinated / missed)
- Top-N most frequent word ranker with `sorted(key=lambda)`
- Model records built by zipping parallel lists (name / accuracy / latency)
- Squared-loss and filtered-loss dicts via dict comprehensions
- Order-preserving deduplication in two versions (O(n²) list-only vs O(n) set + list)
- Mini-tokenizer with full vocab → encode → decode round-trip
- Config merger that produces experiment configs without mutating `base_config`
- Log analyzer that parses, groups, and summarizes multi-experiment training logs

## What I got wrong / worth remembering

- **Wrong loop bound, right output.** Writing `for i in range(0, batch_size)` when the batches happened to number the same as `batch_size` is silently right for one input, broken for every other. Always compute the bound from the *data*, not from a coincidence.
- **Variable shadowing in `zip` loops.** `for model_names, ... in zip(model_names, ...):` destroys the original list. Use different names for loop variables.
- **`list = ...`** shadows the built-in `list` type. Never use built-in names as variables.
- **`sorted(set(x))` is NOT insertion-order dedup.** It gives alphabetical order, which happens to match insertion order for `["a","b","c",...]` but nothing else. Real order-preserving dedup uses a `seen` set for O(1) lookup + a list for order.
- **`.setdefault(key, [])`** builds dict-of-lists in one clean pass instead of pre-declaring separate lists per key (which doesn't generalize).
- **Naming things "best" when they're computed as "last"** is a bug even if the output looks right on monotonically decreasing data. Compute the actual min explicitly with `min(...)`.
- **`x = x + 1` inside a `for x in range(...)` loop** does nothing — the loop variable is reassigned every iteration.
- **Verification is not optional.** At least three of my bugs would have been caught by writing the exact `assert` I was asked for. Skipping the assertion is not saving time; it's deferring the bug.

## Patterns worth internalizing

- **Set for lookup, list for order** — the standard O(n) dedup / vocab build pattern.
- **Dict-of-lists via `setdefault`** — grouping records by key in one pass.
- **`{**base, **override}` or `dict(base_config)`** — safe merge that doesn't mutate the base.
- **`sorted(..., key=lambda x: x[...])`** — sort by a field of the item; return value goes into a new list, original untouched.
- **`min(items, key=lambda x: x["loss"])`** — find the item with the minimum on some field (not the min value itself; the whole item).