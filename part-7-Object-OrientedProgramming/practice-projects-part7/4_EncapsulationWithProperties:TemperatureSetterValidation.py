# M2 — Encapsulation with Properties: Temperature Setter Validation

# Build a LLMConfig class:
# -> __init__(self, model, temperature=0.7, max_tokens=100)
# -> Store _temperature, _max_tokens as underscore-prefixed internals
# -> Expose them via @property getters temperature and max_tokens
# -> Setters (@temperature.setter, @max_tokens.setter) must validate:
#     -> temperature must be a number in [0.0, 2.0];
#        else raise ValueError with a clear message
#     -> max_tokens must be a positive integer; else raise ValueError
# -> Also validate in __init__ (call the setters,
#    don't just assign — otherwise __init__ would bypass validation)
# -> Add __repr__ returning LLMConfig(model='X', temperature=T, max_tokens=M)

# Verification:

# c = LLMConfig("gpt-4")
# assert c.temperature == 0.7
# assert c.max_tokens == 100

# c.temperature = 1.5
# assert c.temperature == 1.5

# # Bad values must raise
# for bad_temp in [-0.1, 2.1, "hot", None]:
#     try:
#         c.temperature = bad_temp
#         raise AssertionError(f"expected ValueError for temperature={bad_temp!r}")
#     except (ValueError, TypeError):
#         pass

# for bad_tokens in [0, -5, 3.14, "many"]:
#     try:
#         c.max_tokens = bad_tokens
#         raise AssertionError(f"expected ValueError for max_tokens={bad_tokens!r}")
#     except (ValueError, TypeError):
#         pass

# # Bad values in __init__ must also raise
# try:
#     LLMConfig("gpt-4", temperature=5.0)
#     raise AssertionError("expected ValueError from __init__")
# except ValueError:
#     pass

# Why this matters: every real config class validates on set,
# not on get. If you let bad values in and only discover them
# when they're used, the error message points to the wrong line.
# This pattern makes config.temperature = -1 crash at the assignment,
# which is where the bug actually is.

class LLMConfig:
    def __init__(self, model, temperature=0.7, max_tokens=100):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model = model

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        if isinstance(temperature, int) or isinstance(temperature, float):
            if 2 >= temperature >= 0:
                self._temperature  = temperature
            else:
                raise ValueError("Temperature out of range!")
        else:
            raise TypeError("Temperature must be numeric!")

    @property
    def max_tokens(self):
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        if isinstance(max_tokens, int) and max_tokens > 0:
            self._max_tokens = max_tokens
        else:
            raise ValueError("max_tokens must be a positive integer")

    def __repr__(self):
        return f"LLMConfig(model={self.model}, temperature={self.temperature}, max_tokens={self.max_tokens})"


c = LLMConfig("gpt-4")
assert c.temperature == 0.7
assert c.max_tokens == 100

c.temperature = 1.5
assert c.temperature == 1.5

# Bad values must raise
for bad_temp in [-0.1, 2.1, "hot", None]:
    try:
        c.temperature = bad_temp
        raise AssertionError(f"expected ValueError for temperature={bad_temp!r}")
    except (ValueError, TypeError):
        pass

for bad_tokens in [0, -5, 3.14, "many"]:
    try:
        c.max_tokens = bad_tokens
        raise AssertionError(f"expected ValueError for max_tokens={bad_tokens!r}")
    except (ValueError, TypeError):
        pass

# Bad values in __init__ must also raise
try:
    LLMConfig("gpt-4", temperature=5.0)
    raise AssertionError("expected ValueError from __init__")
except ValueError:
    pass

print("All assertions passed!")