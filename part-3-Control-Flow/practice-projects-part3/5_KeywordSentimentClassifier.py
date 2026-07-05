# M2 — Keyword Sentiment Classifier

# Hardcode: review = "The model output was surprisingly good but the latency was terrible."
# Define three keyword sets (as hardcoded lists is fine):
# pythonpositive = ["good", "great", "excellent", "love", "amazing"]
# negative = ["bad", "terrible", "hate", "awful", "poor"]
# Lowercase the review, then check how many positive and
# negative keywords appear (use the in operator per keyword).

# Classify:
# more positives → "positive"
# more negatives → "negative"
# equal (including zero of each) → "neutral"

# Print the counts and the classification.
# Verification: For the given review, positive=1 ("good"), negative=1 ("terrible"),
# so → "neutral". Change the review to "This is great and
# amazing" — expect "positive", counts 2 and 0.

review = "The model output was surprisingly good but the latency was terrible."

pythonpositive = ["good", "great", "excellent", "love", "amazing"]
negative = ["bad", "terrible", "hate", "awful", "poor"]

review = review.lower()
pos = 0
neg = 0
result =""
for p in pythonpositive:
    if p in review:
        pos+=1
for p in negative:
    if p in review:
        neg+=1

if pos == neg:
    result = "This 'review' statement is neutral"
elif pos>neg:
    result = "This 'review' statement is positive"
elif pos<neg:
    result = "This 'review' statement is negativee"


print(f'''Total positives in review is -> {pos}
Total negatives in p is -> {neg}''')

print(result)