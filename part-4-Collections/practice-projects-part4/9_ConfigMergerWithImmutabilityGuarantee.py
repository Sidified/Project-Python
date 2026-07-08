# H2 Config Merger with Immutability Guarantee

# You have a base config and a list of experiment-specific overrides:
# base_config = {
#     "learning_rate": 0.001,
#     "batch_size": 32,
#     "epochs": 10,
#     "optimizer": "adam",
#     "dropout": 0.1,
# }

# overrides = [
#     {"learning_rate": 0.01, "dropout": 0.2},
#     {"batch_size": 64, "optimizer": "sgd"},
#     {"epochs": 20},
# ]

# For each override in overrides, produce a merged config that combines
# base_config with the override (override wins on conflicts).
# Store the results in a list experiment_configs.

# Critical requirement: after producing all the merged configs,
# base_config must be completely unchanged. Both its keys and its values
# must be identical to what they were at the start. Verify this by:

# Recording id(base_config) and a snapshot of it at the start.
# Recording id(base_config) at the end — must match.
# Comparing key-by-key that no value in base_config has been mutated.
# Print base_config integrity: True/False.

# Then print each experiment config on its own line, prefixed with Experiment N:.

# Verification: all four experiment configs must have all five keys.
# base_config integrity check must return True. Also assert
# experiment_configs[0]["learning_rate"] == 0.01 and
# base_config["learning_rate"] == 0.001 — if the second one
# is 0.01, you shared a reference.

# Why this matters: this is literally what every ML experiment
# runner does. Mutating a shared base config across experiments
# is the #1 source of "why do all my runs have the same hyperparameters" bugs.

base_config = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 10,
    "optimizer": "adam",
    "dropout": 0.1,
}
id1 = id(base_config)

overrides = [
    {"learning_rate": 0.01, "dropout": 0.2},
    {"batch_size": 64, "optimizer": "sgd"},
    {"epochs": 20},
]

experiment_configs = []


for i in range(0, len(overrides)):
    ex_con = {}
    for key in base_config:
        if  key in overrides[i]:
            ex_con[key] = overrides[i][key]
        else:
            ex_con[key] = base_config[key]
    experiment_configs.append(ex_con)

print(experiment_configs)

id2 = id(base_config)
print("base_config integrity:",id1==id2)

i = 1
for items in experiment_configs:
    print(f"Experiment {i}: {items}")
    i+=1

print(experiment_configs[0]["learning_rate"] == 0.01)
print(base_config["learning_rate"] == 0.001)