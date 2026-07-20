# BOSS — Mini Experiment Tracker

# End-to-end. This uses everything in Part VI plus recalls from Parts IV and V.

# Setup:
# 1. Write a base config to data/base_config.json:

#  {
#        "learning_rate": 0.001,
#        "batch_size": 32,
#        "epochs": 5,
#        "optimizer": "adam"
#  }

# 2. Define a list of experiment overrides in your Python code:

#    experiments = [
#        {"name": "exp_A", "learning_rate": 0.01},
#       {"name": "exp_B", "batch_size": 64, "optimizer": "sgd"},
#        {"name": "exp_C", "learning_rate": 0.005, "epochs": 3},
#    ]

# The pipeline your code must do:
# For each experiment override:
# 1. Load the base config (with error handling — reuse
#    load_config from M1 or write a fresh one).
# 2. Merge it with the override to produce a full config
#    for this experiment. Must not mutate the base
#    config — remember Part IV's H2 lesson.
# 3. Simulate training: generate a fake list
#    of (epoch, loss, accuracy) tuples. Loss starts at 0.9 and
#    decreases by roughly 0.15 per epoch (with a tiny bit of noise
#    if you want — random.uniform is fine). Accuracy starts at 0.5
#    and increases by roughly 0.08 per epoch. Number of epochs
#    comes from the merged config.
# 4. Write the epoch-by-epoch log to data/<exp_name>.jsonl, one
#    JSON line per epoch. Each line should include:
#    experiment, epoch, loss, accuracy.

# Then aggregate:

# 5. Read each of the three JSONL files back
#    (use read_jsonl from M2, or a fresh version).
# 6. Compute per-experiment: number of epochs, final loss,
#    best (min) loss and which epoch, average accuracy.
# 7. Write a summary CSV at data/summary.csv with columns:
#    experiment,num_epochs,final_loss,best_loss,best_epoch,avg_accuracy.

# Verification:

# -> Read data/summary.csv back and assert it has 3 data rows + 1 header row.
# -> Assert every experiment name from your overrides is present in the summary.
# -> Assert the base config is not mutated — after all
#    experiments run, load data/base_config.json fresh and check
#    that learning_rate is still 0.001 (not overridden by exp_A's 0.01).
#    If you mutated the base config in memory, this would still pass because
#    you're reloading from disk — so ALSO assert (before reloading)
#    that your in-memory base_config variable is unchanged.
# -> Assert each JSONL file has the correct number of lines matching
#    the merged epochs value.

# Parts recalled:
# -> Part IV: dict manipulation, grouping, aggregation
# -> Part V: functions, defaults, *args/**kwargs (if you use them for the merge)
# -> Part VI: modules, exceptions, file I/O, JSON, CSV — all four chapters

# Why this problem: this is the skeleton of every ML
# experiment tracker (W&B, MLflow, TensorBoard) at its core — sans the
# fancy UI. If you can build this cleanly, you've built the thing you'll eventually use.

# ------------------------------ PART-1 ---------------------------------

import json
import csv

class ConfigError(Exception):
    pass

item = {
       "learning_rate": 0.001,
       "batch_size": 32,
       "epochs": 5,
       "optimizer": "adam"
       }

path = "part-6-StructuringRealPrograms/practice-projects-part6/data/base_config.json"

with open(path, "w") as file:
    json.dump(item, file, indent=2)

experiments = [
       {"name": "exp_A", "learning_rate": 0.01},
       {"name": "exp_B", "batch_size": 64, "optimizer": "sgd"},
       {"name": "exp_C", "learning_rate": 0.005, "epochs": 3},
   ]

def load_config(path):
    try:
        with open(path, "r") as file:
            data = file.read()
    except FileNotFoundError:
        raise ConfigError(f"Config file not found: {path}")
    
    try:
        fileDict = json.loads(data)
    except (json.JSONDecodeError):
        raise ConfigError(f"Config file is not valid JSON: {path}")
        
    return fileDict
# -----------------------------------------------------------------------


# ------------------------------ PART-2 ---------------------------------

baseConfig = load_config(path)
print("")
print("---------------- PART-1 -------------------------")
print("")
print("This is the base-config ->")
print("")
print(baseConfig)

expDict = {}

for i in experiments:

    name = i["name"]
    exp = baseConfig.copy()

    if name in expDict:
        continue
    else:
        for key in i:    
            if key in exp:
                exp[key] = i[key]
                expDict[name] = exp
print("")
print("---------------- PART-2 -------------------------")
print("")
print("This is the formatted dictionary of all the experiments ->")
print("")
print(expDict)
# -----------------------------------------------------------------------


# ------------------------------ PART-3 ---------------------------------

# simList = {'exp_A': [], 'exp_B': [], 'exp_C': []}
simList = {keys: [] for keys in expDict}

# (epoch, loss, accuracy)

for keys in simList:
    loss = 0.90
    acc = 0.5
    for i in range(1, expDict[keys]['epochs'] + 1):
        expList = []

        expList.append(i)

        expList.append(loss)
        loss-=0.15

        expList.append(acc)
        acc+=0.08

        simList[keys].append(tuple(expList))

print("")
print("---------------- PART-3 -------------------------")
print("")
print("This is the simulated training data")
print("")
print(simList)
# -----------------------------------------------------------------------


