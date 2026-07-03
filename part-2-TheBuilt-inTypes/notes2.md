# Part II — The Built-in Types

## What this part covered

- **Numbers:** `int`, `float`, `complex`. Basic arithmetic, casting between types.
- **Booleans & Truthiness:** `True`/`False`, and how other values (`0`, `""`, `None`, empty containers) evaluate to `False` in a boolean context. Non-empty strings like `"0"` and `" "` are `True` — trap cases.
- **`None`:** the singleton "no value." Compared with `is None`, never `== None`.
- **Strings:** indexing (positive and negative), slicing `[start:stop:step]`, `[::-1]` to reverse.
- **String methods:** `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.removeprefix()`, `.removesuffix()`. All return new strings — strings are immutable.
- **f-strings:** substitution `{var}`, format specs like `{x:.2f}` (decimals), `{x:03d}` (zero-padded), `{x:.2%}` (percent), `{x:<10}` (left-align width), `{x!r}` (repr).
- **I/O and casting:** `input()` always returns a string; cast with `int()`, `float()`, `bool()`, `str()` as needed.

## What I built

- Temperature converter (Celsius → Fahrenheit / Kelvin)
- Truthiness table with aligned f-string columns
- Filename dissector using only indexing and slicing
- ML training-log-style formatted line (`Epoch 003 | Loss: 0.4523 | Acc: 87.32%`)
- LLM prompt template with multi-line f-string
- Message preprocessor chain (`.strip → .removeprefix → .lower → .replace → wrap`) + `id()` check confirming string immutability

## What I got wrong / worth remembering

- **Triple-quoted strings** already handle newlines and indentation literally — don't stuff `\n` and `\t` inside them.
- **Match the spec exactly.** Spacing and formatting details matter; skimming the spec costs correctness.
- **String methods never mutate.** `raw.strip()` produces a new string; `raw` is unchanged unless reassigned. Confirmed via `id()`.