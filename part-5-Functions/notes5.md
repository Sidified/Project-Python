# Part V — Functions

## What this part covered

- **Function basics:** `def`, `return`, positional and keyword arguments, default values.
- **Argument passing in depth:**
  - `*args` collects extra positional arguments as a tuple
  - `**kwargs` collects extra keyword arguments as a dict
  - Default values are evaluated **once, at definition time** — not on each call. Mutable defaults (`def f(x=[])`) share state across calls. Use `None` as sentinel and create the container inside the function.
- **Scope — the LEGB rule:** name lookup goes **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in. Enclosing is the outer function's scope in a nested function — not the module scope.
- **`nonlocal` and `global`:** to *modify* (rebind) a name in an enclosing or global scope, declare it with `nonlocal` or `global`. Just reading it needs no declaration.
- **Lambdas:** small anonymous single-expression functions. Useful inline with `sorted(..., key=lambda ...)`, `map`, `filter`, or to adapt a multi-arg function into a single-arg one.
- **Closures:** an inner function that captures variables from the enclosing scope. The captured variable is a reference to the enclosing scope's binding, not a copy — so if you *mutate* it (list, dict), no `nonlocal` needed; if you *rebind* it (`x = x + 1` on an int), `nonlocal` is required.
- **Recursion:** a function calls itself. Needs a base case (stopping condition) and a recursive step that moves toward the base case. Useful for walking arbitrarily nested structures (dicts, trees, JSON).

## What I built

- Named-argument predict function (shape of every LLM SDK call)
- Safe metrics accumulator using `history=None` sentinel + a broken version that demonstrates the mutable-default trap
- MSE and MAE loss functions with input validation via `ValueError`
- Config builder using `*args` + `**kwargs`
- Model ranker sorted by composite score — both a named function and an equivalent lambda
- Rate limiter as a closure (two versions: `nonlocal` counter and mutable-container counter)
- Recursive key counter for arbitrarily nested config dicts
- `make_pipeline(*steps)` — function composition returning a callable, tested on empty, single-step, and full pipelines

## What I got wrong / worth remembering

- **Integer division (`//`) vs float division (`/`).** Wrote `total // len(predictions)` in loss functions. Silently correct for integer test cases, wrong for float inputs. Third time this "silently right, actually wrong" pattern has bitten — file it permanently.
- **Assertions must be derived from the spec, not from the code's output.** If I run the code, see what it produces, then write an assertion matching that output, the assertion tests nothing. It just confirms the code produces what the code produces. Write assertions from the spec (or hand-computed values) *first*.
- **Enclosing ≠ Global.** In LEGB, when an inner function reads a variable from its outer function, that's the E, not the G. Getting this wrong doesn't hurt you on simple prints, but it breaks your model of closures.
- **Naming a local variable the same as the function** (e.g., `composite_score` inside `def composite_score(...)`) doesn't error out but ruins the function reference inside its own body. Rename the local.
- **Mutating captured mutable containers requires no `nonlocal`;** rebinding an int/string does. This is the same "reference vs rebinding" rule from Part I, showing up again in a different costume.

## Patterns worth internalizing

- **`history=None` sentinel** instead of `history=[]` for defaults involving mutable containers.
- **Closures for stateful callables** (rate limiters, counters, memoizers) — cleaner than global variables, testable in isolation.
- **Recursive walk** of nested dicts: `for k, v in obj.items(): if isinstance(v, dict): recurse(v)`.
- **Function composition via `*args`** — the shape underneath `sklearn.pipeline.Pipeline`, LangChain runnables, HuggingFace transforms.
- **`sorted(..., key=lambda x: ...)`** as the default sort tool; use a named function when the key logic is non-trivial or reusable.