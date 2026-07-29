# Python for AI Engineering — A Self-Directed Learning Journey

> **53 problem sets across 8 parts. Every problem AI-adjacent by design. Honest notes on what broke and how it got fixed.**

This repository documents the foundation phase of my path towards AI Engineering: taking Python from surface-familiarity to real depth, with every problem framed around the shapes you'll see in real AI/ML code — tokenizers, batching, retry decorators, dataclass configs, streaming pipelines, model registries.

This is not a tutorial repo. It is a working record — code, notes, misconceptions, and the corrections that followed.

---

## What This Repo Is (and Isn't)

**Is:**
- A structured, part-by-part working record of Python fundamentals for AI Engineering
- 53 problem sets, each with **verification assertions written from the spec, not from the code's output**
- 8 first-person `notes.md` files documenting what clicked, what didn't, and what got corrected
- Problems deliberately shaped around real AI/ML primitives — no palindromes-for-the-sake-of-palindromes

**Isn't:**
- A tutorial for someone learning Python (this is my learning record, not a curriculum)
- A collection of throwaway toy exercises — every problem was designed to touch a pattern that shows up in real ML code
- A hide-the-mistakes repo — the notes files include the bugs I hit and the misconceptions I had to fix

---

## The 8 Parts

Each part has its own folder. Problem files (`.py`) start with the problem statement as a comment; the solution follows. Every part ends with a `notesN.md` written after finishing the problem set.

| Part | Focus | Problems | Notes |
|------|------------------------------------------------------|:--------:|:-----:|
| [Part I](./part-1-Foundations/)                              | Foundations — memory model, mutability, reference semantics                    | 0 (concept-only) | [notes1.md](./part-1-Foundations/notes1.md) |
| [Part II](./part-2-TheBuilt-inTypes/)                        | Built-in types — numbers, strings, f-strings, I/O                              | 6                 | [notes2.md](./part-2-TheBuilt-inTypes/notes2.md) |
| [Part III](./part-3-Control-Flow/)                           | Control flow — conditionals, loops, `break`/`continue`, for-else               | 7                 | [notes3.md](./part-3-Control-Flow/notes3.md) |
| [Part IV](./part-4-Collections/)                             | Collections — lists, dicts, sets, iteration helpers, comprehensions            | 10                | [notes4.md](./part-4-Collections/notes4.md) |
| [Part V](./part-5-Functions/)                                | Functions — args, scope, closures, recursion, lambdas                          | 8                 | [notes5.md](./part-5-Functions/notes5.md) |
| [Part VI](./part-6-StructuringRealPrograms/)                 | Modules, exceptions, file I/O, JSON, CSV                                       | 7                 | [notes6.md](./part-6-StructuringRealPrograms/notes6.md) |
| [Part VII](./part-7-Object-OrientedProgramming/)             | OOP — classes, inheritance, dunders, properties, ABCs                          | 7                 | [notes7.md](./part-7-Object-OrientedProgramming/notes7.md) |
| [Part VIII](./part-8-AdvancedLanguageFeatures/)              | Generators, decorators, context managers, dataclasses, type hints, regex       | 8                 | [notes8.md](./part-8-AdvancedLanguageFeatures/notes8.md) |

Part I has no code because the honest test for reference semantics is predict-then-explain on snippets, not a fabricated build. Everything after Part II earns real problems.

The conceptual material for every part is in [`PythonBook.md`](./PythonBook.md) at the repo root — refer to it for the underlying concepts behind any problem in this repository.

---

## Selected Highlights

If you want to see the shape of the work without reading all 53 problems, these are the most representative:

