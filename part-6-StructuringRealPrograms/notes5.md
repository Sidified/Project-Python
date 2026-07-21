# Part VI — Structuring Real Programs

## What this part covered

- **Modules, packages, `import`:** how to split code across files. `import x`, `from x import y`, `import x as z`. Modules are just `.py` files; packages are folders with `__init__.py` (implicit-namespace packages don't need it in modern Python but explicit is safer).
- **Exceptions:** `try / except / else / finally`. `raise` to throw. Custom exceptions inherit from `Exception`. `raise NewError(...) from e` chains the traceback, which matters for debugging.
- **Rules I now treat as non-negotiable:**
  - Never write bare `except:` — it catches `KeyboardInterrupt` and `SystemExit` too.
  - Always use `with open(...)` for file I/O — never manual `open()` + `close()`.
  - Never silently swallow (`except: pass`). Log, re-raise, or return a sentinel.
- **File I/O:** modes `"r"`, `"w"`, `"a"`, `"rb"`/`"wb"`. Reading line-by-line with a `for` loop over the file object is memory-safe on huge files. `.readlines()` loads everything into memory — avoid on large files.
- **JSON:** `json.dump(obj, file)` and `json.load(file)` for files; `json.dumps(obj)` and `json.loads(str)` for strings. `indent=2` for human-readable output. Only serializes native Python types (dicts, lists, strings, ints, floats, bools, None) — no tuples or custom objects without a custom encoder.
- **JSONL:** one JSON object per line. Standard format for LLM training data, inference logs, and streaming datasets. Read line-by-line with `json.loads(line)` inside a `try/except`.
- **CSV:** `csv.reader` and `csv.writer` for lists-of-lists; `csv.DictReader` and `csv.DictWriter` for lists-of-dicts. Always open with `newline=""` on write to avoid extra blank lines on Windows. CSV has no types — everything comes back as strings, coerce them yourself.

## What I built

- Corpus file round-trip: write 10 sentences, read them back, compute line/word stats
- `validate_prompt` with a custom `InvalidPromptError` — the shape of input validation for every LLM API call
- `load_config` distinguishing three failure modes cleanly (missing file, invalid JSON, missing required keys) with a custom `ConfigError`
- `read_jsonl` tolerant of malformed and empty lines — real datasets have bad lines
- CSV → JSON converter with explicit type coercion and a documented fail-fast choice on malformed rows
- `retry(fn, max_attempts, on_exception)` — passing a function as an argument, using a closure-style mutable counter to simulate transient failures, re-raising on final attempt
- Mini experiment tracker: base config → merged experiment configs (without mutating base) → simulated training logs written as JSONL → read back → aggregated per experiment → written to summary CSV

## What I got wrong / worth remembering

- **`raise "some string"` is a TypeError in Python 3.** Must raise an `Exception` instance. Latent bug — invisible until the except branch actually fires.
- **Hardcoding per-item logic doesn't generalize.** Third time this pattern has bitten (Part IV BOSS, Part VI BOSS write step, Part VI BOSS aggregation). Any time I find myself writing `if x == 'A' ... elif x == 'B' ... elif x == 'C' ...`, that's the signal to use a dict-of-lists or a loop over `.items()`.
- **Round-tripping through disk is not decorative.** If I aggregate from the in-memory data I built *before* writing to disk, a bug in the write step is invisible. Read back what I wrote; use *that*.
- **Assertions must be derived from the spec, not from what the code produces.** Rewriting Assertion 2 from `{"Experiment_A", ...}` (matching my rename) to `{exp["name"] for exp in experiments}` (matching the source) is the difference between real verification and theater. If the assertion doesn't fail when the code is wrong, the assertion is worthless.
- **`raise NewError(...) from e`** preserves the original traceback, which is the difference between "I know something went wrong" and "I can see exactly what went wrong."
- **stderr vs stdout:** warnings and errors go to `stderr` (`print(..., file=sys.stderr)`). Stdout is for the program's intended output — different pipelines redirect them differently.
- **Loop variables at module scope rebind the module-level name.** `for item in ...:` after `item = {...}` overwrites the earlier `item`. Rename loop variables to avoid this.

## Patterns worth internalizing

- **Custom exceptions for domain errors** (`InvalidPromptError`, `ConfigError`) — lets callers handle validation errors differently from network errors.
- **Try/except at boundaries only** — where the program touches the outside world (file I/O, JSON parsing, network calls, user input). Not in the middle of pure computation.
- **Fail-fast OR skip-and-warn on bad data** — both are valid; make the choice deliberately and document it in a comment.
- **`read_jsonl` pattern**: iterate line-by-line, `try/except json.JSONDecodeError` per line, log-and-continue. Every real JSONL loader is shaped like this.
- **Different formats for different jobs:** JSONL for training/inference logs (streaming, append-friendly), JSON for structured configs (nested, one-object-per-file), CSV for tabular summaries (spreadsheet-compatible, flat).
- **Retry logic with exception filtering**: retry only on the specific transient error class the caller expects (`ConnectionError`, `TimeoutError`) — never a blanket `Exception`, or you'll retry logic bugs.