# M3 — Sort Models by Composite Score (named function AND lambda)

# models = [
#    {"name": "gpt-4", "accuracy": 0.87, "latency_ms": 340},
#    {"name": "claude-opus", "accuracy": 0.91, "latency_ms": 280},
#    {"name": "llama-70b", "accuracy": 0.82, "latency_ms": 190},
#    {"name": "mistral-7b", "accuracy": 0.76, "latency_ms": 95},
# ]

# Composite score: accuracy - 0.001 * latency_ms. Higher is better.

# Do it two ways in the same file:
# 1. Define a named function composite_score(model),
#    use it with sorted(models, key=composite_score, reverse=True)
# 2. Use an inline lambda: sorted(models, key=lambda m: ..., reverse=True)

# Print both results and assert they're identical.

# Verification: sorted_named == sorted_lambda.

models = [
   {"name": "gpt-4", "accuracy": 0.87, "latency_ms": 340},
   {"name": "claude-opus", "accuracy": 0.91, "latency_ms": 280},
   {"name": "llama-70b", "accuracy": 0.82, "latency_ms": 190},
   {"name": "mistral-7b", "accuracy": 0.76, "latency_ms": 95},
]

def composite_score(model):
    accuracy = model["accuracy"]
    latency_ms = model["latency_ms"]

    composite_score = accuracy - (0.001 * latency_ms)
    return composite_score

sorted_named = sorted(models, key=composite_score, reverse=True)
print(sorted_named)

sorted_lambda = sorted(models, key=lambda m: m['accuracy'] - (0.001 * m['latency_ms']), reverse=True)
print(sorted_lambda)

assert sorted_named == sorted_lambda
print("All assertions passed!")