# Part I — Foundations

## What this part covered

- How Python actually executes: source → parser → bytecode → PVM.
- The three-stage pipeline determines *when* errors surface: `SyntaxError` before any code runs, runtime errors (`NameError`, `TypeError`, etc.) during execution.
- Variables in Python are **names bound to objects**, not boxes holding values. Assignment (`b = a`) binds a second name to the same object; it never copies.
- Every Python object is either **mutable** (`list`, `dict`, `set`) or **immutable** (`int`, `float`, `str`, `tuple`, `bool`, `None`, `frozenset`).
- `==` compares values; `is` compares object identity. Reserve `is` for `None` / `True` / `False`.

## What I built

No project for this part. The honest test for the memory model is predict-then-explain on code snippets, not a fabricated build. A "variables project" would have been theatrical.

## What clicked

- The **label / sticky-note model** of variables. Once `a = [1,2,3]; b = a; b.append(4)` made sense, the rest of the chapter followed.
- **Rebinding vs mutation.** Inside a function, `items.append(x)` mutates the shared object (caller sees it); `items = [...]` rebinds the local name to a new object (caller does not see it). Same syntax family, opposite effects.
- **Syntax errors are caught before any code runs** — including errors inside functions that are never called. The whole file must parse before any bytecode executes.

## What tripped me up

- **Tuple immutability with mutable contents.** I assumed `t = (1, 2, [3, 4]); t[2].append(99)` would raise an error. It doesn't. A tuple stores a fixed sequence of *references*. The references can't be added, removed, or swapped — but the objects those references point to can still be mutated if they're mutable themselves. "Immutable container, mutable content" is a real and dangerous combination.
- **SyntaxError vs runtime error timing.** My first instinct was that a syntax error inside an uncalled function would let the rest of the file run. Wrong. Parsing is whole-file; if any part fails to parse, nothing executes.

## Why this matters for AI Engineering

- Reference semantics show up everywhere in ML code: config dicts being mutated across training runs, PyTorch tensors being aliased into optimizer state, dataloaders sharing mutable state across workers. The class of bugs I'll hit later mostly traces back to this chapter.
- The "safe / read-only" illusion — using tuples or `frozen=True` dataclasses as configs while their fields are mutable lists or dicts — is a real source of silent state leakage between experiments. Worth remembering.

## Reference commands

```bash
python3 --version         # verify install
python3                   # REPL
python3 script.py         # run a file
python3 -m py_compile x.py  # syntax-check without running
```