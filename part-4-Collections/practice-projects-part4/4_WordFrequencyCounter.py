# M1 — Word Frequency Counter

# Hardcode:
# text = "the model predicted the cat but the actual label was dog and the model was wrong"

# Count how often each word appears.
# Then print the top 3 most frequent words in descending order of frequency, formatted as:
# 1. the (4)
# 2. model (2)
# 3. was (2)

# Ties can be broken any way; you don't need alphabetical secondary sort.

# Requirements: use a dict for counting, and sorted() with a key= function
# (lambda is fine — you haven't formally hit lambdas yet, but key=lambda kv: kv[1]
# is a 30-second concept: it's a tiny inline function that says
# "sort by the second element of each key-value pair").

# Verification: Sum of all frequency counts must equal len(text.split()). Assert this.

text = "the model predicted the cat but the actual label was dog and the model was wrong"
list = text.split()
count = {}

for item in list:
    count[item] = count.get(item, 0) + 1

sortedCount = sorted(count.items(), key=lambda item: item[1], reverse=True)

top3 = sortedCount[0:3]


for i in range(0,3):
    print(f"1. {top3[i][0]} ({top3[i][1]})")

