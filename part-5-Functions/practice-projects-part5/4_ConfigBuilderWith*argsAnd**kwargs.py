# M2 — Config Builder with *args and **kwargs

# Write build_config(*required, **hyperparams). Requirements:
# -> Must receive at least 2 positional args, otherwise raise ValueError
# -> Returns a dict shaped like:

# {
#      "required": [<positional args as a list>],
#      "hyperparams": {<all kwargs>},
#      "total_kwargs": <count of kwargs>
# }

# Test:
# result = build_config("model_a", "dataset_b", lr=0.01, epochs=10, batch_size=32)

# Verification:
# assert result["required"] == ["model_a", "dataset_b"]
# assert result["total_kwargs"] == 3
# assert result["hyperparams"]["lr"] == 0.01.

# Also verify that build_config("only_one") raises ValueError — call it,
# observe the error, then comment it out.

# Why this matters: *args/**kwargs is how every ML library accepts
# arbitrary hyperparameters. HuggingFace's AutoModel.from_pretrained(model_name, **kwargs)
# is exactly this shape.

def build_config(*required, **hyperparams):
    if len(required) < 2:
        raise ValueError("Must receive at least 2 positional args")
    finalDict = {'required': list(required), 'hyperparams': hyperparams, 'total_kwargs': len(hyperparams)}
    return finalDict

result = build_config("model_a", "dataset_b", lr=0.01, epochs=10, batch_size=32)
print(result)

assert result["required"] == ["model_a", "dataset_b"]
assert result["total_kwargs"] == 3
assert result["hyperparams"]["lr"] == 0.01

print("All assertions passed!")

# This will raise the -> ValueError: Must receive at least 2 positional args
# build_config("only_one")