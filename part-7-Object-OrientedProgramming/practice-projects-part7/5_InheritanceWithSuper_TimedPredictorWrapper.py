# M3 — Inheritance with super(): Timed Predictor Wrapper

# Build a TimedModel subclass of BaseModel (from M1) that wraps predictions with timing.

# Requirements:
# -> TimedModel.__init__(self, name, wrapped_model) — stores the wrapped model and calls super().__init__(name)
# -> TimedModel.predict(self, input_text):
#     -> Records a start time using time.perf_counter()
#     -> Calls self._wrapped.predict(input_text)
#     -> Records end time
#     -> Stores the elapsed seconds in a list self._latencies
#     -> Returns the same result as the wrapped model
# -> average_latency(self): returns the mean of self._latencies; raise ValueError("no calls made") if empty
# -> call_count(self): @property returning len(self._latencies)

# Verification:

# import time

# echo = EchoModel("echo-1")
# timed = TimedModel("timed-echo", echo)

# assert timed.call_count == 0

# result = timed.predict("hello")
# assert result == "ECHO: hello"          # forwards result unchanged
# assert timed.call_count == 1

# for _ in range(4):
#     timed.predict("test")
# assert timed.call_count == 5

# avg = timed.average_latency()
# assert avg > 0                          # every call takes some measurable time
# assert isinstance(avg, float)

# # average_latency before any calls must raise
# fresh = TimedModel("fresh", EchoModel("e"))
# try:
#     fresh.average_latency()
#     raise AssertionError("expected ValueError")
# except ValueError:
#     pass

# Why this matters: this is the wrapper pattern — same interface
# as the wrapped object, adds behavior around it. LangChain's
# callbacks, OpenTelemetry spans on API calls, latency histograms
# in production — all use this shape. Also the exact pattern behind
# PyTorch's torch.no_grad() wrapping model calls at a higher level.

import time

class BaseModel:
    def __init__(self, name):
        self.name = name

    def predict(self, input_text):
        raise NotImplementedError("subclasses must implement predict")
    
    def __repr__(self):
        return f"<{type(self).__name__} name='{self.name}'>"

class TimedModel(BaseModel):
    def __init__(self, name, wrapped_model):
        self._wrapped = wrapped_model
        super().__init__(name)
        self._latencies = []

    def predict(self, input_text):
        start_time = time.perf_counter()
        value = self._wrapped.predict(input_text)
        end_time = time.perf_counter()
        self._latencies.append(end_time - start_time)
        return value

    def average_latency(self):
        if len(self._latencies) != 0:
            return sum(self._latencies)/len(self._latencies)
        else:
            raise ValueError("no calls made")

    @property
    def call_count(self):
        return len(self._latencies)

class EchoModel(BaseModel):
    def __init__(self, name):
        self.name = name
    def predict(self, input_text):
        return f"ECHO: {input_text}"


echo = EchoModel("echo-1")
timed = TimedModel("timed-echo", echo)

assert timed.call_count == 0

result = timed.predict("hello")
assert result == "ECHO: hello"          # forwards result unchanged
assert timed.call_count == 1

for _ in range(4):
    timed.predict("test")
assert timed.call_count == 5

avg = timed.average_latency()
assert avg > 0                          # every call takes some measurable time
assert isinstance(avg, float)

# average_latency before any calls must raise
fresh = TimedModel("fresh", EchoModel("e"))
try:
    fresh.average_latency()
    raise AssertionError("expected ValueError")
except ValueError:
    pass

print("All assertions passed")
