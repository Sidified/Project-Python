# BOSS — Model Registry with ABC and Polymorphism

# End-to-end problem combining ABC, inheritance, polymorphism, dunders, and design decisions.

# Setup: define an abstract base class using abc.ABC and @abstractmethod:

# from abc import ABC, abstractmethod

# class Model(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def predict(self, input_text): ...

#     @abstractmethod
#     def info(self) -> dict: ...      # returns metadata: {"name": ..., "type": ..., other fields}

#     def __repr__(self):
#         return f"<{type(self).__name__} name='{self.name}'>"

# Then build three concrete subclasses. Each must implement both abstract methods:
# 1. RulesModel(Model) — takes a dict of {keyword: response}. predict returns the
#    response for the first keyword found in the input; otherwise returns
#    "no rule matched". info returns {"name": ..., "type": "rules", "num_rules": N}.
# 2. RandomChoiceModel(Model) — takes a list of possible responses. predict returns
#    a random choice from the list (use random.choice). info returns
#    {"name": ..., "type": "random", "num_responses": N}.
# 3. EchoModel(Model) — predict returns f"ECHO: {input_text}".
#    info returns {"name": ..., "type": "echo"}.

# Then build a ModelRegistry class:
# -> __init__(self): internal dict _models (name → Model instance)
# -> register(self, model): adds a model; raise ValueError if a model with that name is already registered
# -> get(self, name): returns the model; raise KeyError with a clear message if not found
# -> unregister(self, name): removes a model; raise KeyError if not found
# -> list_models(self): returns a list of dicts by calling each model's info()
# -> __len__(self): number of registered models
# -> __contains__(self, name): "model-name" in registry works
# -> __iter__(self): iterates over registered models (not names)

# Verification (write all of these):

# # Cannot instantiate the abstract base
# try:
#     Model("bad")
#     raise AssertionError("expected TypeError from abstract class")
# except TypeError:
#     pass

# # Subclasses that skip a method should also fail to instantiate
# class IncompleteModel(Model):
#     def predict(self, input_text):
#         return "incomplete"
#     # missing info() — should fail on instantiation
# try:
#     IncompleteModel("incomplete")
#     raise AssertionError("expected TypeError")
# except TypeError:
#     pass

# # Register and query
# reg = ModelRegistry()
# rules = RulesModel("rules-1", {"hello": "Hi!", "bye": "Goodbye"})
# random_m = RandomChoiceModel("random-1", ["foo", "bar", "baz"])
# echo = EchoModel("echo-1")

# reg.register(rules)
# reg.register(random_m)
# reg.register(echo)

# assert len(reg) == 3
# assert "rules-1" in reg
# assert "nonexistent" not in reg

# # Duplicate registration must raise
# try:
#     reg.register(EchoModel("rules-1"))  # name collision
#     raise AssertionError("expected ValueError")
# except ValueError:
#     pass

# # Get and unregister
# assert reg.get("echo-1") is echo
# reg.unregister("echo-1")
# assert "echo-1" not in reg
# assert len(reg) == 2

# # Missing name on get/unregister must raise KeyError
# for missing in ["not-there"]:
#     try:
#         reg.get(missing)
#         raise AssertionError("expected KeyError")
#     except KeyError:
#         pass

# # list_models returns metadata from each registered model
# metadata = reg.list_models()
# assert isinstance(metadata, list)
# assert all(isinstance(m, dict) for m in metadata)
# assert all("name" in m and "type" in m for m in metadata)

# # Polymorphic use: same call site, different subclasses
# for model in reg:
#     result = model.predict("hello world")
#     assert isinstance(result, str)

# # Direct: rules model matches "hello"
# assert reg.get("rules-1").predict("hello there") == "Hi!"
# assert reg.get("rules-1").predict("goodbye friend") == "Goodbye"
# assert reg.get("rules-1").predict("no match here") == "no rule matched"

# Concepts combined:
# -> Abstract Base Classes (can't instantiate, subclasses must implement all abstractmethods)
# -> Inheritance and super().__init__(name) in each subclass
# -> Polymorphism (for model in reg: model.predict(...) works regardless of concrete type)
# -> Dunder methods (__len__, __contains__, __iter__, __repr__)
# -> Encapsulation (private _models dict, public interface via methods)
# -> Meaningful custom exceptions vs. built-in exceptions (choose the right one)

