# M3 — CSV → JSON Converter with Type Coercion

# Write data/models.csv with this content:
# name,accuracy,latency_ms,timestamp
# gpt-4,0.87,340,2026-01-15
# claude-opus,0.91,280,2026-01-15
# llama-70b,0.82,190,2026-01-15
# mistral-7b,0.76,95,2026-01-15

# Then write csv_to_json(csv_path, json_path) that:
# -> Reads the CSV using the csv.DictReader
# -> Converts each row into a dict with proper types: accuracy → float,
#    latency_ms → int, name and timestamp stay as strings
# -> Writes the resulting list of dicts to json_path as a
#    valid JSON array (use json.dump with indent=2)

# Verification: after running, open the JSON file and load it.
# assert len(loaded) == 4,
# assert type(loaded[0]["accuracy"]) == float,
# assert type(loaded[0]["latency_ms"]) == int,
# assert loaded[0]["name"] == "gpt-4".

# Also — deliberately test the failure case: create a CSV with
# a malformed row (e.g. bad-model,not-a-number,also-broken,2026-01-15)
# and confirm what happens when int("also-broken") is called. Your
# call: either skip malformed rows with a warning, or let the
# function crash. Whichever you choose, document your choice in
# a comment. There's no single right answer, but there's a
# "you made a choice on purpose" vs "you didn't think about it" difference.

# Why this matters: CSV → JSON conversion with type coercion is what
# every data preprocessing pipeline does. And CSVs always have malformed
# rows — deciding how to handle them is a real design decision.

import csv
import json

rows = [
["name", "accuracy" ,"latency_ms", "timestamp"],
["gpt-4", "0.87" ,"340", "2026-01-15"],
["claude-opus", "0.91" ,"280", "2026-01-15"],
["llama-70b", "0.82" ,"190", "2026-01-15"],
["mistral-7b", "0.76", "95", "2026-01-15"]
]
csv_path = "part-6-StructuringRealPrograms/practice-projects-part6/data/models.csv"
json_path = "part-6-StructuringRealPrograms/practice-projects-part6/data/models.json"
with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

def csv_to_json(csv_path, json_path):
    dictList = []
    with open(csv_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key in row:
                if key == "accuracy":
                    row[key] = float(row[key])
                elif key == "latency_ms":
                    row[key] = int(row[key])
            dictList.append(row)
    with open(json_path, "w") as f:
        json.dump(dictList, f, indent=2)

csv_to_json(csv_path, json_path)

with open(json_path, "r") as file:
    content = json.load(file)

assert len(content) == 4
assert type(content[0]["accuracy"]) == float
assert type(content[0]["latency_ms"]) == int
assert content[0]["name"] == "gpt-4"


# Design choice for FAILURE CASE:
# If a CSV row contains invalid numeric data (e.g. "not-a-number" or "also-broken"),
# this function intentionally lets float() or int() raise an exception.
# We fail fast so that malformed data is detected immediately instead of silently
# skipping rows and producing incomplete output.

rows_2 = [
["name", "accuracy" ,"latency_ms", "timestamp"],
["bad_model", "abcXYZ" ,"broken", "2026-01-15"]
]

bad_csv_path = "part-6-StructuringRealPrograms/practice-projects-part6/data/bad_models.csv"
bad_json_path = "part-6-StructuringRealPrograms/practice-projects-part6/data/bad_models.json"
with open(bad_csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows_2)

try:
    csv_to_json(bad_csv_path, bad_json_path)

    assert False, "Expected ValueError for malformed CSV row"

except ValueError:
    print("Malformed CSV test passed!")

print("All assertions passed!")