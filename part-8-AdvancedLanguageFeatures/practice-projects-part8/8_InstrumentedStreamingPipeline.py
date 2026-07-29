# BOSS — Instrumented Streaming Pipeline

# End-to-end problem combining generators, decorators, context managers, and dataclasses.

# Setup:
# Create a JSONL file data/requests.jsonl with 20 records like:
# json
# {"id": 1, "prompt": "hello"}
# {"id": 2, "prompt": "explain gradient descent"}
# Include 1 malformed line and 1 empty line so your stream handling gets exercised.

# Build this system:
# -> @dataclass(frozen=True) PipelineConfig with fields:
#    input_path: str, batch_size: int = 4, max_retries: int = 3.
#    Validate batch_size > 0 and max_retries > 0 in __post_init__.
# -> @contextmanager timed_stage(name: str) that measures how long
#    the block took and prints "<name> took X.XXXXs" to sys.stderr
#    on exit. Use try/finally.
# -> A flaky simulated LLM call wrapped with your @retry decorator from M2:

#    @retry(max_attempts=3, on_exception=ConnectionError)
#    def call_llm(prompt):
#        # 30% chance of ConnectionError, else returns "response for: <prompt>"
#        if random.random() < 0.3:
#            raise ConnectionError("simulated network fail")
#        return f"response for: {prompt}"

# -> A run_pipeline(config: PipelineConfig) generator that:
#       -> Streams records from config.input_path using your stream_jsonl from M1
#       -> Batches them using your chunk from E1, with size config.batch_size
#       -> Wraps each batch's processing in timed_stage(f"batch_{i}")
#       -> Calls call_llm(prompt) for every record in the batch
#       ->Yields each result as {"id": <id>, "response": <response>} — one at a time


# Then run it and verify:

# random.seed(42)   # reproducibility

# config = PipelineConfig(input_path="data/requests.jsonl", batch_size=4, max_retries=3)
# results = list(run_pipeline(config))

# assert len(results) == 20        # 20 valid records, malformed/empty skipped
# assert all("id" in r and "response" in r for r in results)
# assert all(r["response"].startswith("response for:") for r in results)

# # Config validation still works
# try:
#     PipelineConfig(input_path="x", batch_size=0)
#     raise AssertionError("expected ValueError")
# except ValueError:
#     pass

# try:
#     PipelineConfig(input_path="x", batch_size=4, max_retries=0)
#     raise AssertionError("expected ValueError")
# except ValueError:
#     pass

# # Frozen: can't mutate config
# try:
#     config.batch_size = 10
#     raise AssertionError("expected FrozenInstanceError")
# except:
#     pass


# Concepts combined:
# -> Dataclass with frozen + validation (H1)
# -> Generator streaming (M1)
# -> Chunking generator (E1)
# -> Retry decorator (M2)
# -> Context manager timing (M3-style)
# -> Type hints throughout (spec expected)

# Design principle: the entire pipeline is a chain of generators.
# No point in the code loads all records into memory. This is why
# generators matter for AI Engineering — you can build production-shaped
# pipelines that handle datasets larger than RAM by composing lazy operations.

# Why this problem: this is the skeleton of every real inference pipeline.
# Replace the flaky call_llm with a real API call, add batching optimizations,
# and you have production code. The frame is the same.

from dataclasses import dataclass
from contextlib import contextmanager
import time
import sys
import random
from functools import wraps
import json

@dataclass(frozen=True)
class PipelineConfig:
    input_path: str
    batch_size: int = 4
    max_retries: int = 3

    def __post_init__(self):
        if self.batch_size <= 0:
            raise ValueError("WARNING: Batch size should be greater than zero!")
        if self.max_retries <= 0:
            raise ValueError("WARNING: Max retries cannot be less than zero!")

@contextmanager
def timed_stage(name: str):
    try:
        start = time.perf_counter()
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{name} took {elapsed:.4f}s", file=sys.stderr)

def retry(max_attempts=3, on_exception=ConnectionError):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except on_exception as e:
                    print(f"Warning: Attempt {attempt} failed: {e}", file=sys.stderr)
                    last_exception = e
            raise last_exception
            
        return wrapper
    
    return decorator

@retry(max_attempts=3, on_exception=ConnectionError)
def call_llm(prompt):
    # 20% chance of ConnectionError, else returns "response for: <prompt>"
    if random.random() < 0.20:
        raise ConnectionError("simulated network fail")
    return f"response for: {prompt}"
# def call_llm(prompt):
#     value = random.random()
#     print(f"Random value: {value}")
#     if value < 0.3:
#         raise ConnectionError("simulated network fail")
#     return f"response for: {prompt}"


def stream_jsonl(path):
    count = 0
    with open(path, "r") as f:
        for line in f:
            count+=1
            if line.strip() == "":
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                print(f"Warning: malformed JSON on line -> {count}", file=sys.stderr)


def chunk(seq, n):
    itemList = []
    for item in seq:
        itemList.append(item)
        if len(itemList) == n:
            yield itemList
            itemList = []
    if itemList:
        yield itemList

def run_pipeline(config: PipelineConfig):
    seq = stream_jsonl(config.input_path)

    batches = chunk(seq, config.batch_size)

    for batch_num, batch in enumerate(batches, start=1):
        with timed_stage(f"batch_{batch_num}"):
            for record in batch:
                response = call_llm(record['prompt'])
                yield {"id": record['id'], "response": response}


# VERIFICATION

random.seed(42)   # reproducibility

config = PipelineConfig(input_path="part-8-AdvancedLanguageFeatures/practice-projects-part8/data/requests.jsonl", batch_size=4, max_retries=3)
results = list(run_pipeline(config))

assert len(results) == 20        # 20 valid records, malformed/empty skipped
assert all("id" in r and "response" in r for r in results)
assert all(r["response"].startswith("response for:") for r in results)

# Config validation still works
try:
    PipelineConfig(input_path="x", batch_size=0)
    raise AssertionError("expected ValueError")
except ValueError:
    pass

try:
    PipelineConfig(input_path="x", batch_size=4, max_retries=0)
    raise AssertionError("expected ValueError")
except ValueError:
    pass

# Frozen: can't mutate config
try:
    config.batch_size = 10
    raise AssertionError("expected FrozenInstanceError")
except:
    pass

print("All assertions passed!")