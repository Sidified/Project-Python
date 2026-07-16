# M1 — Robust JSON Config Loader

# Write load_config(path, required_keys) where:
# -> path is a file path
# -> required_keys is a list of strings — keys that MUST be present in the loaded JSON

# The function must handle three failure modes distinctly:
# 1. File missing → catch FileNotFoundError, raise a new
#    error ConfigError("Config file not found: <path>")
# 2. Invalid JSON → catch json.JSONDecodeError, raise
#    ConfigError("Config file is not valid JSON: <path>")
# 3. Missing required keys → after parsing, check that every
#    key in required_keys is present; if not, raise ConfigError("Missing required keys: <list>")

# Define ConfigError(Exception) as your custom exception. On success, return the parsed dict.

# Test scenarios (write each test file first, then load):
# -> data/valid_config.json containing all required keys — should return the dict
# -> data/invalid_config.json containing raw text
#    like not json {{  — should raise ConfigError with "not valid JSON"
# -> data/incomplete_config.json missing a required
#    key — should raise ConfigError with "Missing required keys"
# -> A path that doesn't exist — should raise ConfigError with "not found"

# Use required_keys = ["model", "learning_rate", "batch_size"] for testing.

# Verification: each of the 4 scenarios verified with try/except ConfigError.
# In the success case, assert the returned dict has all the required keys.
# In each failure case, assert that the error message contains the
# expected substring ("not found", "not valid JSON", "Missing required keys").

# Why this matters: this is the shape of every config-loading function
# in every real ML codebase. Different failure modes need different error
# messages so the user (or you at 2am) knows why the load failed.

import json

class ConfigError(Exception):
    pass

def load_config(path, required_keys):
    try:
        with open(path, "r") as file:
            data = file.read()
    except FileNotFoundError:
        raise ConfigError(f"Config file not found: {path}")
    
    try:
        fileDict = json.loads(data)
    except (json.JSONDecodeError):
        raise ConfigError(f"Config file is not valid JSON: {path}")
        
    # Check if any required key is missing from the dictionary keys
    missing_keys = [key for key in required_keys if key not in fileDict]

    if missing_keys:
    # Join them into a clean string if there are multiple missing
        missing_str = ", ".join(missing_keys)
        raise ConfigError(f"Missing required keys: {missing_str}")

    
    return fileDict

required_keys = ["model", "learning_rate", "batch_size"]

# -----------------------------------------------------------------------------------------
# Test-Case-1: data/valid_config.json containing all required keys — should return the dict
# -----------------------------------------------------------------------------------------
validConfig = {
    "model": "transformer",
    "learning_rate": 0.001,
    "batch_size": 32
    }
path_1 = "part-6-StructuringRealPrograms/practice-projects-part6/data/valid_config.json"

with open(path_1, "w") as vc:
    json.dump(validConfig, vc, indent=2)

finalDict_1 = load_config(path_1, required_keys)

print(finalDict_1)
assert isinstance(finalDict_1, dict)

for key in required_keys:
    assert key in finalDict_1
    
print("Test Case 1 Passed!")

# ----------------------------------------------------------------------------------------------------------------------------
# Test-Case-2: data/invalid_config.json containing raw text like not json {{  — should raise ConfigError with "not valid JSON"
# ----------------------------------------------------------------------------------------------------------------------------
path_2 = "part-6-StructuringRealPrograms/practice-projects-part6/data/invalid_config.json"

with open(path_2, "w") as ivc:
    ivc.write("Something random, which is not a JSON file.")


try:
    finalDict_2 = load_config(path_2, required_keys)

    # If we reach here, that's actually a failure,
    # because we expected an exception.
    assert False, "Expected ConfigError for invalid JSON"

except ConfigError as e:
    assert "not valid JSON" in str(e)

print("Test Case 2 Passed!")

# -----------------------------------------------------------------------------------------------------------------------
# Test-Case-3: data/incomplete_config.json missing a required key — should raise ConfigError with "Missing required keys"
# -----------------------------------------------------------------------------------------------------------------------
inCompConfig = {
    "model": "transformer",
    "learning_rate": 0.001
    }

path_3 = "part-6-StructuringRealPrograms/practice-projects-part6/data/incomplete_config.json"
with open(path_3, "w") as icc:
    json.dump(inCompConfig, icc, indent=2)

try:
    finalDict_3 = load_config(path_3, required_keys)

    assert False, "Expected ConfigError for incomplete JSON"

except ConfigError as e:
    assert "Missing required keys:" in str(e)

print("Test Case 3 Passed!")

# ----------------------------------------------------------------------------------
# Test-Case-4: A path that doesn't exist — should raise ConfigError with "not found"
# ----------------------------------------------------------------------------------
path_4 = "part-6-StructuringRealPrograms/practice-projects-part6/data/random_path.json"

try:
    finalDict_4 = load_config(path_4, required_keys)

    assert False, "Expected ConfigError for invalid path"

except ConfigError as e:
    assert "file not found" in str(e)

print("Test Case 4 Passed!")