# M3 — Grid Search Combinations
# Hardcode:
# pythonlearning_rates = [0.001, 0.01, 0.1]
# batch_sizes = [16, 32, 64]
# optimizers = ["sgd", "adam"]

# Using nested for loops, print every combination on its own line, formatted like:
# lr=0.001 | batch=16 | opt=sgd
# lr=0.001 | batch=16 | opt=adam

# Also count the total number of combinations and print it at the end.
# Verification: 3 × 3 × 2 = 18 combinations. If your count is anything else,
# a loop is nested wrong or you're missing an iteration.
# Why this problem: this is exactly what hyperparameter grid search does.

pythonlearning_rates = [0.001, 0.01, 0.1]
batch_sizes = [16, 32, 64]
optimizers = ["sgd", "adam"]

for p in pythonlearning_rates:
    for b in batch_sizes:
        for o in optimizers:
            print(f"Ir = {p} | batch = {b} | opt = {o}")

totalCount = len(pythonlearning_rates) * len(batch_sizes) * len(optimizers)
print(totalCount)