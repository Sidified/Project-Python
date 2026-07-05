# Easy1(E1) — Confidence Classifier
# Ask the user for a confidence score (a float between 0 and 1). Classify it:

# < 0.3 → "low confidence"
# 0.3 ≤ score < 0.7 → "medium confidence"
# ≥ 0.7 → "high confidence"

# Print the classification.
# Verification: Your code must produce the correct label
# when tested with 0, 0.3, 0.699, 0.7, and 1.
# If your boundary comparisons are off (using < vs <= wrong), one of these will trip you.

conf = float(input("Please enter your confidence score between 0 and 1 -> "))

if (conf > 1 or conf < 0):
    print("ERROR! You entered an INVALID confidence score")
else:
    if conf>=0.7:
        print("Your confindence is HIGH!")
    elif 0.7 > conf >= 0.3:
        print("Your confidence is MEDIUM")
    else:
        print("Your confidence is LOW")