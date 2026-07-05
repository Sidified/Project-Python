# Part III — Control Flow

## What this part covered

- **Operators:** arithmetic, comparison, logical (`and`, `or`, `not`), membership (`in`, `not in`), identity (`is`). Chained comparisons like `0.3 <= x < 0.7`.
- **`if` / `elif` / `else`:** flat chains read cleaner than nested ones. Only one branch executes.
- **`while` loop:** repeat until a condition is false. Useful for input validation and any "keep going until" logic.
- **`for` loop:** iterate over any iterable (strings, lists, `range(...)`). Preferred when the number of iterations is known or bounded by a collection.
- **`enumerate(...)`:** get `(index, value)` pairs while looping. Preferred over `range(len(...))`.
- **`break`:** exit the loop immediately. **`continue`:** skip to the next iteration.
- **Loop `else` clause:** runs only if the loop completed *without* hitting a `break`. Useful for "search and report if not found" patterns.

## What I built

- Confidence-score classifier (low / medium / high with boundary handling)
- Input validation loop (keeps asking until a valid number is entered)
- Character-stats counter (vowels / digits / spaces / other, verified against `len()`)
- Early-stopping simulator (for + break + for-else to report non-convergence)
- Keyword sentiment classifier (positive vs negative counts using the `in` operator)
- Hyperparameter grid-search combinations (3 nested `for` loops → 18 combinations)
- Palindrome cleaner: explicit `for` loop building a new string, original string left untouched (recalled string immutability from Part II)

## What I got wrong / worth remembering

- **For-else pairing.** The `else` on a loop belongs to the **loop**, not to the `if` inside it. Indentation is what determines pairing, and I paired it wrong initially — the `else` ran on every iteration where the condition was false, instead of once after the loop finished without breaking.
- **Verification means *reading the output*, not just running the code.** If a bug produces extra lines of output, that's the bug telling you it exists. Running ≠ verifying.
- **Read the spec exactly.** Small formatting deviations (`Ir` vs `lr`, spaces around `=`, missing `<n>` in an output message) don't fail correctness but do fail the requirement. Habit worth fixing now.
- **String concatenation in a loop is O(n²).** Strings are immutable, so every `+=` creates a new string. Build a list of chars and `"".join(list)` once at the end — O(n).
- **`x in some_string` is substring matching**, not word matching. `"good" in "goodness"` is `True`. Fine for basic keyword scans; won't hold up when word boundaries matter.