- **[Mini Tokenizer with Encode/Decode Round-Trip](./part-4-Collections/practice-projects-part4/8_MiniTokenizer+ReverseLookup.py)** — build vocabulary from a corpus, encode sentences to IDs, decode back to text, verify the round-trip. Core of every real tokenizer (HuggingFace, sentencepiece, tiktoken).
- **[Log Analyzer (Boss Problem)](./part-4-Collections/practice-projects-part4/10_LogAnalyzer.py)** — parse structured training logs, group by experiment, compute per-experiment stats (final loss, best loss, avg accuracy). The skeleton of a mini experiment tracker.
- **[Config Merger with Immutability Guarantee](./part-4-Collections/practice-projects-part4/9_ConfigMergerWithImmutabilityGuarantee.py)** — produce per-experiment configs without mutating the base. The bug that causes "why do all my runs have the same hyperparameters."
- **[Function Composition Pipeline](./part-5-Functions/practice-projects-part5/8_FunctionCompositionPipeline.py)** — `make_pipeline(*steps)` returning a composed callable. The core idea underneath `sklearn.Pipeline`, LangChain runnables, and HuggingFace transforms.
- **[Robust JSON Config Loader](./part-6-StructuringRealPrograms/practice-projects-part6/3_RobustJSONConfigLoader.py)** — three distinct failure modes (file missing, malformed JSON, missing required keys), each with a distinct error message. The shape of config loading in every real ML codebase.
- **[Mini Experiment Tracker (Boss Problem)](./part-6-StructuringRealPrograms/practice-projects-part6/7_MiniExperimentTracker.py)** — full end-to-end pipeline: base config → merged experiments → simulated training → JSONL logs → aggregated CSV summary. Every piece can fail; error handling matters.
- **[Dataset Class](./part-7-Object-OrientedProgramming/practice-projects-part7/6_DatasetClass.py)** — implements `__len__`, `__getitem__` (with slice support), `__iter__`, and `filter(predicate)`. Exactly the interface PyTorch's `Dataset` requires.
- **[Model Registry with ABC + Polymorphism (Boss Problem)](./part-7-Object-OrientedProgramming/practice-projects-part7/7_ModelRegistryWithABCAndPolymorphism.py)** — abstract base class, concrete implementations, polymorphic iteration. Same skeleton as HuggingFace's model registry and MLflow's model store.
- **[Instrumented Streaming Pipeline (Boss Problem)](./part-8-AdvancedLanguageFeatures/practice-projects-part8/8_InstrumentedStreamingPipeline.py)** — end-to-end lazy pipeline: `@dataclass(frozen=True)` config → JSONL stream → chunked batches → retry-wrapped inference call → yielded results. Constant memory over arbitrarily large inputs. The frame of every real inference pipeline.

---

## The Notes System

Every part has a `notesN.md` written after finishing the problem set. Each captures four things:

1. **What the part covered** — concepts and mechanics
2. **What I built** — the specific projects, with their AI-adjacent framing
3. **What I got wrong and had to correct** — this is the section most learning repos omit
4. **Patterns worth internalizing** — the transferable lessons

The honest documentation matters more than the code. Anyone can copy a working solution; documenting the misconceptions you had to work through is what shows the learning actually happened.

**A recurring pattern I had to break through the second half of the book:** writing assertions that match the code's actual output instead of the spec's requirement. Assertions written from what your code produces test nothing — they just confirm the code produces what the code produces. Writing them from the spec is the difference between real verification and theater. That lesson is baked into every part from IV onward.

---

## Learning Philosophy

- **Every problem must be AI-adjacent.** No fabricated palindrome, calculator, or "manage a library of books" exercises. Even simple problems (temperature converter, character counter) were framed toward primitives that recur in real ML code.
- **Verification is not optional.** Every problem includes assertions derived from the spec, not from the code's output. This is the eval-driven mindset carried in from the start, not bolted on later.
- **Hard problems are cumulative.** "Hard" problems always required concepts from previous parts, not just harder versions of the current part's material. Cross-part integration matters more than depth within any one part.
- **Silently-correct-for-this-input is a bug.** Code that produces the right output for the test cases you ran, but has wrong logic underneath, is worse than obviously-broken code — it hides. Several times through the book, an assertion that "passed" was hiding a real bug. Those are the passages worth re-reading.

---

## Setup

- **OS:** WSL Ubuntu 24.04
- **Editor:** VS Code
- **Environment management:** [uv](https://github.com/astral-sh/uv)
- **Python:** 3.12+

No external dependencies — the entire book uses standard library only.

To run any problem locally:

```bash
git clone https://github.com/Sidified/Project-Python
cd Project-Python
python3 part-4-Collections/practice-projects-part4/8_MiniTokenizer+ReverseLookup.py
```

---

## What's Next

This repository is the **foundation phase** of my AI Engineering path. From here I'm moving into:

- The actual AI Engineering stack — LLM APIs, prompting, embeddings, RAG, evaluation, agents
- Eval-driven AI development — the mindset baked into every problem in this repo, applied to LLM systems where correctness is much harder to define than in `assert x == y`
- Real projects — built and shipped in public on GitHub

Follow along or reach out below.

---

## About Me

I'm **Sid (Siddharth Choudhary)** — IIT Roorkee, Mechanical Engineering '25 grad. I'm on a self-directed learning path towards AI Engineering. This repo is the foundation; new work continues in separate repositories as I ship.

- **LinkedIn:** [@Siddharth Choudhary](https://www.linkedin.com/in/siddharth-choudhary-797391215/)
- **GitHub:** [@Sidified](https://github.com/Sidified)

If you're on a similar path, DMs are open.

---

<sub>License: MIT · Built in public · No sponsored content</sub>