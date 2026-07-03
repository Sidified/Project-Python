# The Python Bible

*A ground-up reference for total beginners, built for long-term revision and mastery.*

---

## How to Use This Reference

This document is designed to be read **linearly the first time** and used as a **searchable reference thereafter**. Every chapter builds on the previous one, so skipping around during your first pass will create gaps you'll pay for later.

Each chapter follows a consistent shape:

- **What & Why** — the concept in plain language, and why Python needs it
- **Mental Model** — an analogy or picture that makes it stick
- **Syntax & Examples** — runnable code with expected output
- **Common Mistakes** — the exact traps beginners fall into
- **Best Practices** — the "Pythonic" way, not just the working way
- **Active Recall** — questions to test yourself without looking

**How to actually learn:**
1. Read a chapter, understanding the intuition, not memorizing syntax.
2. Type every example yourself. Do not copy-paste. Typing builds muscle memory.
3. Answer the Active Recall questions without scrolling up.
4. Move on. Come back for revision after finishing the whole book.

---

## Table of Contents

**Part I — Foundations**
- Chapter 0: Getting Python Running
- Chapter 1: How Python Actually Executes Your Code
- Chapter 2: Variables, Objects, and the Memory Model

**Part II — The Built-in Types**
- Chapter 3: Numbers (`int`, `float`, `complex`)
- Chapter 4: Booleans & Truthiness
- Chapter 5: `None` — The Absence of a Value
- Chapter 6: Strings (Part 1) — Basics, Indexing, Slicing
- Chapter 7: Strings (Part 2) — Methods and f-strings
- Chapter 8: Input, Output, and Type Casting

**Part III — Control Flow**
- Chapter 9: Operators & Expressions
- Chapter 10: Conditional Statements (`if` / `elif` / `else`)
- Chapter 11: The `while` Loop
- Chapter 12: The `for` Loop
- Chapter 13: `break`, `continue`, and the Loop `else` Clause

**Part IV — Collections**
- Chapter 14: Lists
- Chapter 15: Tuples
- Chapter 16: Dictionaries
- Chapter 17: Sets
- Chapter 18: Iteration Helpers — `range`, `enumerate`, `zip`, `sorted`, `reversed`
- Chapter 19: Comprehensions

**Part V — Functions**
- Chapter 20: Functions — The Basics
- Chapter 21: Function Arguments in Depth (`*args`, `**kwargs`)
- Chapter 22: Scope & the LEGB Rule
- Chapter 23: Lambdas and Functional Tools
- Chapter 24: Recursion

**Part VI — Structuring Real Programs**
- Chapter 25: Modules, Packages, and `import`
- Chapter 26: Errors and Exception Handling
- Chapter 27: File I/O
- Chapter 28: JSON and CSV

**Part VII — Object-Oriented Programming**
- Chapter 29: Classes and Objects
- Chapter 30: Inheritance and `super()`
- Chapter 31: Encapsulation, Properties, and Access Control
- Chapter 32: Polymorphism and Dunder Methods
- Chapter 33: Abstract Base Classes

**Part VIII — Advanced Language Features**
- Chapter 34: Iterators and Generators
- Chapter 35: Decorators
- Chapter 36: Context Managers
- Chapter 37: Type Hints and Modern Python
- Chapter 38: Regular Expressions (a Practical Primer)

**Part IX — The Ecosystem**
- Chapter 39: The Standard Library Tour
- Chapter 40: Virtual Environments and `pip`
- Chapter 41: Pythonic Style, Idioms, and Common Pitfalls

**Appendices**
- A: Operator Precedence Table
- B: Reserved Keywords
- C: String Methods Cheat Sheet
- D: List/Dict/Set Methods Cheat Sheet
- E: Dunder Methods Reference

---
---

# Part I — Foundations

---

# Chapter 0: Getting Python Running

## What & Why

Before you can learn Python you need a place to run it. This chapter is not conceptual — it's the practical setup. Skip it only if you already have Python 3 installed and know how to run a `.py` file.

## What is Python, really?

Python is a **programming language** — a formal way to write instructions that a computer can execute. But the word "Python" also refers to the **program that reads and executes** those instructions. That program is called the **Python interpreter**.

So when you "install Python," what you're actually installing is:
1. The interpreter (a program called `python` or `python3`).
2. The **standard library** — thousands of pre-written pieces of code that come free with Python (for working with files, dates, math, the web, etc.).
3. Tools like `pip` (for installing extra libraries) and `venv` (for isolating projects).

## Installation

