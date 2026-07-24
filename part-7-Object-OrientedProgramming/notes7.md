# Part VII — Object-Oriented Programming

## What this part covered

- **Classes and objects:** `class` syntax, `__init__(self, ...)`, `self` refers to the instance, instance attributes assigned in `__init__` become part of every instance.
- **Inheritance and `super()`:** subclasses inherit everything from the parent. `super().__init__(...)` calls the parent's initializer — use when the subclass needs to add its own arguments. If the subclass needs no extra args, don't override `__init__` at all.
- **Encapsulation and access control:** single underscore (`_var`) is a convention meaning "internal, don't touch from outside." Not enforced by Python — it's a signal to other developers (and future me).
- **Properties (`@property`):** turns a method into an attribute-style getter. Add `@name.setter` to validate on assignment. `__init__` should call the setter (`self.temperature = value`) so validation runs — not assign directly to `_temperature`, which would bypass it.
- **Polymorphism:** different subclasses implement the same method (`predict`), and calling code (`model.predict(x)`) works regardless of concrete type. The core idea behind every ML framework's model interface.
- **Dunder methods:** `__init__`, `__repr__`, `__len__`, `__contains__`, `__iter__`, `__getitem__`, `__call__` — implementing these makes custom types feel native (`len(vocab)`, `"hello" in vocab`, `for record in dataset`, `dataset[0:3]`).
- **Abstract Base Classes:** `from abc import ABC, abstractmethod`. Marks methods as required. Subclasses missing any `@abstractmethod` fail at *instantiation* with `TypeError`, not at definition. Useful for defining a contract that concrete implementations must satisfy.

## What I built

- `Vocabulary` — token↔id maps with `add`, `encode`, `decode`, `__len__`, `__contains__`, `__repr__` (shape of every real tokenizer)
- `RunningStats` — accumulate observations online with `update`, `mean`, `reset`, `count` as a property (shape of every metric aggregator in a training loop)
- `BaseModel` + `EchoModel`/`UppercaseModel`/`ReverseModel` + `run_ensemble` — polymorphism across a common `predict` interface
- `LLMConfig` — properties with setter validation, `__init__` invoking setters (so validation runs at construction time too)
- `TimedModel` — wrapper subclass that measures latency around another model's `predict`, using `super().__init__(name)` for the parent's construction
- `Dataset` — JSONL-backed dataset class with `__len__`, `__getitem__` (int and slice), `__iter__`, and a `filter(predicate)` method — the shape of PyTorch's `Dataset`
- `Model` (ABC) + `RulesModel`/`RandomChoiceModel`/`EchoModel` + `ModelRegistry` — abstract interface with concrete implementations, name-keyed registry with polymorphic iteration

## What I got wrong / worth remembering

- **Redefining `__init__` in a subclass to reproduce the parent's behavior is an anti-pattern.** If the subclass needs no extra construction, don't override at all. If it does, call `super().__init__(...)` — don't re-assign `self.name = name` manually. Any future addition to the parent's `__init__` (an internal counter, a registration hook) will silently miss the subclass otherwise.
- **`__init__` calling the setter, not the internal field.** `self.temperature = value` triggers the `@temperature.setter` (with validation). `self._temperature = value` bypasses validation. Easy to get wrong; matters a lot for correctness.
- **ABC prevents instantiation, not definition.** Missing an `@abstractmethod` in a subclass doesn't error until you try to construct an instance. Something to remember when reading traceback line numbers.
- **`__getitem__` gets slice support "for free" when it delegates to a list.** `self._data[idx]` handles both `int` and `slice` because `list.__getitem__` does. No manual isinstance check needed.

## Patterns worth internalizing

- **Underscore-prefixed internals** for state that shouldn't be touched from outside. Communicated by convention, not by language enforcement.
- **Property + setter** for validation-on-assignment. Makes bad values fail *at the assignment line*, which is where the bug actually is.
- **ABC + `@abstractmethod`** to define an interface contract. Concrete subclasses must implement every abstract method or they can't be instantiated.
- **Wrapper pattern** (like `TimedModel`) — same interface as the wrapped object, adds behavior (timing, logging, caching, retries) around the delegated call.
- **Custom `__repr__` using `type(self).__name__`** — subclasses show their real class name in debug output without each subclass having to redefine `__repr__`.
- **Dunder trio for collection-like classes:** `__len__` + `__getitem__` + `__iter__`. This is exactly what PyTorch's `Dataset` requires (the first two) and what makes any custom type feel Pythonic.
- **Polymorphism over conditional dispatch.** `for model in registry: model.predict(x)` is better than `if type == "rules": ... elif type == "random": ...`. Add a new model type → new subclass, no changes to the calling code.

## Why this matters for AI Engineering

- Every real ML framework uses these patterns:
  - **PyTorch `nn.Module`** — subclass with `forward` method (same idea as `predict` here)
  - **HuggingFace tokenizers** — encapsulated vocab state + `encode`/`decode` methods
  - **PyTorch `Dataset`** — `__len__` + `__getitem__` is the entire required interface
  - **Config classes** — usually `@dataclass` (Part VIII), but same encapsulation idea
  - **Model registries** — `torch.hub`, `AutoModel.from_pretrained`, MLflow model registry — same name-keyed polymorphic store I built in BOSS