# Design decision to make explicitly (comment on it in your code):
# should unregister on a missing name raise KeyError, or silently
# do nothing? Different libraries choose differently — dict.pop(k, default)
# silently returns the default; dict.__delitem__ raises. State your
# choice and why. There's no single right answer, but the choice must
# be intentional. This is the "you made a choice on purpose" signal
# I've been asking for since Part VI.

# Why this problem: a ModelRegistry is the shape of torch.hub,
# HuggingFace's AutoModel registry, LangChain's model dispatch,
# MLflow's model registry — same core pattern (name-keyed store
# of polymorphic models, uniform interface). Real registries add
# versioning, persistence, and access control — but the core
# skeleton is what you're building here.

from abc import ABC, abstractmethod
import random

class Model(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def predict(self, input_text):
        pass

    @abstractmethod
    def info(self):
        pass

    def __repr__(self):
        return f"<{type(self).__name__} name='{self.name}'>"

class RulesModel(Model):
    def __init__(self, name, res_dict):
        self.res_dict = res_dict
        super().__init__(name)

    def predict(self, input_text):
        for keyword, response in self.res_dict.items():
            if keyword in input_text:
                return response
        return "no rule matched"

    def info(self):
        return {"name": self.name, "type": "rules", "num_rules": len(self.res_dict)}
                  

class RandomChoiceModel(Model):
    def __init__(self, name, pos_res):
        self.pos_res = pos_res
        super().__init__(name)

    def predict(self, input_text):
        return random.choice(self.pos_res)

    def info(self):
        return {"name": self.name, "type": "random", "num_responses": len(self.pos_res)}


class EchoModel(Model):
    def predict(self, input_text):
        return f"ECHO: {input_text}"

    def info(self):
        return {"name": self.name, "type": "echo"}

class ModelRegistry:
    def __init__(self):
        self._model = {}

    def register(self, model):
        if model.name in self._model:
            raise ValueError("model already registered")
        else:
            self._model[model.name] = model

    def get(self, name):
        if name in self._model:
            return self._model[name]
        else:
            raise KeyError("model not in registry")

    # Design choice for unregister():
    # unregister() raises KeyError if the model name is missing.
    # This makes mistakes visible immediately and matches the behavior
    # of deleting a missing key from a Python dictionary.
        
    def unregister(self, name):
        if name in self._model:
            self._model.pop(name)
        else:
            raise KeyError("model not in registry")

    def list_models(self):
        modelList = []
        for model in self._model.values():
            item = model.info()
            modelList.append(item)
        return modelList

    def __len__(self):
        return len(self._model)

    def __contains__(self, name):
        return name in self._model

    def __iter__(self):
        for model in self._model.values():
            yield model


# Cannot instantiate the abstract base
try:
    Model("bad")
    raise AssertionError("expected TypeError from abstract class")
except TypeError:
    pass

# Subclasses that skip a method should also fail to instantiate
class IncompleteModel(Model):
    def predict(self, input_text):
        return "incomplete"
    # missing info() — should fail on instantiation
try:
    IncompleteModel("incomplete")
    raise AssertionError("expected TypeError")
except TypeError:
    pass

# Register and query
reg = ModelRegistry()
rules = RulesModel("rules-1", {"hello": "Hi!", "bye": "Goodbye"})
random_m = RandomChoiceModel("random-1", ["foo", "bar", "baz"])
echo = EchoModel("echo-1")

reg.register(rules)
reg.register(random_m)
reg.register(echo)

assert len(reg) == 3
assert "rules-1" in reg
assert "nonexistent" not in reg

# Duplicate registration must raise
try:
    reg.register(EchoModel("rules-1"))  # name collision
    raise AssertionError("expected ValueError")
except ValueError:
    pass

# Get and unregister
assert reg.get("echo-1") is echo
reg.unregister("echo-1")
assert "echo-1" not in reg
assert len(reg) == 2

# Missing name on get/unregister must raise KeyError
for missing in ["not-there"]:
    try:
        reg.get(missing)
        raise AssertionError("expected KeyError")
    except KeyError:
        pass

# list_models returns metadata from each registered model
metadata = reg.list_models()
assert isinstance(metadata, list)
assert all(isinstance(m, dict) for m in metadata)
assert all("name" in m and "type" in m for m in metadata)

# Polymorphic use: same call site, different subclasses
for model in reg:
    result = model.predict("hello world")
    assert isinstance(result, str)

# Direct: rules model matches "hello"
assert reg.get("rules-1").predict("hello there") == "Hi!"
assert reg.get("rules-1").predict("goodbye friend") == "Goodbye"
assert reg.get("rules-1").predict("no match here") == "no rule matched"

print("All assertions passed!")        