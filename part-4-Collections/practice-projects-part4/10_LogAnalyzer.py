# BOSS — Log Analyzer
# You're given a list of raw training log lines from multiple experiments:
# logs = [
#     "exp=A epoch=1 loss=0.9 acc=0.55",
#     "exp=A epoch=2 loss=0.7 acc=0.62",
#     "exp=B epoch=1 loss=0.85 acc=0.58",
#     "exp=A epoch=3 loss=0.55 acc=0.71",
#     "exp=B epoch=2 loss=0.65 acc=0.68",
#     "exp=C epoch=1 loss=0.95 acc=0.50",
#     "exp=B epoch=3 loss=0.5 acc=0.75",
#     "exp=A epoch=4 loss=0.45 acc=0.78",
#     "exp=C epoch=2 loss=0.8 acc=0.55",
#     "exp=C epoch=3 loss=0.7 acc=0.60",
# ]

# Parse and summarize:
# 1. Parse each log line into a dict: {"exp": "A", "epoch": 1, "loss": 0.9, "acc": 0.55}.
#    Types matter — epoch is int, loss and acc are float, exp is str. Store all parsed dicts in a list.

# 2. Build a dict by_exp where each key is an experiment
#    name ("A", "B", "C") and the value is a list of that experiment's parsed log entries.

# 3. For each experiment, compute and print:
#    -> Number of epochs recorded
#    -> Final loss (last epoch's loss)
#    -> Best (lowest) loss and which epoch it was in
#    -> Average accuracy across all epochs (2 decimal places)

# Format like this (exact format):
# Experiment A: 4 epochs | final_loss=0.4500 | best_loss=0.4500 @ epoch 4 | avg_acc=0.67
# Experiment B: 3 epochs | final_loss=0.5000 | best_loss=0.5000 @ epoch 3 | avg_acc=0.67
# Experiment C: 3 epochs | final_loss=0.7000 | best_loss=0.7000 @ epoch 3 | avg_acc=0.55

# Finally, print the name of the best-performing experiment overall,
# defined as: highest average accuracy.
# Format: Best experiment: X (avg_acc=0.67).
# If there's a tie, any tied experiment is fine.

# Verification you must include in your code:
# assert len(parsed_logs) == len(logs) — didn't drop any lines
# assert sum(len(v) for v in by_exp.values()) == len(logs) — didn't drop any lines during grouping
# For each experiment: assert len(by_exp[exp]) > 0

# Why this problem: this is what real ML experiment
# tracking looks like at its core (before tools like W&B or MLflow).
# If you can build this cleanly, you can prototype an experiment tracker.

logs = [
    "exp=A epoch=1 loss=0.9 acc=0.55",
    "exp=A epoch=2 loss=0.7 acc=0.62",
    "exp=B epoch=1 loss=0.85 acc=0.58",
    "exp=A epoch=3 loss=0.55 acc=0.71",
    "exp=B epoch=2 loss=0.65 acc=0.68",
    "exp=C epoch=1 loss=0.95 acc=0.50",
    "exp=B epoch=3 loss=0.5 acc=0.75",
    "exp=A epoch=4 loss=0.45 acc=0.78",
    "exp=C epoch=2 loss=0.8 acc=0.55",
    "exp=C epoch=3 loss=0.7 acc=0.60",
]

# Part-1 ---------------------------------------

parsedLogs = []

for items in logs:
    parsedLogs.append(items.split())
# print(parsedLogs)

newParsed = []
for items in parsedLogs:
    container = []
    for i in items:
       a = i.replace('=', ' ')
       aList = a.split()
       container.append(aList)
    newParsed.append(container)
# print(newParsed)

dictList = []
for items in newParsed:
    parsedDict = {}
    for i in items:
        parsedDict[i[0]] = i[1]
    dictList.append(parsedDict)

# print(dictList)

for items in dictList:
    items["epoch"] = int(items["epoch"])
    items["loss"] = float(items["loss"])
    items["acc"] = float(items["acc"])

print(dictList)
# ----------------------------------------------

# Part-2 ---------------------------------------

by_exp = {}
logsA = []
logsC = []
logsB = []

for items in dictList:
    if items['exp'] == 'A':
        logsA.append(items)
    elif items['exp'] == 'B':
        logsB.append(items)
    else:
         logsC.append(items)

by_exp['A'] = logsA
by_exp['B'] = logsB
by_exp['C'] = logsC

print(by_exp)
# ----------------------------------------------

# Part-3 ---------------------------------------

numEp = {}
for keys in by_exp:
    numEp[keys] = (len(by_exp[keys]))
print(numEp)

finalLoss = {}
finalLossAtEp = {}
for keys in by_exp:
    for items in by_exp[keys]:
        idx = numEp[keys] - 1
        finalLoss[keys] = by_exp[keys][idx]['loss']
        finalLossAtEp[keys] = f"best_loss={by_exp[keys][idx]['loss']:.4f} @ epoch {numEp[keys]}"

print(finalLoss)
print(finalLossAtEp)

avgAcc = {}
for keys in by_exp:
    tot_acc = 0
    for items in by_exp[keys]:
        tot_acc += items["acc"]
    avgAcc[keys] = tot_acc/(len(by_exp[keys]))

print(avgAcc)
    
# ----------------------------------------------

# Part-4 ---------------------------------------

for keys in by_exp:
    print(f"Experiment {keys}: {numEp[keys]} epochs | final_loss={finalLoss[keys]:.4f} | {finalLossAtEp[keys]} | {avgAcc[keys]:.2f}")

# ----------------------------------------------