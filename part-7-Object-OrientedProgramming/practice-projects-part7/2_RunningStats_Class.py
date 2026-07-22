# E2 — RunningStats Class (encapsulated state + reset)

# Build RunningStats — a class that accumulates numeric values and reports
# statistics online (without storing all values):
# -> __init__(self): initialize internal counter and running sums
# -> update(self, value): add a new observation
# -> mean(self): return current mean; raise ValueError("no data") if no observations yet
# -> count: a property returning the number of observations
# -> reset(self): clear all state
# -> __repr__(self): return RunningStats(n=N, mean=M) where N is
#    the count and M is the current mean formatted to 4 decimals,
#    or RunningStats(n=0, mean=None) if empty

# Verification:

# s = RunningStats()
# assert s.count == 0
# assert repr(s) == "RunningStats(n=0, mean=None)"

# s.update(1.0)
# s.update(2.0)
# s.update(3.0)
# assert s.count == 3
# assert s.mean() == 2.0
# assert repr(s) == "RunningStats(n=3, mean=2.0000)"

# s.reset()
# assert s.count == 0
# try:
#     s.mean()
#     raise AssertionError("expected ValueError")
# except ValueError:
#     pass

# Why this matters: this is the shape of every metric aggregator
# in every training loop. Running loss, running accuracy,
# moving averages — all this shape.

class RunningStats:
    def __init__(self):
        self._counter = 0
        self._runningSum = 0

    def update(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self._counter += 1
            self._runningSum += value
        else:
            raise TypeError("value must be numeric")
    
    def mean(self):
        if self._counter == 0:
            raise ValueError("no data")
        else:
            return self._runningSum/self._counter
        
    @property
    def count(self):
        return self._counter
    
    def reset(self):
        self._counter = 0
        self._runningSum = 0

    def __repr__(self):
        if self._counter == 0:
            return "RunningStats(n=0, mean=None)"
        else:
            return f"RunningStats(n={self._counter}, mean={(self._runningSum/self._counter):.4f})"
        


s = RunningStats()
assert s.count == 0
assert repr(s) == "RunningStats(n=0, mean=None)"

s.update(1.0)
s.update(2.0)
s.update(3.0)
assert s.count == 3
assert s.mean() == 2.0
assert repr(s) == "RunningStats(n=3, mean=2.0000)"

s.reset()
assert s.count == 0
try:
    s.mean()
    raise AssertionError("expected ValueError")
except ValueError:
    pass

print("All assertions passed!")