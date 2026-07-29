# H1 — Dataclass Config with Validation

# Rebuild Part VII's LLMConfig, but this time using @dataclass.
# The point of this problem is not "learn dataclasses" — it's
# to see the difference between the two approaches and understand
# which pattern to use when.

# Requirements:
# -> @dataclass(frozen=True) for immutability
# -> Fields with type hints: model: str, temperature: float = 0.7,
#    max_tokens: int = 100, stop_sequences: list[str] = field(default_factory=list)
# -> Use field(default_factory=list), never = [] — this is the
#    mutable default argument trap from Part V, translated to dataclasses
# -> __post_init__ validates: temperature in [0.0, 2.0], max_tokens > 0.
#    Raise ValueError on bad values.

# Verification:
# from dataclasses import FrozenInstanceError

# c = LLMConfig(model="gpt-4")
# assert c.temperature == 0.7
# assert c.max_tokens == 100
# assert c.stop_sequences == []

# # Two instances get independent stop_sequences (mutable default trap check)
# c1 = LLMConfig(model="a")
# c2 = LLMConfig(model="b")
# assert c1.stop_sequences is not c2.stop_sequences   # not the same list object

# # Frozen: can't mutate after construction
# try:
#     c.temperature = 1.5
#     raise AssertionError("expected FrozenInstanceError")
# except FrozenInstanceError:
#     pass

# # Validation still runs at construction
# for bad_temp in [-0.1, 2.1, 3.0]:
#     try:
#         LLMConfig(model="x", temperature=bad_temp)
#         raise AssertionError(f"expected ValueError for temp={bad_temp}")
#     except ValueError:
#         pass

# for bad_tokens in [0, -5]:
#     try:
#         LLMConfig(model="x", max_tokens=bad_tokens)
#         raise AssertionError(f"expected ValueError for max_tokens={bad_tokens}")
#     except ValueError:
#         pass

# Parts recalled:
# -> Part V — mutable default argument trap. In dataclasses,
#    this shows up as = [] vs field(default_factory=list).
#    Getting this wrong makes all your LLMConfig instances
#    share the same stop_sequences list.
# -> Part VII — property + setter validation. __post_init__ is
#    the dataclass equivalent for construction-time validation.
#    Compare the amount of code: Part VII's LLMConfig was ~30 lines;
#    this version is ~10.
# -> Part I — immutability. frozen=True enforces immutability at the
#    language level. Compare: Part I's t = (1, 2, [3, 4]) where the
#    tuple was immutable but the inner list wasn't. frozen=True gives
#    you the same protection for structured records, still with the
#    same caveat that mutable fields can still be mutated internally.

# Note the design pattern comparison in your notes.md — when to use each:
# -> @property + setter validation (Part VII style): when the class needs
#    runtime-updatable state, or when validation has to run on every assignment
# -> @dataclass(frozen=True) + __post_init__ (this problem): when the class is
#    a value-object / config / record, validated once at construction

# Why: every modern ML config in every real codebase is a
# dataclassor pydantic model. HuggingFace's TrainingArguments,
# AutoModel configs — all dataclasses.

from dataclasses import dataclass, field, FrozenInstanceError

@dataclass(frozen=True)
class LLMConfig:
    model: str
    temperature: float = 0.7
    max_tokens: int = 100
    stop_sequences: list[str] = field(default_factory=list)

    def __post_init__(self):
        if 0 > self.temperature or self.temperature > 2.0:
            raise ValueError("Temperature out of range!")

        if self.max_tokens <= 0:
            raise ValueError("max_tokens must be a positive integer")


# VERIFICATION

c = LLMConfig(model="gpt-4")
assert c.temperature == 0.7
assert c.max_tokens == 100
assert c.stop_sequences == []

# Two instances get independent stop_sequences (mutable default trap check)
c1 = LLMConfig(model="a")
c2 = LLMConfig(model="b")
assert c1.stop_sequences is not c2.stop_sequences   # not the same list object

# Frozen: can't mutate after construction
try:
    c.temperature = 1.5
    raise AssertionError("expected FrozenInstanceError")
except FrozenInstanceError:
    pass

# Validation still runs at construction
for bad_temp in [-0.1, 2.1, 3.0]:
    try:
        LLMConfig(model="x", temperature=bad_temp)
        raise AssertionError(f"expected ValueError for temp={bad_temp}")
    except ValueError:
        pass

for bad_tokens in [0, -5]:
    try:
        LLMConfig(model="x", max_tokens=bad_tokens)
        raise AssertionError(f"expected ValueError for max_tokens={bad_tokens}")
    except ValueError:
        pass

print("All assertions passed!")