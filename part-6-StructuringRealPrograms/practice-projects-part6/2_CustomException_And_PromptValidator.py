# E2 — Custom Exception & Prompt Validator

# Define a custom exception class:
# class InvalidPromptError(Exception):
#     pass

# Write validate_prompt(text) that raises InvalidPromptError with a clear message if:
# -> text is not a str (e.g., someone passed an int or None)
# -> text.strip() is empty
# -> len(text) > 1000

# Otherwise return text.strip().

# Verification: four test cases, each wrapped in try/except:
# # Should succeed
# assert validate_prompt("  Hello world  ") == "Hello world"

# # Should each raise InvalidPromptError
# for bad_input in [None, "", "   ", "a" * 1001]:
#     try:
#         validate_prompt(bad_input)
#         raise AssertionError(f"Expected InvalidPromptError for input: {bad_input!r}")
#     except InvalidPromptError:
#         pass  # good

# The try/except inside the assertion loop is the
# correct pattern — you expect the error, so catching it is the success case.

# Why this matters: every LLM API you'll call will need input
# validation at the boundary. Custom exceptions let callers
# handle prompt-validation errors differently from, say, network errors.

class InvalidPromptError(Exception):
    pass

def validate_prompt(text):
    if not isinstance(text, str):
        raise InvalidPromptError("Input argument is not a string") 
    if text.strip() == "":
        raise InvalidPromptError("Empty string passed")
    if len(text) > 1000:
        raise InvalidPromptError("String is too long")
    
    return text.strip()

# Should succeed
assert validate_prompt("  Hello world  ") == "Hello world"

# Should each raise InvalidPromptError
for bad_input in [None, "", "   ", "a" * 1001]:
    try:
        validate_prompt(bad_input)
        raise AssertionError(f"Expected InvalidPromptError for input: {bad_input!r}")
    except InvalidPromptError:
        pass  # good

print("All assertions passed!")