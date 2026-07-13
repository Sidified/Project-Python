# E1 — Corpus Round-Trip

# Write a list of 10 sentences (make them up — they can be about anything) to a
# file at data/corpus.txt, one sentence per line. Then read it back and compute:

# Total line count
# Total word count
# Average words per line (2 decimals)
# Longest line (the line itself, and its word count)

# Print all four. Use with open(...) for both the write and the read.
# Never call .close() manually.

# Verification: assert that the total line count matches
# the number of sentences you wrote. Assert that the sum
# of words-per-line across all lines equals your total word count.

sentences = ["Birds sing\n",
"The cat slept peacefully\n",
"She quickly solved the tricky puzzle\n",
"A bright rainbow appeared after the heavy rain\n",
"My grandfather tells fascinating stories every winter evening\n",
"The little puppy chased butterflies across the green field happily\n",
"Learning Python consistently builds confidence and improves problem solving skills\n",
"An old lighthouse stood proudly against crashing waves despite the powerful storm\n",
"Every weekend we cook delicious meals together because experimenting with recipes is surprisingly fun\n",
"Although the mountain trail looked intimidating at first, everyone reached the summit with smiles before sunset"]

lineCount = 0
wordCount = 0
maxLine = [""]

with open("part-6-StructuringRealPrograms/practice-projects-part6/data/corpus.txt", "w") as cp:
    cp.writelines(sentences)

with open("part-6-StructuringRealPrograms/practice-projects-part6/data/corpus.txt", "r") as cp:
    for line in cp:
        lineCount+=1
        wordCount+=len(line.split())
        if len(maxLine[0].split()) < len(line.split()):
            maxLine[0] = line

avgWordPerLine = wordCount/lineCount

assert lineCount == 10
assert sum(len(sentence.split()) for sentence in sentences) == wordCount
print("All assertions passed!")

print(f"The total number of lines are -> {lineCount}")
print(f"The total number of words in all lines combined are -> {wordCount}")
print(f"The average number of words per line, upto two decimal places are -> {avgWordPerLine:.2f}")
print(f"The number of words in the longest line are -> {len(maxLine[0].split())}")
print(f"The line with maximum number of words is -> '{(maxLine[0])}'")