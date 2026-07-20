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

baseConfig = load_config(path)
print("")
print("---------------- PART-1 -------------------------")
print("")
print("This is the base-config ->")
print("")
print(baseConfig)
# -----------------------------------------------------------------------


# ------------------------------ PART-2 ---------------------------------

expDict = {}

for override in experiments:
    name = override["name"]

    merged = {
        **baseConfig,
        **{k: v for k, v in override.items() if k != "name"}
    }

    expDict[name] = merged

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

    jsonlpath = f"part-6-StructuringRealPrograms/practice-projects-part6/data/{item}.jsonl"

    with open(jsonlpath, "w") as f:

        for i in logs:
            jsonLogs = {}

            jsonLogs["Experiment"] = item
            jsonLogs["Epoch"] = i[0]
            jsonLogs["Loss"] = i[1]
            jsonLogs["Accuracy"] = i[2]

            logsList.append(jsonLogs)

            json.dump(jsonLogs, f)
            f.write("\n")

print("")
print("---------------- PART-4 -------------------------")
print("")
print(logsList)
# -----------------------------------------------------------------------


# ------------------------------ PART-5 ---------------------------------

def read_jsonl(jsonlpath):
    records = []

    with open(jsonlpath, "r") as file:
        for line_number, line in enumerate(file, start=1):
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Warning: Skipping invalid JSON on line {line_number} in {jsonlpath}: {e}")

    return records


loadedLogs = {}

for expName in expDict:
    jsonlpath = f"part-6-StructuringRealPrograms/practice-projects-part6/data/{expName}.jsonl"
    loadedLogs[expName] = read_jsonl(jsonlpath)

print("")
print("---------------- PART-5 -------------------------")
print("")

for expName, records in loadedLogs.items():
    print(f"{expName} ->")
    print(records)
    print("")
# -----------------------------------------------------------------------


# ------------------------------ PART-6 ---------------------------------
summary = {}

for expName, records in loadedLogs.items():

    epochNum = len(records)
    finalLoss = records[-1]["Loss"]

    minLoss = [records[0]["Loss"], records[0]["Epoch"]]

    acc = []

    for record in records:

        acc.append(record["Accuracy"])

        if record["Loss"] < minLoss[0]:
            minLoss[0] = record["Loss"]
            minLoss[1] = record["Epoch"]

    avgAcc = sum(acc) / len(acc)

    summary[expName] = {
        "num_epochs": epochNum,
        "final_loss": finalLoss,
        "best_loss": minLoss[0],
        "best_epoch": minLoss[1],
        "avg_accuracy": avgAcc
    }

print("")
print("---------------- PART-6 -------------------------")
print("")

for expName, stats in summary.items():
    print(expName)
    print(stats)
    print("")
# -----------------------------------------------------------------------


# ------------------------------ PART-7 ---------------------------------

rows = [["experiment", "num_epochs", "final_loss", "best_loss", "best_epoch", "avg_accuracy"]]

for expName, stats in summary.items():
    rows.append([
        expName,
        stats["num_epochs"],
        stats["final_loss"],
        stats["best_loss"],
        stats["best_epoch"],
        stats["avg_accuracy"]
    ])

with open(
    "part-6-StructuringRealPrograms/practice-projects-part6/data/summary.csv",
    "w",
    encoding="utf-8",
    newline=""
) as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# -----------------------------------------------------------------------


# -------------------------- VERIFICATIONS ------------------------------

# Assertion - 1
with open("part-6-StructuringRealPrograms/practice-projects-part6/data/summary.csv", "r") as f:
    rows = list(csv.reader(f))

assert len(rows) == len(summary) + 1


# Assertion - 2
summary_names = {row[0] for row in rows[1:]}

expected = {exp["name"] for exp in experiments}

assert summary_names == expected


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
for expName in expDict:
    assert len(loadedLogs[expName]) == expDict[expName]["epochs"]


print("----------------------")
print("All assertions passed!")
print("----------------------")