You need **Python 3.10 or newer**. Python 2 is dead — do not install it, do not use tutorials from 2015, do not read Stack Overflow answers using `print "hello"` (with no parentheses — that's Python 2).

- **Windows:** Install from [python.org](https://www.python.org/downloads/), or better, use WSL (Windows Subsystem for Linux) and install via `apt`.
- **macOS:** Use [python.org](https://www.python.org/downloads/) or `brew install python`.
- **Linux:** Usually already installed. Check with `python3 --version`. If missing: `sudo apt install python3 python3-pip python3-venv`.

### Verify it works

Open your terminal and type:

```bash
python3 --version
```

You should see something like `Python 3.12.3`. If you get "command not found," Python isn't on your PATH — reinstall and check the "Add Python to PATH" box on Windows.

## The two ways to run Python

### 1. The REPL (Read-Eval-Print Loop)

Type `python3` in your terminal with no arguments:

```
$ python3
Python 3.12.3 (main, ...)
>>> 2 + 2
4
>>> print("hello")
hello
>>> exit()
```

The `>>>` is Python's prompt. You type an expression, Python evaluates it, prints the result, and waits for more. This is called an **interactive session** or **REPL**. Use it to test tiny snippets, explore APIs, or check "what does this thing do again?"

### 2. Running a script

Create a file called `hello.py` in any text editor. Write:

```python
print("Hello, world!")
```

Save it. In your terminal, navigate to the folder and run:

```bash
python3 hello.py
```

Output:
```
Hello, world!
```

This is how real programs work. You write code in `.py` files and execute them from the command line.

## Your editor

You need a code editor. Use **VS Code** with the official Python extension (search "Python" in the extensions marketplace, install the one from Microsoft). Alternatives: PyCharm, Sublime Text, Neovim. Do **not** use Notepad, Word, or the default text editor — they don't understand code.

Set up VS Code:
1. Install VS Code.
2. Install the "Python" extension by Microsoft.
3. Open your project folder (`File → Open Folder`).
4. Open a `.py` file — VS Code will prompt you to select the Python interpreter. Pick your `python3`.

## Your first real program

Create `intro.py`:

```python
# This is a comment. Python ignores everything after the # on a line.

# ask the user for their name
name = input("What's your name? ")

# greet them
print("Hello,", name, "!")

# do a small calculation
year = 2026
birth_year = year - 23
print("If you're 23 now, you were born in", birth_year)
```

Run it: `python3 intro.py`. Type your name when it asks. You just wrote a program that took input, did arithmetic, and produced output. That's the whole game — everything else is refinement.

## Common Mistakes at This Stage

- **Confusing `python` and `python3`.** On some systems, `python` still refers to the ancient Python 2. Always use `python3` on Linux/macOS to be safe.
- **Running the REPL when you meant to run a script.** If you type `python3 hello.py` and get dropped into the `>>>` prompt, you probably forgot the filename or aren't in the right folder.
- **Saving files without the `.py` extension.** Python will refuse to run `hello.txt` even if it contains valid code.
- **Using Word or Notepad.** They add invisible formatting characters that break your code. Use a real editor.

## Key Takeaways

- Python is both a language and an interpreter program.
- Two ways to run Python: interactive REPL (`python3` with no args) or a script (`python3 filename.py`).
- Use VS Code + Python extension.
- Always Python 3, never Python 2.

---

# Chapter 1: How Python Actually Executes Your Code

## What & Why

You can write Python for years without knowing what happens between "I press Run" and "output appears." But a rough mental model helps you understand errors, performance, and why some things behave the way they do. This chapter gives you that model — nothing more.

## The Big Picture

Your computer's CPU only understands machine code — raw binary instructions. It has no idea what `print("hello")` means. Something has to translate your Python code into instructions the CPU can run.

That something is the **Python interpreter**. Here's what it does, in three stages:

```
your_code.py  ─►  [Lexer/Parser]  ─►  [Compiler]  ─►  [Python Virtual Machine (PVM)]  ─►  CPU
                    breaks into        turns into        executes bytecode
                     tokens            "bytecode"        one instruction at a time
```

### Stage 1: Parsing

The interpreter reads your `.py` file as text and breaks it into meaningful pieces (tokens): keywords, names, numbers, operators. It then builds a tree structure representing your program's grammar. If your syntax is broken — say, a missing colon after `if` — this is the stage that fails. You get a **SyntaxError**.

### Stage 2: Compilation to Bytecode

The parsed tree gets compiled into **bytecode**: a simpler, lower-level list of instructions like "load the value 5," "add the top two values on the stack," "call this function." Bytecode is not machine code — it's Python's own internal language. It's stored in `.pyc` files inside a folder called `__pycache__/` that Python creates automatically so it doesn't have to re-compile every time.

### Stage 3: Execution by the PVM

The **Python Virtual Machine (PVM)** is a big loop written in C. It reads bytecode instructions one at a time and performs the equivalent action. This is where your program actually "runs."

## Why This Matters (a Little)

- **Errors happen at different stages.** A syntax error stops execution before *any* of your code runs. A `NameError` (variable doesn't exist) or `TypeError` happens during execution — meaning some of your code already ran before the error. This is why you can `print("start")`, then hit a `TypeError`, and see `start` in the output.
- **Python is "interpreted, not compiled" — but that's a simplification.** It *does* compile to bytecode, but the bytecode is then interpreted at runtime. Compare to C, which compiles all the way down to machine code before you run it.
- **Python is slower than C.** Because of this interpretation step. Not usually a problem, but worth knowing.

## Mental Model: The Restaurant Analogy

- Your `.py` file is a recipe written in English.
- The **parser** is a translator who reads the recipe and rewrites it in a simplified checklist (bytecode).
- The **PVM** is the cook who follows the checklist step by step.
- The **CPU** is the stove doing the actual heating.

You never need to see the checklist — but knowing it exists explains why Python can catch some errors early (the translator refuses to translate a nonsense recipe) and others late (the cook realizes halfway through that there's no salt).

## A Tiny Peek at Bytecode

You can actually see the bytecode:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

Output (roughly):
```
  2           0 RESUME                   0

  3           2 LOAD_FAST                0 (a)
              4 LOAD_FAST                1 (b)
              6 BINARY_OP                0 (+)
             10 RETURN_VALUE
```

You do not need to understand this. It's here so you know it's real and not magic.

## Key Takeaways

- Python compiles your code to **bytecode**, then executes bytecode on the **PVM**.
- The `__pycache__` folder holds compiled bytecode. Ignore it, don't check it into git.
- Syntax errors are caught before execution; other errors are caught during execution.
- You don't need to understand bytecode. You just need to know the pipeline exists.

## Active Recall

1. What are the three broad stages between your `.py` file and your CPU actually doing work?
2. What is stored in the `__pycache__` folder, and can you safely delete it?
3. If a `SyntaxError` appears in your program, will any code before the error have already run? What about a `TypeError`?

---

# Chapter 2: Variables, Objects, and the Memory Model

## What & Why

Almost every bug you'll write in your first year comes from misunderstanding what a variable actually *is* in Python. The intuition from math class ("x is a box that holds a number") is **wrong for Python** and will bite you the moment you touch lists, function arguments, or objects.

This chapter fixes that intuition. It's the most important chapter in the book.

## The Wrong Model: Variables as Boxes

In C or older languages, a variable is a physical location in memory — a "box." When you write `x = 5`, the computer allocates a box big enough to hold an integer and writes 5 into it. When you write `x = 10`, it overwrites that box with 10.

**Python does not work like this.** If you carry the box model in your head, Python will confuse you.

## The Right Model: Variables as Labels

In Python, when you write:

```python
x = 5
```

Two separate things happen:

1. Python creates an **object** in memory: an integer with the value 5. This object has:
   - a type (`int`)
   - a value (5)
   - a unique identity (a memory address)
2. Python creates a **name** `x` and sticks it on that object, like a sticky note with "x" written on it.

The variable is the **sticky note**, not the object. The object lives independently in memory.

```
    ┌─────────────┐
x ──►│  int: 5     │
    └─────────────┘
```

Now watch what happens with reassignment:

```python
x = 5
x = 10
```

Python does **not** overwrite the `5` object. Instead:

1. Python creates a new integer object `10`.
2. It peels the `x` sticky note off the `5` and puts it on the `10`.
3. The old `5` object still exists in memory — but nothing points to it, so eventually Python's **garbage collector** cleans it up.

```
    ┌─────────────┐         ┌─────────────┐
    │  int: 5     │      x ─►│  int: 10    │
    └─────────────┘         └─────────────┘
    (orphaned, will
     be cleaned up)
```

## Why This Matters — Multiple Names for One Object

Because variables are labels, **two variables can point to the same object**:

```python
a = [1, 2, 3]
b = a          # b is now a second sticky note on the same list
b.append(4)
print(a)       # [1, 2, 3, 4]  ← surprise!
```

We never touched `a`, but `a` changed. Because `a` and `b` label the same list, and lists are **mutable** (changeable). Mutating through one label affects what the other label sees.

Compare with integers:

```python
a = 5
b = a
b = 10
print(a)       # 5, unchanged
```

Why the difference? Because integers are **immutable**. `b = 10` doesn't mutate the integer 5 — it moves the `b` label to a completely new object. `a` is untouched.

## Mutable vs Immutable — The Central Distinction

Every Python object is either **mutable** (can be changed in place) or **immutable** (cannot).

| Immutable                 | Mutable                        |
| ------------------------- | ------------------------------ |
| `int`, `float`, `complex` | `list`                         |
| `str`                     | `dict`                         |
| `bool`                    | `set`                          |
| `tuple`                   | user-defined classes (usually) |
| `frozenset`               |                                |
| `None`                    |                                |

**Immutable** means: once created, the object's value cannot change. Any "modification" produces a brand new object.

```python
s = "hello"
s = s + " world"    # NOT modifying "hello" — creating a new string "hello world"
                    # and moving the s label onto it.
```

**Mutable** means: the object can be changed in place. The same object continues to exist, but its contents differ.

```python
lst = [1, 2, 3]
lst.append(4)       # Same list object, now contains [1, 2, 3, 4].
                    # Any other name pointing to this list sees the change.
```

## Checking Identity: `id()` and `is`

Every object has a unique identity — you can see it with `id()`, which returns an integer (usually the memory address):

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a))    # e.g. 140234567890000
print(id(b))    # SAME as id(a) — same object
print(id(c))    # DIFFERENT — c is a separate list that happens to look the same
```

The `is` operator asks "are these two names pointing to the exact same object?" It's not the same as `==`, which asks "do these two objects have equal values?"

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

a == c    # True  — same values
a is c    # False — different objects
a is b    # True  — same object
```

**Rule of thumb:**
- Use `==` for value comparison ("do they look the same?").
- Use `is` only for `None`, `True`, `False`: `if x is None:`.

## Small-Integer and String Caching (a Curious Wrinkle)

Python caches small integers (`-5` to `256`) and short strings for performance. So:

```python
a = 100
b = 100
a is b        # True — Python reuses the same cached object

a = 1000
b = 1000
a is b        # False (usually) — no caching for this size
```

Don't rely on this. Never use `is` for integer or string comparison. Use `==`.

## The Function Argument Trap

Because variables are labels, passing a mutable object into a function passes the **label**, not a copy. The function can mutate the original:

```python
def add_item(lst):
    lst.append("new")

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)    # [1, 2, 3, 'new']  ← modified!
```

This is one of the most common sources of surprise for beginners. If you don't want the function to mutate your data, pass a copy:

```python
add_item(my_list.copy())
print(my_list)    # unchanged
```

## Deleting Names with `del`

`del x` removes the sticky note `x`. It does not necessarily destroy the object — that only happens when no names point to it anymore.

```python
a = [1, 2, 3]
b = a
del a           # a no longer exists as a name
print(b)        # [1, 2, 3] — the list is still alive, b still labels it
```

## Common Mistakes

- **Assuming `b = a` copies a list.** It doesn't. It creates a second name for the same list. Use `b = a.copy()` (shallow) or `import copy; b = copy.deepcopy(a)` (deep) to duplicate.
- **Using `is` for value equality.** `if name is "Sid":` may work sometimes because of string caching, but it's wrong. Use `==`.
- **Forgetting that function arguments are references.** Mutating them inside the function mutates the original.
- **Thinking `x = x + 1` modifies the number.** It doesn't. It creates a new number and rebinds `x`. The old number is unaffected.

## Best Practices

- Use `==` for comparing values. Reserve `is` for `None` / `True` / `False`.
- When a function should not modify its input, take a copy.
- When you want two independent lists, always call `.copy()`.
- For deeply nested structures (list of lists of dicts), `.copy()` is not enough — use `copy.deepcopy()`.

## Key Takeaways

- Variables are **labels attached to objects**, not boxes containing values.
- Assignment (`b = a`) binds a name to an object; it never copies.
- **Immutable** objects (int, str, tuple) can never change; "modifying" them creates a new object.
- **Mutable** objects (list, dict, set) can change in place — and any name pointing to them sees the change.
- Use `==` for values, `is` for identity (usually just `None`).

## Active Recall

1. You write `x = 5` then `x = 10`. Did Python overwrite the memory holding 5? What happens to the object that used to hold 5?
2. `a = [1, 2, 3]; b = a; b.append(4)`. What does `a` now contain, and why?
3. What is the difference between `a == b` and `a is b`?
4. You pass a list into a function that appends to it. When the function returns, does your original list see the change?
5. Which of these are immutable in Python: `int`, `list`, `str`, `dict`, `tuple`, `set`?

---

# Part II — The Built-in Types

---

# Chapter 3: Numbers

## What & Why

Every non-trivial program does math. Python gives you three numeric types (`int`, `float`, `complex`) and a rich set of operators. This chapter covers what they are, how they interact, and the sharp corners that will silently corrupt your results if you're not careful.

## The Three Numeric Types

### `int` — integers

Whole numbers, positive, negative, or zero.

```python
age = 23
temperature = -5
big_number = 1_000_000    # underscores allowed for readability; same as 1000000
```

**Python integers have arbitrary precision.** They grow as large as your RAM allows. Unlike most languages, there is no `INT_MAX`.

```python
huge = 2 ** 200
print(huge)   # 1606938044258990275541962092341162602522202993782792835301376
```

In Solidity, `uint256` overflows silently and can cause exploits. In Python, integers simply consume more memory. This is safer but slower — a Python int is heavier than a C int.

### `float` — floating-point numbers

Numbers with a decimal point. Stored using the IEEE 754 double-precision standard (64 bits).

```python
price = 25.99
pi_approx = 3.14159
scientific = 1.5e-3        # 0.0015 — scientific notation
```

**Floats are inexact.** This is the single most important thing to internalize:

```python
>>> 0.1 + 0.2
0.30000000000000004
```

This is not a Python bug. It's how floating-point works on every language on every computer, because `0.1` and `0.2` cannot be represented exactly in binary. Never use `==` on floats:

```python
0.1 + 0.2 == 0.3    # False!
```

If you need to compare floats, use a tolerance:

```python
abs((0.1 + 0.2) - 0.3) < 1e-9    # True
```

Or for financial calculations, don't use `float` at all — use the `decimal.Decimal` type from the standard library, which gives you exact base-10 arithmetic.

### `complex` — complex numbers

Numbers with a real and imaginary part. You will almost never use these unless you do scientific computing.

```python
z = 2 + 3j        # j is the imaginary unit
print(z.real)     # 2.0
print(z.imag)     # 3.0
```

## Arithmetic Operators

| Operator | Meaning            | Example  | Result |
| -------- | ------------------ | -------- | ------ |
| `+`      | Addition           | `5 + 2`  | `7`    |
| `-`      | Subtraction        | `5 - 2`  | `3`    |
| `*`      | Multiplication     | `5 * 2`  | `10`   |
| `/`      | True division      | `5 / 2`  | `2.5`  |
| `//`     | Floor division     | `5 // 2` | `2`    |
| `%`      | Modulo (remainder) | `5 % 2`  | `1`    |
| `**`     | Exponentiation     | `5 ** 2` | `25`   |

### The `/` vs `//` Trap

- `/` **always returns a float**, even when the result is a whole number.
- `//` returns an integer if both operands are integers.

```python
10 / 2      # 5.0  (float!)
10 // 2     # 5    (int)
10 / 3      # 3.3333...
10 // 3     # 3    (rounded DOWN, not truncated)
-10 // 3    # -4   (NOT -3 — always rounds toward negative infinity)
```

The last case surprises everyone: floor division rounds *down*, not *toward zero*. For negative numbers this differs from what C or Java do.

### The Modulo `%` Operator

Returns the remainder after division. Enormously useful.

```python
7 % 3       # 1
10 % 2      # 0 — because 10 is even
n % 2 == 0  # True if n is even, False if odd

# Wrapping around: "every 12 hours"
hour = 25
hour % 24   # 1 — 25 hours is 1 AM
```

### The `**` Operator

Exponentiation. Right-associative.

```python
2 ** 10     # 1024
2 ** 0.5    # 1.4142... — square root (returns float)
2 ** -1     # 0.5 — negative exponent
```

## Mixing Types: Implicit Promotion

When you mix `int` and `float` in an expression, Python promotes the int to a float and returns a float:

```python
3 + 4.0     # 7.0 (float)
5 * 2       # 10 (int)
```

You never lose precision going int → float in principle, though very large ints can lose precision when converted (floats only have ~15-17 significant decimal digits).

## Explicit Type Conversion

You can force conversions with the type's constructor function:

```python
int(3.9)      # 3   — truncates toward zero (does NOT round)
int(-3.9)     # -3
int("42")     # 42
int("3.5")    # ValueError! int() can't parse decimal strings
int("hello")  # ValueError!

float(3)      # 3.0
float("3.5")  # 3.5
float("inf")  # inf — a real value
float("nan")  # nan — "not a number"

str(42)       # "42"
str(3.14)     # "3.14"
```

Notice `int(3.9)` gives `3`, not `4`. It truncates (drops the fractional part), not rounds. To round properly, use `round()`:

```python
round(3.5)    # 4
round(2.5)    # 2 — surprise! Python uses "banker's rounding" (rounds to even)
round(3.14159, 2)   # 3.14 — second arg is decimal places
```

## Useful Built-in Numeric Functions

```python
abs(-5)         # 5
min(3, 1, 4)    # 1
max(3, 1, 4)    # 4
sum([1, 2, 3])  # 6
pow(2, 10)      # 1024 — same as 2 ** 10
pow(2, 10, 7)   # (2 ** 10) % 7 = 2 — three-arg form is faster
divmod(17, 5)   # (3, 2) — returns (quotient, remainder) as a tuple
round(3.7)      # 4
```

## The `math` Module

For heavier math, import the `math` module:

```python
import math

math.sqrt(16)       # 4.0
math.pi             # 3.141592653589793
math.e              # 2.718281828459045
math.floor(3.9)     # 3 — always rounds down
math.ceil(3.1)      # 4 — always rounds up
math.log(100, 10)   # 2.0 — log base 10 of 100
math.factorial(5)   # 120
math.gcd(24, 36)    # 12 — greatest common divisor
math.inf            # infinity
math.nan            # not a number
```

## Common Mistakes

- **Comparing floats with `==`.** `0.1 + 0.2 == 0.3` is `False`. Use tolerance-based comparison or `math.isclose(a, b)`.
- **Assuming `/` returns an integer.** `10 / 2` is `5.0`, not `5`. If you need an int, use `//` or cast: `int(10 / 2)`.
- **Confusing `int(x)` with `round(x)`.** `int(3.9)` is `3`. `round(3.9)` is `4`.
- **Using `float` for money.** Use `decimal.Decimal` or store cents as integers.
- **Forgetting `int("3.5")` fails.** To parse a decimal string as an integer, go through float first: `int(float("3.5"))`.

## Best Practices

- Use underscores in large numeric literals for readability: `1_000_000` not `1000000`.
- Prefer `//` and `%` for integer math; use `/` only when a float is expected.
- Import `math` for anything beyond arithmetic — don't reinvent square roots or logarithms.
- For financial or scientific-precision math, use `decimal.Decimal` or `fractions.Fraction`.

## Key Takeaways

- Three numeric types: `int` (arbitrary precision), `float` (approximate), `complex` (rare).
- `/` returns float, `//` returns int-floor, `%` returns remainder, `**` is power.
- Floats are inexact — never compare with `==`.
- `int(x)` truncates; `round(x)` rounds (with banker's rule at .5).
- Use the `math` module for more than basic arithmetic.

## Active Recall

1. What's the difference between `10 / 3`, `10 // 3`, and `10 % 3`?
2. Why does `0.1 + 0.2 == 0.3` return `False`?
3. `int(-3.7)` gives what value? What about `round(-3.7)`?
4. What does `n % 2 == 0` test for?
5. What type does `10 / 2` return, and why might this crash a function that expects an integer?

---

# Chapter 4: Booleans & Truthiness

## What & Why

A **Boolean** is a value that's either `True` or `False`. They control every branch of every program — every `if`, every `while`, every filter. Understanding what Python considers "true" (**truthiness**) is essential; the rules are broader than you might expect.

## The `bool` Type

```python
x = True
y = False
print(type(x))    # <class 'bool'>
```

**Strict capitalization.** Only `True` and `False` are valid. Writing `true` or `TRUE` gives a `NameError`.

Booleans are actually a subclass of `int` in Python: `True` equals 1 and `False` equals 0. This is legal but weird:

```python
True + True     # 2
False * 5       # 0
sum([True, True, False, True])   # 3 — counts how many are True
```

## Comparison Operators — The Boolean Producers

Any comparison returns a Boolean:

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `<`      | Less than                |
| `>`      | Greater than             |
| `<=`     | Less than or equal to    |
| `>=`     | Greater than or equal to |

```python
5 == 5      # True
5 == "5"    # False — int and str never compare equal
5 < 10      # True
"apple" < "banana"    # True — strings compare alphabetically (lex order)
```

### Chained Comparisons — a Pythonic Superpower

Python lets you chain comparisons in the mathematically natural way:

```python
age = 25
if 18 <= age < 65:
    print("working age")
```

This is exactly `18 <= age and age < 65`. Most other languages don't support this. Use it — it reads beautifully.

## Logical Operators

| Operator | Meaning                              |
| -------- | ------------------------------------ |
| `and`    | True only if both operands are true  |
| `or`     | True if at least one operand is true |
| `not`    | Inverts a Boolean                    |

```python
True and False    # False
True or False     # True
not True          # False

age = 25
has_id = True
if age >= 18 and has_id:
    print("can enter")
```

### Short-Circuit Evaluation — Important

`and` / `or` are lazy. They stop evaluating as soon as they can determine the result.

```python
False and expensive_function()   # expensive_function is NEVER called
True or expensive_function()     # expensive_function is NEVER called
```

This is not just an optimization — it's essential for safety:

```python
if user is not None and user.age > 18:   # safe
    ...

# If we wrote it the other way:
if user.age > 18 and user is not None:   # crashes when user is None!
    ...
```

### `and` / `or` Return Values (Not Just Booleans!)

Here's a subtlety that trips beginners:

```python
"hello" and "world"    # "world"  — NOT True
"" and "world"         # ""       — NOT False
None or "default"      # "default"
0 or 5                 # 5
```

`and` returns the first falsy value it finds, or the last value if all are truthy.
`or` returns the first truthy value it finds, or the last value if all are falsy.

This is heavily used for defaults:

```python
name = user_input or "Anonymous"   # if user_input is empty, use "Anonymous"
```

## Truthiness — What Counts as True?

Python does not require Booleans in `if` statements. **Every value has an implicit truthiness.**

**Falsy values** (evaluate as False):
- `False`
- `None`
- `0`, `0.0`, `0j`
- Empty sequences: `""`, `[]`, `()`, `{}` (empty dict), `set()`
- Any custom object whose `__bool__` returns `False`

**Truthy values** (evaluate as True): *everything else*.

```python
if []:              # doesn't run — empty list is falsy
    print("empty")

if [0]:             # runs — list with one item is truthy, even if item is falsy!
    print("has content")

if "hello":         # runs — non-empty string is truthy
    print("has text")

if 0:               # doesn't run
    print("zero")
```

This lets you write concise, idiomatic checks:

```python
# Instead of:
if len(my_list) > 0:
    process(my_list)

# Write:
if my_list:
    process(my_list)
```

## The `bool()` Function

Convert any value to its Boolean equivalent:

```python
bool(0)          # False
bool(1)          # True
bool("")         # False
bool("no")       # True (any non-empty string!)
bool([])         # False
bool([0])        # True
bool(None)       # False
```

Watch out: `bool("False")` is `True` because it's a non-empty string. To parse the string `"False"`, you have to check explicitly.

## `is` vs `==` for Booleans

```python
x = True
x == True    # True
x is True    # True — because True is a singleton

# But avoid `if x is True:` — just write `if x:`
```

Use `is` only for `None`, `True`, `False`. For anything else, `==`.

## Common Mistakes

- **Writing `true` / `false` / `TRUE`.** Only `True` and `False` are valid.
- **Assuming `and` returns a Boolean.** `"a" and "b"` returns `"b"`, not `True`.
- **Testing existence with `== None`.** Use `x is None`. It's faster and more idiomatic.
- **Testing empty containers with `len(x) == 0`.** Use `if not x:` instead.
- **Assuming `bool("False")` is `False`.** It's `True` — any non-empty string is truthy.
- **Ordering condition wrong in `and`.** `if user.age > 18 and user is not None:` crashes when `user` is `None`. Check for None first.

## Best Practices

- Use `if x:` and `if not x:` — Pythonic and short.
- Use `is None` and `is not None` for None checks.
- Use chained comparisons: `0 < x < 10`.
- Use short-circuit `or` for defaults: `name = user_name or "Anonymous"`.

## Key Takeaways

- Booleans are `True` and `False`, case-sensitive.
- Comparison operators return Booleans; chained comparisons are Pythonic.
- **Every value has a truthiness.** Falsy: `False`, `None`, `0`, empty containers.
- `and` / `or` short-circuit and return the actual operand, not just True/False.
- Use `is None`, not `== None`.

## Active Recall

1. Which of the following are falsy: `0`, `[]`, `"0"`, `None`, `[False]`, `{}`, `"False"`?
2. What does `"hello" or "world"` return? What about `"" or "world"`?
3. Why is `if x is not None and x.value > 0:` safer than reversing the operands?
4. What's the difference between `if x == None:` and `if x is None:`? Which should you use?
5. Rewrite `if len(my_list) == 0: print("empty")` in Pythonic form.

---

# Chapter 5: `None` — The Absence of a Value

## What & Why

`None` represents "no value here." It's not zero, not an empty string, not false — it's the deliberate absence of a value. Every language has some form of it (`null`, `nil`, `undefined`). In Python, it's `None`, and it's used constantly.

## What `None` Is

`None` is the sole instance of a type called `NoneType`. There is exactly one `None` in the entire Python universe — every variable set to `None` points to the same object.

```python
x = None
y = None
x is y      # True — same object

print(type(None))    # <class 'NoneType'>
```

You cannot create another `None`. You cannot subclass `NoneType` in normal code.

## When You Encounter `None`

### 1. As an explicit "empty" marker

```python
result = None
# ... later, after some work
if condition:
    result = compute_something()

if result is None:
    print("nothing was computed")
```

### 2. As the default return of functions with no `return`

```python
def greet(name):
    print(f"Hello, {name}")

x = greet("Sid")
print(x)     # None — greet() has no return statement
```

Every function returns something. If you don't say `return X`, Python returns `None` for you.

### 3. As default argument values

```python
def send_email(to, subject, body=None):
    if body is None:
        body = "(no content)"
    ...
```

### 4. As the return value of mutating methods

Many list/dict methods that mutate in place return `None`:

```python
result = [3, 1, 2].sort()
print(result)     # None — sort() mutates and returns None!
```

This is the source of an enormous number of beginner bugs.

## The Right Way to Check for `None`

Always use `is` and `is not`:

```python
if x is None:
    ...
if x is not None:
    ...
```

**Never** use `== None`. It works but is un-Pythonic, potentially slower, and can be overridden by custom classes with weird `__eq__` methods.

## Why `None` Is Better Than 0, "", or []

Suppose a function tries to fetch a user's age from a database. What if the age is unknown?

- If you return `0`, callers can't distinguish "unknown" from "newborn."
- If you return `-1` as a sentinel, everyone has to know that convention.
- If you return `None`, the caller knows immediately: "there's no value here."

```python
age = fetch_age(user_id)
if age is None:
    print("age unknown")
else:
    print(f"age is {age}")
```

This distinction — **missing** vs. **zero** — is architecturally important for data pipelines, AI eval logic, and any system where the difference between "the model returned 0" and "the model failed to return anything" matters.

## `None` in Optional Arguments — the Mutable Default Trap

This is one of Python's most infamous gotchas:

```python
def add_item(item, bucket=[]):    # DON'T DO THIS
    bucket.append(item)
    return bucket

print(add_item("a"))    # ['a']
print(add_item("b"))    # ['a', 'b']  ← surprise!
```

Default arguments are evaluated **once**, when the function is defined — not every time it's called. That single list persists across calls.

The fix: use `None` as the default and create a fresh list inside:

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(add_item("a"))    # ['a']
print(add_item("b"))    # ['b']  ← correct
```

Rule: **never use mutable defaults (`[]`, `{}`, `set()`). Use `None` and create the container inside the function.**

## Common Mistakes

- **`if x == None:`** — works but wrong. Use `if x is None:`.
- **Assigning the result of a mutating method:** `sorted_list = my_list.sort()` gives you `None`. Use `sorted_list = sorted(my_list)` or call `.sort()` on its own line.
- **Mutable default arguments.** Always use `None` and initialize inside.
- **Confusing `None`, `False`, and `0`.** They're all falsy but they're not equal: `None != False != 0`.

## Best Practices

- Use `None` explicitly for "missing" data — don't invent sentinel values.
- Type-annotate `None`-able returns: `def find_user(id) -> User | None:`.
- Check with `is` / `is not`, always.
- For default arguments that need containers, always use `None`.

## Key Takeaways

- `None` is a unique singleton meaning "no value."
- Functions without `return` return `None` implicitly.
- Mutating methods (`list.sort()`, `list.append()`) return `None`.
- Use `is None` / `is not None`, never `== None`.
- Never use mutable default arguments — use `None` and check inside.

## Active Recall

1. What does the function `def f(x): print(x)` return when called?
2. Why should you write `if x is None:` instead of `if x == None:`?
3. What does `result = my_list.sort()` set `result` to, and why?
4. Explain the "mutable default argument" trap and how to fix it.
5. Why is `None` architecturally better than returning `0` or `""` to signal "no data"?

---

# Chapter 6: Strings (Part 1) — Basics, Indexing, Slicing

## What & Why

Text is everywhere: user input, file contents, API responses, LLM outputs, log lines. In Python, text is represented by the `str` type. Strings are one of the most-used types in the language, so this chapter and the next are worth dwelling on.

## What a String Is

A string is an **immutable, ordered sequence of characters**. "Ordered" means each character has a position (index). "Immutable" means once you create a string, you cannot change it — every "modification" gives you a new string.

## Creating Strings

Four ways to write a string literal:

```python
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''triple single quotes — can span
multiple lines'''
s4 = """triple double quotes — also multi-line
and often used for docstrings"""
```

Single and double quotes are 100% equivalent. Use whichever avoids escaping:

```python
"It's fine"          # easier than 'It\'s fine'
'She said "hi"'      # easier than "She said \"hi\""
```

Triple quotes let you write literal newlines and are used for docstrings (explained later).

## Escape Sequences

Some characters need special notation:

| Escape   | Meaning                   |
| -------- | ------------------------- |
| `\n`     | newline                   |
| `\t`     | tab                       |
| `\\`     | a literal backslash       |
| `\'`     | a literal single quote    |
| `\"`     | a literal double quote    |
| `\0`     | null character            |
| `\uXXXX` | Unicode character (4 hex) |

```python
print("line 1\nline 2")
# line 1
# line 2

print("a\tb\tc")
# a	b	c
```

### Raw Strings

Prefix a string with `r` to disable escape processing. Useful for file paths and regex:

```python
path = r"C:\Users\Sid\Documents"    # backslashes stay as-is
print(path)     # C:\Users\Sid\Documents

# without r, this would be interpreted as \U, \S, \D
```

## String Length: `len()`

```python
len("hello")     # 5
len("")          # 0
len("hi there")  # 8 — spaces count
len("héllo")     # 5 — each character counts once
```

## Indexing — Grabbing One Character

Every character has an index. Indexing starts at **0** on the left, and negative indices count from the right.

```
Index:   0   1   2   3   4
String:  P   y   t   h   o
Neg:    -5  -4  -3  -2  -1
```

```python
s = "Python"
s[0]     # 'P'
s[1]     # 'y'
s[-1]    # 'n'  — last character
s[-2]    # 'o'  — second-to-last
s[100]   # IndexError: string index out of range
```

Negative indexing is enormously useful when you don't know the length: `filename[-4:]` grabs the last 4 characters without needing `len(filename) - 4`.

## Slicing — Grabbing a Range

`s[start:end]` returns a new string from `start` (inclusive) to `end` (exclusive).

```python
s = "Python"
s[0:3]    # 'Pyt'
s[1:4]    # 'yth'
s[:3]     # 'Pyt'   — omit start = 0
s[3:]     # 'hon'   — omit end = len(s)
s[:]      # 'Python' — full copy
```

**The end is exclusive.** `s[0:3]` gives indices 0, 1, 2 — three characters. Once you internalize "start inclusive, end exclusive," almost every slicing operation becomes obvious.

### Negative Slice Indices

```python
s = "Python"
s[-3:]     # 'hon'  — last three characters
s[:-2]     # 'Pyth' — everything except last two
s[-4:-1]   # 'tho'  — from index -4 up to but not including -1
```

### The Third Argument: Step

`s[start:end:step]`. Step controls the stride.

```python
s = "abcdefgh"
s[::2]     # 'aceg'    — every second character
s[1::2]    # 'bdfh'    — every second, starting at index 1
s[::-1]    # 'hgfedcba' — REVERSED string, a common trick
s[::-2]    # 'hfdb'    — every second, reversed
```

`s[::-1]` is the idiomatic Pythonic way to reverse a string.

### Slicing Never Errors

Slice indices out of range are silently clamped:

```python
s = "abc"
s[0:100]     # 'abc'  — no error
s[100:200]   # ''     — empty string, no error
s[100]       # IndexError! (single-item indexing DOES error)
```

## String Concatenation

Add strings with `+`:

```python
first = "Sid"
last = "Hary"
full = first + " " + last
print(full)    # Sid Hary
```

Multiply a string with `*` to repeat:

```python
"ab" * 3        # 'ababab'
"-" * 20        # '--------------------'
```

You can only add strings to strings — `"5" + 5` raises `TypeError`. Cast first: `"5" + str(5)` or `int("5") + 5`.

## Membership: `in` and `not in`

Check if a substring appears in a string:

```python
"py" in "python"        # True
"Py" in "python"        # False — case sensitive
"z" not in "python"     # True

# Common use:
name = input("Enter name: ")
if "@" in name:
    print("that looks like an email")
```

## Immutability — the Fundamental Rule

Once created, a string cannot be modified:

```python
s = "hello"
s[0] = "H"      # TypeError: 'str' object does not support item assignment
```

To "change" a string, build a new one:

```python
s = "hello"
s = "H" + s[1:]     # 'Hello' — new string, s now labels it
```

This is why every string method that appears to modify a string actually **returns a new string**. The original is untouched.

## Iterating Over Strings

Strings are sequences, so you can loop character-by-character:

```python
for ch in "hello":
    print(ch)
# h
# e
# l
# l
# o
```

## Common Mistakes

- **Trying to modify a character by index.** `s[0] = "H"` fails. Rebuild the string.
- **Forgetting slicing is end-exclusive.** `s[0:5]` gives 5 characters (indices 0-4), not 6.
- **Confusing indexing out-of-range vs. slicing out-of-range.** `s[100]` errors; `s[100:200]` returns empty.
- **Using `+` to build strings inside a loop for long strings.** This is O(n²) in Python because each concatenation creates a new string. For many joins, use `"".join(list_of_strings)` (covered in Chapter 7).
- **Assuming `"5" == 5`.** They're different types, always unequal.

## Best Practices

- Prefer single quotes for short strings, double for strings containing apostrophes.
- Use raw strings (`r"..."`) for file paths and regex.
- Use `in` for substring checks — clean and fast.
- Reverse a string with `s[::-1]`.
- Never mutate; always rebuild.

## Key Takeaways

- Strings are immutable, ordered sequences of characters.
- Index from 0 (left) or -1 (right). Slicing is `[start:end:step]` with end exclusive.
- `+` concatenates, `*` repeats, `in` tests membership.
- Slices never error; single-index access does.
- To "modify" a string, build a new one.

## Active Recall

1. Given `s = "Python"`, what does `s[1:4]` return? What about `s[-2:]`?
2. Write the Pythonic one-liner to reverse a string.
3. What error does `"hello"[0] = "H"` produce, and why?
4. What's the difference between `"apple"[10]` and `"apple"[10:20]`?
5. What's a raw string, and when should you use one?

---

# Chapter 7: Strings (Part 2) — Methods and f-strings

## What & Why

Chapter 6 was structure. This chapter is action — the tools you'll use every day to inspect, clean, split, join, and format strings. Nearly every real Python program uses these constantly.

## The Golden Rule (Again)

Every string method returns a **new string**. The original is never modified. So:

```python
name = "sid"
name.upper()           # returns "SID" — but name is still "sid"
print(name)            # sid

name = name.upper()    # NOW name labels "SID"
print(name)            # SID
```

If you forget to reassign, your "change" vanishes. This is one of the most common beginner bugs.

## Case Manipulation

```python
"hello".upper()          # 'HELLO'
"HELLO".lower()          # 'hello'
"hello world".title()    # 'Hello World' — first letter of each word
"hello world".capitalize() # 'Hello world' — only first letter of string
"Hello".swapcase()       # 'hELLO'
```

Use `.lower()` for case-insensitive comparisons:

```python
if user_input.lower() == "yes":
    ...
```

## Trimming Whitespace

```python
"  hello  ".strip()      # 'hello' — removes both sides
"  hello  ".lstrip()     # 'hello  ' — left only
"  hello  ".rstrip()     # '  hello' — right only
```

By default these remove spaces, tabs, newlines. You can pass characters to strip:

```python
"###hello###".strip("#")     # 'hello'
"www.google.com".strip("mwc.")   # 'google' — strips ANY of those characters
```

**Enormously useful** when cleaning input from users, files, or LLMs, all of which love to add trailing newlines.

## Searching and Counting

```python
s = "the quick brown fox jumps over the lazy dog"

s.count("the")           # 2
s.find("fox")            # 16   — index of first occurrence
s.find("cat")            # -1   — DID NOT ERROR, returns -1
s.index("fox")           # 16   — same as find, but ERRORS if not found
s.index("cat")           # ValueError!

s.startswith("the")      # True
s.endswith("dog")        # True
s.endswith(".txt")       # False
```

### The `find()` Trap

`.find()` returns `-1` on failure — but `-1` is also a valid index (the last character). If you use `.find()`'s output as a slice or index without checking, you'll silently get the wrong character:

```python
s = "hello"
idx = s.find("z")     # -1
s[idx]                # 'o' — WRONG! You wanted "not found."
```

Fix: either check for `-1` explicitly, or use `.index()` and let it raise:

```python
idx = s.find("z")
if idx == -1:
    print("not found")
else:
    ...
```

Or use `in`, which is clearer:

```python
if "z" in s:
    ...
```

## Replacing

```python
"hello world".replace("world", "Python")   # 'hello Python'
"aaaa".replace("a", "b")                   # 'bbbb'
"aaaa".replace("a", "b", 2)                # 'bbaa' — only first 2
```

Returns a new string. Remember to reassign.

## Splitting and Joining — the Bridge to Lists

### `split()` — string → list

Break a string into pieces. Default splits on any whitespace:

```python
"the quick brown fox".split()          # ['the', 'quick', 'brown', 'fox']
"a,b,c,d".split(",")                    # ['a', 'b', 'c', 'd']
"a,,b,,c".split(",,")                   # ['a', 'b', 'c']
"one line\ntwo line".split("\n")        # ['one line', 'two line']

"a,b,c".split(",", 1)                   # ['a', 'b,c'] — split at most once
```

`splitlines()` splits on any line boundary and is safer than `.split("\n")` when files have mixed line endings:

```python
"line1\nline2\r\nline3".splitlines()    # ['line1', 'line2', 'line3']
```

### `join()` — list → string

The inverse. You call `.join()` on the **separator string**, passing an iterable of strings.

```python
",".join(["a", "b", "c"])           # 'a,b,c'
" ".join(["hello", "world"])         # 'hello world'
"\n".join(["line 1", "line 2"])      # 'line 1\nline 2'
"".join(["h", "e", "l", "l", "o"])   # 'hello'
```

The syntax feels backwards at first (`sep.join(iterable)` instead of `iterable.join(sep)`), but it makes sense: `join` is a method on strings, not on lists. Just memorize the pattern.

All items in the iterable must be strings. Cast first if not:

```python
nums = [1, 2, 3]
",".join(nums)             # TypeError!
",".join(str(n) for n in nums)    # '1,2,3'
```

## Type-Checking Predicates

Methods that return True/False about the string's contents:

```python
"12345".isdigit()          # True
"abc".isalpha()            # True
"abc123".isalnum()         # True
"   ".isspace()            # True
"HELLO".isupper()          # True
"hello".islower()          # True
"Hello".istitle()          # True — first letter of each word capitalized
"".isdigit()               # False — empty strings return False for these
```

Watch out for edge cases: `"3.14".isdigit()` is `False` because of the dot. `"-5".isdigit()` is also `False`.

## String Formatting

You have four ways to build strings with variables. Learn f-strings; use them almost always. The others exist mainly so you can read old code.

### 1. Concatenation (the awkward way)

```python
name = "Sid"
age = 23
msg = "Hello, " + name + "! You are " + str(age) + " years old."
```

Manual, error-prone, and requires casting numbers to strings.

### 2. `%` Formatting (the ancient way — used in old code)

```python
msg = "Hello, %s! You are %d years old." % (name, age)
```

C-style. Don't write new code with this, but you'll see it in old codebases.

### 3. `.format()` (the transitional way)

```python
msg = "Hello, {}! You are {} years old.".format(name, age)
msg = "Hello, {name}! You are {age} years old.".format(name=name, age=age)
```

Better than `%` but verbose.

### 4. **f-strings** (the modern way — use these)

Prefix the string with `f`. Put expressions inside `{}`.

```python
name = "Sid"
age = 23
msg = f"Hello, {name}! You are {age} years old."
```

Anything inside `{}` is a **Python expression**, not just a variable:

```python
f"Next year I'll be {age + 1}"
f"Half your age is {age / 2}"
f"Your name uppercase: {name.upper()}"
f"Are you an adult? {age >= 18}"
```

### f-string Formatting Options

Add a format spec after `:`.

```python
pi = 3.14159265
f"{pi:.2f}"          # '3.14'   — 2 decimal places
f"{pi:.4f}"          # '3.1416' — 4 decimal places
f"{pi:10.2f}"        # '      3.14' — width 10, 2 decimals

n = 42
f"{n:5}"             # '   42'    — right-aligned, width 5
f"{n:<5}"            # '42   '    — left-aligned
f"{n:>5}"            # '   42'    — right-aligned (default for numbers)
f"{n:^5}"            # ' 42  '    — centered
f"{n:05}"            # '00042'    — zero-padded

f"{1234567:,}"       # '1,234,567' — thousands separator
f"{0.75:.1%}"        # '75.0%'    — as a percentage
f"{255:x}"           # 'ff'       — hex
f"{255:b}"           # '11111111' — binary
```

Debugging trick — the `=` sign in f-strings (Python 3.8+):

```python
x = 10
print(f"{x=}")         # x=10
print(f"{x + 5=}")     # x + 5=15
```

Fantastic for debugging.

## Multi-line f-strings

Use triple quotes:

```python
name = "Sid"
score = 95
report = f"""
Student Report
--------------
Name:  {name}
Score: {score}
Grade: {'A' if score >= 90 else 'B'}
"""
```

## Common Mistakes

- **Not reassigning after a method call.** `s.strip()` returns a new string; the original is unchanged.
- **Using `.find()` and forgetting the `-1` case.** Prefer `in`.
- **Trying to `join()` a list of non-strings.** `",".join([1,2,3])` fails; cast first.
- **Using `%` or `.format()` in new code.** Use f-strings.
- **Forgetting the `f` prefix.** `"{name}"` is literal, not formatted.

## Best Practices

- **f-strings** for formatting. Always.
- `.strip()` all user input and file lines. Trailing whitespace is a real enemy.
- Use `.lower()` for case-insensitive comparisons.
- Use `in` for substring checks, not `.find()`.
- Prefer `.join()` over `+=` in loops — vastly faster for many strings.

## Key Takeaways

- All string methods return **new strings** — reassign or lose your work.
- `.strip()`, `.split()`, `.join()`, `.replace()` are the workhorses.
- `.find()` returns -1 on failure; `.index()` raises. Use `in` for pure membership.
- f-strings (`f"{expr}"`) are the modern way to format strings, and support inline expressions, formatting specs, and debugging with `=`.

## Active Recall

1. What does `"  hello  ".strip()` return? Does the original string change?
2. Write a one-liner that turns `"a,b,c,d"` into a list of characters, then back into a string with `|` between them.
3. What's the difference between `.find("x")` and `.index("x")` when `"x"` isn't in the string?
4. What does `f"{2 + 3:5.2f}"` produce?
5. Given `nums = [1, 2, 3]`, how do you produce the string `"1-2-3"`?

---

# Chapter 8: Input, Output, and Type Casting

## What & Why

Programs need to communicate with the outside world: read from users, print results, save state. This chapter covers `print()` (output), `input()` (user input), and the essential casting operations that connect them to the rest of your code.

## `print()` — Output

The universal way to show output:

```python
print("Hello")            # Hello
print("Hello", "World")   # Hello World  — args separated by space
print(1, 2, 3)            # 1 2 3
print()                   # (blank line)
```

### Keyword Arguments: `sep`, `end`, `file`

```python
print("a", "b", "c", sep=", ")     # a, b, c
print("a", "b", "c", sep="")       # abc
print("no newline", end="")        # doesn't add \n at the end
print("A")
print("B", end="")
print("C")
# A
# BC
```

Default `sep` is a space, default `end` is `\n`. Override both when you want fine control.

`print()` also accepts `file=` to write to a file instead of stdout — you'll see this later.

### Debugging with f-strings

Modern debugging pattern:

```python
name = "Sid"
score = 95
print(f"{name=}, {score=}")     # name='Sid', score=95
```

## `input()` — Read from the User

Pauses the program and waits for the user to type a line, then press Enter.

```python
name = input("What is your name? ")
print(f"Hello, {name}")
```

**Critical fact:** `input()` **always returns a string**, no matter what the user types. If they type `25`, you get the string `"25"`, not the integer `25`.

```python
age = input("Age? ")     # user types 25
print(type(age))          # <class 'str'>
age + 5                   # TypeError! Cannot add str and int
```

This is the single most common beginner error. Every value that comes from `input()` (or from a file, or from a text-based API) is a string until you convert it.

## Type Casting — Converting Between Types

Every built-in type has a constructor function:

```python
int("42")        # 42
int("42.5")      # ValueError! int() can't parse decimal strings
int(42.9)        # 42 — truncates toward zero (does NOT round)
int(True)        # 1
int(False)       # 0

float("3.14")    # 3.14
float("42")      # 42.0
float(42)        # 42.0
float("inf")     # inf

str(42)          # '42'
str(3.14)        # '3.14'
str(True)        # 'True'
str([1, 2, 3])   # '[1, 2, 3]'  — always works, gives a repr

bool(0)          # False
bool(1)          # True
bool("")         # False
bool("anything") # True — non-empty string
bool([])         # False

list("hello")    # ['h', 'e', 'l', 'l', 'o']
list((1, 2, 3))  # [1, 2, 3]
tuple([1, 2, 3]) # (1, 2, 3)
set([1, 2, 2])   # {1, 2}
```

### Safe Casting Pattern

Raw `int(user_input)` crashes on any non-numeric input. In real programs, wrap in a `try`:

```python
raw = input("Age? ")
try:
    age = int(raw)
except ValueError:
    print("that wasn't a number")
    age = None
```

You'll learn `try`/`except` properly in Chapter 26.

## Reading Multiple Values in One Line

Common idiom: read multiple space-separated numbers:

```python
# Input: "10 20 30"
line = input("Enter three numbers: ")
a, b, c = line.split()          # ['10', '20', '30']
a, b, c = int(a), int(b), int(c)
```

Or in one shot with a comprehension (covered later):

```python
nums = [int(x) for x in input().split()]
```

## `print()` vs `return`

Beginners often confuse these. They are completely different.

- `print()` sends text to the screen (or wherever stdout points).
- `return` sends a value back from a function to its caller.

```python
def add(a, b):
    return a + b       # sends the result back

def add_print(a, b):
    print(a + b)       # displays the result — but returns None!

x = add(2, 3)          # x = 5
y = add_print(2, 3)    # prints 5, but y = None
```

You cannot do arithmetic on `print()`'s output. `print()` is for humans; `return` is for the program.

## Common Mistakes

- **Doing math on `input()` directly.** `input("age: ") + 5` crashes. Cast first.
- **Using `int()` on a decimal string.** `int("3.14")` fails. Go through float: `int(float("3.14"))`.
- **Assuming `int(3.9)` rounds.** It truncates to 3. Use `round()` for rounding.
- **Confusing `print()` with `return`.** Functions that only `print()` return `None`.
- **`bool("False")` returns `True`** — any non-empty string is truthy. To parse a Boolean from text, compare explicitly: `raw.lower() == "true"`.

## Best Practices

- Immediately cast `input()` results to the type you need: `age = int(input("Age? "))`.
- Use f-strings in `print()`, not concatenation.
- For robust input, wrap casting in `try/except`.
- Return values from functions; use `print()` only in top-level scripts or for logging.

## Key Takeaways

- `input()` always returns a string. Cast before doing math.
- `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()` are the standard casts.
- `int()` truncates; `round()` rounds.
- `print()` is for output; `return` is for passing values within your program.
- `print()` accepts `sep` and `end` keyword arguments for formatting.

## Active Recall

1. What is the type of `input("age: ")`, no matter what the user types?
2. Cast the string `"3.14"` to an integer. What's the pitfall, and how do you avoid it?
3. What does `print("a", "b", "c", sep="-", end="!")` produce?
4. Why is `bool("False")` equal to `True`?
5. What's the difference between a function that ends with `print(result)` and one that ends with `return result`?

---

# Part III — Control Flow

---

# Chapter 9: Operators & Expressions

## What & Why

You've seen operators piecemeal. This chapter is the consolidated reference: every operator, its precedence, and the traps in each category. Come back to this chapter for lookups.

## Category 1: Arithmetic Operators

Covered in Chapter 3. Summary:

| Op   | Meaning        | Example  | Result |
| ---- | -------------- | -------- | ------ |
| `+`  | Add            | `3 + 2`  | `5`    |
| `-`  | Subtract       | `3 - 2`  | `1`    |
| `*`  | Multiply       | `3 * 2`  | `6`    |
| `/`  | Divide (float) | `7 / 2`  | `3.5`  |
| `//` | Floor divide   | `7 // 2` | `3`    |
| `%`  | Modulo         | `7 % 2`  | `1`    |
| `**` | Power          | `2 ** 3` | `8`    |

`+` and `*` also work on strings and lists (concatenation and repetition).

## Category 2: Comparison Operators

Return `True` or `False`.

| Op   | Meaning                  |
| ---- | ------------------------ |
| `==` | Equal                    |
| `!=` | Not equal                |
| `<`  | Less than                |
| `>`  | Greater than             |
| `<=` | Less than or equal to    |
| `>=` | Greater than or equal to |

Chained: `18 <= age < 65` reads as `(18 <= age) and (age < 65)`.

**Trap:** `==` compares values across compatible types. `1 == 1.0` is `True`. `1 == "1"` is `False` (never equal across incompatible types, no error either).

## Category 3: Logical Operators

| Op    | Meaning      |
| ----- | ------------ |
| `and` | Both true    |
| `or`  | At least one |
| `not` | Negate       |

Return the operand value (not necessarily a Boolean) — see Chapter 4.

## Category 4: Assignment Operators

Basic:

```python
x = 5
```

**Compound assignment** — modify in place:

| Op    | Equivalent   |
| ----- | ------------ |
| `+=`  | `x = x + y`  |
| `-=`  | `x = x - y`  |
| `*=`  | `x = x * y`  |
| `/=`  | `x = x / y`  |
| `//=` | `x = x // y` |
| `%=`  | `x = x % y`  |
| `**=` | `x = x ** y` |

```python
counter = 0
counter += 1        # counter is now 1
counter *= 5        # counter is now 5
```

For **mutable objects**, `+=` may actually mutate in place instead of rebinding:

```python
a = [1, 2, 3]
b = a
a += [4]           # mutates the list in place — b is also [1, 2, 3, 4]

a = a + [5]        # creates a new list — b unchanged
```

This is subtle but important for lists. `+=` on a list is equivalent to `.extend()`.

## Category 5: Identity Operators

`is` and `is not` — checked against object identity, not value.

```python
a = [1, 2, 3]
b = a
a is b          # True — same object
a == b          # True — same values

c = [1, 2, 3]
a is c          # False — different objects
a == c          # True — same values
```

Only use `is` for `None`, `True`, `False`.

## Category 6: Membership Operators

`in` and `not in` — test if a value appears in a collection.

```python
3 in [1, 2, 3]           # True
"py" in "python"         # True
"apple" in {"apple", "banana"}   # True
"key" in {"key": 1}      # True — checks dict keys, not values
```

For dicts, `in` tests keys only, not values.

## Category 7: Bitwise Operators (Rarely Used)

Operate on the binary representation of integers.

| Op   | Meaning      | Example   | Result |
| ---- | ------------ | --------- | ------ |
| `&`  | AND          | `5 & 3`   | `1`    |
| `\|` | OR           | `5 \| 3`  | `7`    |
| `^`  | XOR          | `5 ^ 3`   | `6`    |
| `~`  | NOT (invert) | `~5`      | `-6`   |
| `<<` | Left shift   | `1 << 3`  | `8`    |
| `>>` | Right shift  | `16 >> 2` | `4`    |

You'll almost never need these unless you're working with hardware, bitmasks, or cryptography. Move on.

## The `not`, `and`, `or` Return-Value Trick

Reviewed in Chapter 4 but worth repeating with examples:

```python
0 or "hello"         # "hello"
"" or None or 42     # 42
"a" or "b"           # "a"

None and "x"         # None (short-circuits, never evaluates "x")
1 and 2 and 3        # 3 (all truthy — returns last)
1 and 0 and "x"      # 0 (stops at first falsy)
```

Idiomatic uses:

```python
# Default value if empty:
name = user_input or "Anonymous"

# Conditional attribute access:
user = get_user()
name = user and user.name    # None if user is None, else user.name
```

## Operator Precedence

When multiple operators appear, precedence decides the order. Learn the highlights; use parentheses for clarity in real code.

From highest (evaluated first) to lowest:

1. `**`
2. Unary `+x`, `-x`, `~x`
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. `<<`, `>>`
6. `&`
7. `^`
8. `|`
9. Comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in`
10. `not`
11. `and`
12. `or`
13. Ternary (`x if cond else y`)
14. Assignment (`=`, `+=`, etc.)

Examples:

```python
2 + 3 * 4              # 14   (multiplication first)
(2 + 3) * 4            # 20   (parens override)
2 ** 3 ** 2            # 512  (right-associative: 2 ** (3 ** 2))
not True or False      # False (not True → False; False or False → False)
```

**Best practice:** if a reader has to think about precedence, add parentheses. Clarity beats cleverness.

## The Ternary Expression

Python's inline "if" — a single expression that picks between two values.

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

Equivalent to:

```python
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

The ternary form is preferred for **simple, single-value** decisions. Do not nest ternaries — it becomes unreadable fast.

## The Walrus Operator `:=` (Python 3.8+)

Assigns a value **as part of an expression**. Useful in `while`, `if`, and comprehensions.

```python
# Instead of:
line = input()
while line != "quit":
    print(line)
    line = input()

# You can write:
while (line := input()) != "quit":
    print(line)
```

Nice for avoiding repetition. Don't overuse it — it can obscure code.

## Common Mistakes

- **Forgetting operator precedence.** `not x == y` means `not (x == y)`, not `(not x) == y`. Use parentheses.
- **Using `is` for value comparison.** Use `==` unless comparing to `None`, `True`, `False`.
- **Using `and`/`or` where you meant `&`/`|`.** Bitwise vs. logical — very different. `and`/`or` for booleans; `&`/`|` for bits or NumPy arrays.
- **`x += [1]` mutating in place** unexpectedly for lists. Aliased lists change together.
- **Chained comparisons with mixed operators.** `1 == 1 == True` is `True`, but this can hide bugs. Prefer explicit `and`.

## Best Practices

- Use parentheses whenever precedence isn't obvious.
- Prefer `x is None` over `x == None`.
- Reach for ternary only for one-line, simple decisions.
- Use `+=` for accumulators (`total += n`) and pattern matches (`counters[key] += 1`).
- Reserve bitwise operators for genuine bit manipulation.

## Key Takeaways

- Seven categories of operators: arithmetic, comparison, logical, assignment, identity, membership, bitwise.
- `and` / `or` short-circuit and return operand values, not just Booleans.
- Precedence exists; parentheses always win.
- The ternary `x if cond else y` is a compact conditional expression.
- `:=` (walrus) assigns inline; use sparingly.

## Active Recall

1. Evaluate: `2 + 3 * 4 ** 2 // 5`.
2. What's the difference in effect between `a = a + [5]` and `a += [5]` when another variable also points to `a`?
3. When does `and` return something other than `True` or `False`?
4. Write a ternary expression that assigns `"even"` to `parity` if `n` is even, else `"odd"`.
5. What's the difference between `x in dict` and `x in dict.values()`?

---

# Chapter 10: Conditional Statements

## What & Why

`if`/`elif`/`else` lets your program choose between paths. Along with loops (next chapter), it's the entire foundation of program logic.

## The Basic `if`

```python
if condition:
    # runs only if condition is truthy
    do_something()
```

The condition can be anything with a truthiness — a Boolean, a comparison, a variable, a call, whatever. Python evaluates it, and if truthy, runs the indented block.

Notice the **colon** at the end of `if condition:`. That's not optional. Forgetting it is the single most common syntax error.

```python
age = 20
if age >= 18:
    print("adult")
```

## Indentation Defines Blocks

Python has **no braces** `{ }`. Instead, code blocks are defined by indentation. Every line indented at the same level inside an `if` belongs to the `if`.

```python
if age >= 18:
    print("adult")
    print("can vote")
print("this always runs — not indented under the if")
```

**Rules:**
- Use consistent indentation. **Four spaces** is the standard.
- Never mix tabs and spaces. Ever.
- Every code block (`if`, `for`, `def`, `class`, etc.) requires an indented body.

Bad indentation → `IndentationError`. Mixing tabs and spaces → `TabError` or worse: invisible bugs where two lines look aligned but aren't.

## `if` / `else`

```python
if age >= 18:
    print("adult")
else:
    print("minor")
```

`else` catches "everything the `if` didn't match." It has no condition of its own.

## `if` / `elif` / `else`

Multi-way branching. `elif` = "else if."

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

Python evaluates from top to bottom. The **first** matching condition wins; the rest are skipped. Order matters:

```python
# WRONG order: if you got 95, all four fire? No — only the first, which is score >= 60.
if score >= 60:
    grade = "D"
elif score >= 70:
    grade = "C"     # unreachable!
elif score >= 80:
    grade = "B"     # unreachable!
elif score >= 90:
    grade = "A"     # unreachable!
```

Order your conditions from most specific/highest to most general.

## Independent `if`s vs. `if`/`elif`

Compare:

```python
# Version A — three independent ifs
if score >= 90: print("A-tier")
if score >= 80: print("B-tier")
if score >= 70: print("C-tier")

# Version B — chained
if score >= 90: print("A-tier")
elif score >= 80: print("B-tier")
elif score >= 70: print("C-tier")
```

With `score = 95`:
- Version A prints **all three** (each `if` runs independently).
- Version B prints **only "A-tier"** (first match wins, others skipped).

Use `elif` when the conditions are mutually exclusive (only one should fire).

## Nested `if`

You can put `if`s inside `if`s.

```python
if user_logged_in:
    if user.is_admin:
        show_admin_panel()
    else:
        show_user_dashboard()
else:
    show_login_page()
```

Nesting works but hurts readability quickly. Flatten when you can:

```python
# Flatter alternative
if user_logged_in and user.is_admin:
    show_admin_panel()
elif user_logged_in:
    show_user_dashboard()
else:
    show_login_page()
```

Or use early returns / guard clauses when inside a function:

```python
def render():
    if not user_logged_in:
        show_login_page()
        return
    if user.is_admin:
        show_admin_panel()
        return
    show_user_dashboard()
```

Guard clauses reduce nesting depth and are easier to reason about.

## The Ternary Expression Revisited

For single-value conditionals, the ternary is cleaner than `if`/`else`:

```python
label = "adult" if age >= 18 else "minor"
```

Use it when both branches produce a single value that you're assigning. Don't use it for side effects.

## `match` / `case` — Structural Pattern Matching (Python 3.10+)

The modern replacement for long `elif` chains when you're matching on a value's shape. Similar to `switch` in other languages, but much more powerful.

```python
def describe(x):
    match x:
        case 0:
            return "zero"
        case 1 | 2 | 3:
            return "small positive"
        case int() if x < 0:
            return "negative"
        case str():
            return f"a string of length {len(x)}"
        case [a, b]:
            return f"a two-item list: {a}, {b}"
        case {"name": name, "age": age}:
            return f"a dict with name={name}, age={age}"
        case _:
            return "something else"
```

The `_` case is the catch-all (like `default` in switch).

For most beginners, `if`/`elif` is enough. Learn `match` when you're comfortable — it shines for parsing complex data structures like JSON responses.

## Common Mistakes

- **Missing colon.** `if x > 5` (no colon) is a `SyntaxError`.
- **Using `=` instead of `==`.** `if x = 5:` is a `SyntaxError`. Use `==` for comparison.
- **Wrong `elif` order.** Wider conditions first swallow narrower ones.
- **Mixing tabs and spaces.** Configure your editor to insert spaces for tabs, always.
- **Testing floats with `==`.** `if 0.1 + 0.2 == 0.3:` doesn't work (Chapter 3). Use tolerance.
- **Overly deep nesting.** More than 2-3 levels is a signal to refactor.

## Best Practices

- Use `if x:` and `if not x:` for truthiness checks, not `if len(x) > 0:` or `if x == True:`.
- Prefer `elif` chains over nested `if`s when conditions are mutually exclusive.
- Use guard clauses (early returns) to flatten nested logic in functions.
- Use `match`/`case` when matching on structure, `if`/`elif` otherwise.
- Use ternary for concise assignments; avoid for side effects.

## Key Takeaways

- Indentation defines blocks. Four spaces. Never mix tabs and spaces.
- `if`/`elif`/`else` picks one branch; independent `if`s pick multiple.
- Order matters — put specific conditions first.
- Ternary for concise value selection; `match`/`case` for structural patterns.

## Active Recall

1. What error do you get if you forget the colon after `if x > 5`?
2. Write an `if`/`elif`/`else` block that prints "child" if age < 13, "teen" if age < 20, "adult" otherwise.
3. What's the difference between three separate `if` statements and an `if`/`elif`/`elif` chain?
4. Rewrite `x = "yes" if is_ok else "no"` as an if/else block.
5. Why is `if score >= 60: ... elif score >= 90:` a bug?

---

# Chapter 11: The `while` Loop

## What & Why

A `while` loop repeats a block of code as long as a condition stays true. Use it when you don't know in advance how many times you'll loop — you're waiting for something to happen (a user typing "quit," a value converging, a queue emptying).

## Basic Syntax

```python
while condition:
    # runs repeatedly as long as condition is truthy
    body
```

Example — count from 1 to 5:

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

Output:
```
1
2
3
4
5
```

Three ingredients every `while` loop needs:

1. **Initialization** before the loop (`i = 1`).
2. **A condition** that becomes false eventually (`i <= 5`).
3. **A state change** inside the loop that moves toward that condition (`i += 1`).

Forget any of these and you get either no iterations, or an infinite loop.

## The Infinite Loop Trap

```python
i = 1
while i <= 5:
    print(i)
    # forgot i += 1
```

`i` stays 1 forever. Your terminal spits out `1` endlessly. Kill with **Ctrl+C**.

This is not a rare mistake — you will do it. When you do, don't panic: `Ctrl+C` on the terminal always kills a running Python program.

## `while True` — the Intentional Infinite Loop

Sometimes you *want* to loop forever, until an internal condition triggers `break`:

```python
while True:
    user = input("Command? ").strip().lower()
    if user == "quit":
        break
    print(f"You said: {user}")
```

`break` (covered in Chapter 13) immediately exits the innermost enclosing loop.

## `while` with Sentinel Values

Reading input until a specific value:

```python
total = 0
while True:
    n = input("Enter a number (or 'done'): ")
    if n == "done":
        break
    total += int(n)
print(f"Total: {total}")
```

Or with the walrus operator:

```python
total = 0
while (n := input("Enter a number (or 'done'): ")) != "done":
    total += int(n)
```

## `while` for Retry Loops

```python
attempts = 3
while attempts > 0:
    password = input("Password: ")
    if password == "secret":
        print("granted")
        break
    attempts -= 1
    print(f"wrong ({attempts} left)")
else:
    print("locked out")
```

The `else` on a loop is a quirky Python feature (see Chapter 13): it runs if the loop finishes **without** hitting `break`.

## Common `while` Patterns

**Waiting for convergence** (numerical algorithms):

```python
x = 1.0
while abs(x - x_new) > 1e-9:
    x_new = better_estimate(x)
    x = x_new
```

**Consuming a queue:**

```python
tasks = load_tasks()
while tasks:
    task = tasks.pop(0)
    process(task)
# loop exits when tasks is empty (empty list is falsy)
```

**Reading a stream** (file, network) until end-of-data.

## Common Mistakes

- **Forgetting to update the loop variable.** Instant infinite loop.
- **Off-by-one errors.** `while i < 5:` runs 5 times (i = 0,1,2,3,4); `while i <= 5:` runs 6 times. Be deliberate.
- **Updating the wrong variable.** `while i < 5: j += 1` never terminates.
- **Reading input twice inadvertently.** A common bug pattern is calling `input()` at both the top of the loop and just before `while` — you accidentally skip processing the first input. Use the walrus pattern or restructure.

## Best Practices

- Prefer `for` loops when iterating a known collection or a fixed count. Save `while` for conditional / stateful loops.
- Update your loop variable at the **bottom** of the body — easier to spot omissions.
- If you find yourself writing a counter (`i = 0; while i < N: ... i += 1`), you almost certainly want a `for` loop with `range()`.
- Explicit `while True: ... break` is fine and idiomatic when the exit condition is complex.

## Key Takeaways

- `while` is for **condition-based** repetition — repeat until something happens.
- Three ingredients: initialize, check, update.
- Forgetting to update = infinite loop. `Ctrl+C` kills a runaway program.
- Use `while True: ... break` when the exit condition is easier to test inside the loop.

## Active Recall

1. What are the three essential parts of any `while` loop?
2. What key combination stops an infinite loop running in your terminal?
3. Write a `while` loop that reads numbers from the user and adds them to a total until they type "done."
4. Why is `while i < 5:` with `i = 0` different from `while i <= 5:` with `i = 0` in the number of iterations?
5. When would you prefer `while` over `for`?

---

# Chapter 12: The `for` Loop

## What & Why

The `for` loop is Python's tool for **iterating over collections** — lists, tuples, strings, dictionaries, files, ranges, anything that produces values one at a time. Where `while` says "keep going until a condition changes," `for` says "walk through every item in this thing."

## Basic Syntax

```python
for variable in iterable:
    body
```

- `iterable` is anything you can iterate over (list, string, tuple, dict, set, range, file, generator...).
- `variable` gets assigned each item on each pass.

## Iterating Over Common Things

**List:**
```python
for name in ["Alice", "Bob", "Charlie"]:
    print(name)
```

**String:**
```python
for ch in "hello":
    print(ch)
```

**Tuple:**
```python
for x in (1, 2, 3):
    print(x)
```

**Range:**
```python
for i in range(5):
    print(i)     # 0, 1, 2, 3, 4
```

**Dict (iterates over keys by default):**
```python
prices = {"apple": 3, "banana": 2}
for key in prices:
    print(key, prices[key])
```

**Set (unordered):**
```python
for item in {1, 2, 3}:
    print(item)     # order not guaranteed
```

## `range()` — Generating Number Sequences

`range()` is the natural companion of `for`. It generates a sequence of integers **lazily** — it doesn't actually build a list in memory, so it's cheap.

Three forms:

```python
range(stop)                 # 0 to stop-1
range(start, stop)          # start to stop-1
range(start, stop, step)    # start to stop-1, jumping by step
```

Examples:

```python
list(range(5))           # [0, 1, 2, 3, 4]
list(range(1, 6))        # [1, 2, 3, 4, 5]
list(range(0, 10, 2))    # [0, 2, 4, 6, 8]
list(range(10, 0, -1))   # [10, 9, 8, ..., 1]
list(range(10, 0, -2))   # [10, 8, 6, 4, 2]
```

Rules:
- `stop` is **exclusive** (like slicing). `range(5)` produces 0, 1, 2, 3, 4 — not 5.
- `step` can be negative to count down.
- `step` cannot be zero.

## `for i in range(n)` — the C-Style Loop

If you're used to `for (i = 0; i < n; i++)` from C or Java, this is the Python equivalent:

```python
for i in range(n):
    print(i)
```

But almost always, if you're iterating a collection, you don't want an index at all — you want the items directly:

```python
# NOT Pythonic:
for i in range(len(my_list)):
    print(my_list[i])

# Pythonic:
for item in my_list:
    print(item)
```

You only need `range(len(...))` when you truly need the index. And even then, `enumerate` (next chapter) is usually better.

## Loop Variables Are Just Variables

The loop variable persists after the loop ends:

```python
for i in range(5):
    pass
print(i)     # 4 — the last value it held
```

This is legal but rarely useful. Don't rely on it.

## Iterating a Dictionary

Three ways, each explicit about what you want:

```python
prices = {"apple": 3, "banana": 2, "cherry": 5}

# Keys (default):
for k in prices:
    print(k)
# apple, banana, cherry

# Values:
for v in prices.values():
    print(v)
# 3, 2, 5

# Both — using .items() and tuple unpacking:
for k, v in prices.items():
    print(f"{k}: {v}")
# apple: 3
# banana: 2
# cherry: 5
```

`.items()` is the standard idiom when you need both.

## Nested Loops

Loops inside loops. Every iteration of the outer loop runs the entire inner loop.

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)
```

3 × 3 = 9 iterations total. Nested loops multiply — three nested loops of 100 = 1,000,000 iterations. Be aware.

Common use: iterating grids, comparing every pair of items.

## Iterating While Modifying — Don't

A famous trap: modifying a list while iterating over it.

```python
nums = [1, 2, 3, 4, 5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)     # BAD — modifies during iteration
# result: [1, 3, 5]?  actually [1, 3, 5] here, but this is FRAGILE
```

The iteration uses an internal index that gets out of sync when the list shrinks. Sometimes it works, sometimes items get skipped, sometimes it errors. **Never modify a collection while iterating over it.**

Fixes:

```python
# Option 1: iterate over a copy
for n in nums.copy():
    if n % 2 == 0:
        nums.remove(n)

# Option 2 (much better): build a new list
nums = [n for n in nums if n % 2 != 0]
```

Same rule applies to dicts and sets — collect changes, apply after the loop.

## Common Mistakes

- **Using `range(len(x))` when you don't need the index.** Iterate over `x` directly.
- **Off-by-one with `range()`.** `range(1, 10)` gives 1..9, not 1..10. Stop is exclusive.
- **Modifying a list during iteration.** Iterate a copy or build a new list.
- **Iterating a dict expecting keys AND values.** By default you get keys only. Use `.items()`.
- **Reusing the loop variable name.** `for i in range(5): for i in range(3): ...` shadows the outer `i`.

## Best Practices

- Iterate over the collection directly, not by index.
- Use `.items()` for dicts when you need both keys and values.
- Use `range()` only when you truly need a numeric sequence.
- Keep loops shallow — nested triple-nesting is a design smell.
- Never mutate a collection while looping over it.

## Key Takeaways

- `for` iterates over any iterable — lists, strings, dicts, ranges, files.
- `range(start, stop, step)` produces integers lazily; `stop` is exclusive.
- Iterate directly over items, not indices — very Pythonic.
- Use `.items()` for key + value in dicts.
- Never mutate what you're iterating over.

## Active Recall

1. What are the three forms of `range()` and what does each argument mean?
2. What's the difference between `for k in my_dict:` and `for k, v in my_dict.items():`?
3. Why is `for i in range(len(my_list)): print(my_list[i])` un-Pythonic?
4. What happens if you remove items from a list while iterating over it?
5. Write a nested loop that prints all pairs `(i, j)` where `0 <= i < 3` and `0 <= j < i`.

---

# Chapter 13: `break`, `continue`, and the Loop `else` Clause

## What & Why

The default flow of a loop is "run to completion, then move on." Sometimes you want to **skip** an iteration, **exit early**, or **check whether the loop ran cleanly**. These three tools cover all three cases.

## `break` — Exit the Loop Immediately

`break` instantly terminates the **innermost** enclosing loop. Execution resumes at the first line after the loop.

```python
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        break
    print(n)
print("done")
```

Output:
```
1
2
done
```

The moment `n == 3`, `break` fires, the loop stops, and we jump to `print("done")`.

**Classic use — linear search:**

```python
target = 42
for i, val in enumerate(numbers):
    if val == target:
        print(f"found at index {i}")
        break
else:
    print("not found")   # this else fires only if we DIDN'T break
```

## `continue` — Skip to the Next Iteration

`continue` skips the rest of the current iteration and jumps to the top of the loop for the next one.

```python
for n in range(1, 6):
    if n % 2 == 0:
        continue
    print(n)
```

Output:
```
1
3
5
```

Even numbers hit `continue` and skip the `print`. Odd numbers get printed normally.

**Use case:** filter out unwanted items early and keep the main body clean.

```python
for log_line in log_lines:
    if log_line.startswith("#"):     # skip comments
        continue
    if not log_line.strip():         # skip blank lines
        continue
    process(log_line)                # main work stays uncluttered
```

## `break` vs `continue` at a Glance

| Keyword    | Effect                                      |
| ---------- | ------------------------------------------- |
| `break`    | Exit the loop entirely.                     |
| `continue` | Abandon this iteration; start the next one. |

Both only affect the **innermost** loop. In nested loops, `break` from the inner loop returns to the outer loop, not out of everything.

To break out of nested loops, either:
- refactor into a function and use `return`, or
- set a flag and `break` twice.

```python
found = False
for row in grid:
    for cell in row:
        if cell == "X":
            found = True
            break
    if found:
        break
```

## The Loop `else` Clause — Python's Weirdest Feature

Both `for` and `while` can have an `else` block attached. It runs **when the loop finishes normally** — i.e., without a `break`.

```python
for n in [1, 2, 3]:
    if n == 5:
        print("found")
        break
else:
    print("not found")   # runs because we never hit break
```

Output: `not found`.

Change the list to include 5:

```python
for n in [1, 2, 3, 5]:
    if n == 5:
        print("found")
        break
else:
    print("not found")
```

Output: `found`. The `else` was skipped because we `break`ed out.

**Mental model:** think of the loop's `else` as "did the loop complete its search without finding the exit door?" It's most useful for search loops that need a "not found" fallback.

Why is it useful? Without it:

```python
found = False
for n in items:
    if is_target(n):
        found = True
        break

if not found:
    print("not found")
```

With it:

```python
for n in items:
    if is_target(n):
        break
else:
    print("not found")
```

Cleaner, one less variable to track.

## `pass` — the Do-Nothing Statement

Python disallows empty blocks. If you want a placeholder — for example, an `if` you'll fill in later — use `pass`:

```python
if user_is_admin:
    pass   # TODO: implement admin flow
else:
    show_dashboard()
```

Without `pass`, you'd get `IndentationError: expected an indented block`. `pass` is a legal no-op.

You'll see it most often in empty class bodies:

```python
class MyException(Exception):
    pass
```

## Common Mistakes

- **Confusing `break` and `continue`.** `break` exits; `continue` skips. When in doubt, ask: "am I done with the whole loop, or just this one iteration?"
- **Expecting `break` to exit nested loops.** It only exits one level.
- **Assuming `else` on a loop always runs.** It only runs when the loop **completes without `break`**.
- **Using `else` on loops without understanding the trigger.** If it confuses readers, restructure with a `found` flag.
- **Forgetting `pass` in an empty block.** Empty blocks are syntax errors.

## Best Practices

- Use `continue` to filter unwanted items at the top of the loop — keeps the main body flat.
- Use `break` for early-exit searches, saving CPU when the answer is found.
- Reach for the loop `else` only when it makes the code clearly cleaner, not just to show off.
- For deeply nested breaks, refactor into a function and use `return`.

## Key Takeaways

- `break` exits the innermost loop immediately.
- `continue` jumps to the next iteration.
- The loop `else` runs only if the loop finishes without a `break` — useful for "not found" cases.
- `pass` is a placeholder for an empty block.

## Active Recall

1. In `for n in [1,2,3]: if n == 2: break`, what values of `n` are actually processed before the loop exits?
2. Write a loop that prints only numbers not divisible by 3, using `continue`.
3. Under what specific condition does a `for`-loop's `else` block execute?
4. If `break` fires inside a nested inner loop, does the outer loop also exit? How do you exit both?
5. Why does Python have the `pass` statement — what would happen without it?

---

# Part IV — Collections

---

# Chapter 14: Lists

## What & Why

A **list** is Python's most-used data structure: an ordered, mutable collection of items. Think of it as a dynamic array — a sequence you can grow, shrink, reorder, and mutate freely. Every real Python program uses lists constantly.

## Creating Lists

```python
empty = []
nums = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True, None]     # heterogeneous — legal!
nested = [[1, 2], [3, 4], [5, 6]]            # 2D — list of lists
from_string = list("abc")                    # ['a', 'b', 'c']
from_range = list(range(5))                  # [0, 1, 2, 3, 4]
```

Lists can hold anything — different types side by side, even other lists. Under the hood, a list stores pointers to objects, not the objects themselves, which is why heterogeneity is free.

## Indexing and Slicing (Same as Strings)

```python
lst = ["a", "b", "c", "d", "e"]
lst[0]        # 'a'
lst[-1]       # 'e'
lst[1:4]      # ['b', 'c', 'd']
lst[::-1]     # ['e', 'd', 'c', 'b', 'a'] — reversed copy
lst[::2]      # ['a', 'c', 'e']  — every other element
```

Slicing returns a **new list** (shallow copy). Indexing returns a reference to the item.

Lists are mutable, so unlike strings, you **can** assign by index:

```python
lst[0] = "z"
print(lst)     # ['z', 'b', 'c', 'd', 'e']
```

You can even assign to a slice — replacing multiple items at once:

```python
lst[1:3] = ["X", "Y", "Z"]     # replaces 2 items with 3 items!
print(lst)     # ['z', 'X', 'Y', 'Z', 'd', 'e']

lst[:] = []    # empties the list in place
```

## The Big List Methods

### Adding items

```python
lst = [1, 2, 3]

lst.append(4)          # [1, 2, 3, 4]  — add one item at the end
lst.insert(0, "start") # ['start', 1, 2, 3, 4] — insert at index 0
lst.extend([5, 6])     # ['start', 1, 2, 3, 4, 5, 6] — add multiple

# Alternative to extend:
lst += [7, 8]          # same as extend

# Do NOT confuse:
lst.append([9, 10])    # adds ONE item that is a list: [..., [9, 10]]
lst.extend([9, 10])    # adds TWO items: [..., 9, 10]
```

### Removing items

```python
lst = ["a", "b", "c", "b", "d"]

lst.remove("b")        # removes FIRST occurrence — ['a', 'c', 'b', 'd']
lst.pop()              # removes and RETURNS last item — 'd'
lst.pop(0)             # removes and RETURNS item at index 0 — 'a'
del lst[0]             # removes item at index 0 (no return value)
lst.clear()            # empties the list — []
```

**`.remove()` errors** if the value isn't present (`ValueError`). Check with `in` first:

```python
if "x" in lst:
    lst.remove("x")
```

### Searching and counting

```python
lst = [10, 20, 30, 20, 10]

lst.index(20)          # 1 — first occurrence
lst.index(20, 2)       # 3 — search from index 2 onward
lst.index(99)          # ValueError!
lst.count(20)          # 2
20 in lst              # True
```

### Sorting and reversing

Two flavors: **in-place** and **new-copy**.

**In-place (returns `None`):**
```python
lst = [3, 1, 4, 1, 5, 9, 2, 6]
lst.sort()             # lst is now [1, 1, 2, 3, 4, 5, 6, 9]
lst.sort(reverse=True) # lst is now [9, 6, 5, 4, 3, 2, 1, 1]
lst.reverse()          # reverses in place
```

**Returning a new list:**
```python
lst = [3, 1, 4, 1, 5]
new = sorted(lst)          # new = [1, 1, 3, 4, 5], lst unchanged
new = sorted(lst, reverse=True)
new = list(reversed(lst))  # note: reversed() returns an iterator; wrap in list()
```

### The `.sort()` None trap

This is one of the most common beginner bugs:

```python
result = my_list.sort()      # WRONG — result is None
result = sorted(my_list)     # RIGHT — result is the sorted list
```

`.sort()` mutates in place and returns `None`. If you assign the result to a variable and pass it around, downstream code gets `None`, and you'll get cryptic errors later. **Rule:** if you want to assign the sorted version to a variable, use `sorted()`, not `.sort()`.

### Custom sort with `key=`

Sort by a computed value:

```python
words = ["banana", "apple", "cherry"]
sorted(words)                        # ['apple', 'banana', 'cherry'] — alphabetical
sorted(words, key=len)               # ['apple', 'banana', 'cherry'] — by length
sorted(words, key=len, reverse=True)  # ['banana', 'cherry', 'apple']

# Sort a list of dicts by a field:
users = [{"name": "Sid", "age": 23}, {"name": "Alice", "age": 30}]
sorted(users, key=lambda u: u["age"])
```

`key=` takes a function that Python calls on each item to produce a comparable value. `lambda` (Chapter 23) is the shortest way to write a small key function.

## Copying Lists — the Aliasing Trap

Revisit Chapter 2's warning:

```python
a = [1, 2, 3]
b = a               # NOT a copy — b is the same list
b.append(4)
print(a)            # [1, 2, 3, 4] — a was mutated!
```

To copy:

```python
b = a.copy()                # shallow copy
b = a[:]                    # also a shallow copy (idiomatic)
b = list(a)                 # also a shallow copy
```

All three make a new list with the same items. If the items are simple (int, str), that's enough.

But watch what happens with nested lists:

```python
a = [[1, 2], [3, 4]]
b = a.copy()                # shallow — copies outer list but not inner lists
b[0].append("X")
print(a)                    # [[1, 2, 'X'], [3, 4]] — inner list shared!
```

`.copy()` copies **one level deep**. Nested structures still share their inner objects. For true independence:

```python
import copy
b = copy.deepcopy(a)        # recursively duplicates everything
```

**Rule of thumb:** shallow copy is enough when your list holds immutable items (ints, strings, tuples). If items are mutable and you'll mutate them separately, use `deepcopy`.

## Built-in Functions with Lists

```python
lst = [3, 1, 4, 1, 5, 9]

len(lst)          # 6
min(lst)          # 1
max(lst)          # 9
sum(lst)          # 23
sorted(lst)       # [1, 1, 3, 4, 5, 9] (new list)
list(reversed(lst))  # [9, 5, 1, 4, 1, 3] (new list)
any(lst)          # True — is any item truthy?
all(lst)          # True — are all items truthy?
```

`any()` and `all()` are especially useful with lists of Booleans:

```python
scores = [80, 90, 75, 60]
all(s >= 60 for s in scores)     # True — everyone passed
any(s >= 90 for s in scores)     # True — someone scored ≥ 90
```

## Nested Lists (2D)

A list of lists represents a grid:

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

grid[0]           # [1, 2, 3] — row 0
grid[1][2]        # 6 — row 1, column 2
grid[0][0] = "X"  # mutate a single cell
```

Iterate:

```python
for row in grid:
    for cell in row:
        print(cell, end=" ")
    print()
```

**Trap: `[[0] * 3] * 3` is dangerous.**

```python
grid = [[0] * 3] * 3
grid[0][0] = 1
print(grid)     # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] — ALL rows changed!
```

`* 3` creates three references to the **same** inner list. Modifying one visible row modifies "all" of them because they're actually one row. Correct way:

```python
grid = [[0] * 3 for _ in range(3)]     # comprehension — creates 3 independent rows
```

## Common Mistakes

- **`sorted_list = my_list.sort()`** — result is `None`. Use `sorted()` for a new list.
- **`b = a` thinking it copies.** It doesn't.
- **`.copy()` on nested lists** — shallow only. Use `copy.deepcopy` when needed.
- **`.remove()` on a missing value** — raises. Check `in` first.
- **Modifying a list while iterating.** Build a new list or iterate over a copy.
- **`[[0]*3]*3`** — aliased rows. Use a comprehension.
- **Confusing `append` and `extend`** — `append` adds one item; `extend` adds each item of an iterable.

## Best Practices

- Use `sorted()` when you want a new list; use `.sort()` when you want to mutate in place.
- Prefer list comprehensions (Chapter 19) for building lists from other iterables.
- Use `.copy()` or `list(x)` when you need to duplicate a list.
- Reserve `del` for removing by index; use `.remove()` for removing by value.
- Iterate directly (`for x in lst`) not by index.

## Key Takeaways

- Lists are ordered, mutable, heterogeneous, and indexed from 0.
- Every list method modifies in place returns `None` (`.sort()`, `.reverse()`, `.append()`, ...).
- The "copy" methods (`.copy()`, `[:]`, `list()`) are **shallow**. For nested data, use `copy.deepcopy`.
- `sorted()` and `reversed()` return new sequences; the methods on the list itself mutate.
- `[[0]*3]*3` creates aliased rows. Use a comprehension for 2D grids.

## Active Recall

1. What does `x = [1,2,3].sort()` set `x` to?
2. `a = [[1,2],[3,4]]; b = a.copy(); b[0].append("X"); print(a)` — what does this print, and why?
3. `.append([1,2])` vs `.extend([1,2])` — describe the difference.
4. Why does `[[0]*3]*3` produce aliased rows, and how do you fix it?
5. Write a one-liner that sorts a list of dicts `users` by their `"age"` field, descending.

---

# Chapter 15: Tuples

## What & Why

A **tuple** is Python's **immutable** ordered sequence. Think of it as a "frozen list": same indexing, same iteration, but once created, it can't be changed. Use tuples when a group of values belongs together conceptually and should never be modified.

## Creating Tuples

```python
empty = ()
single = (42,)              # THE trailing comma — see below
pair = (1, 2)
triple = (1, 2, 3)
mixed = ("Sid", 23, True)

# The parens are actually optional in most contexts:
point = 1, 2, 3             # this is a tuple!
```

### The Single-Element Trap

Python treats `(x)` as "x wrapped in parentheses" — not a tuple. To make a one-element tuple, you need a trailing comma:

```python
(1)          # int — the parens are just grouping
(1,)         # tuple with one element
type((1))    # <class 'int'>
type((1,))   # <class 'tuple'>
```

This surprises everyone. The trailing comma is what makes it a tuple, not the parens.

For consistency, some Pythonistas write `1,` (no parens at all) to emphasize this. `(1,)` is the standard.

## Indexing, Slicing, Iteration

Same as strings and lists:

```python
t = (10, 20, 30, 40, 50)
t[0]         # 10
t[-1]        # 50
t[1:4]       # (20, 30, 40) — slicing returns a tuple
len(t)       # 5

for x in t:
    print(x)

30 in t      # True
```

## Immutability

You **cannot** modify a tuple after creation:

```python
t = (1, 2, 3)
t[0] = 99        # TypeError: 'tuple' object does not support item assignment
t.append(4)      # AttributeError: 'tuple' has no attribute 'append'
```

But — this trips beginners — a tuple can **contain** mutable objects, and those can still change:

```python
t = ([1, 2], [3, 4])     # tuple of lists
t[0].append(99)          # the LIST inside the tuple is mutable
print(t)                 # ([1, 2, 99], [3, 4])
```

The tuple itself doesn't change (still two lists at those positions), but the objects it holds can.

## The Two Tuple Methods

Tuples are minimalist:

```python
t = (1, 2, 3, 2, 1)
t.index(2)     # 1 — first occurrence
t.count(1)     # 2
```

That's it. No `.append`, no `.remove`, no `.sort`. That's the point — tuples are for data that shouldn't change.

## Tuple Unpacking — the Killer Feature

Assign multiple variables at once from any sequence:

```python
point = (3, 4)
x, y = point         # x = 3, y = 4

a, b, c = [1, 2, 3]  # works with any sequence, not just tuples

# Classic swap without a temporary:
a, b = b, a
```

If the number of names doesn't match the number of items, it fails:

```python
a, b = (1, 2, 3)     # ValueError: too many values to unpack
a, b, c = (1, 2)     # ValueError: not enough values to unpack
```

### Star Unpacking

Grab the middle-ish part with `*`:

```python
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

first, *rest = [1, 2, 3, 4]
# first = 1, rest = [2, 3, 4]

*head, tail = [1, 2, 3, 4]
# head = [1, 2, 3], tail = 4
```

`*name` captures "everything else" as a list. Only one starred variable per assignment.

### Function Returns

Tuples are how you return multiple values from a function:

```python
def get_min_max(nums):
    return min(nums), max(nums)      # implicitly a tuple

lo, hi = get_min_max([3, 1, 4, 1, 5])
```

The parentheses are optional but often written for clarity.

### Iterating with Unpacking

Especially useful with `enumerate` and `.items()`:

```python
for i, name in enumerate(["Alice", "Bob"]):
    print(i, name)

for key, value in my_dict.items():
    print(key, value)
```

Each iteration yields a tuple; unpacking splits it inline.

## Tuples vs Lists — When to Use Which

| Use a **tuple** for                                 | Use a **list** for                |
| --------------------------------------------------- | --------------------------------- |
| Fixed groups (coordinates, RGB colors, dates)       | Dynamic collections               |
| Function returns of multiple values                 | Anything you'll append to later   |
| Records where order and meaning matter              | Homogeneous data                  |
| Dictionary keys (tuples are hashable, lists aren't) | Any collection you'll sort/filter |
| Data you want protected from accidental mutation    |                                   |

**Rule of thumb:** if items are conceptually different (name, age, email), tuple. If they're the same kind of thing (a list of names), list.

## Tuples as Dict Keys

Because tuples are immutable, they can serve as dictionary keys — lists can't.

```python
positions = {(0, 0): "origin", (1, 0): "east"}
positions[(0, 0)]     # 'origin'

# You cannot do:
positions = {[0, 0]: "origin"}     # TypeError: unhashable type: 'list'
```

## Named Tuples — a Small Upgrade

For records with named fields, `collections.namedtuple` is much clearer than positional access:

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

p.x           # 3
p.y           # 4
p[0]          # 3 — still indexable like a tuple

x, y = p      # still unpackable

# But immutable — p.x = 5 fails
```

Named tuples give you tuple-like efficiency with attribute access. For richer records, `dataclasses` (Chapter 37) is often better in modern code.

## Common Mistakes

- **Single-element trap:** `(1)` is an int; `(1,)` is a tuple.
- **Assuming tuples are deeply immutable.** The tuple itself can't change, but mutable objects inside can.
- **Trying `.append()` on a tuple.** Tuples don't support it — convert to a list, modify, convert back if needed.
- **Ignoring named tuples** when you have records with meaningful fields.

## Best Practices

- Use tuples for fixed, heterogeneous records (a point, a database row).
- Use lists for homogeneous sequences you'll modify.
- Prefer named tuples over positional tuples when fields have meaning.
- Take advantage of unpacking — it's one of Python's cleanest features.
- Return multiple values from functions as tuples.

## Key Takeaways

- Tuples are immutable ordered sequences: `(a, b, c)`.
- Single-element: `(x,)` with the trailing comma.
- Parens are usually optional — the commas make the tuple.
- Support indexing, slicing, iteration, `in`, `len`.
- Immutable containers, but their contents may be mutable.
- Unpacking (`a, b = t`) and star-unpacking (`first, *rest = t`) are Pythonic superpowers.
- Tuples can be dict keys; lists can't.

## Active Recall

1. What's the difference between `(5)` and `(5,)`? What type is each?
2. Can you modify the items inside a tuple? Give an example.
3. Explain what `a, *middle, b = [1, 2, 3, 4, 5]` binds to each variable.
4. Why can a tuple be a dict key but a list cannot?
5. When would you choose a tuple over a list?

---

# Chapter 16: Dictionaries

## What & Why

A **dictionary** (or `dict`) stores data as **key → value** pairs. Where a list finds items by numeric position, a dictionary finds items by an arbitrary key (usually a string). Dictionaries are, along with lists, one of the two most-used data structures in Python — used for configs, JSON, database records, caches, counters, and much more.

## Under the Hood: The Hash Table

A dict is a **hash table**. When you insert `d["name"] = "Sid"`, Python:

1. Computes a hash of `"name"` (an integer).
2. Uses that hash to pick a bucket in memory.
3. Stores the value there.

Lookup, insert, and delete are **O(1) on average** — nearly instant, regardless of dict size. That's why dicts are so useful: you can look up "user 12345's email" in a million-user table without scanning.

But this requires **hashable keys** — keys whose hash is stable. That's why only immutable types can be keys.

## Creating Dictionaries

```python
empty = {}
scores = {"Alice": 90, "Bob": 85, "Charlie": 72}
mixed_keys = {1: "one", "two": 2, (3, 4): "point"}
from_pairs = dict([("a", 1), ("b", 2)])         # {'a': 1, 'b': 2}
from_kwargs = dict(name="Sid", age=23)          # {'name': 'Sid', 'age': 23}
```

Note the syntax collision with sets:
- `{}` is an **empty dict**, not an empty set.
- `set()` gives you an empty set.

## Accessing and Modifying

### Bracket notation

```python
scores["Alice"]         # 90

scores["Alice"] = 95    # update
scores["David"] = 88    # insert

del scores["Bob"]       # remove
```

**Trap: KeyError on missing keys.**

```python
scores["Eve"]           # KeyError: 'Eve'
```

If you're not sure the key exists, `[key]` will crash your program. Use `.get()` instead (below).

### The `.get()` method — safe access

```python
scores.get("Eve")             # None — no crash
scores.get("Eve", 0)          # 0 — return this default if missing
```

Always prefer `.get()` when the key might not exist. This is one of the most important idioms in the language.

### Membership: `in`

```python
"Alice" in scores       # True — checks KEYS by default
"Alice" in scores.keys()   # same thing, more explicit
90 in scores.values()   # True — check values
```

## Iterating Over a Dictionary

Three ways:

```python
scores = {"Alice": 90, "Bob": 85, "Charlie": 72}

# 1. Keys (default):
for name in scores:
    print(name)

# 2. Values:
for score in scores.values():
    print(score)

# 3. Both, using .items() and tuple unpacking:
for name, score in scores.items():
    print(f"{name}: {score}")
```

`.items()` is the standard idiom when you need both.

## Insertion Order Is Guaranteed (Python 3.7+)

Modern Python dicts remember the order you inserted keys:

```python
d = {}
d["first"] = 1
d["second"] = 2
d["third"] = 3
list(d.keys())     # ['first', 'second', 'third']  — always in insertion order
```

This wasn't true in older Python. If you ever see references to `collections.OrderedDict`, that's a leftover from when order wasn't guaranteed — you rarely need it now.

## Essential Dict Methods

```python
d = {"a": 1, "b": 2, "c": 3}

# Access:
d.get("a")              # 1
d.get("z", 0)           # 0 (default)

# Iterating:
d.keys()                # dict_keys(['a', 'b', 'c'])
d.values()              # dict_values([1, 2, 3])
d.items()               # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Modification:
d["d"] = 4              # insert or update
d.update({"e": 5, "a": 99})   # merge — updates existing, adds new
d.pop("a")              # removes and returns value; errors if missing
d.pop("z", None)        # returns default if missing
d.popitem()             # removes and returns the LAST inserted (key, value) pair
d.clear()               # empties the dict

# Setting defaults:
d.setdefault("x", 0)    # if "x" missing, sets it to 0 and returns 0
                        # if "x" exists, returns its value (no change)

# Copy:
new = d.copy()          # shallow copy
```

### The Views: `.keys()`, `.values()`, `.items()`

These return **view objects**, not lists. They reflect the underlying dict live:

```python
d = {"a": 1, "b": 2}
keys = d.keys()
print(keys)         # dict_keys(['a', 'b'])

d["c"] = 3
print(keys)         # dict_keys(['a', 'b', 'c']) — updated automatically!
```

You can iterate them, use `in`, take `len`, but you can't index (`keys[0]` fails). To get a list, wrap: `list(d.keys())`.

## Building Dictionaries Dynamically

### Counting occurrences

Classic pattern:

```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

print(counts)   # {'apple': 3, 'banana': 2, 'cherry': 1}
```

`counts.get(w, 0)` gives 0 for missing keys — no need to check separately.

Even cleaner with `collections.Counter`:

```python
from collections import Counter
counts = Counter(words)     # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
```

### Grouping items

```python
students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A"), ("Dave", "B")]
by_grade = {}
for name, grade in students:
    by_grade.setdefault(grade, []).append(name)

# {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'Dave']}
```

`setdefault` inserts an empty list only if the key doesn't yet exist. Then `.append` modifies it in place.

The more modern replacement is `collections.defaultdict`:

```python
from collections import defaultdict
by_grade = defaultdict(list)
for name, grade in students:
    by_grade[grade].append(name)     # no need to setdefault
```

## Merging Dictionaries

Multiple options:

```python
a = {"x": 1, "y": 2}
b = {"y": 20, "z": 30}

# 1. .update() — in place, mutates a:
a.update(b)
# a is now {'x': 1, 'y': 20, 'z': 30}

# 2. Merge with ** unpacking (creates new dict):
merged = {**a, **b}
# {'x': 1, 'y': 20, 'z': 30}

# 3. The | operator (Python 3.9+, cleanest):
merged = a | b
# {'x': 1, 'y': 20, 'z': 30}
```

`b`'s values win where keys collide.

## Hashable Keys — What Can Be a Key?

Only **immutable** (technically, hashable) objects.

Allowed:
- `int`, `float`, `bool`
- `str`
- `tuple` (if all its elements are hashable)
- `frozenset`
- `None`

Forbidden:
- `list` — mutable
- `dict` — mutable
- `set` — mutable
- Regular tuples containing mutable items

```python
d = {(1, 2): "ok"}                # fine
d = {[1, 2]: "bad"}               # TypeError: unhashable type: 'list'
d = {(1, [2]): "bad"}             # tuple contains a list — unhashable
```

**Why?** Because dict lookup uses the key's hash. If the key mutated after insertion, its hash would change, and the value would be permanently unreachable.

## Nested Dictionaries

Common in JSON-like data:

```python
users = {
    "u1": {"name": "Sid", "email": "sid@example.com", "roles": ["admin"]},
    "u2": {"name": "Alice", "email": "alice@example.com", "roles": ["user"]},
}

users["u1"]["name"]              # 'Sid'
users["u1"]["roles"].append("editor")

# Safe deep access with chained .get():
users.get("u3", {}).get("name")  # None — no crash even if "u3" missing
```

## Common Mistakes

- **`d[key]` for missing keys.** Crashes with `KeyError`. Use `d.get(key)` or `d.get(key, default)`.
- **`{}` for empty set** — that's an empty **dict**. Use `set()`.
- **Using a list as a dict key.** Fails — lists are unhashable.
- **`for key, value in my_dict:`** — fails, iterating gives keys only. Use `.items()`.
- **Mutating a dict while iterating over it.** Same issue as lists — don't do it. Iterate over `list(d.keys())` if you must delete during iteration.

## Best Practices

- Always use `.get()` when the key might not exist.
- Use `.items()` when iterating for both keys and values.
- Prefer `collections.Counter` for counting, `defaultdict` for grouping.
- Use dict comprehensions (Chapter 19) for transformations.
- Merge with `|` (Python 3.9+) or `{**a, **b}` — clearer than `.update()` when you don't want to mutate.

## Key Takeaways

- Dicts are hash tables — O(1) key lookup on average.
- Keys must be hashable (immutable); values can be anything.
- `d[k]` crashes on missing keys; `d.get(k)` returns None safely.
- Iterate with `for k, v in d.items():`.
- Dict order is insertion order (Python 3.7+).

## Active Recall

1. What error does `d["missing_key"]` produce, and how do you avoid it?
2. Write a loop that prints each key and value from a dict, using tuple unpacking.
3. Why can't you use a list as a dict key? What can you use instead?
4. How do you count how many times each word appears in a list, using a plain dict?
5. Given `a = {"x": 1}` and `b = {"y": 2}`, what are three ways to merge them into a new dict?

---

# Chapter 17: Sets

## What & Why

A **set** is an unordered collection of **unique** elements. Think of it as a bag where duplicates are automatically discarded and order doesn't matter. Sets are optimized for two things: **fast membership testing** and **set-theoretic operations** (union, intersection, difference).

## Creating Sets

```python
empty = set()                   # empty set — NOT {}
nums = {1, 2, 3}
letters = {"a", "b", "c"}
from_list = set([1, 2, 2, 3, 3, 3])   # {1, 2, 3} — duplicates dropped
from_string = set("hello")            # {'h', 'e', 'l', 'o'} — unique chars
```

**Reminder:** `{}` is an empty **dict**. `set()` is the only way to create an empty set.

## Automatic Deduplication

```python
set([1, 2, 2, 3, 3, 3])         # {1, 2, 3}
list(set([1, 2, 2, 3]))         # [1, 2, 3] — dedup a list quickly
```

This is one of the most common uses of sets: turn a list into a set to remove duplicates.

## Sets Are Unordered

```python
s = {3, 1, 2}
print(s)      # {1, 2, 3} — but this order is not guaranteed
```

You cannot index a set (`s[0]` errors) or slice it. Iteration order is unspecified. If order matters, use a list.

## Membership — Sets' Superpower

Testing `x in s` is **O(1)** on a set (constant time), versus **O(n)** on a list. For membership-heavy code, sets are dramatically faster.

```python
allowed = {"admin", "editor", "viewer"}
if user_role in allowed:
    ...
```

If your list has 1 million items and you check membership 1 million times, converting to a set once at the start turns O(n²) work into O(n).

## Modifying Sets

```python
s = {1, 2, 3}

s.add(4)              # {1, 2, 3, 4}
s.add(1)              # unchanged — already present, no error
s.remove(2)           # {1, 3, 4}
s.remove(99)          # KeyError!
s.discard(99)         # like remove, but silent if missing
s.pop()               # removes and returns an arbitrary element
s.clear()             # empties the set
```

**`.remove()` vs `.discard()`:** remove raises on missing; discard doesn't. Use discard when the value might not be there.

## Set Operations

Direct mapping to mathematical set theory. Both operator and method forms work.

Let `A = {1, 2, 3}` and `B = {3, 4, 5}`.

| Operation            | Operator | Method                      | Result        |
| -------------------- | -------- | --------------------------- | ------------- |
| Union                | `A \| B` | `A.union(B)`                | `{1,2,3,4,5}` |
| Intersection         | `A & B`  | `A.intersection(B)`         | `{3}`         |
| Difference           | `A - B`  | `A.difference(B)`           | `{1, 2}`      |
| Symmetric difference | `A ^ B`  | `A.symmetric_difference(B)` | `{1,2,4,5}`   |

Symmetric difference = items in exactly one of the two sets (not both).

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A | B    # {1, 2, 3, 4, 5, 6}
A & B    # {3, 4}
A - B    # {1, 2}
B - A    # {5, 6}
A ^ B    # {1, 2, 5, 6}
```

Practical uses:

```python
# Which items are in both lists?
common = set(list1) & set(list2)

# Which items are only in list1?
only_in_1 = set(list1) - set(list2)
```

## Subset and Superset

```python
{1, 2}.issubset({1, 2, 3})       # True
{1, 2, 3}.issuperset({1, 2})     # True
{1, 2} <= {1, 2, 3}              # True — operator form
{1, 2} < {1, 2, 3}               # True — proper subset (strict)
{1, 4}.isdisjoint({2, 3})        # True — no common elements
```

## Hashability Constraint (Again)

Just like dict keys, **set elements must be hashable**. You cannot put lists, dicts, or sets inside a set:

```python
{1, 2, [3, 4]}       # TypeError: unhashable type: 'list'
{1, 2, {3, 4}}       # TypeError: unhashable type: 'set'
```

You can nest tuples:

```python
{(1, 2), (3, 4)}     # fine
```

For nested sets, use `frozenset` (a hashable, immutable version of a set):

```python
{frozenset([1, 2]), frozenset([3, 4])}   # set of frozensets — legal
```

## The `9 == 9.0` Collision

Sets consider `9` and `9.0` duplicates because `9 == 9.0` is `True` and they hash to the same value:

```python
{9, 9.0}      # {9} — the float is silently dropped
{9.0, 9}      # {9.0} — whichever is inserted first wins
```

Same for `True == 1`:

```python
{True, 1}     # {True}
```

If you need to distinguish, store them as tuples with a type tag: `{("int", 9), ("float", 9.0)}`.

## `frozenset` — the Immutable Cousin

A `frozenset` is a set you can't modify after creation. Because it's immutable, it's hashable — you can use it as a dict key or put it inside another set.

```python
fs = frozenset([1, 2, 3])
fs.add(4)         # AttributeError — no such method

d = {fs: "some value"}    # OK
```

Rare in day-to-day code but occasionally useful.

## Common Mistakes

- **Using `{}` for an empty set.** That's an empty dict. Use `set()`.
- **Indexing a set.** No, sets aren't indexed.
- **Adding unhashable items.** Lists inside sets fail; use tuples or frozensets.
- **Relying on set order.** Ordered as a side effect of insertion — but not guaranteed.
- **`.remove()` on a missing element.** Raises. Use `.discard()` when you're unsure.

## Best Practices

- Use `set(my_list)` for fast dedup.
- Use `x in my_set` for fast membership on large data.
- Prefer operators (`|`, `&`, `-`, `^`) over method calls for readability.
- Reach for `frozenset` when you need a hashable set (dict key, member of another set).

## Key Takeaways

- Sets are unordered collections of unique, hashable elements.
- Automatic deduplication and O(1) membership tests are their killer features.
- `{}` is a dict; `set()` is the only way to create an empty set.
- Full support for mathematical set operations: union, intersection, difference, symmetric difference.
- Cannot contain unhashable objects (no lists, dicts, sets inside).

## Active Recall

1. Why doesn't `{}` create an empty set? What does it create, and how do you actually make an empty set?
2. Why is `x in my_set` faster than `x in my_list` for large collections?
3. Given `A = {1,2,3}` and `B = {2,3,4}`, what are `A | B`, `A & B`, `A - B`, and `A ^ B`?
4. Why does `{9, 9.0}` result in a set with one element?
5. What's a `frozenset`, and when would you use one?

---

# Chapter 18: Iteration Helpers — `range`, `enumerate`, `zip`, `sorted`, `reversed`

## What & Why

Python gives you a set of built-in functions specifically designed to make loops cleaner, more expressive, and more Pythonic. If you find yourself writing `for i in range(len(items))` and then indexing into the list, you've missed a helper. This chapter is where beginners graduate from "translating loops from other languages" into writing genuine Python.

These five helpers — `range`, `enumerate`, `zip`, `sorted`, `reversed` — cover 90% of iteration patterns you'll ever need.

## Mental Model

All of these return **iterators** (or iterator-like objects), not lists. That means:

- They're lazy — they produce values one at a time, on demand.
- They don't allocate memory for the full sequence.
- You can loop over them once. After that, they're exhausted.
- You can convert them to a list with `list(...)` if you need to see all values at once.

Think of them as "recipes" for producing values, not "boxes" holding values.

## `range(stop)` / `range(start, stop)` / `range(start, stop, step)`

Generates an arithmetic sequence of integers.

```python
list(range(5))              # [0, 1, 2, 3, 4]
list(range(2, 7))           # [2, 3, 4, 5, 6]
list(range(0, 10, 2))       # [0, 2, 4, 6, 8]
list(range(10, 0, -1))      # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list(range(10, 0, -2))      # [10, 8, 6, 4, 2]
```

**Key point:** the `stop` value is *exclusive*. `range(5)` gives you 0 through 4, not 0 through 5. This trips up almost every beginner once.

**Why exclusive?** Because `range(len(items))` gives you exactly the valid indices of `items`. If it were inclusive, you'd always have to write `len(items) - 1`. Half-open ranges also compose cleanly: `range(0, 5) + range(5, 10)` covers 0 through 9 with no overlap or gap.

`range` objects are memory-efficient. `range(1_000_000_000)` uses a handful of bytes — it stores start, stop, step, not a billion integers.

## `enumerate(iterable, start=0)`

Yields `(index, value)` pairs while you iterate.

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

**Why it exists:** the un-Pythonic pattern below appears in millions of tutorials from other languages:

```python
# DON'T do this
for i in range(len(fruits)):
    print(i, fruits[i])
```

This works, but it's noisy, error-prone (off-by-one when you edit it), and unidiomatic. `enumerate` is the answer.

You can change the starting index:

```python
for line_no, line in enumerate(open("file.txt"), start=1):
    print(f"Line {line_no}: {line}")
```

## `zip(*iterables)`

Pairs elements from multiple iterables position-by-position.

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [92, 78, 85]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 92
# Bob: 78
# Charlie: 85
```

You can zip three or more:

```python
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]

for x, y, z in zip(a, b, c):
    print(x + y + z)
# 111
# 222
# 333
```

**Length mismatch:** `zip` stops at the shortest iterable, silently truncating.

```python
list(zip([1, 2, 3], [10, 20]))      # [(1, 10), (2, 20)] — the 3 is dropped
```

To catch this instead of silently ignoring it, use `zip(..., strict=True)` (Python 3.10+), which raises `ValueError` on length mismatch. Use `strict=True` when you're pairing data that should always match — it catches bugs.

**Unzipping** with the star operator:

```python
pairs = [("Alice", 92), ("Bob", 78)]
names, scores = zip(*pairs)
print(names)   # ('Alice', 'Bob')
print(scores)  # (92, 78)
```

**Building a dict from parallel lists:**

```python
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = dict(zip(keys, vals))    # {'a': 1, 'b': 2, 'c': 3}
```

## `sorted(iterable, key=None, reverse=False)`

Returns a **new sorted list** from any iterable. Unlike `list.sort()`, `sorted` does *not* modify the original and works on anything iterable (tuples, sets, dict keys, strings).

```python
sorted([3, 1, 2])              # [1, 2, 3]
sorted("cba")                  # ['a', 'b', 'c']  — strings sorted char-by-char
sorted({3, 1, 2})              # [1, 2, 3]
sorted([3, 1, 2], reverse=True) # [3, 2, 1]
```

The `key` parameter is a function that maps each element to the value used for comparison — this is one of the most powerful patterns in Python.

```python
words = ["banana", "pie", "Washington", "book"]
sorted(words, key=len)              # ['pie', 'book', 'banana', 'Washington']
sorted(words, key=str.lower)        # case-insensitive alphabetical

people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted(people, key=lambda p: p["age"])   # sort by age
```

Sorting is stable — items with equal keys keep their original order. This lets you sort by multiple criteria via chained sorts (sort by secondary key first, then primary), or via a tuple key:

```python
sorted(people, key=lambda p: (p["age"], p["name"]))
```

## `reversed(sequence)`

Returns an iterator that walks the sequence backwards.

```python
list(reversed([1, 2, 3]))       # [3, 2, 1]
list(reversed("hello"))         # ['o', 'l', 'l', 'e', 'h']

for x in reversed(range(5)):
    print(x)                    # 4, 3, 2, 1, 0
```

`reversed` requires an object that knows its length and supports indexing (or defines `__reversed__`). Sets and dicts can be reversed since Python 3.8 (dicts) but only lists, tuples, strings, and ranges are the everyday targets.

**`reversed(list)` vs `list[::-1]`:** the slice creates a new list; `reversed` returns a lazy iterator. Prefer `reversed` in `for` loops (no copy); use `[::-1]` when you actually want a reversed list.

## Combining Them

Real Python code combines these fluently:

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [92, 78, 85]

# Rank by score, highest first
ranked = sorted(zip(names, scores), key=lambda p: p[1], reverse=True)
for rank, (name, score) in enumerate(ranked, start=1):
    print(f"#{rank}: {name} ({score})")
# #1: Alice (92)
# #2: Charlie (85)
# #3: Bob (78)
```

Read that line by line and appreciate: `zip` pairs, `sorted` orders, `enumerate` ranks — no manual index bookkeeping anywhere.

## Common Mistakes

- **`for i in range(len(items))` when you meant `enumerate`.** Classic non-Pythonic pattern.
- **Assuming `range` is a list.** It's a lazy range object. `range(5) + range(5)` fails; `list(range(5)) + list(range(5))` works.
- **Reusing a `zip` object.** Iterators are one-shot. If you loop over `z = zip(a, b)` twice, the second loop is empty.
- **Off-by-one with inclusive/exclusive `range`.** `range(1, 10)` is 1..9, not 1..10.
- **Silent truncation from `zip` with mismatched lengths.** Use `strict=True` when you care.

## Best Practices

- Reach for `enumerate` any time you need both index and value.
- Use `zip` for parallel iteration; use `zip(..., strict=True)` when lengths should match.
- Prefer `sorted(x)` for readability unless you specifically need in-place `x.sort()`.
- Use `key=` with a `lambda` or `operator.itemgetter` / `operator.attrgetter` for complex sorts.
- Combine helpers — Python code reads beautifully when you chain them.

## Key Takeaways

- `range(stop)` — exclusive of `stop`. Half-open on purpose.
- `enumerate(iter)` — `(index, value)` pairs. Replaces `range(len(...))` everywhere.
- `zip(a, b)` — parallel iteration. Stops at shortest; use `strict=True` to enforce equality.
- `sorted(iter, key=..., reverse=...)` — returns a new list, works on any iterable, stable sort.
- `reversed(seq)` — lazy backwards iterator.
- All of these return iterators or list-like lazy objects, not eager lists.

## Active Recall

1. Why is `range(5)` "exclusive" of 5? What's the design benefit?
2. Rewrite `for i in range(len(items)): print(i, items[i])` the Pythonic way.
3. What does `zip([1,2,3], [10,20])` produce? How do you make Python complain instead of silently truncating?
4. What's the difference between `sorted(x)` and `x.sort()`?
5. When would you use `reversed(x)` vs `x[::-1]`?

---

# Chapter 19: Comprehensions — The Signature Python Idiom

## What & Why

A comprehension is a compact syntax for building a list, dict, set, or generator from an iterable in one expression. It's arguably the most recognizable Python feature — once you're fluent, you'll use them daily.

They exist because 80% of the loops you'd write in other languages are "start with an empty collection, iterate over something, filter, transform, and append." Comprehensions turn that four-line ritual into one readable line.

## Mental Model

Read a comprehension left-to-right as: **"Give me an EXPRESSION for each ITEM in ITERABLE, optionally where CONDITION."**

Equivalence:

```python
# The loop
squares = []
for x in range(10):
    squares.append(x * x)

# The comprehension
squares = [x * x for x in range(10)]
```

Same result. The comprehension is one line, clearer intent, and usually slightly faster because the loop runs inside the interpreter core.

## List Comprehensions

**Basic form:**

```python
[EXPRESSION for VAR in ITERABLE]
```

Examples:

```python
[x * 2 for x in range(5)]           # [0, 2, 4, 6, 8]
[len(w) for w in ["ab", "cde", "f"]] # [2, 3, 1]
[c.upper() for c in "abc"]          # ['A', 'B', 'C']
```

**With a filter:**

```python
[EXPRESSION for VAR in ITERABLE if CONDITION]
```

```python
[x for x in range(20) if x % 2 == 0]         # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
[w for w in words if len(w) > 3]              # keep long words
[x * x for x in range(10) if x % 2 == 0]      # squares of evens
```

**With a conditional expression (transform, not filter):**

Filters (`if` at the end) *drop* items. A conditional expression (`if / else` in the middle) *transforms* items:

```python
# Filter — drops odd numbers
[x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]

# Transform — keeps every item, but changes odd ones
[x if x % 2 == 0 else -1 for x in range(10)]  # [0, -1, 2, -1, 4, -1, 6, -1, 8, -1]
```

**Nested comprehensions** (mirror the order of nested `for` loops):

```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Read left-to-right, matching the equivalent nested loops:

```python
flat = []
for row in matrix:
    for x in row:
        flat.append(x)
```

**Building a matrix:**

```python
# 3x3 grid of zeros — no aliasing (unlike [[0]*3]*3)
grid = [[0 for _ in range(3)] for _ in range(3)]
```

Recall Chapter 14's `[[0]*3]*3` aliasing bug. A comprehension creates a *new* inner list each iteration, so mutating one row doesn't affect the others. This is the Pythonic way to build 2D structures.

## Dict Comprehensions

Same shape, but with `key: value` and curly braces:

```python
{k: v for k, v in iterable}
```

```python
# Squares dict
{x: x * x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Swap keys and values
d = {"a": 1, "b": 2, "c": 3}
{v: k for k, v in d.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Filter a dict
{k: v for k, v in d.items() if v > 1}
# {'b': 2, 'c': 3}

# Word length map
words = ["apple", "banana", "kiwi"]
{w: len(w) for w in words}
# {'apple': 5, 'banana': 6, 'kiwi': 4}
```

## Set Comprehensions

Same shape, curly braces, no `key: value`:

```python
{EXPRESSION for VAR in ITERABLE}
```

```python
{x % 5 for x in range(20)}     # {0, 1, 2, 3, 4}
{c.lower() for c in "Hello World"}   # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
```

Automatic dedup, because it's a set.

## Generator Expressions

Wrap the same expression in parentheses instead of brackets, and you get a **generator** — a lazy iterator that yields values one at a time without building the full collection in memory.

```python
gen = (x * x for x in range(10))
next(gen)   # 0
next(gen)   # 1
sum(x * x for x in range(1_000_000))     # doesn't allocate a million-element list
```

When passing a generator expression as the *sole* argument to a function, you can drop the outer parens:

```python
sum(x * x for x in range(10))          # not sum((x * x for x in range(10)))
max(len(w) for w in words)
any(x < 0 for x in numbers)
```

**When to prefer generator over list comprehension:**
- Huge or infinite data — avoid loading everything in memory.
- Only need to iterate once.
- Feeding into `sum`, `any`, `all`, `min`, `max`, `join`, etc.

Use a list comprehension when you need to index into the result, iterate over it multiple times, or actually see all the values.

## Readability Ceiling

Comprehensions are wonderful — until they aren't. If your comprehension:
- has more than one `if` and one `for`
- spans more than one screen line
- requires the reader to reparse it

...convert it back to a `for` loop. Readability wins. A three-line loop that someone can understand at a glance is better than a comprehension nobody can debug.

**Bad:**
```python
result = [x*y for x in range(10) if x > 2 for y in range(10) if y > x if (x + y) % 2 == 0]
```

**Better as an explicit loop.** Comprehensions are a tool, not a badge.

## Common Mistakes

- **Using `[]` when you meant `{}`.** Curly braces give a set (or dict); brackets give a list.
- **`if` position matters.** `[x for x in items if cond]` filters. `[x if cond else other for x in items]` transforms. Beginners swap these.
- **Nesting order.** In a nested comprehension, the `for` clauses are in the same order as nested loops (outer first).
- **Overusing them.** Not every loop is clearer as a comprehension.
- **Reusing a generator expression.** Like all iterators, they're one-shot. `g = (x for x in range(3)); list(g); list(g)` — the second `list` is empty.

## Best Practices

- Prefer comprehensions for simple map/filter operations — one `for`, at most one `if`.
- Use generator expressions when passing to reducers (`sum`, `any`, `all`, `join`) or when data is large.
- Fall back to loops when a comprehension becomes hard to read.
- Use dict/set comprehensions for building lookup structures — they're clearer than the `dict(...)` / `set(...)` calls with tuples.

## Key Takeaways

- Comprehensions are compact syntax for build-a-collection-from-an-iterable loops.
- Four flavors: list `[...]`, dict `{k: v for ...}`, set `{...}`, generator `(...)`.
- `if` at the end filters; `if/else` in the middle transforms.
- Nested `for` clauses read outer-to-inner.
- Generator expressions are lazy — memory-friendly for large/infinite data.
- Readability > cleverness. Loops are fine when comprehensions get gnarly.

## Active Recall

1. Write a list comprehension that squares only the even numbers from 0 to 19.
2. What's the difference between `[x for x in nums if x > 0]` and `[x if x > 0 else 0 for x in nums]`?
3. Write a dict comprehension that swaps the keys and values of `{"a": 1, "b": 2}`.
4. Why does `sum(x*x for x in range(1_000_000))` use less memory than `sum([x*x for x in range(1_000_000)])`?
5. When is a comprehension a bad choice compared to a plain `for` loop?

---

# Chapter 20: Functions — The Fundamental Unit of Reuse

## What & Why

A function is a named, reusable block of code that (optionally) accepts inputs and (optionally) returns an output. Every non-trivial program is built from functions.

Why functions exist:

1. **DRY (Don't Repeat Yourself)** — write the logic once, call it many places.
2. **Abstraction** — name a concept, hide the details behind the name.
3. **Testing** — small functions with clear inputs and outputs are the atoms of testable code.
4. **Composition** — combine small functions to build bigger behavior.

Learn to write short, focused functions and half of good programming falls out for free.

## Mental Model

A function has:

- A **name**.
- A **signature** — the parameters it accepts.
- A **body** — the code that runs.
- A **return value** — what it hands back to whoever called it.

The function definition is itself a normal Python object bound to a name. `def greet(): ...` creates a function object and stores it in the variable `greet`. That's why you can pass functions around, put them in lists, and assign them to other variables. They're first-class values.

## Syntax

```python
def function_name(parameter1, parameter2):
    """Optional docstring describing the function."""
    # body
    return result
```

Concrete example:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

result = add(3, 4)
print(result)    # 7
```

Parts:

- `def` — the keyword that starts a definition.
- `add` — the name (identifier rules: letters, digits, underscores; can't start with a digit).
- `(a, b)` — parameters, comma-separated.
- `:` — starts the body.
- Indented block — the body. Four spaces per level, always.
- `"""..."""` — optional docstring, the first statement in the body.
- `return` — hands a value back.

## Parameters vs Arguments

- **Parameter** — the name in the function definition. Placeholders. `a` and `b` above.
- **Argument** — the actual value passed in when calling. `3` and `4` above.

You'll hear these used interchangeably in casual speech; that's fine — the meaning is usually clear from context.

## Calling Functions

Two ways to pass arguments:

```python
def rectangle_area(width, height):
    return width * height

# Positional — order matters
rectangle_area(5, 3)              # width=5, height=3

# Keyword — order doesn't matter
rectangle_area(height=3, width=5)  # same result
```

Keyword arguments make calls self-documenting:

```python
send_email("hello", to="alice@example.com", subject="Hi")
```

vs

```python
send_email("hello", "alice@example.com", "Hi")
```

The second one — what's what? Reach for keyword arguments when the meaning isn't obvious from position.

## Default Values

Parameters can have defaults, making them optional:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Sid")                     # 'Hello, Sid!'
greet("Sid", greeting="Namaste") # 'Namaste, Sid!'
greet("Sid", "Hey")              # 'Hey, Sid!'
```

Rule: parameters with defaults must come *after* parameters without defaults. `def f(a=1, b): ...` is a syntax error.

**Trap:** default values are evaluated *once*, when the function is defined, not each time it's called. Never use a mutable object as a default value:

```python
def append_item(item, items=[]):   # DANGER — shared list!
    items.append(item)
    return items

append_item(1)   # [1]
append_item(2)   # [1, 2]  ← surprise! same list, not a fresh []
```

Fix — the None-sentinel pattern (Chapter 5):

```python
def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## `return` and Implicit `None`

`return` sends a value back to the caller and immediately exits the function.

```python
def absolute(x):
    if x < 0:
        return -x
    return x
```

Multiple return statements are fine — often clearer than nesting `if/else`.

A function without `return` (or with a bare `return`) returns `None`:

```python
def noop():
    pass

print(noop())    # None
```

This is why `print("hi")` is a statement-flavored function — `print` returns `None`, and beginners often confuse it with `return` (Chapter 8). `print` displays; `return` gives back a value.

## Returning Multiple Values

Python returns a *single* object — but that object can be a tuple, which unpacks nicely:

```python
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

lo, hi = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(lo, hi)    # 1 9
```

Under the hood, `return a, b` builds a tuple. `a, b = f()` unpacks it. Very ergonomic — use freely.

## Docstrings

The string literal on the first line of a function is its **docstring**, accessible via `help(function)` or `function.__doc__`.

```python
def bmi(weight_kg, height_m):
    """Compute Body Mass Index.

    Args:
        weight_kg: Body weight in kilograms.
        height_m: Height in meters.

    Returns:
        BMI as a float.
    """
    return weight_kg / (height_m ** 2)

help(bmi)
```

Docstrings are Python's convention for API documentation. Tools like Sphinx generate documentation from them. Get in the habit of writing at least one line: what the function does, in one sentence.

## Type Hints (Preview)

You can annotate parameters and returns with types. They're optional and don't affect runtime behavior, but they help IDEs, static checkers like `mypy`, and human readers.

```python
def bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)
```

Chapter 37 covers type hints in depth. For now, know they exist and don't be surprised when you see them.

## Functions Are Objects

Because functions are first-class values, you can:

```python
def square(x):
    return x * x

f = square              # bind another name to the same function
print(f(5))             # 25

funcs = [square, len, print]
for fn in funcs:
    print(fn)           # prints each function object

def apply(fn, x):       # pass a function as an argument
    return fn(x)

apply(square, 7)        # 49
```

This is the foundation of higher-order patterns: `map`, `filter`, `sorted(key=...)`, decorators, callbacks.

## Common Mistakes

- **Mutable default arguments.** `def f(x=[]):` is a subtle time bomb.
- **Confusing `print` with `return`.** `print` shows a value; `return` gives it back. If a function ends with `print`, calling code can't use the result.
- **Forgetting to `return`.** Without an explicit return, you get `None`. Then `result * 2` explodes with a `TypeError`.
- **Modifying arguments in place unexpectedly.** Passing a list into a function and mutating it changes the caller's list (Chapter 2's "arguments are labels" rule).
- **Reusing built-in names as parameters.** `def f(list, len):` shadows the built-ins inside the function.

## Best Practices

- Keep functions short. One responsibility, one screen.
- Name them with verbs: `compute_total`, `send_email`, `is_valid`.
- Return values, don't print — the caller can decide what to do with the result.
- Write a one-line docstring at minimum.
- Use keyword arguments when calls would otherwise be ambiguous.
- Prefer pure functions (same input → same output, no side effects) where practical. They're the easiest to test and reason about.
- Reserve `None` returns for functions that genuinely don't produce a value. Otherwise, always return something meaningful.

## Key Takeaways

- Functions are named, reusable blocks with parameters and an optional return.
- Parameters are placeholders; arguments are the actual values.
- Positional vs keyword arguments; defaults must come after non-defaults.
- Mutable defaults are a classic trap — use `None` + reassign.
- `return` sends a value back; no `return` → returns `None`.
- Multiple returns work via tuple packing/unpacking.
- Functions are first-class objects — assign, pass, and store them.
- Docstrings document intent; type hints document types.

## Active Recall

1. What's the difference between a parameter and an argument?
2. Why does the following go wrong across multiple calls?
   ```python
   def add(item, items=[]):
       items.append(item)
       return items
   ```
3. What does a function return if it has no `return` statement?
4. Why is it better to `return` a result than to `print` it inside a function?
5. Given `def f(a, b=2, c=3):`, list three valid ways to call it.

---

# Chapter 21: Function Arguments Deep Dive — `*args`, `**kwargs`, and More

## What & Why

Python's argument system is more flexible than most languages. You can accept:

- A fixed number of positional args
- A fixed number of keyword args
- An arbitrary number of positional args (`*args`)
- An arbitrary number of keyword args (`**kwargs`)
- Positional-only args (forced to be positional)
- Keyword-only args (forced to be keyword)

Once you know these tools, you can design ergonomic APIs and read any Python library with confidence.

## `*args` — Variable Positional Arguments

`*args` collects any extra positional arguments into a tuple.

```python
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)          # 6
total(1, 2, 3, 4, 5)    # 15
total()                 # 0
```

Inside the function, `numbers` is an ordinary tuple. The name `args` is just convention — `*numbers`, `*items`, whatever describes the data works. The `*` is the magic.

You can combine with normal parameters:

```python
def log(level, *messages):
    for msg in messages:
        print(f"[{level}] {msg}")

log("INFO", "starting", "loading config", "ready")
```

## `**kwargs` — Variable Keyword Arguments

`**kwargs` collects extra keyword arguments into a dict.

```python
def make_person(**info):
    return info

make_person(name="Alice", age=30, city="Delhi")
# {'name': 'Alice', 'age': 30, 'city': 'Delhi'}
```

Again, `kwargs` is convention. `**options`, `**props`, whatever.

## Full Signature

You can combine all four kinds:

```python
def f(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)

f(1, 2, 3, 4, c=99, x="extra", y="stuff")
# 1 2 (3, 4) 99 {'x': 'extra', 'y': 'stuff'}
```

Order in the signature:

1. Positional-or-keyword parameters (regular ones)
2. `*args`
3. Keyword-only parameters (with or without defaults)
4. `**kwargs`

Anything after `*args` in the signature can only be passed by keyword — because positional arguments after `*args` would be swallowed by `*args`. This is exactly how you make keyword-only parameters:

```python
def open_file(path, *, mode="r", encoding="utf-8"):
    # mode and encoding MUST be passed as keywords
    ...

open_file("a.txt", "w")           # TypeError!
open_file("a.txt", mode="w")      # OK
```

The bare `*` in the signature says "everything after me is keyword-only." Extremely useful for making APIs clearer — callers can't accidentally swap flag positions.

## Positional-Only Parameters (Python 3.8+)

The bare `/` says "everything before me is positional-only":

```python
def divide(a, b, /):
    return a / b

divide(10, 2)          # 5
divide(a=10, b=2)      # TypeError!
```

Used in the standard library (e.g., `len(obj, /)`), but you'll rarely need it in application code. Know it exists so you're not confused reading built-in signatures.

Full form:

```python
def f(pos_only, /, standard, *, kw_only):
    ...
```

- `pos_only` — must be positional
- `standard` — can be either
- `kw_only` — must be keyword

## Unpacking on the Call Side

The `*` and `**` symbols also work at the call site — this time they *unpack*.

```python
def total(a, b, c):
    return a + b + c

nums = [1, 2, 3]
total(*nums)         # unpack list into positional args → total(1, 2, 3)

kwargs = {"a": 1, "b": 2, "c": 3}
total(**kwargs)      # unpack dict into keyword args → total(a=1, b=2, c=3)
```

This is the mirror image of `*args` and `**kwargs` in a definition:

- In a **def**, `*` and `**` **collect** many args into a container.
- In a **call**, `*` and `**` **spread** a container into many args.

Extremely handy for forwarding arguments:

```python
def wrapper(*args, **kwargs):
    print("Before call")
    result = actual_function(*args, **kwargs)   # forward everything
    print("After call")
    return result
```

This is the pattern that makes decorators work (Chapter 35).

## Argument Order at the Call Site

When calling:

1. Positional args come first.
2. Keyword args come after.
3. You cannot pass the same parameter both positionally and by keyword.

```python
def f(a, b, c):
    return a, b, c

f(1, 2, 3)                    # OK
f(1, b=2, c=3)                # OK
f(a=1, 2, 3)                  # SyntaxError — keyword before positional
f(1, 2, a=10)                 # TypeError — a already passed positionally
```

## Common Mistakes

- **Confusing definition-side and call-side `*`.** In `def f(*args)`, the star *collects*. In `f(*items)`, the star *unpacks*.
- **Mixing up `*` and `**`.** Single star for lists/tuples/iterables. Double star for dicts.
- **Passing keyword args positionally to a keyword-only parameter.** `open_file("a", "w")` fails when `mode` is keyword-only.
- **Duplicate values.** `f(1, a=1)` when `a` is the first positional parameter — Python won't let you set it twice.
- **Ordering in the signature.** Non-default before default. `*args` before keyword-only. `**kwargs` last.

## Best Practices

- Use `*args` when the number of things is genuinely variable (e.g., `print`, `max`, `min`).
- Use `**kwargs` for forwarding or when you're building an API that mirrors another function's kwargs.
- Use keyword-only parameters (`*` in the signature) for boolean/flag arguments — `f(x, *, verbose=True)` reads better at call sites than `f(x, True)`.
- Prefer explicit parameters when you know them. `**kwargs` catches everything, which is powerful but obscures the interface. Overuse makes IDE completion and readers miserable.
- Positional-only is niche — use only when you have a strong reason (e.g., a very-frequently-called API where parameter names are noise, or you want freedom to rename).

## Key Takeaways

- `*args` collects extra positional args into a tuple; `**kwargs` collects extra keyword args into a dict.
- The star/double-star in a **call** unpacks — the mirror image of collect.
- Bare `*` in a signature starts keyword-only parameters.
- Bare `/` in a signature ends positional-only parameters (Python 3.8+).
- Full order: `positional_only, /, standard, *args, keyword_only, **kwargs`.
- Same names (`args`, `kwargs`) are convention, not required. The stars are the magic.

## Active Recall

1. What data type is `args` inside `def f(*args)`? What about `kwargs` in `**kwargs`?
2. In `f(*mylist)`, is the star collecting or unpacking? Which side of the call is it on?
3. Rewrite `def f(x, y=True)` so that `y` can only be passed by keyword.
4. What does `def f(a, b, /, c, *, d)` mean for each of a, b, c, d?
5. Write a function `debug(fn)` that calls `fn` with any arguments and prints them first: `debug(print, "hello", end="!")`.

---

# Chapter 22: Scope & the LEGB Rule

## What & Why

**Scope** is the set of rules Python uses to look up a name. When you write `print(x)`, Python has to figure out *which* `x` you mean. If you don't understand scope, you'll spend hours chasing bugs where a variable is "empty" or has a stale value.

## The LEGB Rule

Python looks up names in this order, stopping at the first match:

1. **L**ocal — inside the current function.
2. **E**nclosing — inside any enclosing function (for nested functions).
3. **G**lobal — at the top level of the current module (file).
4. **B**uilt-in — Python's built-in names (`print`, `len`, `range`, ...).

If a name isn't found anywhere, you get `NameError`.

## Local Scope

Every function creates a new local scope. Variables assigned inside the function live only inside it.

```python
def f():
    x = 10       # local to f
    print(x)

f()         # 10
print(x)    # NameError — x doesn't exist out here
```

Parameters are also local:

```python
def greet(name):
    print(f"Hello, {name}")

greet("Sid")
print(name)     # NameError
```

## Global Scope

Names defined at the top level of the module are global — visible everywhere in the file:

```python
message = "Hello from the top"

def show():
    print(message)     # reads global — works fine

show()   # Hello from the top
```

Reading globals from inside a function is fine. Writing them requires more work.

## Reading vs Writing — The Assignment Rule

If you *assign* to a name inside a function, Python treats it as **local**, even if a global with the same name exists. This causes the most common scope bug in Python.

```python
count = 0

def increment():
    count = count + 1     # UnboundLocalError

increment()
```

Why? Python scans the function body first. It sees `count = ...` and decides `count` is local. Then when it runs the right-hand side, `count` (local) hasn't been assigned yet. Boom.

## The `global` Keyword

To assign to a global from inside a function, declare it:

```python
count = 0

def increment():
    global count
    count = count + 1

increment()
print(count)      # 1
```

**Use sparingly.** Global mutable state makes code hard to reason about and test. Prefer returning values:

```python
def increment(count):
    return count + 1

count = increment(count)
```

## Enclosing Scope & Nested Functions

Functions can be defined inside other functions. The inner function can *read* variables from the outer function's scope — that's the "E" in LEGB.

```python
def outer():
    x = 10
    def inner():
        print(x)     # reads enclosing scope
    inner()

outer()    # 10
```

To *assign* to an enclosing variable from an inner function, use `nonlocal`:

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 99
    inner()
    print(x)         # 99

outer()
```

Without `nonlocal`, `x = 99` would create a new local `x` inside `inner` and leave the outer one alone.

- `global` — target the module-level scope
- `nonlocal` — target the nearest enclosing function's scope

## Built-in Scope

Python's built-in names live in the last-checked scope. That's how you can use `len`, `print`, `range` without importing anything.

You can shadow built-ins accidentally — a classic beginner trap:

```python
list = [1, 2, 3]        # shadowed the built-in `list`!
x = list(range(5))      # TypeError — a list isn't callable
```

Don't name variables `list`, `dict`, `set`, `str`, `id`, `type`, `input`, `print`, etc.

## Closures

When an inner function references variables from an enclosing scope, and the outer function returns the inner one, the inner function *closes over* those variables. It carries them along.

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor    # `factor` is captured from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))    # 10
print(triple(5))    # 15
```

`double` and `triple` are two different function objects, each carrying its own `factor`. This is a **closure** — a function bundled with the variables it references from its defining scope.

Closures are the mechanism behind decorators, callbacks, and partial application.

## The Scope Visualization

```
┌───────────────────────────────────────┐
│  Built-in scope (len, print, range)   │
│  ┌─────────────────────────────────┐  │
│  │  Global scope (module top)      │  │
│  │  ┌───────────────────────────┐  │  │
│  │  │  Enclosing (outer fn)     │  │  │
│  │  │  ┌─────────────────────┐  │  │  │
│  │  │  │  Local (inner fn)   │  │  │  │
│  │  │  └─────────────────────┘  │  │  │
│  │  └───────────────────────────┘  │  │
│  └─────────────────────────────────┘  │
└───────────────────────────────────────┘
```

Lookup: bubble outward from the innermost scope. First match wins.

## Common Mistakes

- **`UnboundLocalError` from assigning to a global.** Fix with `global` or (better) pass the value in and return it.
- **Shadowing built-ins.** Never name variables `list`, `dict`, `id`, `type`, `input`, etc.
- **Assuming `nonlocal` works for module globals.** It doesn't — `nonlocal` targets *enclosing function* scope. Use `global` for module level.
- **Late-binding closure trap.** Loop variables are captured by reference, not value:
  ```python
  funcs = [lambda: i for i in range(3)]
  [f() for f in funcs]     # [2, 2, 2] — not [0, 1, 2]!
  ```
  Fix with a default argument (which captures at definition time):
  ```python
  funcs = [lambda i=i: i for i in range(3)]
  [f() for f in funcs]     # [0, 1, 2]
  ```

## Best Practices

- Prefer passing values in and returning them out. Avoid mutable global state.
- Keep function bodies short — fewer names, fewer scope questions.
- Use `nonlocal` when you legitimately need to mutate enclosing state (rare — often a signal to refactor into a class).
- Never shadow built-ins.

## Key Takeaways

- LEGB: Local → Enclosing → Global → Built-in. Lookup order.
- Assigning to a name inside a function makes it local by default.
- `global x` — assignments target module scope.
- `nonlocal x` — assignments target the nearest enclosing function scope.
- Closures = inner function + captured variables from enclosing scope.
- Late-binding: closures capture variables by reference, not by value.

## Active Recall

1. Explain the LEGB rule in your own words.
2. Why does this raise `UnboundLocalError`?
   ```python
   count = 0
   def f():
       count = count + 1
   f()
   ```
3. What's the difference between `global` and `nonlocal`?
4. What does the following print, and why?
   ```python
   fns = [lambda: i for i in range(3)]
   print([f() for f in fns])
   ```
5. Why is naming a variable `list` a bad idea?

---

# Chapter 23: Lambdas and Functional Tools

## What & Why

A **lambda** is a one-line, anonymous function. You use it when you need a small function *right now* and don't want the ceremony of a `def` statement — usually as an argument to another function like `sorted`, `map`, or `filter`.

Python isn't a purely functional language, but it borrows enough that you'll frequently see `sorted(items, key=lambda x: x[1])`. This chapter is about being fluent in that syntax.

## Lambda Syntax

```python
lambda parameters: expression
```

That's it. No `def`, no `return`, no name. It evaluates to a function object.

```python
square = lambda x: x * x
print(square(5))         # 25

add = lambda a, b: a + b
print(add(3, 4))         # 7
```

Restrictions vs `def`:

- Body is a single expression (not a statement, not multiple lines).
- No annotations, no docstring.
- Anonymous by design (though you can assign it to a name, as above).

**Style note:** if you find yourself writing `square = lambda x: x * x`, use `def` instead. Lambdas shine when passed inline as arguments; naming them defeats the purpose. Linters (PEP 8) explicitly discourage `name = lambda ...`.

## Where Lambdas Actually Shine

**As sort keys:**

```python
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted(people, key=lambda p: p["age"])
```

**As map/filter functions:**

```python
list(map(lambda x: x * 2, [1, 2, 3]))       # [2, 4, 6]
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))  # [2, 4]
```

**As small callbacks:**

```python
button.on_click(lambda: print("clicked"))
```

For anything more complex than one clean expression, use `def`. Multi-line lambdas via tricks like nested ternaries are just torture for the reader.

## `map(function, iterable)`

Applies a function to each element of an iterable, returning an iterator of results.

```python
nums = [1, 2, 3, 4]
list(map(lambda x: x ** 2, nums))     # [1, 4, 9, 16]

# Also works with multiple iterables — function takes multiple args
list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30]))    # [11, 22, 33]
```

`map` returns a lazy iterator, so you often wrap it in `list()` to see results, or feed it into `sum`, `max`, etc.

**Idiomatic Python alternative:** a list comprehension. `[x**2 for x in nums]` is usually preferred because it reads more naturally and doesn't require a lambda. Reach for `map` when you already have a named function that fits (e.g., `map(int, ["1", "2", "3"])`).

## `filter(function, iterable)`

Keeps only the elements for which the function returns truthy.

```python
nums = [-2, -1, 0, 1, 2]
list(filter(lambda x: x > 0, nums))    # [1, 2]

# Passing None as the function keeps only truthy values
list(filter(None, [0, 1, "", "hi", None, [], [1]]))   # [1, 'hi', [1]]
```

Again, list comprehensions with `if` are usually more Pythonic: `[x for x in nums if x > 0]`.

## `functools.reduce(function, iterable, [initial])`

Folds an iterable down to a single value by applying a two-argument function repeatedly.

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])       # 10  (like sum)
reduce(lambda a, b: a * b, [1, 2, 3, 4])       # 24  (factorial-ish)
reduce(lambda a, b: a + b, [1, 2, 3, 4], 100)  # 110 (initial value)
```

Reduce is powerful but often less clear than a plain loop or a built-in (`sum`, `max`, `min`, `math.prod`). Guido himself proposed removing it from the built-ins (it lives in `functools` now for that reason). Use when nothing else fits.

## `sorted(..., key=...)` and `min`/`max`

The `key` parameter takes a function that maps each element to the value used for comparison. Lambdas make this ergonomic:

```python
words = ["banana", "pie", "Washington", "book"]
sorted(words, key=lambda w: len(w))            # sort by length
sorted(words, key=lambda w: w.lower())         # case-insensitive

# Tuple keys sort lexicographically — great for multi-level sort
sorted(people, key=lambda p: (p["age"], p["name"]))

max([1, 2, 3, -10], key=lambda x: abs(x))      # -10  (largest by magnitude)
min(words, key=len)                             # 'pie'
```

For simple attribute or item access, `operator.itemgetter` and `operator.attrgetter` are faster and cleaner than lambdas:

```python
from operator import itemgetter, attrgetter

sorted(people, key=itemgetter("age"))          # equivalent, faster
sorted(objects, key=attrgetter("timestamp"))
```

## `any` and `all`

Not strictly "functional tools," but they pair beautifully with generator expressions:

```python
any(x < 0 for x in nums)         # True if any negative
all(x > 0 for x in nums)         # True if all positive
any(x.startswith("A") for x in names)
```

These short-circuit — `any` returns True on first truthy; `all` returns False on first falsy. Efficient.

## Common Mistakes

- **Assigning lambdas to names.** Just use `def`.
- **Trying to put statements in lambdas.** `lambda x: print(x)` works because `print` is an expression; `lambda x: x = 5` doesn't because assignment is a statement.
- **Forgetting `list()` around `map`/`filter`.** They return iterators; `print(map(...))` gives `<map object at 0x...>`.
- **Using `map`/`filter` where a comprehension is clearer.** Comprehensions are usually more Pythonic.
- **Late-binding trap with lambdas in loops** (Chapter 22):
  ```python
  fns = [lambda: i for i in range(3)]      # all return 2
  fns = [lambda i=i: i for i in range(3)]  # each captures its own i
  ```

## Best Practices

- Lambdas belong inline as arguments. If you'd name it, `def` it.
- Prefer comprehensions over `map`/`filter` for readability.
- Use `operator.itemgetter`/`attrgetter` for simple keys.
- Reserve `reduce` for cases where no built-in helper fits.

## Key Takeaways

- Lambda: `lambda params: expression`. Anonymous, one expression, function object.
- `map(f, iter)` — apply `f` to each item; returns iterator.
- `filter(f, iter)` — keep items where `f` is truthy; returns iterator.
- `functools.reduce(f, iter)` — fold to a single value.
- `sorted`/`min`/`max` with `key=` — one of the most common places to use a lambda.
- `any` / `all` — pair with generator expressions.
- Comprehensions are often more Pythonic than `map`/`filter`.

## Active Recall

1. Write a lambda that returns the last character of a string.
2. Use `sorted` with a lambda to sort a list of tuples by the second element.
3. What's the difference between `map(f, xs)` and `[f(x) for x in xs]` in terms of return type?
4. Why is `x = lambda a: a + 1` considered bad style?
5. Rewrite this using a comprehension: `list(filter(lambda x: x % 2 == 0, range(10)))`.

---

# Chapter 24: Recursion

## What & Why

A function that calls itself is **recursive**. Recursion turns a problem into a smaller version of itself, plus a "base case" that stops the recursion.

You'll use recursion for:

- Naturally recursive data (trees, nested structures, JSON walking).
- Divide-and-conquer algorithms (mergesort, quicksort).
- Backtracking (mazes, permutations).
- Problems expressed most naturally as "solve n by solving n-1."

You'll *avoid* recursion for problems that iterate cleanly (loops are usually faster and safer in Python) and for very deep chains (Python's default recursion limit is 1000).

## Mental Model

Every recursive function has two parts:

1. **Base case(s)** — a condition where the function returns without calling itself. Without this, infinite recursion → `RecursionError`.
2. **Recursive case** — the function calls itself on a smaller/simpler input, then combines the result.

Think of recursion as the mathematical definition:

- `factorial(0) = 1`                        ← base case
- `factorial(n) = n * factorial(n - 1)`     ← recursive case

Every call adds a **stack frame** — a chunk of memory holding that call's local variables. When a call returns, its frame pops off. Deep recursion → deep stack → potentially explode the stack limit.

## Factorial — The Canonical Example

```python
def factorial(n):
    if n < 0:
        raise ValueError("factorial not defined for negative n")
    if n == 0 or n == 1:      # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))    # 120
```

Trace:

```
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * 1)))
= 120
```

Each call is waiting for its recursive call to return before finishing its own multiplication.

## Fibonacci — And Why Naive Recursion Bites

Fibonacci: `fib(n) = fib(n-1) + fib(n-2)`, with `fib(0) = 0, fib(1) = 1`.

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Works — but appallingly slow. `fib(35)` takes seconds. Why? Because it computes `fib(30)` many, many times over as it branches. The call tree is roughly `2**n` in size.

Fix with **memoization** — cache results:

```python
from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

fib(100)     # instant
```

The `@cache` decorator (Python 3.9+) remembers past return values so repeated calls with the same input return instantly. Chapter 35 covers decorators; for now, know that `@cache` above a function is a huge speedup for pure recursive functions.

Same result without the decorator, using a dict:

```python
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result
```

Or — often the sensible answer — just use a loop:

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

Loops are usually faster and don't risk hitting the recursion limit. Recursion is a mental model, not a mandate.

## Recursion Depth

Python's default recursion limit is 1000 frames. Beyond that:

```python
def blow_up(n):
    return blow_up(n + 1)

blow_up(0)   # RecursionError: maximum recursion depth exceeded
```

You can raise it with `sys.setrecursionlimit(5000)`, but that's a bandaid. If you're hitting the limit, your algorithm should probably be iterative.

Python does **not** perform tail-call optimization. `return f(...)` at the end of a function still adds a stack frame. This is a language design choice — Guido has stated tracebacks are more valuable than tail-call optimization.

## Where Recursion Shines: Tree/Nested Data

Some structures are recursive by nature. Walking JSON:

```python
def walk(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            print(k)
            walk(v)
    elif isinstance(obj, list):
        for item in obj:
            walk(item)
    else:
        print(obj)

data = {"name": "Sid", "skills": ["Python", "Solidity"], "address": {"city": "Sohagpur"}}
walk(data)
```

Trying to do this iteratively means maintaining your own stack — you're basically simulating recursion. Just use recursion.

Directory traversal, parsing nested expressions, and tree-search algorithms all fit this shape.

## Reasoning About Recursion

The trick: **trust the recursion**. When designing a recursive function, assume the recursive call works correctly for smaller inputs, then just handle:

1. What's the base case?
2. Assuming `f(n-1)` is correct, how do I use it to compute `f(n)`?

Don't try to trace the full call tree in your head — you'll get lost. Trust the induction. If base case is right and the recursive step correctly reduces to the base case, the whole thing is right.

## Common Mistakes

- **No base case (or wrong base case).** Infinite recursion → `RecursionError`.
- **Base case never reached.** e.g., `factorial(n - 2)` misses odd numbers when starting from odd `n`.
- **Missing return.** Forgetting `return` on the recursive call — the result vanishes and you get `None`.
- **Exponential blowup without memoization.** Naive Fibonacci.
- **Using recursion when a loop is trivially better.** Sum of a list, printing 1..n, etc.
- **Deep recursion.** Python's stack limit is 1000. Deep trees, huge inputs → convert to iteration.

## Best Practices

- Always define the base case first — write it before the recursive step.
- Ensure the recursive call moves toward the base case.
- Use `@functools.cache` for pure functions with repeated subproblems.
- Prefer iteration when the problem is fundamentally sequential (summing, counting, walking a flat list).
- Reach for recursion when data is recursive (trees, JSON, nested structures).

## Key Takeaways

- Recursion = a function calling itself, driven by a base case and a recursive step.
- Every call adds a stack frame; Python caps recursion at ~1000.
- Naive branching recursion (like Fibonacci) blows up without memoization.
- `@functools.cache` gives free memoization.
- Loops are usually the better answer for sequential problems; recursion shines on tree-shaped data.
- Trust the recursion — assume the smaller call works, and build the answer from there.

## Active Recall

1. What are the two essential ingredients of every recursive function?
2. Why is naive recursive `fib(n)` exponentially slow?
3. What does `@cache` do, and why does it fix recursive Fibonacci?
4. What's Python's default recursion limit? What happens when you exceed it?
5. Give an example of a problem where recursion is more natural than iteration.

---

# Chapter 25: Modules, Packages, and Imports

## What & Why

A **module** is just a Python file. Once you have more than a hundred lines of code, keeping everything in one file becomes painful. Modules let you split code across multiple files and pull in functionality from Python's massive standard library and from the third-party ecosystem.

Understanding imports well matters because 95% of real Python work is gluing together other people's code — `numpy`, `requests`, `pandas`, `openai`, whatever. If you can't confidently import, you can't build anything real.

## Modules

**Any `.py` file is a module.** If you have `math_utils.py` with:

```python
# math_utils.py
def square(x):
    return x * x

def cube(x):
    return x * x * x

PI = 3.14159
```

...you can import it from another file in the same directory:

```python
# main.py
import math_utils

print(math_utils.square(5))    # 25
print(math_utils.PI)           # 3.14159
```

## Import Forms

Four flavors, from most to least specific:

```python
import math                    # bring in the module; use as math.sqrt(9)
import math as m               # rename it locally
from math import sqrt          # bring in one name; use as sqrt(9)
from math import sqrt as s     # rename it
from math import sqrt, pi, cos # bring in several names
from math import *             # bring in EVERYTHING (avoid — see below)
```

**Style preference (PEP 8):**

- Prefer `import module` for readability — `math.sqrt(9)` makes it obvious where `sqrt` comes from.
- `from module import name` is fine for commonly-used names (e.g., `from typing import Optional`).
- **Never use `from module import *`** in production code. It pollutes your namespace, makes it impossible to know what's from where, and can silently shadow built-ins. The only place `*` imports are OK is in a REPL for quick exploration.

## How Python Finds Modules — `sys.path`

When you write `import foo`, Python searches these locations in order:

1. Built-in modules (compiled into the interpreter — `sys`, `builtins`).
2. The directory of the script being run.
3. Directories in the `PYTHONPATH` environment variable.
4. Site-packages directories (where `pip` installs third-party packages).

`sys.path` (a list) contains all these directories. Inspect it:

```python
import sys
print(sys.path)
```

If your import fails with `ModuleNotFoundError`, it's usually because the module isn't in any of these places — often a venv issue (Chapter 40) or you're running the wrong Python.

## Standard Library vs Third-Party

- **Standard library** — modules that ship with Python. No install needed. Examples: `math`, `os`, `sys`, `json`, `re`, `pathlib`, `datetime`, `collections`, `itertools`, `functools`.
- **Third-party** — installed via `pip install <name>` (or `uv add <name>`). Examples: `requests`, `numpy`, `pandas`, `flask`.

You import both the same way. Python doesn't care where a module came from.

## Packages

A **package** is a directory of modules. If you have:

```
mypackage/
    __init__.py
    tools.py
    formatters.py
```

...then `mypackage` is a package containing modules `tools` and `formatters`. You import them like:

```python
import mypackage.tools
from mypackage.formatters import bold
```

The `__init__.py` marks the directory as a package. It can be empty, or it can contain code that runs when the package is first imported (often used to expose a curated public API).

Packages can nest arbitrarily deep:

```
mypackage/
    __init__.py
    subpackage/
        __init__.py
        helpers.py
```

```python
from mypackage.subpackage.helpers import do_thing
```

## Relative Imports (Inside a Package)

Within a package, you can use relative imports:

```python
# Inside mypackage/subpackage/helpers.py
from .. import tools                # up one level
from ..formatters import bold       # up one level, then into formatters
from . import sibling               # same directory
```

- `.` — current package.
- `..` — parent package.

Relative imports only work inside packages, and only when the package is run as part of a proper import structure — not as a script. This trips up beginners often.

## `if __name__ == "__main__":`

Every module has a special variable `__name__`. When you *run* a file directly (`python foo.py`), Python sets `__name__ = "__main__"`. When you *import* it, Python sets `__name__` to the module's name (`"foo"`).

You use this to distinguish "am I being run as a script?" from "am I being imported as a library?":

```python
# calculator.py
def add(a, b):
    return a + b

def main():
    print(add(3, 4))

if __name__ == "__main__":
    main()
```

- `python calculator.py` → `__name__` is `"__main__"` → `main()` runs.
- `import calculator` from another file → `__name__` is `"calculator"` → `main()` does NOT run. You just get the definitions.

This is why every Python script you'll ever see ends with that block. It lets a file work as both a script and a library.

## What Happens When You Import

1. Python locates the module file.
2. Compiles it to bytecode (cached in `__pycache__/`).
3. Executes the module's code top-to-bottom, creating a module object.
4. Binds the module to the name in your local namespace.

**Critical insight:** the module code runs *once* per interpreter session. Subsequent imports don't re-execute — they just bind the existing module object. This makes imports cheap but also means module-level side effects (e.g., `print("loading")` at the top) only fire once.

To force reload during development:

```python
import importlib
importlib.reload(mymodule)
```

Rarely needed in normal code.

## Naming a Script Same as a Standard-Library Module

If you name your file `math.py` and do `import math`, Python will import *your* file (because your script's directory comes first on `sys.path`). Then all the actual `math` functions vanish and you get inscrutable errors. Don't name files after standard-library modules.

## Common Mistakes

- **`from module import *`.** Namespace pollution. Avoid.
- **Shadowing standard-library names.** `math.py`, `random.py`, `email.py` — all bad file names.
- **Circular imports.** Module A imports B, B imports A. Python doesn't handle this well; refactor to break the cycle (extract shared code into a third module).
- **Forgetting `if __name__ == "__main__":`.** If your script also does work at module level, importing it triggers that work.
- **Editing an already-imported module and expecting changes.** Restart the interpreter or use `importlib.reload`.
- **Running a package-internal file directly.** Relative imports break because there's no package context.

## Best Practices

- One file = one concept. Long files get modularized.
- Group imports at the top of the file: (1) standard library, (2) third-party, (3) local (PEP 8 order), separated by blank lines.
- Use `import module` over `from module import *`.
- Wrap runnable code in `if __name__ == "__main__":`.
- Give modules descriptive lowercase names with underscores if needed: `image_utils.py`, not `imageUtils.py`.

## Key Takeaways

- Every `.py` file is a module.
- A directory of modules with `__init__.py` is a package.
- Four import forms: `import`, `import as`, `from import`, `from import as`. Avoid `import *`.
- Python finds modules via `sys.path`.
- `if __name__ == "__main__":` distinguishes script vs library usage.
- Module code runs once on first import; cached thereafter.

## Active Recall

1. What's the difference between a module and a package?
2. Why is `from module import *` discouraged?
3. What does `__name__ == "__main__"` mean, and why use it?
4. If your file is named `random.py`, what happens when you `import random`?
5. Where does Python look for modules? (Give at least three places.)

---

# Chapter 26: Errors and Exceptions

## What & Why

Things go wrong. Files don't exist. Network calls time out. Users type "abc" when you expected a number. Division by zero happens. **Exceptions** are Python's way of signaling and handling these situations without cluttering every function with error-check-return-code plumbing.

Exception handling is one of the most important skills in real Python code. Missing it entirely (as your original notes do) is a big gap.

## Two Kinds of Errors

- **Syntax errors** — your code doesn't parse. Python refuses to run it at all. `if x = 5:` is a syntax error. You can't `try/except` your way past these.
- **Exceptions** — runtime errors. Code parses fine, but something goes wrong while running. These you *can* catch and handle.

## The Traceback

When an unhandled exception fires, Python prints a **traceback**: the chain of function calls leading to the error, plus the error type and message.

```
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    process(data)
  File "app.py", line 8, in process
    return 10 / count
ZeroDivisionError: division by zero
```

Read tracebacks **bottom-up**: the last line is the actual error. Then look above to see where you were when it happened. This is your #1 debugging tool.

## try / except

The basic form:

```python
try:
    result = 10 / x
except ZeroDivisionError:
    print("Can't divide by zero")
    result = None
```

If the code in `try` raises `ZeroDivisionError`, control jumps to the `except` block. Otherwise, the `except` block is skipped.

**Catch the specific exception you expect.** Bare `except:` (which catches everything, including keyboard interrupts) is almost always a bug in disguise.

## Multiple `except` Blocks

```python
try:
    value = int(user_input)
    result = 100 / value
except ValueError:
    print("Not a valid number")
except ZeroDivisionError:
    print("Can't divide by zero")
except (TypeError, KeyError) as e:      # tuple = catch any of these
    print(f"Something else went wrong: {e}")
```

Order matters. Python checks each `except` in order and jumps to the first match. Put specific exceptions before general ones.

## `as` — Capturing the Exception Object

```python
try:
    ...
except ValueError as e:
    print(f"Bad value: {e}")
    print(type(e))       # <class 'ValueError'>
```

`e` is the exception object. It has attributes like `args` and, for many exceptions, extra data. Use `str(e)` for a readable message.

## `else` and `finally`

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("Missing file")
else:
    print("Success!")     # runs only if try succeeded
    contents = f.read()
    f.close()
finally:
    print("Always runs")  # runs whether or not exception occurred
```

- `else` — runs if no exception was raised in `try`. Useful when you want a "success" branch that's *not* inside the `try` (so its own exceptions don't get accidentally caught).
- `finally` — always runs, even if you `return` from inside `try` or an unhandled exception propagates. Used for cleanup (closing files, releasing locks). The `with` statement (context managers, Chapter 36) is usually cleaner than `finally` for resource cleanup.

## Exception Hierarchy

Python's exceptions form a tree. Catching a parent catches all children. Selected hierarchy:

```
BaseException
 ├── SystemExit                 (sys.exit)
 ├── KeyboardInterrupt          (Ctrl+C)
 ├── GeneratorExit
 └── Exception                  ← catch this or below
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    ├── OverflowError
      │    └── FloatingPointError
      ├── AttributeError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── NameError
      ├── TypeError
      ├── ValueError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    ├── TimeoutError
      │    └── ConnectionError
      └── StopIteration
```

**Practical rule:** `except Exception:` catches most things but NOT `KeyboardInterrupt` or `SystemExit`. `except BaseException:` catches everything — almost always wrong.

Common exception types to know:
- `ValueError` — right type, wrong value. `int("abc")`.
- `TypeError` — wrong type. `"hi" + 3`.
- `KeyError` — dict key not found.
- `IndexError` — list index out of range.
- `AttributeError` — object doesn't have that attribute. `[].foo`.
- `NameError` — variable doesn't exist.
- `FileNotFoundError` — trying to open a nonexistent file.
- `ZeroDivisionError` — division by zero.
- `StopIteration` — iterator is exhausted (rarely caught directly).

## Raising Exceptions

Use `raise` to signal an error yourself:

```python
def sqrt(x):
    if x < 0:
        raise ValueError(f"sqrt undefined for negative number: {x}")
    return x ** 0.5
```

You can re-raise the current exception with a bare `raise`:

```python
try:
    do_thing()
except ValueError:
    log("something failed")
    raise           # re-raises so caller can handle
```

You can chain exceptions with `from`:

```python
try:
    do_low_level()
except LowLevelError as e:
    raise HighLevelError("something went wrong") from e
```

This preserves the original cause in the traceback — very helpful for debugging library code.

## Custom Exceptions

Define your own by subclassing `Exception`:

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Balance {self.balance} < {amount}")
        self.balance -= amount
```

Callers can catch your specific type:

```python
try:
    account.withdraw(1_000_000)
except InsufficientFundsError as e:
    print(f"Nope: {e}")
```

Custom exceptions make libraries much easier to use — callers can distinguish "your bug" from "expected failure mode."

## EAFP vs LBYL

Python has a distinctive philosophy: **Easier to Ask Forgiveness than Permission (EAFP)** — try the operation and catch the exception if it fails. Contrast with **Look Before You Leap (LBYL)** — check preconditions before every operation.

```python
# EAFP — Pythonic
try:
    value = my_dict[key]
except KeyError:
    value = "default"

# LBYL — verbose, sometimes racy (file could get deleted between check and use)
if key in my_dict:
    value = my_dict[key]
else:
    value = "default"
```

EAFP is usually preferred in Python. It's often more concise and avoids race conditions in concurrent or filesystem contexts. That said, LBYL is fine when the check is cheap and the "error" path is common — `if key in my_dict` is perfectly reasonable when misses are expected.

## `assert` — Not for Runtime Validation

`assert condition, "message"` raises `AssertionError` if the condition is false.

```python
def factorial(n):
    assert n >= 0, "n must be non-negative"
    ...
```

**Assertions can be disabled** with `python -O`. Never use them for user-facing validation, security checks, or anything you need to actually happen. They're for internal invariants and debugging — "this should never be false; if it is, my logic has a bug."

## Common Mistakes

- **Bare `except:` or `except Exception:` with no plan.** Swallows *everything*, including `KeyboardInterrupt` (bare) and every unrelated bug. Catch specific exceptions.
- **Silent `except: pass`.** Errors vanish; debugging becomes impossible.
- **Catching too broadly.** `except:` around a whole function often hides the real problem.
- **Using exceptions for control flow in tight loops.** Exceptions are cheap-ish but not free; a plain `if` may be faster.
- **`assert` for validating user input.** Use `if ... raise ValueError` instead.
- **Not chaining with `from`.** Losing the original cause when re-raising.

## Best Practices

- Catch the narrowest exception you can meaningfully handle.
- Handle exceptions at the layer that can *do something* about them — not everywhere.
- Log or re-raise; don't silently swallow.
- Use `finally` (or `with`) for cleanup.
- Define custom exceptions when your code has domain-specific failure modes.
- Prefer EAFP over LBYL in Python.
- Read tracebacks bottom-up: the last line is what happened, the lines above are the path there.

## Key Takeaways

- Exceptions are runtime errors that can be caught with `try/except`.
- Catch specific exception types; bare `except:` is almost always a bug.
- `else` runs after successful `try`; `finally` always runs.
- All standard exceptions inherit from `Exception`; use it as the broadest reasonable catch.
- Raise your own with `raise ExceptionType("message")`.
- Chain with `raise X from y` to preserve causes.
- EAFP is idiomatic Python; LBYL is fine when misses are expected.

## Active Recall

1. What's the difference between a syntax error and an exception?
2. Why is `except:` (bare) considered dangerous?
3. What's the difference between `else` and `finally` in try/except?
4. Give three ways `int(x)` can fail (with different exception types).
5. Write a custom exception `TooManyAttemptsError` and raise it after 3 failed attempts.

---

# Chapter 27: File I/O

## What & Why

Every non-trivial program eventually reads or writes files — configuration, logs, data sets, model outputs, saved state. Python's file API is small and easy to remember once you understand the pieces.

## The `open()` Function

```python
f = open(path, mode="r", encoding="utf-8")
```

Parameters that matter:

- **`path`** — string or `pathlib.Path` to the file.
- **`mode`** — how you're opening it (read, write, append, binary).
- **`encoding`** — character encoding for text files. Always specify `"utf-8"` explicitly; the default is platform-dependent and will bite you on Windows.

## Modes

| Mode                        | Meaning                                                          |
| --------------------------- | ---------------------------------------------------------------- |
| `"r"`                       | Read (default). File must exist.                                 |
| `"w"`                       | Write. **Truncates** the file if it exists, creates it if not.   |
| `"a"`                       | Append. Creates if missing. Writes go to the end.                |
| `"x"`                       | Exclusive create. Errors if file exists.                         |
| `"r+"`                      | Read + write. File must exist.                                   |
| `"w+"`                      | Read + write. Truncates existing file.                           |
| `"b"` (add to any of above) | Binary mode. `"rb"`, `"wb"`, etc. Works with `bytes`, not `str`. |
| `"t"` (add to any of above) | Text mode. Default.                                              |

**Text vs binary:** text mode decodes bytes to `str` using the encoding. Binary mode gives you raw `bytes`. Use binary for images, PDFs, videos, model files. Use text for `.txt`, `.csv`, `.json`, `.py`, etc.

## The `with` Statement — Always Use It

**Never** use bare `open()` in real code. Always use a `with` block:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    contents = f.read()
```

The `with` statement guarantees the file is closed when the block exits — even if an exception is raised. This is the context manager pattern; Chapter 36 covers it in depth.

Without `with`, you'd need `try/finally`:

```python
f = open("data.txt")
try:
    contents = f.read()
finally:
    f.close()
```

`with` is shorter, safer, and idiomatic. Just always use it.

## Reading

Three main ways to read text files:

```python
# 1. Read the entire file into a string
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2. Read all lines into a list
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()      # each element includes trailing '\n'

# 3. Iterate line by line — best for large files
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")    # strip trailing newline
        print(line)
```

Method 3 is the winner for anything larger than a few kilobytes. It's memory-efficient and streams the file — the whole thing never has to live in RAM at once.

`readline()` reads one line at a time, returning `""` at EOF — rarely needed with iteration.

## Writing

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")            # you handle newlines yourself
    f.write("World\n")

# Write many lines at once
lines = ["line1\n", "line2\n", "line3\n"]
with open("out.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

Notes:

- `write()` does NOT add a newline — you provide `\n` yourself.
- `writelines()` doesn't add newlines either. Bad naming, but historical.
- Opening in `"w"` truncates. If you want to add to the end, use `"a"` (append).

**Alternative — `print` to a file:**

```python
with open("out.txt", "w", encoding="utf-8") as f:
    print("Hello", file=f)        # adds newline automatically
    print("World", file=f)
```

Convenient when you already use `print` and want the same behavior.

## Appending

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"[{timestamp}] event\n")
```

`"a"` never truncates. Each write goes to the end. Good for logs.

## Binary Files

```python
# Read an image
with open("photo.jpg", "rb") as f:
    data = f.read()               # bytes, not str
print(type(data))                 # <class 'bytes'>

# Copy binary file
with open("src.bin", "rb") as src, open("dst.bin", "wb") as dst:
    dst.write(src.read())
```

Notice you can open multiple files in one `with` — just separate with commas.

## Cursor / Seek

Files have a position (byte offset). You can move it:

```python
with open("file.txt", "rb") as f:
    f.read(10)         # read first 10 bytes
    print(f.tell())    # 10
    f.seek(0)          # back to start
    f.seek(5)          # position 5 from start
    f.seek(0, 2)       # go to end (whence=2)
```

Rarely needed in day-to-day work, but essential for random-access file formats.

## `pathlib` — The Modern Way to Handle Paths

For anything more than a hardcoded filename, use `pathlib.Path` instead of raw strings.

```python
from pathlib import Path

# Build paths
data_dir = Path("data")
file = data_dir / "raw" / "input.csv"       # / operator joins paths
print(file)                                  # data/raw/input.csv (or backslashes on Windows)

# Check existence
file.exists()
file.is_file()
file.is_dir()

# Simple read/write
text = file.read_text(encoding="utf-8")
file.write_text("hello", encoding="utf-8")
data = file.read_bytes()

# Metadata
file.name         # "input.csv"
file.stem         # "input"
file.suffix       # ".csv"
file.parent       # Path("data/raw")

# Iterate a directory
for p in data_dir.iterdir():
    print(p)

# Recursive glob
for py_file in Path(".").rglob("*.py"):
    print(py_file)

# Make directories
Path("output/plots").mkdir(parents=True, exist_ok=True)
```

`pathlib` is:

- **Cross-platform** — handles slashes correctly on Windows and Unix.
- **Object-oriented** — operations are methods on `Path`, not scattered `os.path` functions.
- **Concise** — `Path("a") / "b" / "c"` beats `os.path.join("a", "b", "c")`.

Prefer `pathlib` over `os.path` in any new code. It's been the recommended API for years.

## Common Mistakes

- **Not using `with`.** Files stay open, may not flush, and if an exception fires the file leaks.
- **Not specifying encoding.** Defaults are platform-dependent; explicit `encoding="utf-8"` avoids nasty surprises.
- **Reading gigabyte files with `.read()`.** Iterate line-by-line for large files.
- **Confusing `"w"` and `"a"`.** `"w"` obliterates the file. If it had data before, it's gone.
- **Forgetting `\n` in `write()`.** Everything ends up on one line.
- **Using `open()` returns as a truthiness check.** File objects are always truthy — check `path.exists()` instead.
- **String concatenation for paths.** `"data/" + name` fails on Windows and has edge cases. Use `Path` or `os.path.join`.

## Best Practices

- Always use `with open(...) as f:`.
- Always specify `encoding="utf-8"` for text files.
- Iterate line-by-line for large files.
- Use `pathlib.Path` for path manipulation.
- Use `path.read_text()` and `path.write_text()` for the simple case of reading/writing an entire text file.
- Never assume a file exists; check with `path.exists()` or catch `FileNotFoundError`.

## Key Takeaways

- `open(path, mode, encoding=...)` opens a file. Modes: `r`, `w`, `a`, `x`, plus `+` and `b`.
- Always use `with` — auto-closes even on exception.
- Read: `.read()`, `.readlines()`, or iterate line-by-line (best for large files).
- Write: `.write()` doesn't add newlines; you provide `\n`.
- Text mode gives you `str`; binary mode (`"rb"`, `"wb"`) gives you `bytes`.
- Use `pathlib.Path` for paths — cross-platform, object-oriented.

## Active Recall

1. Why should you always use `with` when opening files?
2. What does mode `"w"` do to an existing file? What about `"a"`?
3. When should you use `"rb"` instead of `"r"`?
4. How would you read a 5GB file without loading it all into memory?
5. Convert this to use `pathlib`: `path = "data" + "/" + filename; if os.path.exists(path): ...`

---

# Chapter 28: JSON and CSV

## What & Why

You'll spend a huge fraction of your career moving data between programs. Two formats dominate that traffic:

- **JSON** — structured data (dicts and lists), the lingua franca of web APIs and config files.
- **CSV** — tabular data (rows and columns), the workhorse of spreadsheets and simple datasets.

Python's standard library handles both. In AI/ML work you'll also use `pandas` for CSV, but the built-in `csv` module is faster and simpler for basic tasks and doesn't add a dependency.

## JSON — Overview

JSON is a text format that closely mirrors Python's dicts and lists:

```json
{
  "name": "Sid",
  "age": 23,
  "skills": ["Python", "Solidity"],
  "location": {"city": "Sohagpur", "state": "MP"}
}
```

Type mapping between JSON and Python:

| JSON        | Python           |
| ----------- | ---------------- |
| object `{}` | `dict`           |
| array `[]`  | `list`           |
| string      | `str`            |
| number      | `int` or `float` |
| `true`      | `True`           |
| `false`     | `False`          |
| `null`      | `None`           |

Not everything Python can represent goes into JSON: tuples become lists, sets fail, custom objects need custom handling, `datetime` isn't supported (you serialize to ISO string yourself).

## The `json` Module — Four Functions

```python
import json

# Python object → JSON string
s = json.dumps(obj)

# Python object → JSON file
with open("out.json", "w", encoding="utf-8") as f:
    json.dump(obj, f)

# JSON string → Python object
obj = json.loads(s)

# JSON file → Python object
with open("in.json", "r", encoding="utf-8") as f:
    obj = json.load(f)
```

Mnemonic: `s` on the end = **string**. No `s` = file.

## Writing JSON

```python
import json

data = {
    "name": "Sid",
    "age": 23,
    "skills": ["Python", "Solidity"],
    "active": True,
    "score": None
}

# Compact — one line
json.dumps(data)
# '{"name": "Sid", "age": 23, "skills": ["Python", "Solidity"], "active": true, "score": null}'

# Pretty-printed
print(json.dumps(data, indent=2))
# {
#   "name": "Sid",
#   "age": 23,
#   "skills": [
#     "Python",
#     "Solidity"
#   ],
#   "active": true,
#   "score": null
# }

# Sort keys for deterministic output (useful for diffs, tests)
json.dumps(data, indent=2, sort_keys=True)

# Handle non-ASCII characters properly
json.dumps({"greeting": "नमस्ते"}, ensure_ascii=False)
```

Write to a file:

```python
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

## Reading JSON

```python
# From a string
s = '{"name": "Sid", "age": 23}'
obj = json.loads(s)
print(obj["name"])     # 'Sid'

# From a file
with open("data.json", "r", encoding="utf-8") as f:
    obj = json.load(f)
```

If the JSON is malformed, you get a `json.JSONDecodeError` (a subclass of `ValueError`). Wrap in `try/except` when parsing untrusted input.

## Custom Objects

By default, `json.dumps` can't serialize things like `datetime`, `set`, or your own classes:

```python
from datetime import datetime
json.dumps({"now": datetime.now()})     # TypeError!
```

Two common fixes:

**1. Preprocess the data:**

```python
data = {"now": datetime.now().isoformat()}      # convert to string first
json.dumps(data)
```

**2. Provide a `default=` function:**

```python
def convert(o):
    if isinstance(o, datetime):
        return o.isoformat()
    if isinstance(o, set):
        return list(o)
    raise TypeError(f"Not JSON serializable: {type(o)}")

json.dumps({"now": datetime.now(), "tags": {"a", "b"}}, default=convert)
```

`json.dumps` calls `default(o)` for any object it doesn't know how to serialize.

## JSON Gotchas

- **JSON keys must be strings.** `json.dumps({1: "a"})` silently converts `1` to `"1"`. When you load it back, the key is `"1"`, not `1`.
- **NaN and Infinity aren't valid JSON.** Python's `json` module emits them anyway by default (with `allow_nan=True`); strict JSON parsers won't accept them. Pass `allow_nan=False` to reject them explicitly.
- **Tuples become lists.** JSON has no tuple. Roundtripping a tuple gives you a list.
- **Sets fail entirely.** Convert to a list first.
- **No comments.** Real JSON forbids comments. If you need commented config, use YAML or TOML.

## CSV — Overview

CSV (comma-separated values) is plain text organized as rows and columns, with a comma between fields. Example:

```
name,age,city
Alice,30,Delhi
Bob,25,Mumbai
Charlie,28,Bengaluru
```

Sounds simple, isn't quite: fields containing commas need quoting, fields with quotes need escaping, line endings vary between systems. Use the `csv` module — never hand-roll `.split(",")`.

## The `csv` Module — Reading

```python
import csv

# Basic — each row is a list of strings
with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['name', 'age', 'city']
# ['Alice', '30', 'Delhi']
# ...

# DictReader — each row is a dict keyed by header
with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

**Note the `newline=""` argument.** Always pass this when opening a CSV file. It disables Python's newline translation, which the `csv` module handles itself. Skipping it causes weird blank rows on Windows.

**All values are strings.** If you need numbers, cast them yourself: `int(row["age"])`.

## The `csv` Module — Writing

```python
import csv

# Basic — write rows as lists
rows = [
    ["name", "age", "city"],
    ["Alice", 30, "Delhi"],
    ["Bob", 25, "Mumbai"],
]

with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)                # writes all rows
    # or: for row in rows: writer.writerow(row)

# DictWriter — write dicts
records = [
    {"name": "Alice", "age": 30, "city": "Delhi"},
    {"name": "Bob", "age": 25, "city": "Mumbai"},
]

with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(records)
```

## CSV Gotchas

- **Every field is a string on read.** Numbers, booleans, dates — you cast manually.
- **Missing `newline=""`.** Cross-platform blank-row bug.
- **Special characters (comma, quote, newline in a field).** The `csv` module handles these correctly. Rolling your own with `str.split(",")` gets it wrong.
- **Wrong delimiter.** Sometimes files use `;` or `\t` instead of `,`. Pass `delimiter=";"` or `delimiter="\t"` to the reader/writer.
- **BOM (byte-order-mark) at the start.** Files exported from Excel sometimes begin with `\ufeff`. Open with `encoding="utf-8-sig"` to strip it.

## When to Use `pandas` Instead

For data analysis, `pandas` is far more powerful:

```python
import pandas as pd
df = pd.read_csv("data.csv")
df["age"].mean()
df[df["age"] > 25]
```

Use `pandas` for anything analytical — filtering, aggregation, groupby, joins. Use the stdlib `csv` module for simple read/write in scripts where you don't want a heavy dependency, and for row-by-row streaming of huge files.

## Common Mistakes

- **`json.dumps` on non-serializable objects.** Provide a `default=` or preprocess.
- **Assuming JSON preserves tuples.** It doesn't. They roundtrip as lists.
- **Comments in JSON.** Invalid. Switch formats or generate the JSON from code.
- **`.split(",")` for CSV.** Fails on quoted fields, escaped quotes, and embedded newlines.
- **Forgetting `newline=""` on CSV files.**
- **Treating CSV numbers as numbers automatically.** They're strings until you cast.

## Best Practices

- Use `json.dump(..., indent=2)` for human-readable config; compact for machine-to-machine.
- Include `ensure_ascii=False` to preserve non-ASCII characters in JSON.
- Use `DictReader` and `DictWriter` for CSV when files have headers — it's much more readable than positional indexing.
- Cast CSV strings to their real types explicitly and validate as you go.
- For anything more complex than read-a-file-into-memory, use `pandas`.

## Key Takeaways

- JSON: use `json.dumps` / `json.loads` for strings, `json.dump` / `json.load` for files. `s` = string.
- JSON supports dict, list, str, int, float, bool, None. Not tuples, sets, datetimes, or custom classes without help.
- Pretty-print with `indent=2`. Non-ASCII: `ensure_ascii=False`.
- CSV: use the `csv` module, not `.split(",")`. Open with `newline=""`.
- `csv.DictReader` / `DictWriter` keep code readable when files have headers.
- Every CSV field is a string; cast to int/float yourself.

## Active Recall

1. What's the difference between `json.dumps` and `json.dump`? Same for `loads`/`load`.
2. Why do tuples not roundtrip through JSON?
3. Why do you always pass `newline=""` when opening a CSV file?
4. How would you write a Python `datetime` to JSON?
5. Given a CSV with columns `name,age`, write code that prints the average age.

---

# Chapter 29: Classes and Objects — Object-Oriented Programming Begins

## What & Why

**Object-Oriented Programming (OOP)** organizes code around **objects** — bundles of related data and the functions that operate on that data.

You've been using objects all along. Strings, lists, dicts, files — they're all objects, each with their own methods (`s.upper()`, `lst.append(x)`, `f.read()`). Now you'll learn to define your own types.

Why bother? Because as programs grow, keeping data and its behavior together (an object) reads much better than passing loose dicts to unrelated functions.

Compare:

```python
# Procedural — data and behavior separate
account = {"balance": 100}
def deposit(acc, amount): acc["balance"] += amount
def withdraw(acc, amount): acc["balance"] -= amount
deposit(account, 50)
```

vs

```python
# Object-oriented — data and behavior together
account = Account(balance=100)
account.deposit(50)
account.withdraw(30)
```

The OOP version reads more naturally, and callers don't need to know how `deposit` implements the update.

## Mental Model

- **Class** — the blueprint. Describes what data every instance holds and what operations it supports.
- **Object (instance)** — a specific thing built from that blueprint. Each has its own data.

Blueprint → house. Class → object. `Account` is a class. `my_account = Account(100)` creates an instance.

## Defining a Class

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def show(self):
        print(f"{self.owner}: ₹{self.balance}")
```

Piece by piece:

- `class Account:` — declares the class. Convention: **PascalCase** (also called CapWords) for class names.
- `def __init__(self, ...):` — the **constructor** (technically the *initializer*). Runs automatically when you create an instance.
- `self` — the first parameter of every instance method. It's the instance being operated on. When you call `account.deposit(50)`, Python translates it to `Account.deposit(account, 50)` — `self` is `account`.
- `self.owner = owner` — creates an **attribute** on the instance.

## Creating Instances

```python
alice = Account("Alice", 100)
bob = Account("Bob")             # balance defaults to 0

alice.deposit(50)                # method call — self is alice
bob.deposit(200)
alice.show()                     # Alice: ₹150
bob.show()                       # Bob: ₹200
```

`Account("Alice", 100)` calls `__init__(self=<new object>, owner="Alice", balance=100)` behind the scenes.

## Instance Attributes vs Class Attributes

- **Instance attributes** — assigned to `self` in methods. Each instance has its own.
- **Class attributes** — defined directly in the class body. Shared across all instances.

```python
class Dog:
    species = "Canis familiaris"    # class attribute — same for every dog

    def __init__(self, name, age):
        self.name = name             # instance attribute
        self.age = age

a = Dog("Buddy", 3)
b = Dog("Max", 5)

print(a.species)     # 'Canis familiaris'
print(b.species)     # 'Canis familiaris'
print(a.name)        # 'Buddy'
print(b.name)        # 'Max'

Dog.species = "Canis lupus familiaris"   # changes for ALL instances
print(a.species)                          # 'Canis lupus familiaris'
```

Class attributes are perfect for constants and defaults shared across instances. Do NOT put mutable objects (lists, dicts) as class attributes unless you want them shared:

```python
class BadDog:
    tricks = []            # SHARED — every dog's tricks list is the same list

    def __init__(self, name):
        self.name = name

    def teach(self, trick):
        self.tricks.append(trick)

a = BadDog("Buddy")
b = BadDog("Max")
a.teach("sit")
print(b.tricks)          # ['sit']  ← ugh
```

Fix: initialize inside `__init__`:

```python
class GoodDog:
    def __init__(self, name):
        self.name = name
        self.tricks = []        # per-instance
```

This is basically the same trap as mutable default arguments (Chapter 5).

## Methods — Three Flavors

```python
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):                          # instance method
        return Circle.pi * self.radius ** 2

    @classmethod
    def unit_circle(cls):                    # class method
        return cls(1)                        # cls is the class itself

    @staticmethod
    def describe():                          # static method
        return "A circle is a round shape."
```

- **Instance methods** — take `self`. Operate on a specific instance. 95% of methods.
- **Class methods** — decorated with `@classmethod`. First parameter is `cls` (the class itself). Used for alternative constructors (like `unit_circle` above) or class-level operations.
- **Static methods** — decorated with `@staticmethod`. Take neither `self` nor `cls`. Just functions logically grouped with the class. Rarely essential — often a plain function outside the class is fine.

Usage:

```python
c = Circle(5)
c.area()                # 78.53975  — instance method

u = Circle.unit_circle()   # 1  — class method, alternate constructor
u.area()                   # 3.14159

Circle.describe()          # class-level call
```

## Everything Is an Object

Python is deeply object-oriented. Every value is an object with a type:

```python
type(5)              # <class 'int'>
type("hi")           # <class 'str'>
type([1,2])          # <class 'list'>
type(len)            # <class 'builtin_function_or_method'>
type(print)          # <class 'builtin_function_or_method'>
type(int)            # <class 'type'>       ← classes are objects too!
```

When you call `int("5")`, you're calling the class `int` as if it were a function — that's how construction works.

## `self` Isn't Magic

`self` is just a name — the first parameter of an instance method. Convention says name it `self`; the language doesn't enforce it. When you call `account.deposit(50)`, Python looks up `deposit` on the class, sees it's a function, and calls it with `account` as the first argument.

That's it. All the "magic" of OOP is really just this convention plus attribute lookup.

## Common Mistakes

- **Forgetting `self`.** Methods must take `self` as their first parameter. Skip it and you get `TypeError: method takes 0 positional arguments but 1 was given`.
- **Assigning to `self` at the top level (outside a method).** You can't; there's no `self` there.
- **Mutable class attributes.** Shared across all instances. Almost always a bug.
- **Using instance state where a class attribute would do.** Constants that don't change per-instance belong at the class level.
- **Forgetting to call `__init__` via `super().__init__()`** when inheriting (Chapter 30).

## Best Practices

- Class names in **PascalCase**: `BankAccount`, `HTTPClient`.
- Method and attribute names in **snake_case**: `account_balance`, `deposit_funds`.
- Keep `__init__` focused on setting attributes, not doing heavy work.
- Group related methods together.
- If a "class" has no state and just holds a bunch of functions, make it a module instead.
- Reach for OOP when you have data + behavior that belong together, especially when you'll have many similar objects.

## Key Takeaways

- Class = blueprint; object = instance built from it.
- `__init__(self, ...)` is the initializer, called when an instance is created.
- `self` is the current instance; it's the first parameter of every instance method.
- Instance attributes (`self.x`) are per-object; class attributes (in the class body) are shared.
- `@classmethod` takes `cls`; `@staticmethod` takes neither.
- Convention: PascalCase for class names, snake_case for methods and attributes.

## Active Recall

1. What's the difference between a class and an object?
2. What does `self` refer to inside a method?
3. What's the difference between an instance attribute and a class attribute? Give an example of when each is right.
4. Why is defining `tricks = []` at the class level usually a bug?
5. What's the difference between `@classmethod` and `@staticmethod`?

---

# Chapter 30: Inheritance and `super()`

## What & Why

**Inheritance** lets a new class reuse and extend an existing class. The new class (**child** / **subclass**) gets all the parent's attributes and methods for free, and can add or override behavior.

Use it to:

- Share code between related classes (`Dog` and `Cat` both inherit from `Animal`).
- Model "is-a" relationships (a `Manager` is an `Employee`).
- Customize third-party classes.

Don't overuse it. Inheritance is a powerful hammer, and beginners tend to see everything as a nail. Prefer **composition** (holding another object as an attribute) when the relationship is "has-a," not "is-a."

## Basic Syntax

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow")


d = Dog("Buddy")
c = Cat("Whiskers")
d.speak()      # Buddy says woof
c.speak()      # Whiskers says meow
```

`class Dog(Animal):` — parentheses list the parent class(es). Dog inherits `__init__` from Animal automatically. Dog overrides `speak`.

## `super()` — Calling the Parent

When you want to *extend* rather than *replace* a parent method, use `super()`:

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)       # run Animal's __init__ first
        self.breed = breed

d = Dog("Buddy", "Labrador")
print(d.name, d.breed)               # Buddy Labrador
```

**Without `super().__init__(name)`**, `self.name` never gets set — Python doesn't call parent constructors automatically. This is one of the most common inheritance bugs.

`super()` returns a proxy object that delegates method calls to the parent class. You call any parent method through it:

```python
class Cat(Animal):
    def speak(self):
        super().speak()                          # do what parent does
        print(f"{self.name} also purrs")         # then add behavior
```

## `isinstance` and `issubclass`

Check relationships at runtime:

```python
d = Dog("Buddy", "Lab")

isinstance(d, Dog)         # True
isinstance(d, Animal)      # True — subclass instances count as parent instances
isinstance(d, Cat)         # False

issubclass(Dog, Animal)    # True
issubclass(Dog, Dog)       # True — a class is a subclass of itself
```

Use `isinstance` for type checks, not `type(x) == Dog` — `isinstance` correctly handles subclasses.

## Multi-Level Inheritance

```python
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, wheels, brand):
        super().__init__(wheels)
        self.brand = brand

class ElectricCar(Car):
    def __init__(self, wheels, brand, battery_kwh):
        super().__init__(wheels, brand)
        self.battery_kwh = battery_kwh

e = ElectricCar(4, "Tesla", 75)
print(e.wheels, e.brand, e.battery_kwh)  # 4 Tesla 75
```

Each `super().__init__` walks one step up the chain.

## Multiple Inheritance and MRO

Python allows a class to inherit from *multiple* parents:

```python
class Flyer:
    def move(self):
        print("Flying")

class Swimmer:
    def move(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

Duck().move()   # Flying
```

Which parent's `move` wins? Python uses the **Method Resolution Order (MRO)** — a specific, deterministic order in which classes are searched for methods. Inspect it:

```python
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyer'>, <class 'Swimmer'>, <class 'object'>)
```

The MRO is computed using the C3 linearization algorithm. In practice, it goes left-to-right through parents, respecting each parent's own MRO.

`object` is the root of every class hierarchy in Python. Even if you don't inherit from anything, you implicitly inherit from `object`.

**Diamond inheritance** — two parents share a common grandparent — is where MRO gets tricky. `super()` navigates the MRO correctly, calling each class in linearization order exactly once. Getting this right is why Python has C3.

**Practical advice:** most application code uses single inheritance. Multiple inheritance is powerful but easy to abuse. **Mixins** — small classes designed to be combined with others via multiple inheritance to add narrow behavior — are the legitimate use case:

```python
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(JSONSerializableMixin):
    def __init__(self, name):
        self.name = name

u = User("Sid")
u.to_json()      # '{"name": "Sid"}'
```

## Method Overriding

A subclass can redefine any method it inherits. The subclass version wins:

```python
class Base:
    def greet(self):
        print("Hello from Base")

class Child(Base):
    def greet(self):
        print("Hello from Child")

Child().greet()     # Hello from Child
```

If the child wants to extend rather than fully replace, use `super()`:

```python
class Child(Base):
    def greet(self):
        super().greet()
        print("...and Child too")
```

## When NOT to Use Inheritance

Inheritance implies "is-a." If your relationship is "has-a" or "uses-a," prefer composition:

```python
# Composition — Car HAS-A engine
class Engine:
    def start(self): print("Vroom")

class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()
```

vs inheritance, which would incorrectly say "a Car IS-AN Engine."

Rule of thumb: prefer composition unless you have a genuine "is-a" relationship *and* you'll benefit from polymorphism (Chapter 32).

## Common Mistakes

- **Forgetting `super().__init__(...)`** in a child. Parent attributes never get set.
- **Using inheritance for code reuse only.** If there's no "is-a" relationship, use composition.
- **Deep inheritance chains.** Four levels of inheritance is usually a design smell.
- **Trying to remember MRO by hand for complex hierarchies.** Just call `super()` and let Python figure it out.
- **Overriding a parent method with a *different* signature.** Technically legal, but usually a Liskov substitution violation and confusing.

## Best Practices

- Prefer composition over inheritance when both work.
- Use inheritance for "is-a" relationships.
- Always call `super().__init__(...)` in a subclass constructor.
- Keep inheritance chains shallow (2–3 levels max is a good default).
- Use mixins sparingly for cross-cutting concerns.
- Use `isinstance` for type checks (handles subclasses correctly).

## Key Takeaways

- `class Child(Parent):` sets up inheritance. Child gets parent's attributes/methods.
- `super()` calls the parent's method — essential for extending `__init__`.
- All classes inherit from `object` implicitly.
- `isinstance` and `issubclass` respect the hierarchy.
- Python supports multiple inheritance; MRO decides the order.
- Prefer composition when the relationship is "has-a."

## Active Recall

1. What does `super().__init__(name)` do inside a subclass's `__init__`?
2. What's the difference between `isinstance(x, Animal)` and `type(x) == Animal`?
3. What does `Duck.__mro__` tell you?
4. Give an example where composition is a better fit than inheritance.
5. If both parents in multiple inheritance define `speak`, whose method gets called?

---

# Chapter 31: Encapsulation and Properties

## What & Why

**Encapsulation** is the OOP principle that says: keep internal state private, expose a controlled interface. Callers shouldn't need to know (or depend on) how your class is implemented internally.

In many languages (Java, C#), encapsulation is enforced by keywords: `private`, `protected`, `public`. Python takes a different stance — it enforces almost nothing, relying on convention. **"We're all consenting adults here."**

But convention plus a couple of nice mechanisms (name mangling, properties) is more than enough.

## Naming Conventions

Python uses underscores to signal intent:

- **`name`** — public. Freely accessible.
- **`_name`** — "protected by convention." Meant for internal or subclass use. Nothing prevents access — this is documentation, not a lock.
- **`__name`** — "private-ish." Triggers **name mangling** (see below).
- **`__name__`** — dunder ("double underscore"). Reserved for Python's own use. Don't invent your own.
- **`name_`** — trailing underscore to avoid clashing with keywords. E.g. `class_ = ...` because `class` is reserved.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance          # public
        self._internal_id = generate_id()   # meant to be private, but visible
        self.__secret_key = "s3cr3t"    # name-mangled
```

## Name Mangling — What `__name` Actually Does

When you write `self.__secret_key = ...` inside a class, Python rewrites the attribute name to `_ClassName__secret_key`:

```python
class Vault:
    def __init__(self):
        self.__key = "hidden"

v = Vault()
print(v.__key)              # AttributeError
print(v._Vault__key)        # 'hidden'  ← still accessible
```

Name mangling is *not* privacy. It's a mechanism to prevent accidental name clashes in inheritance:

```python
class A:
    def __init__(self):
        self.__x = 1        # becomes _A__x

class B(A):
    def __init__(self):
        super().__init__()
        self.__x = 2        # becomes _B__x — doesn't collide!
```

If both used `self._x`, the subclass would silently overwrite the parent's. `__` names avoid that.

**Practical advice:** use `_name` (single underscore) 99% of the time. Reserve `__name` for real name-collision concerns, mostly in libraries with deep inheritance.

## Getters and Setters — Why Python Doesn't Need Them

In Java, you write:

```java
private int balance;
public int getBalance() { return balance; }
public void setBalance(int b) { balance = b; }
```

...because if you start with a public field and later need to add logic, callers break. Getters/setters give you room to add validation later without changing the interface.

In Python you'd just write:

```python
class Account:
    def __init__(self):
        self.balance = 0
```

If later you need validation, you turn `balance` into a **property**. Callers don't have to change a thing.

## `@property` — Computed Attributes

The `@property` decorator turns a method into something that *looks like* an attribute but runs code when accessed:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
print(r.area)         # 12  ← no parentheses; looks like an attribute
```

`r.area` calls the method, but syntactically feels like accessing a field. This lets you replace a stored field with a computed one without breaking any caller.

## Setters and Deleters

You can also intercept writes and deletions:

```python
class Account:
    def __init__(self, balance):
        self._balance = balance     # store in the "underscore" version

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance cannot be negative")
        self._balance = value

    @balance.deleter
    def balance(self):
        raise AttributeError("cannot delete balance")


a = Account(100)
print(a.balance)      # 100
a.balance = 200       # goes through setter
print(a.balance)      # 200
a.balance = -50       # ValueError
```

Notice `@balance.setter` — the decorator name matches the property, not `@setter`. Same for `@balance.deleter`.

This is the pattern that makes "getter/setter" unnecessary in Python: start with a plain attribute; upgrade to a property when you need logic.

## `@property` for Read-Only Fields

Common use case: computed values that shouldn't be assignable:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

c = Circle(5)
print(c.diameter)     # 10
c.diameter = 20       # AttributeError — no setter defined
```

Without a setter, assignment fails. That's the pattern for read-only attributes.

## `@cached_property`

If a computation is expensive and the underlying data doesn't change, use `functools.cached_property`:

```python
from functools import cached_property

class Dataset:
    def __init__(self, path):
        self.path = path

    @cached_property
    def size_mb(self):
        # expensive filesystem operation
        return Path(self.path).stat().st_size / 1_000_000
```

First access computes; subsequent accesses return the cached value. Ideal for values that are pure functions of the object's data.

## Common Mistakes

- **Assuming `__name` is private.** It's name-mangled, not private. `_Class__name` still works.
- **Overusing `__` names.** For most classes, `_name` (single underscore) is enough.
- **Naming an attribute the same as the property setter's parameter.** Store in `self._x`, expose via `self.x` — don't collide with yourself.
- **Writing Java-style getters/setters unnecessarily.** In Python, use bare attributes until you need the hook, then convert to a property.
- **Forgetting to use `@propname.setter`.** `@setter` doesn't exist as a standalone decorator.

## Best Practices

- Public by default: `self.x`. Underscore signals "internal" via `self._x`.
- Reserve `__name` for name-collision safety in inheritance-heavy code.
- Use properties when you need to add validation, computation, or side effects to attribute access.
- Prefer read-only properties (no setter) for computed values.
- Use `@cached_property` for expensive computations that don't change.

## Key Takeaways

- Python has no enforced privacy — only conventions and mangling.
- `_name` = "please don't touch" (convention).
- `__name` = name-mangled to `_ClassName__name` (collision avoidance, not privacy).
- `@property` turns a method into a read-only-looking attribute.
- `@propname.setter` / `@propname.deleter` intercept writes and deletes.
- Start with a plain attribute; upgrade to a property when logic is needed — callers don't change.

## Active Recall

1. What's the difference in intent between `self._x` and `self.__x`?
2. What does name mangling actually do to `self.__key`?
3. Why doesn't Python need Java-style getters and setters?
4. Write a `Temperature` class with a `celsius` property that rejects values below -273.15.
5. What's `@cached_property` for, and how does it differ from `@property`?

---

# Chapter 32: Polymorphism and Dunder Methods

## What & Why

**Polymorphism** — one interface, many implementations. Different objects respond to the same call in their own way.

You've already seen it: `len(x)` works on strings, lists, dicts, tuples, sets, and any custom class that implements `__len__`. `+` adds numbers, concatenates strings and lists. `for x in y:` iterates over anything with `__iter__`.

The mechanism: **dunder methods** (double-underscore methods, also called magic methods). They're hooks that Python calls in response to built-in operations. Define `__len__` and `len(obj)` works. Define `__add__` and `obj + other` works. Define `__str__` and `print(obj)` gives a nice output.

This chapter is a tour of the dunders you'll actually use.

## The Ones You'll Use Constantly

### `__init__` — Constructor

Already covered in Chapter 29. Runs when the object is created.

### `__str__` — Human-Readable String

Called by `print(obj)` and `str(obj)`. Should return an informative, human-friendly string.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(p)              # Point(3, 4)
str(p)                # 'Point(3, 4)'
```

Without `__str__`, `print(p)` gives you `<__main__.Point object at 0x7f...>` — useless.

### `__repr__` — Unambiguous Representation

Called by `repr(obj)` and shown when you inspect an object in the REPL. Should return a string that ideally could be pasted back into Python to recreate the object.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
p                     # Point(x=3, y=4)  — REPL uses __repr__
print([p, p])         # [Point(x=3, y=4), Point(x=3, y=4)]  — containers use __repr__ for elements
```

**Rules of thumb:**

- Define `__repr__` for every non-trivial class. Debugging is impossible without it.
- If you only define one, define `__repr__`. `str(obj)` falls back to `__repr__` when `__str__` is missing.
- `__str__` for end-users; `__repr__` for developers.

This is the biggest gap in most beginner tutorials: they teach `__str__` and skip `__repr__` entirely. `__repr__` is what shows up in every debug print, every list, every error message. Define it.

### `__len__` — Length

Called by `len(obj)`.

```python
class Playlist:
    def __init__(self):
        self.songs = []

    def __len__(self):
        return len(self.songs)

p = Playlist()
p.songs = ["a", "b", "c"]
len(p)     # 3
```

Bonus: any object with `__len__` becomes truthy/falsy based on length (Chapter 4). Empty playlist → falsy.

### `__eq__` — Equality

Called by `obj1 == obj2`. Without it, `==` defaults to identity (`is`) — different Point(3, 4) objects wouldn't be equal.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

Point(3, 4) == Point(3, 4)     # True
Point(3, 4) == Point(1, 2)     # False
Point(3, 4) == "hello"         # False (NotImplemented → Python falls back)
```

Return `NotImplemented` (the singleton, not `False`) when the other type isn't comparable. Python then tries the other operand's `__eq__`.

### `__hash__` — Hashability

When you override `__eq__`, Python **sets `__hash__` to None**, making your object unhashable (can't be a dict key or set member). If you want hashability back, define `__hash__` too — and make sure it's consistent with `__eq__` (equal objects must have equal hashes):

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
```

Now `Point` instances work as dict keys and set members.

## Arithmetic Dunders

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

Vector(1, 2) + Vector(3, 4)     # Vector(4, 6)
Vector(1, 2) * 3                # Vector(3, 6)
```

Full family:

| Operator     | Dunder         |
| ------------ | -------------- |
| `+`          | `__add__`      |
| `-`          | `__sub__`      |
| `*`          | `__mul__`      |
| `/`          | `__truediv__`  |
| `//`         | `__floordiv__` |
| `%`          | `__mod__`      |
| `**`         | `__pow__`      |
| `-x` (unary) | `__neg__`      |
| `+x` (unary) | `__pos__`      |
| `abs(x)`     | `__abs__`      |

Reflected versions (`__radd__`, `__rmul__`) let `3 * v` work when `v.__mul__(3)` doesn't handle the int-first case:

```python
def __rmul__(self, scalar):
    return self * scalar
```

Compound assignment (`+=`) uses `__iadd__` if defined; otherwise falls back to `__add__` and rebind.

## Comparison Dunders

```python
class Weight:
    def __init__(self, kg):
        self.kg = kg

    def __lt__(self, other): return self.kg < other.kg
    def __le__(self, other): return self.kg <= other.kg
    def __gt__(self, other): return self.kg > other.kg
    def __ge__(self, other): return self.kg >= other.kg
    def __eq__(self, other): return self.kg == other.kg
```

You don't need to define all six — Python fills in some from others. But defining all of them (or using `@functools.total_ordering` to auto-generate them from `__eq__` + one other) is cleanest:

```python
from functools import total_ordering

@total_ordering
class Weight:
    def __init__(self, kg):
        self.kg = kg
    def __eq__(self, other): return self.kg == other.kg
    def __lt__(self, other): return self.kg < other.kg
    # total_ordering fills in <=, >, >=, !=
```

## Container Dunders

Make your object indexable, iterable, and support `in`:

```python
class Deck:
    def __init__(self):
        self.cards = ["♠A", "♥K", "♦Q", "♣J"]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i):
        return self.cards[i]

    def __setitem__(self, i, value):
        self.cards[i] = value

    def __contains__(self, item):
        return item in self.cards

    def __iter__(self):
        return iter(self.cards)

d = Deck()
len(d)              # 4
d[0]                # '♠A'
d[1] = "♥Q"
"♣J" in d           # True
for card in d:      # iteration
    print(card)
```

Just implementing `__getitem__` and `__len__` gives you a lot for free — Python can iterate and use `in` on the sequence.

## `__call__` — Objects That Act Like Functions

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
double(5)          # 10  — instance called like a function
```

Useful for stateful callbacks, function-like objects, decorators with parameters (Chapter 35).

## `__bool__` — Custom Truthiness

Override to customize what `bool(obj)` and `if obj:` do:

```python
class Cart:
    def __init__(self):
        self.items = []

    def __bool__(self):
        return len(self.items) > 0
```

If you don't define `__bool__`, Python uses `__len__` (0 → False, else True). If neither, all instances are truthy.

## Selected Dunder Reference

| Dunder                                      | Called by                           |
| ------------------------------------------- | ----------------------------------- |
| `__init__`                                  | `Class(...)` — object creation      |
| `__repr__`                                  | `repr(x)`, REPL display, containers |
| `__str__`                                   | `str(x)`, `print(x)`, `f"{x}"`      |
| `__bool__`                                  | `bool(x)`, `if x:`                  |
| `__len__`                                   | `len(x)`, truthiness (fallback)     |
| `__eq__`, `__ne__`                          | `==`, `!=`                          |
| `__lt__`, `__le__`, `__gt__`, `__ge__`      | `<`, `<=`, `>`, `>=`                |
| `__hash__`                                  | `hash(x)`, dict/set membership      |
| `__add__`, `__sub__`, `__mul__`, ...        | arithmetic operators                |
| `__getitem__`, `__setitem__`, `__delitem__` | `x[i]`, `x[i] = v`, `del x[i]`      |
| `__contains__`                              | `y in x`                            |
| `__iter__`                                  | `for _ in x:`, `iter(x)`            |
| `__next__`                                  | `next(x)` on iterators              |
| `__call__`                                  | `x(...)`                            |
| `__enter__`, `__exit__`                     | `with x:` (Chapter 36)              |

## Common Mistakes

- **Skipping `__repr__`.** Debug output turns into cryptic memory addresses.
- **Defining `__eq__` without `__hash__`.** Object becomes unhashable — surprise breakage in sets/dicts.
- **Returning `False` instead of `NotImplemented`** in `__eq__` when other type is unknown.
- **Confusing `__str__` and `__repr__`.** Convention: `__str__` for humans, `__repr__` for developers.
- **Making `__eq__` inconsistent with `__hash__`.** Equal objects must have equal hashes.

## Best Practices

- Always define `__repr__`. Always.
- Add `__str__` when the default (`__repr__` fallback) isn't user-friendly.
- Define `__eq__` and `__hash__` together, keeping them consistent.
- Use `@functools.total_ordering` to avoid boilerplate on comparisons.
- Only implement operator dunders when they genuinely make sense — don't overload `+` to mean "concatenate names."

## Key Takeaways

- Dunders are Python's mechanism for making classes behave like built-ins.
- `__str__` for users; `__repr__` for developers. Define `__repr__` always.
- `__eq__` and `__hash__` must be consistent; overriding `__eq__` disables default hashing.
- Container behavior: `__len__`, `__getitem__`, `__iter__`, `__contains__`.
- Arithmetic dunders let your class support `+`, `-`, `*`, etc.
- `__call__` makes instances callable like functions.

## Active Recall

1. What's the difference between `__str__` and `__repr__`, and which should you define first?
2. Why does defining `__eq__` also require defining `__hash__` (if you want the object hashable)?
3. What does implementing `__len__` give you for free?
4. What does `NotImplemented` mean in `__eq__`? Why not return `False`?
5. What dunder makes `for x in obj:` work? What about `if x in obj:`?

---

# Chapter 33: Abstract Base Classes

## What & Why

An **Abstract Base Class (ABC)** is a class that can't be instantiated directly — it exists to define an interface that subclasses must implement.

The pattern:

- Define an ABC listing the methods every subclass MUST provide.
- Subclasses inherit from it and are required to override those methods.
- If a subclass forgets to implement one, Python refuses to instantiate it.

Why bother in Python, which usually gets by on duck typing?

- **Documentation.** The ABC codifies the contract: "if you want to be a `Shape`, you must have `area` and `perimeter`."
- **Enforcement.** You catch missing methods at instantiation time, not the first time someone calls the missing method in production.
- **`isinstance` checks that mean something.** `isinstance(x, Shape)` is a real interface check, not "hopefully this has an `area` method."

## Basic Syntax

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# Attempting to instantiate Shape directly:
# Shape()   # TypeError: Can't instantiate abstract class Shape

# Missing method:
class BrokenTriangle(Shape):
    def area(self):
        return 0

# BrokenTriangle()   # TypeError — didn't implement perimeter
```

`ABC` is the base class; `@abstractmethod` marks methods that subclasses must override.

## Concrete Methods in an ABC

An ABC can have both abstract and concrete methods:

```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):        # concrete — shared by all subclasses
        print(f"{self.__class__.__name__}: area={self.area():.2f}, perim={self.perimeter():.2f}")


Circle(5).describe()   # Circle: area=78.54, perim=31.42
```

This is a common pattern: put shared code in the ABC, force subclasses to implement the variable pieces.

## Abstract Properties

```python
class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    @property
    def sound(self):
        return "Woof"


d = Dog()
print(d.sound)     # Woof
```

Stack `@property` on top of `@abstractmethod`. The order matters — `@abstractmethod` must be innermost.

## The `Protocol` Alternative (Modern Python)

Python 3.8+ offers **`typing.Protocol`** — structural subtyping (duck typing with type-hint-level checking):

```python
from typing import Protocol

class Sized(Protocol):
    def __len__(self) -> int: ...


def show_size(x: Sized) -> None:
    print(len(x))

show_size([1, 2, 3])       # works — list has __len__
show_size("hello")          # works — str has __len__
```

You don't need to inherit from `Sized` — you just need `__len__`. Static type checkers verify structurally.

- **ABC** — nominal ("you must inherit from Shape"). Enforced at runtime.
- **Protocol** — structural ("you must have these methods"). Enforced at type-check time (or with `runtime_checkable`).

Use ABCs when you want runtime enforcement or shared implementation. Use Protocols when you want a lightweight, duck-typed interface for type hints.

## When to Use ABCs

- You're defining a framework where users must implement certain methods (plugins, storage backends, model interfaces).
- You want `isinstance` checks to mean something.
- You have shared implementation that should be inherited but the specifics vary.

For most small applications, ABCs are overkill. You often just use duck typing. But once you start building libraries or larger systems, ABCs earn their keep.

## Common Mistakes

- **Forgetting to inherit from `ABC`.** Just adding `@abstractmethod` to a class doesn't work without `ABC` (or `metaclass=ABCMeta`) as a base.
- **Instantiating an abstract class in tests.** Doesn't work — subclass or mock.
- **Missing an abstract method in a subclass.** You'll get a `TypeError` at instantiation, not at first use — which is the whole point.
- **Ordering decorators wrong on abstract properties.** `@property` first, then `@abstractmethod`.

## Best Practices

- Use ABCs to define a clear contract for a family of related classes.
- Include docstrings in abstract methods describing what implementations must do.
- Prefer `Protocol` for structural typing without inheritance.
- Don't over-engineer — small projects rarely need ABCs.

## Key Takeaways

- ABCs let you define interfaces subclasses must implement.
- Inherit from `abc.ABC` and mark methods with `@abstractmethod`.
- Abstract classes can't be instantiated directly.
- Subclasses that skip an abstract method also can't be instantiated.
- ABCs can mix abstract and concrete methods.
- `typing.Protocol` gives you structural duck typing for type hints.

## Active Recall

1. What happens if you try to instantiate a class with `@abstractmethod` methods that weren't overridden?
2. Can an ABC have regular (non-abstract) methods too?
3. What's the difference between an ABC and a `Protocol`?
4. Why is `@abstractmethod` more useful than a comment saying "subclasses should implement this"?
5. Write an ABC `Logger` with an abstract method `log(message)` and a concrete method `warn(message)` that calls `self.log(f"WARN: {message}")`.

---

# Chapter 34: Iterators and Generators

## What & Why

An **iterator** is an object that produces values one at a time when you call `next()` on it. That's the mechanism behind every `for` loop in Python — the loop repeatedly calls `next()` until the iterator is exhausted.

A **generator** is a special kind of iterator that you write using a function with the `yield` keyword. Generators are the easiest way to define custom iterators, and they're also lazy — they produce values on demand instead of building the entire sequence in memory.

Once you understand these, you can:

- Process streams of data (log lines, network events) with constant memory.
- Represent infinite sequences (`primes()`, `naturals()`).
- Chain transformations without materializing intermediate lists.
- Write clean pipelines that work on huge datasets.

## The Iterator Protocol

Any object that implements two dunders is an iterator:

- `__iter__(self)` — returns the iterator (often `self`).
- `__next__(self)` — returns the next value, or raises `StopIteration` when done.

An **iterable** is anything you can call `iter()` on to get an iterator. Lists, tuples, strings, dicts, sets, files — all iterable.

```python
lst = [10, 20, 30]
it = iter(lst)          # get iterator from iterable
print(next(it))         # 10
print(next(it))         # 20
print(next(it))         # 30
print(next(it))         # StopIteration
```

`for x in lst:` is essentially:

```python
it = iter(lst)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    # loop body
```

## Building an Iterator Manually

The verbose way — implement the protocol yourself:

```python
class Countdown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        current = self.n
        self.n -= 1
        return current

for x in Countdown(3):
    print(x)
# 3
# 2
# 1
```

Works but tedious. There's a better way.

## Generators — Functions with `yield`

A function containing `yield` is a **generator function**. Calling it doesn't run the code; instead, it returns a **generator object** (which is an iterator). Each call to `next()` runs the function until it hits a `yield`, at which point it pauses and returns the yielded value. Next `next()` call resumes right where it paused.

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for x in countdown(3):
    print(x)
# 3
# 2
# 1
```

Way cleaner. Compare to the class version above — same behavior, far less code.

**Mental model:** think of `yield` as "pause here and hand back a value; when someone asks for the next one, resume from right here."

When the function ends (or hits a bare `return`), the generator raises `StopIteration` automatically.

## Lazy Evaluation

Generators produce values on demand. This has huge memory implications:

```python
# Eager — builds the full list
squares_list = [x * x for x in range(10_000_000)]        # 400 MB in RAM

# Lazy — builds a generator; no memory allocated upfront
squares_gen = (x * x for x in range(10_000_000))         # tiny

sum(squares_gen)       # streams through, constant memory
```

The generator expression `(...)` is a compact way to create a generator without writing a function. Same syntax as a list comprehension, parentheses instead of brackets.

## Infinite Generators

Because generators are lazy, they can represent infinite sequences:

```python
def naturals():
    n = 1
    while True:
        yield n
        n += 1

it = naturals()
next(it)     # 1
next(it)     # 2
next(it)     # 3
```

Just don't try `list(naturals())` — it'll run forever. Combine with something that stops:

```python
from itertools import islice

first_ten = list(islice(naturals(), 10))    # [1, 2, ..., 10]
```

## `yield from` — Delegating

If a generator wants to yield everything from another iterable, you can:

```python
def flatten(nested):
    for sublist in nested:
        for item in sublist:
            yield item
```

Or use `yield from`:

```python
def flatten(nested):
    for sublist in nested:
        yield from sublist

list(flatten([[1, 2], [3, 4], [5]]))    # [1, 2, 3, 4, 5]
```

`yield from x` is equivalent to `for item in x: yield item`, plus a few subtleties around exceptions and return values. Cleaner in nested cases.

## When Iteration Ends

Iterators are one-shot. Once exhausted, they stay exhausted:

```python
g = (x*x for x in range(3))
list(g)      # [0, 1, 4]
list(g)      # []  ← already exhausted
```

If you need to iterate multiple times, either build a list (`list(gen)`) or wrap the generator in a function you can call again:

```python
def squares():
    for x in range(3):
        yield x * x

list(squares())    # [0, 1, 4]
list(squares())    # [0, 1, 4]  ← fresh generator each call
```

## Practical Uses

**Streaming a log file line by line:**

```python
def read_lines(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip()

for line in read_lines("app.log"):
    if "ERROR" in line:
        print(line)
```

Constant memory regardless of file size.

**Chunking:**

```python
def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i+n]

for c in chunks(range(10), 3):
    print(list(c))
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]
# [9]
```

**Building a data pipeline:**

```python
lines      = read_lines("data.log")
parsed     = (parse(line) for line in lines)
errors     = (p for p in parsed if p.level == "ERROR")
messages   = (e.message for e in errors)

for msg in messages:
    print(msg)
```

Each stage is lazy. No intermediate list. Works on gigabyte files.

## The `itertools` Module

The standard library's `itertools` has a treasure chest of generator utilities:

```python
from itertools import count, cycle, repeat, islice, chain, takewhile, dropwhile, groupby

count(10)                 # 10, 11, 12, ... (infinite)
cycle([1, 2, 3])          # 1, 2, 3, 1, 2, 3, ... (infinite)
repeat("hi", 3)           # hi, hi, hi
islice(count(), 5)        # first 5 of infinite counter
chain([1,2], [3,4])       # 1, 2, 3, 4
takewhile(lambda x: x < 5, [1, 2, 6, 3])  # 1, 2 (stops at first False)
```

Bookmark `itertools`. You'll return to it often.

## Common Mistakes

- **Consuming a generator twice.** They exhaust; re-create if needed.
- **`list(infinite_gen)`.** Boom.
- **Forgetting that generator expressions live inside parens.** `sum(x for x in ...)` OK; standalone `x for x in ...` isn't valid syntax.
- **Confusing `return` in a generator with a yielded value.** A bare `return` just ends the generator. `return value` also ends it and packages `value` inside the `StopIteration` (rarely used).
- **Thinking `yield` makes a function slow.** It's about laziness, not speed — often faster than list construction when you don't need all values.

## Best Practices

- Prefer generator expressions over list comprehensions when the result feeds a reducer (`sum`, `any`, `all`, `max`).
- Use generators to process large or streaming data with constant memory.
- Give generator functions verb-like names: `read_records`, `emit_events`.
- Use `yield from` to delegate to inner iterables.
- Reach for `itertools` before writing complex generator logic by hand.

## Key Takeaways

- Iterator = object with `__iter__` and `__next__`. Iterable = anything you can `iter()`.
- `for` loops use the iterator protocol under the hood.
- Generator = function with `yield`. Cleanest way to write iterators.
- Generators are lazy — values produced on demand, constant memory.
- Iterators are one-shot; recreate them if you need to iterate again.
- Generator expression: `(expr for x in iter)` — parens, not brackets.
- `itertools` has a rich toolkit of generator utilities.

## Active Recall

1. What two dunder methods define an iterator?
2. What's the difference between an iterator and an iterable?
3. What happens when a generator function hits `yield`? What happens on the next `next()`?
4. Why can generator expressions represent infinite sequences?
5. Write a generator that yields the Fibonacci numbers indefinitely.

---

# Chapter 35: Decorators

## What & Why

A **decorator** is a function that wraps another function, adding behavior without changing the wrapped function's code. You've already seen them: `@staticmethod`, `@classmethod`, `@property`, `@cache`, `@abstractmethod`. This chapter teaches you to write your own.

Common uses:

- **Logging** — trace which functions were called and with what arguments.
- **Timing** — measure how long a function takes.
- **Caching / memoization** — remember past results.
- **Authorization** — reject calls if the user isn't logged in.
- **Retries** — auto-retry on transient failure.

Decorators keep this cross-cutting behavior out of the function body and let you turn it on/off with a single line.

## Building Up

Recall: functions are first-class objects (Chapter 20). You can pass them around, store them, and return them from other functions.

**Step 1 — a function that takes another function:**

```python
def call_twice(fn, x):
    return fn(x), fn(x)

def square(x):
    return x * x

call_twice(square, 5)    # (25, 25)
```

**Step 2 — a function that returns a new function:**

```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
add5(10)                  # 15
```

`adder` closes over `n` — that's a **closure** (Chapter 22).

**Step 3 — a decorator: takes a function, returns a modified function:**

```python
def log_calls(fn):
    def wrapper(*args, **kwargs):
        print(f"calling {fn.__name__} with {args} {kwargs}")
        result = fn(*args, **kwargs)
        print(f"  returned {result}")
        return result
    return wrapper

def add(a, b):
    return a + b

add = log_calls(add)     # replace add with the wrapped version

add(3, 4)
# calling add with (3, 4) {}
#   returned 7
```

`log_calls(add)` returns a new function (`wrapper`) that logs, calls the original, logs again, and returns the result. Reassigning `add = log_calls(add)` swaps the original for the wrapped version.

## The `@` Syntax

`@decorator` above a function definition is syntactic sugar for `func = decorator(func)`:

```python
@log_calls
def add(a, b):
    return a + b

# Equivalent to:
def add(a, b):
    return a + b
add = log_calls(add)
```

Same result, cleaner syntax. Read `@log_calls` as "wrap the next function in `log_calls`."

## Preserving Metadata with `functools.wraps`

When you wrap a function, the wrapper doesn't inherit its name, docstring, or signature:

```python
def log_calls(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)   # 'wrapper'  ← should be 'add'
print(add.__doc__)    # None       ← lost the docstring
```

Fix: use `functools.wraps` on the inner function:

```python
from functools import wraps

def log_calls(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)   # 'add'
print(add.__doc__)    # 'Add two numbers.'
```

**Always use `@wraps` in your decorators.** It preserves the wrapped function's identity for introspection, help text, IDEs, and stack traces.

## Practical Example — Timing

```python
import time
from functools import wraps

def timing(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{fn.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timing
def slow_operation():
    time.sleep(0.5)
    return 42

slow_operation()
# slow_operation took 0.5003s
# 42
```

## Decorators with Arguments

Sometimes you want to configure the decorator: `@retry(times=3)`, `@rate_limit(per_second=10)`. This requires one more layer: a function that *returns* a decorator.

```python
from functools import wraps

def retry(times):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    print(f"attempt {attempt+1} failed: {e}")
            raise RuntimeError(f"{fn.__name__} failed after {times} attempts")
        return wrapper
    return decorator

@retry(times=3)
def fragile():
    import random
    if random.random() < 0.7:
        raise ValueError("bad luck")
    return "ok"

fragile()
```

Three layers deep:

1. `retry(3)` returns `decorator`.
2. `decorator(fragile)` returns `wrapper`.
3. `wrapper(...)` is what actually runs when you call `fragile(...)`.

Read `@retry(times=3)` as: "call `retry(times=3)` to get a decorator, then apply that decorator to the next function."

## Stacking Decorators

You can apply multiple decorators. They apply bottom-up (nearest to the function first):

```python
@log_calls
@timing
def work():
    ...
```

Equivalent to:

```python
def work(): ...
work = log_calls(timing(work))
```

`timing` wraps `work` first; then `log_calls` wraps the result. When you call `work()`, `log_calls`'s wrapper runs first (outermost), then delegates to `timing`'s wrapper, which delegates to the original.

## Decorating Methods

Decorators work on class methods too. Just remember: methods take `self`, so your wrapper's `*args` will include it:

```python
def log_calls(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        print(f"{self.__class__.__name__}.{fn.__name__} called")
        return fn(self, *args, **kwargs)
    return wrapper

class Account:
    @log_calls
    def deposit(self, amount):
        ...
```

## Class-Based Decorators

Decorators can also be classes with `__call__`:

```python
class CountCalls:
    def __init__(self, fn):
        self.fn = fn
        self.count = 0
        wraps(fn)(self)

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.fn(*args, **kwargs)

@CountCalls
def hello():
    print("hello")

hello()
hello()
hello()
print(hello.count)   # 3
```

Useful when the decorator needs mutable state or its own methods.

## Common Mistakes

- **Forgetting `@wraps(fn)`.** Wrapped functions lose their name and docstring.
- **Confusing `@decorator` and `@decorator()`.** With arguments, you need parentheses (`@retry(3)`, not `@retry`). Without arguments, no parens (`@log_calls`, not `@log_calls()`) unless the decorator is designed to accept optional arguments.
- **Order matters when stacking.** `@a @b def f` applies `b` first, then `a`.
- **Mutating the decorated function.** Return a wrapper; don't reach into the original.
- **Doing heavy work at decoration time instead of call time.** Decoration happens once when the file is loaded. Anything you want to happen per-call belongs in `wrapper`.

## Best Practices

- Always `@wraps(fn)` on your wrapper.
- Keep decorators small and single-purpose.
- Prefer built-in / library decorators (`functools.cache`, `functools.lru_cache`) when they fit — no need to reinvent memoization.
- Name decorators descriptively: `retry`, `log_calls`, `require_admin`.
- Don't overuse. A decorator that only shows up in one place is often better as an explicit call in the function body.

## Key Takeaways

- Decorator = function that takes a function and returns a (usually enhanced) function.
- `@decorator` is sugar for `func = decorator(func)`.
- Use `@functools.wraps` inside your decorator to preserve name, docstring, and signature.
- Decorators with arguments require three nested functions (or a class + `__call__`).
- Stacked decorators apply bottom-up.
- `functools` provides several ready-made decorators (`cache`, `lru_cache`, `wraps`, `total_ordering`).

## Active Recall

1. Write a minimal decorator that just prints "called" before every invocation.
2. What does `@functools.wraps(fn)` do, and why is it important?
3. What's the difference between `@retry` and `@retry(3)` in a decorator definition?
4. If you stack `@a @b` above a function, which one wraps the function directly?
5. When should you prefer a class-based decorator over a function-based one?

---

# Chapter 36: Context Managers

## What & Why

A **context manager** is an object that manages a resource — sets it up on entry, tears it down on exit, guaranteeing the teardown even if an exception fires.

The `with` statement is how you use them:

```python
with open("data.txt") as f:
    contents = f.read()
# f is automatically closed here, even on exception
```

You already know one context manager (files, Chapter 27). Others: database connections, network sockets, locks, temporary directories, in-memory redirects. Anywhere you have "acquire → do stuff → release," context managers are the right tool.

## The Protocol

An object is a context manager if it defines two dunders:

- `__enter__(self)` — runs when the `with` block starts. Return value gets bound to the `as` variable.
- `__exit__(self, exc_type, exc_val, exc_tb)` — runs when the block exits (normally or via exception). Return truthy to suppress the exception; return falsy (or nothing) to let it propagate.

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"took {self.elapsed:.4f}s")

with Timer():
    sum(i*i for i in range(1_000_000))
# took 0.0512s
```

If `__exit__` returns `True`, any exception raised inside the `with` block is swallowed. Rarely what you want — usually you let it propagate.

## The `contextlib.contextmanager` Decorator

Writing `__enter__`/`__exit__` classes is boilerplate. The `contextlib` module's `@contextmanager` decorator lets you write context managers as generators:

```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    yield                        # value here becomes the `as` variable
    elapsed = time.perf_counter() - start
    print(f"took {elapsed:.4f}s")

with timer():
    sum(i*i for i in range(1_000_000))
```

Everything before `yield` is `__enter__`. Everything after is `__exit__`. The yielded value (if any) is what the `as` binds to.

To handle exceptions with cleanup, use `try/finally`:

```python
@contextmanager
def open_conn(url):
    conn = connect(url)
    try:
        yield conn
    finally:
        conn.close()

with open_conn("db://...") as conn:
    conn.execute("...")
```

The `finally` guarantees `conn.close()` runs even if something inside the `with` throws.

## Multiple Context Managers

You can nest with-blocks, but a single `with` can manage multiple:

```python
with open("in.txt") as fin, open("out.txt", "w") as fout:
    for line in fin:
        fout.write(line.upper())
```

For long lists, Python 3.10+ supports parenthesized syntax:

```python
with (
    open("in.txt") as fin,
    open("out.txt", "w") as fout,
    open("log.txt", "a") as log,
):
    ...
```

## Suppressing Exceptions with `contextlib.suppress`

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("temp.tmp")     # if the file doesn't exist, no error
```

Cleaner than an empty `try/except`.

## Redirecting stdout with `contextlib.redirect_stdout`

```python
from contextlib import redirect_stdout
from io import StringIO

buf = StringIO()
with redirect_stdout(buf):
    print("captured!")
print("normal")

print(buf.getvalue())     # 'captured!\n'
```

Useful in tests to capture print output.

## Practical Examples

**Temporary working directory:**

```python
import os
from contextlib import contextmanager

@contextmanager
def cd(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)

with cd("/tmp"):
    # do stuff in /tmp
    ...
# back to original directory
```

**Database transaction:**

```python
@contextmanager
def transaction(conn):
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise

with transaction(conn) as c:
    c.execute("...")
    c.execute("...")
```

Commit if the block succeeds; rollback if anything raises.

## Common Mistakes

- **Forgetting `try/finally` inside `@contextmanager` generators.** If the `with` block raises, your cleanup after `yield` won't run.
- **Returning nothing from `__enter__`.** `with obj as x:` binds `x` to whatever `__enter__` returns; without a return, `x` is `None`.
- **Swallowing exceptions accidentally** by returning `True` from `__exit__`.
- **Using `with` on something that isn't a context manager.** Get `AttributeError: __enter__`.

## Best Practices

- Use `with` for every resource acquisition — files, locks, sockets, DB connections.
- Prefer `@contextmanager` for simple context managers; use the class form when you need methods or state beyond enter/exit.
- Include `try/finally` in generator-based context managers to ensure cleanup on exceptions.
- Let exceptions propagate — swallow them only when you truly know they're expected.

## Key Takeaways

- Context managers pair resource setup (`__enter__`) with guaranteed teardown (`__exit__`).
- `with` is the syntax that drives them.
- Files, locks, DB connections, temp files — all naturally context-managed.
- `@contextlib.contextmanager` lets you write context managers as generators.
- One `with` can manage multiple resources (comma-separated).
- `contextlib.suppress`, `redirect_stdout`, and friends give you handy stdlib helpers.

## Active Recall

1. What two dunder methods define a context manager?
2. What does `with open(...) as f:` guarantee that a bare `f = open(...)` doesn't?
3. Write a context manager using `@contextmanager` that prints "start" and "end" around a block.
4. What happens if `__exit__` returns `True`?
5. Why does `@contextmanager` typically use `try/finally` around `yield`?

---

# Chapter 37: Type Hints and Modern Python

## What & Why

Python is dynamically typed — you never *have* to declare what type a variable holds. But as codebases grow, "what does this function expect, and what does it return?" becomes a real cost. **Type hints** let you annotate expected types without changing how the code runs. Python itself mostly ignores them at runtime; they exist for humans and for tools — editors, linters, and type checkers like `mypy` or `pyright`.

Type hints are not a different language. They're optional annotations layered on top of ordinary Python. Nothing stops you from lying to them, and the interpreter will not stop you either — but your tooling will scream, and that's the point.

## Mental Model

Think of type hints as a contract you post on the door of a function: "I accept an `int`, I hand back a `str`." Nobody enforces the contract at the door (Python won't check it while running), but a type checker reads every contract in your codebase and tells you, ahead of time, everywhere you've broken one.

## Basic Syntax

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

age: int = 23
price: float = 19.99
is_active: bool = True
```

- `name: str` annotates a parameter.
- `-> str` annotates the return type.
- Variable annotations (`age: int = 23`) are optional and rarely necessary — usually the right-hand side already makes the type obvious.

## Collection Types

```python
from typing import List, Dict, Tuple, Set  # pre-3.9 style

def total(prices: List[float]) -> float:
    return sum(prices)
```

**Python 3.9+** lets you use the built-in generics directly — no `typing` import needed:

```python
def total(prices: list[float]) -> float:
    return sum(prices)

def lookup(table: dict[str, int]) -> int:
    ...

def coords() -> tuple[float, float]:
    return (1.0, 2.0)

def unique_ids() -> set[int]:
    ...
```

Use `list[float]`, `dict[str, int]`, `tuple[int, ...]` (variable-length tuple), `set[str]` — this is the modern, preferred style. Only reach for `typing.List` etc. if you're supporting Python < 3.9.

## Optional and Union Types

A value that might be `None`:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    ...  # returns a str, or None if not found
```

`Optional[str]` means "`str` or `None`" — shorthand for `Union[str, None]`.

**Python 3.10+** gives you the `|` syntax, which is now preferred over `Union`/`Optional`:

```python
def find_user(user_id: int) -> str | None:
    ...

def parse(value: int | float | str) -> str:
    ...
```

## Type Aliases

When a type gets long or reused, name it:

```python
type UserId = int          # Python 3.12+ `type` statement
type UserRecord = dict[str, str | int]

def get_user(uid: UserId) -> UserRecord:
    ...
```

Pre-3.12, do the same thing with a plain assignment:

```python
UserId = int
UserRecord = dict[str, "str | int"]
```

## Functions as Values: `Callable`

```python
from typing import Callable

def apply(fn: Callable[[int, int], int], a: int, b: int) -> int:
    return fn(a, b)
```

`Callable[[int, int], int]` reads as "a function taking two ints, returning an int."

## `Any` — the Escape Hatch

```python
from typing import Any

def process(data: Any) -> None:
    ...
```

`Any` tells the type checker "stop checking this." Useful during migration or for genuinely dynamic data, but overusing it defeats the whole point — it's the type-hint equivalent of `# type: ignore` everywhere.

## Type Hints for Classes

```python
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
```

Note the quoted `"Point"` — when a class refers to its own type inside its own body, the class doesn't exist yet at definition time, so you use a **string forward reference**. (With `from __future__ import annotations` at the top of the file, all annotations become strings automatically and you can drop the quotes.)

## `TypedDict` — Typed Dictionaries

For dict-shaped data with known keys (e.g., JSON-like structures):

```python
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float

m: Movie = {"title": "Arrival", "year": 2016, "rating": 8.0}
```

A type checker now verifies every `Movie` has exactly those keys with those types.

## `dataclasses` — Typed, Boilerplate-Free Classes

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
print(p)          # Point(x=1.0, y=2.0)
print(p.x)        # 1.0
```

`@dataclass` auto-generates `__init__`, `__repr__`, and `__eq__` from your type-annotated class attributes. It's the modern replacement for hand-writing simple data-holding classes (Chapter 29). Add `frozen=True` for immutability:

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
p.x = 5.0   # FrozenInstanceError
```

## Running a Type Checker

Type hints do nothing by themselves. Install and run `mypy`:

```bash
pip install mypy
mypy myscript.py
```

```python
def add(a: int, b: int) -> int:
    return a + b

add("2", "3")   # mypy: error — Argument 1 has incompatible type "str"; expected "int"
```

Python itself will happily run `add("2", "3")` (and concatenate the strings) — the type checker is the only thing that catches this before runtime.

## Common Mistakes

- **Thinking type hints are enforced at runtime.** They are not. `def f(x: int): ...` will run just fine if you call `f("hello")`.
- **Over-annotating simple local variables.** `count: int = 0` is noise — the `0` already tells you (and the type checker) it's an `int`. Annotate function signatures; leave obvious locals alone.
- **Mixing `typing.List` and `list[...]` inconsistently** in the same codebase. Pick the modern (`list[...]`) style unless you need to support very old Python.
- **Forgetting `-> None`** on functions that don't return anything meaningful — omitting the return annotation entirely is different from saying "this returns `None`" as far as some checkers are concerned. Be explicit.
- **Using mutable defaults in dataclasses** the same way you'd avoid them in functions (Chapter 21) — `x: list = []` as a dataclass field raises an error; use `field(default_factory=list)`.

## Best Practices

- Annotate public function signatures at minimum — parameters and return type. That's where the value is highest.
- Prefer the modern built-in generics (`list[int]`, `dict[str, int]`) and `|` unions over `typing.List`/`Optional` in any codebase targeting Python 3.10+.
- Run `mypy` (or `pyright`) in CI once your codebase is annotated — hints without enforcement slowly rot.
- Use `dataclass` instead of hand-rolled `__init__`/`__repr__`/`__eq__` for simple data containers.
- Use `Any` sparingly and deliberately — it should be a conscious opt-out, not a default.

## Key Takeaways

- Type hints are optional, non-enforced annotations for humans and tooling, not the interpreter.
- Modern syntax: `list[int]`, `dict[str, int]`, `int | None` (3.9+/3.10+).
- `Callable`, `TypedDict`, and type aliases (`type X = ...`) cover functions, dict-shapes, and reusable names.
- `@dataclass` generates boilerplate (`__init__`, `__repr__`, `__eq__`) from annotated class attributes.
- Type checking requires a separate tool — `mypy` or `pyright` — run as a static analysis step, not at runtime.

## Active Recall

1. Does `def f(x: int) -> int: return x` raise an error if called as `f("a")`? Why or why not?
2. Write a type hint for a function that takes a list of strings and returns a dictionary mapping each string to its length.
3. What's the modern (3.10+) way to say "this parameter accepts an `int` or `None`"?
4. What does `@dataclass` generate for you automatically?
5. Why would you use a string forward reference (`"Point"`) inside the `Point` class itself?

---

# Chapter 38: Regular Expressions (a Practical Primer)

## What & Why

A **regular expression** (regex) is a mini-language for describing *patterns* in text — "a string that starts with three digits, then a dash, then four more digits" rather than one exact string. Python's `re` module lets you search, match, extract, split, and replace text using these patterns.

Regex is not for every string problem — if `"foo" in text` or `text.startswith("foo")` (Chapter 7) solves it, use that; it's faster and more readable. Reach for regex when the thing you're matching has *structure* but not a *fixed* value: emails, phone numbers, log lines, URLs, IDs with a known shape.

## Mental Model

A regex pattern is a tiny program that walks through your string character by character, trying to match its rules. `\d+` doesn't mean a specific number — it means "one or more digit characters, whatever they are." You're describing shape, not content.

## The `re` Module — Core Functions

```python
import re

text = "My phone number is 555-1234."

re.search(r"\d{3}-\d{4}", text)   # Match object if found anywhere, else None
re.match(r"\d{3}-\d{4}", text)    # Only checks from the START of the string
re.findall(r"\d{3}-\d{4}", text)  # List of all non-overlapping matches
re.sub(r"\d{3}-\d{4}", "XXX-XXXX", text)  # Replace all matches
```

The `r` prefix makes it a **raw string** — backslashes are taken literally instead of being interpreted as escape sequences. Always use `r"..."` for regex patterns; without it, `"\d"` might not mean what you think.

## Pattern Syntax Cheat Sheet

| Pattern  | Meaning                                      |
| -------- | -------------------------------------------- |
| `.`      | any character except newline                 |
| `\d`     | any digit (`0-9`)                            |
| `\D`     | any non-digit                                |
| `\w`     | word character (letters, digits, underscore) |
| `\W`     | non-word character                           |
| `\s`     | whitespace (space, tab, newline)             |
| `\S`     | non-whitespace                               |
| `^`      | start of string                              |
| `$`      | end of string                                |
| `*`      | 0 or more of the preceding                   |
| `+`      | 1 or more of the preceding                   |
| `?`      | 0 or 1 of the preceding (optional)           |
| `{n}`    | exactly n                                    |
| `{n,m}`  | between n and m                              |
| `[abc]`  | any one of a, b, c                           |
| `[^abc]` | any character NOT a, b, c                    |
| `[a-z]`  | any character in range a to z                |
| `(...)`  | a group (captures the match)                 |
| `\|`     | alternation ("or")                           |

## Working with Match Objects

```python
match = re.search(r"(\d{3})-(\d{4})", "call 555-1234 now")
if match:
    print(match.group())     # '555-1234'  (the whole match)
    print(match.group(1))    # '555'       (first group)
    print(match.group(2))    # '1234'      (second group)
    print(match.span())      # (5, 13)     (start, end indices)
```

Always check `if match:` before calling `.group()` — a failed search returns `None`, and calling `.group()` on `None` raises `AttributeError`.

## Named Groups

```python
match = re.search(r"(?P<area>\d{3})-(?P<number>\d{4})", "555-1234")
print(match.group("area"))    # '555'
print(match.group("number"))  # '1234'
```

Named groups make code that extracts multiple pieces far more readable than positional `group(1)`, `group(2)`.

## `findall` vs. `finditer`

```python
text = "cats: 3, dogs: 5, birds: 2"

re.findall(r"\d+", text)          # ['3', '5', '2']  -- just the strings

for m in re.finditer(r"\d+", text):
    print(m.group(), m.span())    # each match AND its position
```

Use `findall` when you just want the values; `finditer` when you also need position or want to process one match at a time without building the full list in memory.

## Splitting and Substituting

```python
re.split(r"\s*,\s*", "a, b,  c ,d")   # ['a', 'b', 'c', 'd']

re.sub(r"\s+", " ", "too    many   spaces")   # 'too many spaces'

# using a function as the replacement
re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "a1 b22 c3")
# 'a2 b44 c6'
```

## Compiling Patterns

If you reuse the same pattern many times (e.g., inside a loop), compile it once:

```python
phone_pattern = re.compile(r"\d{3}-\d{4}")

for line in lines:
    if phone_pattern.search(line):
        ...
```

`re.compile` pre-processes the pattern so repeated use is faster, and it lets you name the pattern for readability.

## Common Real-World Patterns

```python
EMAIL   = r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}"
URL     = r"https?://[^\s]+"
DIGITS_ONLY = r"^\d+$"
WHITESPACE_TRIM = r"^\s+|\s+$"
```

These are starting points, not bulletproof validators — real email/URL validation is famously messy. For anything user-facing and important (like actually validating an email before sending mail), use a dedicated library, not a hand-rolled regex.

## Common Mistakes

- **Forgetting the `r` prefix.** `"\d"` and `r"\d"` can behave differently because `\d` isn't a recognized Python escape sequence (you'll usually get a `DeprecationWarning`), while `\n` or `\t` without `r` get silently interpreted as newline/tab.
- **Using `match` when you meant `search`.** `re.match` only checks the *beginning* of the string; if your pattern could appear anywhere, use `re.search`.
- **Not checking for `None`** before calling `.group()`.
- **Greedy quantifiers grabbing too much.** `<.+>` on `"<a><b>"` matches the whole thing (`<a><b>`), not just `<a>`, because `+` is greedy by default. Use `<.+?>` (the `?` makes it non-greedy / lazy) to match as little as possible instead.
- **Reaching for regex for simple substring checks.** `"@" in email` is often enough; don't regex-ify everything.

## Best Practices

- Always use raw strings (`r"..."`) for patterns.
- Compile patterns you reuse.
- Use named groups (`(?P<name>...)`) for multi-part extractions — it documents itself.
- Test patterns against edge cases (empty string, no match, multiple matches) before trusting them in production.
- For anything beyond "does this loosely look right," don't hand-roll email/URL/phone validation regexes — use a library or a proper API.

## Key Takeaways

- `re.search`, `re.match`, `re.findall`, `re.finditer`, `re.sub`, `re.split` are the core toolbox.
- Always use raw strings for patterns.
- `\d \w \s` (and their uppercase negations) plus `* + ? {n,m}` quantifiers cover most patterns you'll need.
- Match objects need a `None` check before you call `.group()`.
- Compile patterns you'll reuse with `re.compile`.

## Active Recall

1. Why should regex patterns always be written as raw strings?
2. What's the difference between `re.match` and `re.search`?
3. Write a regex that matches a string made entirely of digits, from start to end.
4. What does the `?` do after a quantifier like `+` or `*` (e.g., `.+?`)?
5. When would you prefer `re.finditer` over `re.findall`?

---
---

# Part IX — The Ecosystem

Everything up to this point has been the language itself. This final part zooms out: how do you find and use code other people wrote, how do you keep projects isolated from each other, and how do you make sure the code you write *looks* like Python instead of like a translation from another language you learned first.

---

# Chapter 39: The Standard Library Tour

## What & Why

Python ships with a **standard library** — a huge collection of modules that come installed with every Python interpreter, no `pip install` required. The community's unofficial motto is "batteries included." Before reaching for a third-party package, check whether the standard library already solves your problem — it usually does, for common tasks.

This chapter is a map, not an exhaustive manual. The goal is that when a problem shows up, you recognize "oh, that's a `pathlib` problem" or "that's what `itertools` is for," and go read the docs for that specific module.

## Mental Model

Think of the standard library as a toolbox that came with the house. You don't need to buy a wrench for basic plumbing — there's already one in the drawer. Learn what's in the drawer before you go shopping.

## `os` and `pathlib` — Filesystem and OS Interaction

```python
import os
os.getcwd()               # current working directory
os.listdir(".")           # files in a directory
os.environ["HOME"]        # environment variables
os.path.join("a", "b")    # 'a/b' (OS-correct path joining)
```

`pathlib` (modern, object-oriented alternative) is generally preferred:

```python
from pathlib import Path

p = Path("data") / "file.csv"    # path joining with /
p.exists()
p.is_file()
p.suffix                          # '.csv'
p.stem                            # 'file'
p.parent                          # Path('data')
for file in Path(".").glob("*.py"):
    print(file)
```

## `sys` — Interpreter and Runtime Info

```python
import sys
sys.argv          # command-line arguments
sys.exit(1)       # exit the program with a status code
sys.version       # Python version string
```

## `datetime` — Dates and Times

```python
from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)

now.strftime("%Y-%m-%d %H:%M")     # format as string
datetime.strptime("2026-07-02", "%Y-%m-%d")  # parse a string
```

## `collections` — Specialized Containers

```python
from collections import Counter, defaultdict, namedtuple, deque

Counter("mississippi")             # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

d = defaultdict(list)
d["missing_key"].append(1)         # no KeyError — auto-creates []

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)                    # p.x == 1, p.y == 2

dq = deque([1, 2, 3])
dq.appendleft(0)                   # efficient append/pop from both ends
```

`Counter` is one of the most underused stdlib tools — anytime you're tallying occurrences, reach for it instead of a manual dict-counting loop.

## `itertools` — Iterator Building Blocks

```python
from itertools import chain, combinations, permutations, product, count, cycle

list(chain([1, 2], [3, 4]))              # [1, 2, 3, 4]
list(combinations([1, 2, 3], 2))         # [(1,2), (1,3), (2,3)]
list(permutations([1, 2], 2))            # [(1,2), (2,1)]
list(product([1, 2], ["a", "b"]))        # [(1,'a'), (1,'b'), (2,'a'), (2,'b')]
```

`itertools` pairs naturally with generators (Chapter 34) — most of it returns lazy iterators, not lists.

## `functools` — Function Tools

```python
from functools import reduce, lru_cache, partial

reduce(lambda a, b: a + b, [1, 2, 3, 4])   # 10

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

add_five = partial(lambda a, b: a + b, 5)
add_five(10)   # 15
```

You've already met `functools.wraps` (Chapter 35) and `@dataclass`'s cousin utilities live here too.

## `json` and `csv` — Covered in Chapter 28

Already familiar: `json.load/dump`, `csv.reader/writer`.

## `random` — Randomness

```python
import random
random.random()             # float in [0.0, 1.0)
random.randint(1, 6)        # int in [1, 6], inclusive both ends
random.choice(["a", "b"])   # random element
random.shuffle(my_list)     # shuffles in place
```

Not cryptographically secure — for security-sensitive randomness (tokens, passwords), use the `secrets` module instead.

## `re` — Covered in Chapter 38

## `math` and `statistics`

```python
import math
math.sqrt(16)       # 4.0
math.ceil(4.1)      # 5
math.floor(4.9)     # 4
math.pi             # 3.14159...

import statistics
statistics.mean([1, 2, 3, 4])      # 2.5
statistics.median([1, 2, 3, 4])    # 2.5
```

## `subprocess` — Running Other Programs

```python
import subprocess

result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
```

The modern way to shell out from Python; avoid `os.system` in new code.

## `logging` — Real Programs Don't Use `print` for Diagnostics

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting process")
logging.warning("Something looks off")
logging.error("Something failed")
```

`logging` gives you levels, timestamps, and the ability to route output to files — things `print` doesn't.

## `unittest` — Built-in Testing

```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()
```

In practice, most teams use the third-party `pytest` instead (simpler syntax, better output) — but `unittest` needs zero installation and is worth knowing.

## Quick-Reference Table

| Module               | Use it for                                |
| -------------------- | ----------------------------------------- |
| `os`, `pathlib`      | files, directories, paths                 |
| `sys`                | command-line args, interpreter info       |
| `datetime`           | dates, times                              |
| `collections`        | Counter, defaultdict, deque, namedtuple   |
| `itertools`          | combinations, permutations, lazy chaining |
| `functools`          | reduce, caching, partial application      |
| `json`, `csv`        | structured data formats                   |
| `random`, `secrets`  | randomness (general vs. security)         |
| `re`                 | pattern matching in text                  |
| `math`, `statistics` | numeric computation                       |
| `subprocess`         | running shell commands                    |
| `logging`            | structured diagnostic output              |
| `unittest`           | built-in testing framework                |

## Common Mistakes

- **Reaching for a third-party package before checking the standard library.** Counting things? `Counter`. Combos? `itertools`. Dates? `datetime`. Check first.
- **Using `os.path` string-joining when `pathlib` would be cleaner** on new code — both work, but `pathlib` reads better and handles cross-platform separators for you.
- **Using `print` for debugging in code that ships.** Use `logging` so output can be filtered, leveled, and redirected.
- **Using `random` for security-sensitive values** (tokens, password resets). Use `secrets` instead — `random` is predictable given its seed.

## Best Practices

- Skim the standard library's module index once, even briefly — knowing *that something exists* is 90% of using it later.
- Prefer `pathlib` over manual string path manipulation in new code.
- Default to `logging`, not `print`, for anything beyond a quick script.
- When in doubt between writing something yourself and checking the stdlib — check the stdlib first.

## Key Takeaways

- Python's standard library covers files, dates, data structures, iteration, randomness, text patterns, math, subprocesses, logging, and testing — all with zero installs.
- `pathlib`, `collections`, `itertools`, and `functools` are especially high-leverage modules worth knowing well.
- `logging` replaces `print` for real diagnostic output; `secrets` replaces `random` for anything security-related.

## Active Recall

1. What's the difference between `os.path.join` and `pathlib.Path`'s `/` operator, functionally?
2. Which module would you reach for to count occurrences of items in a list without writing a loop?
3. What does `functools.lru_cache` do, and when would you use it?
4. Why is `secrets` preferred over `random` for generating a password-reset token?
5. Name three standard library modules you'd use to build a script that downloads a JSON file, logs its progress, and writes results to a CSV.

---

# Chapter 40: Virtual Environments and `pip`

## What & Why

Real projects depend on third-party packages — code other people wrote and published. `pip` is Python's package installer. But if you install packages globally (system-wide), every project on your machine shares the same set of package versions — and sooner or later, Project A needs `requests==2.20` while Project B needs `requests==2.31`, and you can't have both installed globally at once.

A **virtual environment** (venv) solves this: it's an isolated, self-contained Python installation just for one project, with its own packages, completely separate from your system Python and from every other project's venv.

## Mental Model

Think of your system Python as the shared kitchen in an apartment building — if everyone cooks there, ingredients get mixed up and someone's recipe breaks someone else's. A virtual environment is your own private kitchen for one project: nothing you install there affects anyone else's.

## Creating and Using a Venv (`venv`, built-in)

```bash
# create a venv named .venv in the current folder
python3 -m venv .venv

# activate it
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

# your prompt now shows (.venv) — you're inside the isolated environment
(.venv) $ python --version
(.venv) $ pip install requests

# leave the venv
(.venv) $ deactivate
```

While activated, `python` and `pip` point at the venv's isolated copies, not your system-wide ones. Anything you `pip install` goes into `.venv`, not your global Python.

**Convention:** name the folder `.venv` (dot-prefixed, hidden) and add it to `.gitignore` — never commit a virtual environment to version control. It's regenerable and often gigabytes across a team; what you commit instead is a list of *what* to install.

## `pip` — The Package Installer

```bash
pip install requests               # install the latest version
pip install requests==2.31.0       # install a specific version
pip install "requests>=2.20,<3.0"  # install within a version range
pip uninstall requests
pip list                           # show installed packages
pip show requests                  # details about one package
```

## `requirements.txt` — Recording Dependencies

To let anyone (including future-you) recreate your exact environment:

```bash
pip freeze > requirements.txt
```

This writes every installed package and its exact version to a file:

```
requests==2.31.0
numpy==1.26.4
```

Someone else clones your project and runs:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

...and now they have an identical environment. This file **is** committed to version control — it's the recipe, not the private kitchen.

## Modern Alternative: `uv`

`pip` + `venv` is the standard-library-adjacent baseline every Python developer should know. In practice, many projects now use faster, more ergonomic tools built on the same ideas — `uv` (from Astral) is a popular one, offering drop-in-compatible, much faster installs and built-in project/venv management:

```bash
uv venv                     # create a venv
uv pip install requests     # install into it, much faster than pip
uv add requests             # add + record as a project dependency
```

The concepts are identical — isolation per project, a recorded list of dependencies — just faster tooling on top.

## Where Packages Come From: PyPI

`pip install X` fetches `X` from the **Python Package Index** (PyPI, pypi.org) — the central public repository for Python packages, analogous to npm for JavaScript or crates.io for Rust. Anyone can publish a package there; always check a package's popularity, maintenance status, and source before trusting it in a real project.

## Common Mistakes

- **Installing packages globally, then wondering why Project B broke when you upgraded something for Project A.** Always work inside a venv.
- **Forgetting to activate the venv** before running `pip install` — you'll silently install into the system Python instead.
- **Committing `.venv/` to git.** It's large, platform-specific, and regenerable — commit `requirements.txt` instead, never the venv folder itself.
- **Never pinning versions.** `pip freeze > requirements.txt` after installing gives you exact, reproducible versions; a `requirements.txt` with no version numbers can silently install a newer, incompatible package months later.
- **Confusing `pip install X` with `import X`.** The package name on PyPI and the name you `import` aren't always identical (`pip install beautifulsoup4` but `import bs4`) — check the package's docs.

## Best Practices

- One venv per project, always. Never install project dependencies globally.
- Commit `requirements.txt` (or a modern equivalent like `pyproject.toml`); never commit the venv folder itself.
- Pin versions for anything you deploy; loosen them only when you have a good reason.
- Regenerate your venv from `requirements.txt` periodically to make sure it's actually reproducible, not just "works on my machine."

## Key Takeaways

- A virtual environment isolates one project's packages from your system Python and from every other project.
- `python3 -m venv .venv` creates one; `source .venv/bin/activate` enters it; `deactivate` leaves it.
- `pip install`, `pip uninstall`, `pip freeze > requirements.txt`, `pip install -r requirements.txt` cover the day-to-day workflow.
- Commit `requirements.txt`; never commit the `.venv` folder.
- Faster modern tools like `uv` implement the same core ideas with better ergonomics.

## Active Recall

1. Why shouldn't you `pip install` packages globally for every project?
2. What command creates a virtual environment named `.venv`?
3. What's the difference between `requirements.txt` and the `.venv` folder — which do you commit to git, and why?
4. What does `pip freeze` do, and when would you run it?
5. If a teammate clones your repo, what two commands do they need to run to get an identical environment (assuming they already have the venv created and activated)?

---

# Chapter 41: Pythonic Style, Idioms, and Common Pitfalls

## What & Why

You now know the language. This final chapter is about *taste* — writing code that looks like it was written by someone fluent in Python, not by someone translating from another language they learned first. This is what "Pythonic" means: idiomatic, readable, using the language's own tools instead of fighting them.

## The Zen of Python

Type this into any Python REPL:

```python
>>> import this
```

You'll get a short poem — Python's own design philosophy, written by Tim Peters. A few of its most load-bearing lines: "Explicit is better than implicit." "Simple is better than complex." "Readability counts." "There should be one — and preferably only one — obvious way to do it." Every idiom below is really just these principles applied to a specific situation.

## Idiom: Iterate Directly, Don't Index

```python
# Not Pythonic
for i in range(len(items)):
    print(items[i])

# Pythonic
for item in items:
    print(item)

# Need the index too? enumerate, not manual counting.
for i, item in enumerate(items):
    print(i, item)
```

## Idiom: Unpacking Instead of Indexing

```python
# Not Pythonic
point = (3, 4)
x = point[0]
y = point[1]

# Pythonic
x, y = point
```

## Idiom: `in` for Membership, Never Manual Loops

```python
# Not Pythonic
found = False
for item in items:
    if item == target:
        found = True
        break

# Pythonic
found = target in items
```

## Idiom: EAFP over LBYL

**EAFP** — "Easier to Ask Forgiveness than Permission" — is the Pythonic default over **LBYL** — "Look Before You Leap":

```python
# LBYL (not Pythonic, and has a race condition)
if key in my_dict:
    value = my_dict[key]
else:
    value = default

# EAFP (Pythonic)
try:
    value = my_dict[key]
except KeyError:
    value = default

# ...though for this exact case, .get() beats both:
value = my_dict.get(key, default)
```

Python favors trying the operation and catching the exception over checking every precondition first — it's usually shorter, and it avoids race conditions where the condition changes between the check and the use.

## Idiom: Comprehensions over Manual Accumulation

```python
# Not Pythonic
squares = []
for n in range(10):
    if n % 2 == 0:
        squares.append(n ** 2)

# Pythonic
squares = [n ** 2 for n in range(10) if n % 2 == 0]
```

(Chapter 19.) Don't take this too far, though — a comprehension that needs three lines and two nested conditions to read is no longer more Pythonic than a plain loop; "readability counts" outranks "always comprehend."

## Idiom: Context Managers for Resources

```python
# Not Pythonic
f = open("data.txt")
data = f.read()
f.close()

# Pythonic
with open("data.txt") as f:
    data = f.read()
```

## Idiom: `is` for `None`, `==` for Values

```python
if x is None:      # correct
if x == None:       # works, but not idiomatic — is is for identity checks
```

`None` is a singleton (Chapter 5) — `is` is both faster and clearer about intent.

## Idiom: f-strings over `.format()` or `%`

```python
name = "Sid"
# Not Pythonic (in modern code)
"Hello, %s" % name
"Hello, {}".format(name)

# Pythonic
f"Hello, {name}"
```

## Idiom: Truthiness — Don't Over-Compare

```python
# Not Pythonic
if len(my_list) > 0:
if my_string != "":
if my_bool == True:

# Pythonic
if my_list:
if my_string:
if my_bool:
```

(Chapter 4.) Empty collections, empty strings, `0`, and `None` are already falsy — no need to spell out the comparison.

## Naming Conventions (PEP 8)

| What                      | Convention                | Example                     |
| ------------------------- | ------------------------- | --------------------------- |
| Variables, functions      | `snake_case`              | `total_price`, `get_user()` |
| Constants                 | `UPPER_SNAKE_CASE`        | `MAX_RETRIES`               |
| Classes                   | `PascalCase`              | `UserAccount`               |
| "Private" (by convention) | leading underscore        | `_internal_helper`          |
| "Really don't touch this" | double leading underscore | `__mangled_name`            |
| Modules/packages          | short, lowercase          | `utils`, `mypackage`        |

Python has no true "private" — leading underscores are a social contract (Chapter 31), not enforcement.

## Common Pitfalls (Traps Every Beginner Hits)

**Mutable default arguments:**
```python
def add_item(item, bucket=[]):   # DANGER — the same list is reused every call!
    bucket.append(item)
    return bucket

def add_item(item, bucket=None):  # correct
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

**Modifying a list while iterating over it:**
```python
for item in my_list:
    if should_remove(item):
        my_list.remove(item)   # skips elements, corrupts iteration

# Correct: iterate over a copy, or build a new list
my_list = [item for item in my_list if not should_remove(item)]
```

**Late binding in closures/loops:**
```python
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]   # [2, 2, 2] -- NOT [0, 1, 2]

# Fix: default-argument trick to capture the value at creation time
funcs = [lambda i=i: i for i in range(3)]
[f() for f in funcs]   # [0, 1, 2]
```

**Shadowing built-ins:**
```python
list = [1, 2, 3]    # now list() the built-in is unreachable in this scope!
str = "hello"        # same problem
```

Avoid naming variables `list`, `dict`, `str`, `type`, `id`, `input`, etc.

**Comparing floats with `==`:**
```python
0.1 + 0.2 == 0.3          # False! floating point precision
abs((0.1 + 0.2) - 0.3) < 1e-9   # correct way to compare floats
```

**Chained `and`/`or` where a comprehension or `any`/`all` would be clearer:**
```python
# Not Pythonic
result = x is not None and x > 0 and x < 100

# Pythonic, when checking a collection
all(0 < x < 100 for x in values)
```

## A Note on `if __name__ == "__main__":`

You've seen this pattern throughout the book. Every `.py` file gets a special `__name__` variable — Python sets it to `"__main__"` when the file is run directly, or to the module's name when it's imported elsewhere. Gating your "run this script" code behind this check means the file works both as a standalone script *and* as an importable module without side effects on import:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

## Common Mistakes

- **Writing Java/C-style code in Python** — manual index loops, verbose getter/setter boilerplate, over-engineered class hierarchies for simple data.
- **Ignoring PEP 8** naming and formatting conventions, making code harder for other Python developers to read at a glance.
- **Premature abstraction** — building a class hierarchy or plugin system for a script that will be run twice.
- **Not running a linter/formatter.** Tools like `ruff`, `black`, and `flake8` catch most of the pitfalls in this chapter automatically — use them.

## Best Practices

- Run a formatter (`black`) and a linter (`ruff` or `flake8`) on every project — they enforce most of PEP 8 and catch many of the pitfalls above for free.
- Read other people's well-regarded Python code (standard library source, popular open-source projects) to internalize idiom by exposure.
- When something feels verbose, ask "does Python already have a shorter way to say this?" — it usually does.
- Prefer clarity over cleverness. A comprehension that needs a comment to explain it should probably be a loop.

## Key Takeaways

- "Pythonic" means idiomatic: using the language's own tools (`in`, unpacking, comprehensions, context managers, EAFP) instead of manually reimplementing them.
- PEP 8 naming conventions (`snake_case` for functions/variables, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants) are the community standard.
- Mutable default arguments, floating-point equality, late-binding closures, and shadowing built-ins are the classic beginner traps — now you know them by name.
- `if __name__ == "__main__":` lets a file work as both a script and an importable module.
- Linters and formatters (`ruff`, `black`) enforce most of this automatically — use them from day one.

## Active Recall

1. Why is `def f(items=[]):` dangerous as a function signature?
2. What does EAFP stand for, and give an example of EAFP vs. LBYL for dictionary access.
3. Why does `0.1 + 0.2 == 0.3` evaluate to `False`?
4. What's wrong with naming a variable `list` or `dict`?
5. What does `if __name__ == "__main__":` actually check, and why does it matter?

---
---

# Appendices

---

# Appendix A: Operator Precedence Table

From highest to lowest precedence (operators higher in the table bind tighter):

| Precedence  | Operator(s)                                                      | Description                                                 |
| ----------- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| 1 (highest) | `()`                                                             | Parentheses (grouping)                                      |
| 2           | `**`                                                             | Exponentiation (right-associative: `2**3**2` = `2**(3**2)`) |
| 3           | `+x`, `-x`, `~x`                                                 | Unary positive, negative, bitwise NOT                       |
| 4           | `*`, `/`, `//`, `%`                                              | Multiplication, division, floor division, modulo            |
| 5           | `+`, `-`                                                         | Addition, subtraction                                       |
| 6           | `<<`, `>>`                                                       | Bitwise shifts                                              |
| 7           | `&`                                                              | Bitwise AND                                                 |
| 8           | `^`                                                              | Bitwise XOR                                                 |
| 9           | `\|`                                                             | Bitwise OR                                                  |
| 10          | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons and membership                                  |
| 11          | `not x`                                                          | Boolean NOT                                                 |
| 12          | `and`                                                            | Boolean AND                                                 |
| 13          | `or`                                                             | Boolean OR                                                  |
| 14          | `if / else`                                                      | Conditional expression (ternary)                            |
| 15          | `lambda`                                                         | Lambda expression                                           |
| 16 (lowest) | `=`, `+=`, `-=`, etc.                                            | Assignment (technically a statement, not an expression)     |

**Rule of thumb:** when in doubt, use parentheses. Nobody loses points for `(a and b) or c` being "unnecessarily" explicit — they lose time debugging `a and b or c` when it doesn't do what they expected.

---

# Appendix B: Reserved Keywords

These 35 words are reserved by Python — you cannot use them as variable, function, or class names.

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

**Soft keywords** (only special in specific contexts, usable as names elsewhere): `match`, `case`, `_`, `type`.

---

# Appendix C: String Methods Cheat Sheet

| Method                              | What it does                                       |
| ----------------------------------- | -------------------------------------------------- |
| `s.upper()`                         | uppercase copy                                     |
| `s.lower()`                         | lowercase copy                                     |
| `s.title()`                         | Title Case Copy                                    |
| `s.capitalize()`                    | Capitalize just the first character                |
| `s.strip()`                         | remove leading/trailing whitespace                 |
| `s.lstrip()` / `s.rstrip()`         | strip from left / right only                       |
| `s.split(sep)`                      | split into a list on `sep` (default: whitespace)   |
| `s.rsplit(sep, n)`                  | split from the right, at most `n` times            |
| `s.join(iterable)`                  | join elements of `iterable` using `s` as separator |
| `s.replace(old, new)`               | replace all occurrences                            |
| `s.find(sub)`                       | index of first occurrence, or `-1` if not found    |
| `s.index(sub)`                      | like `find`, but raises `ValueError` if not found  |
| `s.startswith(sub)`                 | `True`/`False`                                     |
| `s.endswith(sub)`                   | `True`/`False`                                     |
| `s.count(sub)`                      | number of non-overlapping occurrences              |
| `s.isalpha()`                       | `True` if all characters are letters               |
| `s.isdigit()`                       | `True` if all characters are digits                |
| `s.isalnum()`                       | `True` if all characters are letters or digits     |
| `s.isspace()`                       | `True` if all characters are whitespace            |
| `s.isupper()` / `s.islower()`       | case checks                                        |
| `s.zfill(width)`                    | pad with leading zeros to `width`                  |
| `s.center(width)`                   | center-pad with spaces to `width`                  |
| `s.ljust(width)` / `s.rjust(width)` | left/right-align, pad to `width`                   |
| `s.format(...)`                     | old-style formatting (prefer f-strings)            |
| `f"{value}"`                        | f-string interpolation (preferred)                 |

---

# Appendix D: List/Dict/Set Methods Cheat Sheet

## List

| Method                              | What it does                                                   |
| ----------------------------------- | -------------------------------------------------------------- |
| `lst.append(x)`                     | add `x` to the end                                             |
| `lst.extend(iterable)`              | append every item from `iterable`                              |
| `lst.insert(i, x)`                  | insert `x` at index `i`                                        |
| `lst.remove(x)`                     | remove first occurrence of `x` (raises `ValueError` if absent) |
| `lst.pop(i=-1)`                     | remove and return item at index `i` (default: last)            |
| `lst.clear()`                       | remove all items                                               |
| `lst.index(x)`                      | index of first occurrence of `x`                               |
| `lst.count(x)`                      | number of occurrences of `x`                                   |
| `lst.sort(key=None, reverse=False)` | sort in place                                                  |
| `lst.reverse()`                     | reverse in place                                               |
| `lst.copy()`                        | shallow copy                                                   |
| `sorted(lst)`                       | return a new sorted list (doesn't mutate)                      |

## Dict

| Method                       | What it does                                             |
| ---------------------------- | -------------------------------------------------------- |
| `d.get(key, default)`        | value at `key`, or `default` if missing (never raises)   |
| `d.keys()`                   | view of all keys                                         |
| `d.values()`                 | view of all values                                       |
| `d.items()`                  | view of `(key, value)` pairs                             |
| `d.pop(key, default)`        | remove and return value at `key`                         |
| `d.setdefault(key, default)` | value at `key`, setting it to `default` first if missing |
| `d.update(other)`            | merge another dict/iterable of pairs into `d`            |
| `d.clear()`                  | remove all items                                         |
| `key in d`                   | membership check on keys                                 |

## Set

| Method                                    | What it does                                  |
| ----------------------------------------- | --------------------------------------------- |
| `s.add(x)`                                | add element `x`                               |
| `s.remove(x)`                             | remove `x` (raises `KeyError` if absent)      |
| `s.discard(x)`                            | remove `x` if present, no error if absent     |
| `s.pop()`                                 | remove and return an arbitrary element        |
| `s1.union(s2)` / `s1 \| s2`               | all elements in either set                    |
| `s1.intersection(s2)` / `s1 & s2`         | elements in both sets                         |
| `s1.difference(s2)` / `s1 - s2`           | elements in `s1` but not `s2`                 |
| `s1.symmetric_difference(s2)` / `s1 ^ s2` | elements in exactly one of the sets           |
| `s1.issubset(s2)` / `s1 <= s2`            | `True` if every element of `s1` is in `s2`    |
| `s1.issuperset(s2)` / `s1 >= s2`          | `True` if `s1` contains every element of `s2` |

---

# Appendix E: Dunder Methods Reference

| Dunder                                                                    | Triggered by                              | Purpose                                                      |
| ------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------ |
| `__init__(self, ...)`                                                     | `ClassName(...)`                          | Initialize a new instance                                    |
| `__new__(cls, ...)`                                                       | `ClassName(...)` (before `__init__`)      | Create the instance itself (rarely overridden)               |
| `__repr__(self)`                                                          | `repr(obj)`, REPL echo                    | Unambiguous, developer-facing string                         |
| `__str__(self)`                                                           | `str(obj)`, `print(obj)`                  | Readable, user-facing string                                 |
| `__eq__(self, other)`                                                     | `obj == other`                            | Equality comparison                                          |
| `__ne__(self, other)`                                                     | `obj != other`                            | Inequality (usually auto-derived from `__eq__`)              |
| `__lt__`, `__le__`, `__gt__`, `__ge__`                                    | `<`, `<=`, `>`, `>=`                      | Ordering comparisons                                         |
| `__hash__(self)`                                                          | `hash(obj)`, use as dict key / set member | Must be consistent with `__eq__`                             |
| `__len__(self)`                                                           | `len(obj)`                                | Length                                                       |
| `__getitem__(self, key)`                                                  | `obj[key]`                                | Indexing / subscripting                                      |
| `__setitem__(self, key, value)`                                           | `obj[key] = value`                        | Assign via subscript                                         |
| `__delitem__(self, key)`                                                  | `del obj[key]`                            | Delete via subscript                                         |
| `__contains__(self, item)`                                                | `item in obj`                             | Membership test                                              |
| `__iter__(self)`                                                          | `for x in obj`, `iter(obj)`               | Return an iterator                                           |
| `__next__(self)`                                                          | `next(obj)`                               | Produce the next value (on an iterator)                      |
| `__call__(self, ...)`                                                     | `obj(...)`                                | Make an instance callable like a function                    |
| `__enter__(self)` / `__exit__(self, *exc)`                                | `with obj:`                               | Context manager protocol                                     |
| `__add__(self, other)`                                                    | `obj + other`                             | Addition (and `__radd__`, `__iadd__` for reflected/in-place) |
| `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__` | `-`, `*`, `/`, `//`, `%`, `**`            | Arithmetic operators                                         |
| `__bool__(self)`                                                          | `bool(obj)`, truthiness checks            | Truthy/falsy evaluation                                      |
| `__format__(self, spec)`                                                  | `f"{obj:spec}"`, `format(obj, spec)`      | Custom format-spec handling                                  |
| `__del__(self)`                                                           | object garbage collection                 | Cleanup (rarely needed; unpredictable timing)                |

**Rule of thumb:** implement `__repr__` on almost every class you write — it's the single highest-leverage dunder for debugging. Add `__eq__`/`__hash__`, `__lt__` etc., `__len__`/`__getitem__`/`__iter__`, or `__enter__`/`__exit__` only when your object actually needs to behave like a value, a collection, or a resource, respectively.
