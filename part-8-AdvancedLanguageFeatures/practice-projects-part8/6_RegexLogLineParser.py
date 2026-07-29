# M4 — Regex Log Line Parser

# Given log lines like:

# 2026-07-15 14:32:07 [INFO] user_id=1234 action=login duration_ms=45
# 2026-07-15 14:32:12 [ERROR] user_id=5678 action=purchase duration_ms=2341 error=timeout

# Write parse_log_line(line) using regex that returns a dict:
# {
#     "timestamp": "2026-07-15 14:32:07",
#     "level": "INFO",
#     "fields": {"user_id": "1234", "action": "login", "duration_ms": "45"}
# }

# Requirements:
# -> Use raw strings (r"...") for patterns
# -> Timestamp and level captured via one regex with named groups
# -> Key-value pairs extracted via re.findall on the rest of the line
# -> Return None on malformed lines (missing timestamp or level) — document this choice in a comment

# Verification:
# result = parse_log_line("2026-07-15 14:32:07 [INFO] user_id=1234 action=login")
# assert result["timestamp"] == "2026-07-15 14:32:07"
# assert result["level"] == "INFO"
# assert result["fields"] == {"user_id": "1234", "action": "login"}

# assert parse_log_line("garbage without a timestamp") is None

# Smallest problem in the set. Regex is low priority but you need
# functional literacy. Don't spend an hour perfecting the pattern;
# get it working and move on.

# Why: log parsing is unavoidable in real systems. When a service emits
# structured logs that aren't JSON, regex is often what stands between
# you and useful debugging.

import re

def parse_log_line(line):
    parsed_dict = {}

    timestamp_level = re.search(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>[^\]]+)\]", line)

    # Return None instead of raising an exception for malformed log lines.
    if not timestamp_level:
        return None
    
    parsed_dict["timestamp"] = timestamp_level.group("timestamp")
    parsed_dict["level"] = timestamp_level.group("level")

    kv_pairs = re.findall(r"(\w+)=(\w+)", line)
    result_dict = dict(kv_pairs)
    parsed_dict["fields"] = result_dict

    return parsed_dict

# VERIFICATION

result = parse_log_line("2026-07-15 14:32:07 [INFO] user_id=1234 action=login")
assert result["timestamp"] == "2026-07-15 14:32:07"
assert result["level"] == "INFO"
assert result["fields"] == {"user_id": "1234", "action": "login"}

assert parse_log_line("garbage without a timestamp") is None

print("All assertions passed!")