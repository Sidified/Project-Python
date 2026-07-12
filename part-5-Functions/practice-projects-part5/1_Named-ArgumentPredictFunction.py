# E1 — Named-Argument Predict Function

# Write predict(input_text, model="gpt-4", temperature=0.7, max_tokens=100).
# Don't call any real API.
# Return the string:
# "Would call model=<model> on '<input_text>' with temp=<temperature>, max_tokens=<max_tokens>""

# Test three call styles:
# predict("hello")
# predict("hello", temperature=0.2, max_tokens=50)
# predict("hello", "claude-opus", 0.5, 200)

# Verification: assert each call returns the exact expected string.
# Include the assertions in your code.

# Why this matters: this is the shape of every LLM SDK function you'll ever call.
# Default-with-override is how they're designed.


def predict(input_text, model="gpt-4", temperature=0.7, max_tokens=100):
    result = f"Would call model={model} on '{input_text}' with temp={temperature}, max_tokens={max_tokens}"
    print(result)
    return result


result1 = predict("hello")
assert result1 == "Would call model=gpt-4 on 'hello' with temp=0.7, max_tokens=100"

result2 = predict("hello", temperature=0.2, max_tokens=50)
assert result2 == "Would call model=gpt-4 on 'hello' with temp=0.2, max_tokens=50"

result3 = predict("hello", "claude-opus", 0.5, 200)
assert result3 == "Would call model=claude-opus on 'hello' with temp=0.5, max_tokens=200"

print("All assertions passed!")
