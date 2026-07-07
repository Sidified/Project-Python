# M2 — Zip Two Lists into Records

# Hardcode:
# model_names = ["gpt-4", "claude-opus", "llama-70b", "mistral-7b"]
# accuracies = [0.87, 0.91, 0.82, 0.76]
# latencies_ms = [340, 280, 190, 95]

# Using zip, build a list of dicts where each dict looks like:
# {"name": "gpt-4", "accuracy": 0.87, "latency_ms": 340}

# Then print each dict on its own line, and finally print
# the name of the model with the highest accuracy and the model with the lowest latency.

# Verification: The list must have len(model_names) records.
# The highest-accuracy model should be claude-opus,
# lowest-latency should be mistral-7b.

model_names = ["gpt-4", "claude-opus", "llama-70b", "mistral-7b"]
accuracies = [0.87, 0.91, 0.82, 0.76]
latencies_ms = [340, 280, 190, 95]

aiList = []

for model_names, accuracies, latencies_ms in zip(model_names, accuracies, latencies_ms):
    aiList.append({"name" : model_names, "accuracy": accuracies, "latency_ms": latencies_ms})

for item in aiList:
    print(item)

sortAcc = sorted(aiList, key=lambda item: item["accuracy"], reverse=True)
print(f"The model with the highest accuracy is {sortAcc[0]["name"]}")

sortLowLat = sorted(aiList, key=lambda item: item["latency_ms"])
print(f"The model with the lowest latency is {sortLowLat[0]["name"]}")