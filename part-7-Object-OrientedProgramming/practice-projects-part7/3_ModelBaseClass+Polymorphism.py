# M1 — Model Base Class + Polymorphism

# Define a base class BaseModel:
# -> __init__(self, name): stores self.name = name
# -> predict(self, input_text): raises NotImplementedError("subclasses must implement predict")
# -> __repr__(self): returns <ClassName name='<name>'>
#    — use type(self).__name__ to get the actual subclass name, not hardcoded BaseModel

# Define three subclasses:
# -> EchoModel(BaseModel): predict(input_text) returns f"ECHO: {input_text}"
# -> UppercaseModel(BaseModel): predict(input_text) returns input_text.upper()
# -> ReverseModel(BaseModel): predict(input_text) returns input_text[::-1]

# Then write a function run_ensemble(models, input_text) that takes
# a list of models and an input, calls .predict() on each,
# and returns a dict {model.name: prediction}.

# Verification:

# python
# models = [
#     EchoModel("echo-1"),
#     UppercaseModel("upper-1"),
#     ReverseModel("reverse-1"),
# ]
# results = run_ensemble(models, "hello")
# assert results == {
#     "echo-1": "ECHO: hello",
#     "upper-1": "HELLO",
#     "reverse-1": "olleh",
# }

# # Must raise NotImplementedError if BaseModel.predict is called directly
# try:
#     BaseModel("base").predict("test")
#     raise AssertionError("expected NotImplementedError")
# except NotImplementedError:
#     pass

# # __repr__ should reflect the actual subclass
# assert repr(EchoModel("e1")) == "<EchoModel name='e1'>"

# Why this matters: this is the polymorphism pattern behind every
# model interface — HuggingFace's PreTrainedModel, LangChain's Runnable,
# sklearn's estimators. Different concrete implementations, same .predict()
# interface. Your run_ensemble doesn't know or care which subclass is
# which — it just calls .predict().

class BaseModel:
    def __init__(self, name):
        self.name = name

    def predict(self, input_text):
        raise NotImplementedError("subclasses must implement predict")
    
    def __repr__(self):
        return f"<{type(self).__name__} name='{self.name}'>"
    

class EchoModel(BaseModel):
    def __init__(self, name):
        self.name = name
    def predict(self, input_text):
        return f"ECHO: {input_text}"

class UppercaseModel(BaseModel):
    def __init__(self, name):
        self.name = name
    def predict(self,input_text):
        return input_text.upper()

class ReverseModel(BaseModel):
    def __init__(self, name):
        self.name = name
    def predict(self, input_text):
        return input_text[::-1]
    
def run_ensemble(models, input_text):
    modelDict = {}
    for model in models:
        prediction = model.predict(input_text)
        modelDict[model.name] = prediction
    return modelDict


models = [
    EchoModel("echo-1"),
    UppercaseModel("upper-1"),
    ReverseModel("reverse-1"),
]
results = run_ensemble(models, "hello")
assert results == {
    "echo-1": "ECHO: hello",
    "upper-1": "HELLO",
    "reverse-1": "olleh",
}

# Must raise NotImplementedError if BaseModel.predict is called directly
try:
    BaseModel("base").predict("test")
    raise AssertionError("expected NotImplementedError")
except NotImplementedError:
    pass

# __repr__ should reflect the actual subclass
assert repr(EchoModel("e1")) == "<EchoModel name='e1'>"

print("All assertions passed!")