# Part VIII — Advanced Language Features

## What this part covered

- **Iterators and generators.** Iterator protocol (`__iter__`/`__next__`) exists but generators using `yield` cover 95% of what you'd ever build. `yield` pauses execution and resumes on next call. Generators are lazy (produce values on demand) and one-shot (exhausted after full consumption).
- **Lazy evaluation.** `(x*x for x in range(N))` uses constant memory; `[x*x for x in range(N)]` allocates all N values. Matters at scale.
- **Decorators.** `@decorator` is syntactic sugar for `func = decorator(func)`. Basic form takes a function and returns a wrapper. Decorators with arguments need three nested levels. `@functools.wraps` is not optional — without it, the wrapped function loses its `__name__`, `__doc__`, and signature.
- **Context managers.** `with` guarantees cleanup even on exceptions. `@contextmanager` from `contextlib` lets you write context managers as generators — code before `yield` is enter, code after (in `finally`) is exit.
- **Type hints.** Function signatures like `def f(x: int) -> str:`, modern collection syntax `list[int]` / `dict[str, float]`, `str | None` for optionals. Python doesn't enforce these — `mypy`/`pyright` do. Serious modern codebases use them universally.
- **`@dataclass`.** Auto-generates `__init__`, `__repr__`, `__eq__` from typed field declarations. `frozen=True` for immutability. `__post_init__` for validation after construction. `field(default_factory=list)` — never `= []` — to avoid the shared-mutable-default trap in class form.
- **Regex.** Raw strings (`r"..."`), core functions (`search`, `findall`, `sub`), named groups `(?P<name>...)`. Useful for structured text (log lines, PII detection, etc.), overkill for anything a `.split()` can handle.

## What I built

- `chunk(iterable, size)` — generator that batches any iterable, lazy enough to work on `itertools.count()`
- `@timeit` — the shape of every ML training script's per-epoch timer
- `stream_jsonl(path)` — streaming replacement for Part VI's list-based `read_jsonl`. Works on datasets larger than RAM.
- `@retry(max_attempts, on_exception)` — three-level decorator factory. Same logic as Part VI's `retry()` function, restructured as a decorator (which is how every real API client wraps calls).
- `@contextmanager` `random_seed(seed)` — save random state, use a fixed seed, restore on exit. Reproducibility primitive.
- `parse_log_line` — regex with named groups + `re.findall` for key-value fields.
- `LLMConfig` as `@dataclass(frozen=True)` with `__post_init__` validation. About 10 lines; Part VII's equivalent was 30.
- End-to-end inference pipeline: dataclass config → JSONL stream → chunk batches → retry-wrapped LLM call → yielded results. Fully lazy end-to-end.

## What I got wrong / worth remembering

- **Retry logic doesn't guarantee success — it just gives transient failures another chance.** At 30% failure rate with 3 retries, the probability of any single call exhausting retries is 2.7%; across 20 calls, that compounds to ~42% chance of at least one hard failure. Real pipelines handle exhausted retries explicitly (log the failed record, yield an error object, continue) — they don't just crash. Lowering the failure probability made my demo work; production requires actual failure handling.
- **`random.seed(saved_seed)` is not the same as restoring state.** Once you've drawn from the random stream, the position matters. The right way to save/restore is `getstate()`/`setstate()`, which capture the full internal state, not just the seed.
- **`field(default_factory=list)`, never `= []`.** In a dataclass, `= []` triggers the same mutable-default trap as in function arguments — all instances would share the same list. This is the same lesson from Part V, in a different costume.
- **`frozen=True` prevents attribute reassignment, not deep mutation.** Same caveat as Part I's tuple-with-mutable-list. If a `frozen` dataclass has a `list` field, you can still mutate the list contents. Immutable container, mutable content.

## Patterns worth internalizing

- **Stream, don't materialize.** For pipelines, keep everything as generators from the source through to the sink. `list(...)` at any intermediate step defeats the whole point and makes datasets that don't fit in RAM impossible to process.
- **Decorators for cross-cutting concerns** — timing, retry, logging, auth — kept separate from business logic. Reading modern ML code fluently requires reading `@` stacks fluently.
- **`@contextmanager` for acquire/use/release patterns.** Random state, GPU memory, database connections, temporary files. The `try/finally` around `yield` is the important structural bit.
- **`@dataclass(frozen=True)` + `__post_init__` for configs.** Compact, type-checkable, immutable, validated once at construction. Contrast to Part VII's `@property` + setter approach: use dataclass for value-objects/configs, property/setter for classes with runtime-updatable state.
- **Compose small generators into pipelines** rather than writing one big loop. `chunk(stream_jsonl(path), batch_size)` reads naturally and each piece is independently testable.

## Why this matters for AI Engineering

- **Streaming pipelines** are the only way to work with real datasets. Training data files are gigabytes to terabytes; you can't `list()` them.
- **Retry decorators** wrap every real API call to OpenAI, Anthropic, or any inference endpoint. Rate limits, transient network errors, timeouts — the retry decorator is the frontline defense.
- **`@dataclass`** is the shape of every modern config. HuggingFace's `TrainingArguments`, PyTorch Lightning configs, Weights & Biases configs — all dataclasses.
- **Context managers** show up in the ML APIs constantly: `with torch.no_grad():`, `with autocast():`, `with mlflow.start_run():`. Understanding what they *do* (setup/cleanup, guaranteed even on exception) is required literacy.
- **Type hints** — reading HuggingFace, PyTorch, LangChain source is much easier when type signatures are parseable at a glance.
- **Regex** — log parsing, PII redaction, extracting structured info from LLM outputs. Not a daily tool, but non-negotiable functional literacy.