# ------------------------------ PART-4 ---------------------------------
logsList = []
for item in simList:
    logs = simList[item]
    for i in logs:
        jsonLogs = {}
        jsonLogs["Experiment"] = item
        jsonLogs["Epoch"] = i[0]
        jsonLogs["Loss"] = i[1]
        jsonLogs["Accuracy"] = i[2]
        logsList.append(jsonLogs)

path_A = "part-6-StructuringRealPrograms/practice-projects-part6/data/exp_A.jsonl"
path_B = "part-6-StructuringRealPrograms/practice-projects-part6/data/exp_B.jsonl"
path_C = "part-6-StructuringRealPrograms/practice-projects-part6/data/exp_C.jsonl"

open(path_A, "w").close()
open(path_B, "w").close()
open(path_C, "w").close()

for items in logsList:
    if items['Experiment'] == 'exp_A':
        with open(path_A, 'a') as f:
            json.dump(items, f)
            f.write("\n")
    elif items['Experiment'] == 'exp_B':
        with open(path_B, 'a') as f:
            json.dump(items, f)
            f.write("\n")
    elif items['Experiment'] == 'exp_C':
        with open(path_C, 'a') as f:
            json.dump(items, f)
            f.write("\n")

print("")
print("---------------- PART-4 -------------------------")
print("")
print(logsList)
# -----------------------------------------------------------------------


# ------------------------------ PART-5 ---------------------------------

def read_jsonl(path):
    records = []

    with open(path, "r") as file:
        for line in file:
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                raise("JSONDecodeError")

        return records


expA = read_jsonl(path_A)
expB = read_jsonl(path_B)
expC = read_jsonl(path_C)

print("")
print("---------------- PART-5 -------------------------")
print("")
print("Experiment A ->")
print(expA)
print("")
print("Experiment B ->")
print(expB)
print("")
print("Experiment C ->")
print(expC)
print("")
# -----------------------------------------------------------------------


# ------------------------------ PART-6 ---------------------------------

epochNumA = 0
epochNumB = 0
epochNumC = 0

finalLossA = 0
finalLossB = 0
finalLossC = 0

minLossA = []
minLossB = []
minLossC = []

accA = []
accB = []
accC = []

for i in logsList:
    if i['Experiment'] == 'exp_A':
        epochNumA +=1
        accA.append(i['Accuracy'])
        finalLossA = i['Loss']
        if len(minLossA) == 0:
            minLossA.append(i['Loss'])
            minLossA.append(epochNumA)
        elif minLossA[0] > i['Loss']:
            minLossA[0] = i['Loss']
            minLossA[1] = epochNumA
    elif i['Experiment'] == 'exp_B':
        epochNumB +=1
        accB.append(i['Accuracy'])
        finalLossB = i['Loss']
        if len(minLossB) == 0:
            minLossB.append(i['Loss'])
            minLossB.append(epochNumB)
        elif minLossB[0] > i['Loss']:
            minLossB[0] = i['Loss']
            minLossB[1] = epochNumB
    elif i['Experiment'] == 'exp_C':
        epochNumC +=1
        accC.append(i['Accuracy'])
        finalLossC = i['Loss']
        if len(minLossC) == 0:
            minLossC.append(i['Loss'])
            minLossC.append(epochNumC)
        elif minLossC[0] > i['Loss']:
            minLossC[0] = i['Loss']
            minLossC[1] = epochNumC

avgAccA = sum(accA)/len(accA)
avgAccB = sum(accB)/len(accB)
avgAccC = sum(accC)/len(accC)

print("---------------- PART-6 -------------------------")
print(epochNumA, epochNumB, epochNumC)
print(finalLossA, finalLossB, finalLossC)
print(minLossA, minLossB, minLossC)
print(avgAccA, avgAccB, avgAccC)
# -----------------------------------------------------------------------


# ------------------------------ PART-7 ---------------------------------

rows = [['experiment', 'num_epochs', 'final_loss', 'best_loss', 'best_epoch', 'avg_accuracy'],
        ['Experiment_A', epochNumA, finalLossA, minLossA[0], minLossA[1], avgAccA],
        ['Experiment_B', epochNumB, finalLossB, minLossB[0], minLossB[1], avgAccB],
        ['Experiment_C', epochNumC, finalLossC, minLossC[0], minLossC[1], avgAccC]]

with open("part-6-StructuringRealPrograms/practice-projects-part6/data/summary.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)  # Write all rows at once
# -----------------------------------------------------------------------


# -------------------------- VERIFICATIONS ------------------------------

# Assertion - 1
with open("part-6-StructuringRealPrograms/practice-projects-part6/data/summary.csv", "r") as f:
    rows = list(csv.reader(f))

assert len(rows) == 4

# Assertion - 2
summary_names = [row[0] for row in rows[1:]]

expected = {"Experiment_A", "Experiment_B", "Experiment_C"}

assert set(summary_names) == expected

# Assertion - 3
assert baseConfig["learning_rate"] == 0.001
assert baseConfig["batch_size"] == 32
assert baseConfig["epochs"] == 5
assert baseConfig["optimizer"] == "adam"

# Assertion - 4
fresh_config = load_config(path)

assert fresh_config["learning_rate"] == 0.001
assert fresh_config["batch_size"] == 32
assert fresh_config["epochs"] == 5
assert fresh_config["optimizer"] == "adam"

# Assertion - 5
assert len(expA) == expDict["exp_A"]["epochs"]
assert len(expB) == expDict["exp_B"]["epochs"]
assert len(expC) == expDict["exp_C"]["epochs"]

print("----------------------")
print("All assertions passed!")
print("----------------------")