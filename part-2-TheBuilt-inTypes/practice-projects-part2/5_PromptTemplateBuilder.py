# Ask the user for two inputs: a topic and an audience.
# Build and print a multi-line prompt that looks like:
# ----------------------------------------
# System: You are an expert educator.
# User request:
#  Topic: <topic>
#  Audience: <audience>
#  Format: 3 short paragraphs
#  Style: Simple, no jargon.

# Please begin your explanation below.
# -----------------------------------------
# Use a triple-quoted f-string. Substitute the inputs into the right spots.

topic = input("Please enter your topic -> ")
audience = input("Please enter your audience -> ")

prompt = (f'''System: You are an expert educator.
User request:
    Topic: {topic}
    Audience: {audience}
    Format: 3 short paragraphs
    Style: Simple, no jargon.
            
Please begin your explanation below.''')

print(prompt)
print(repr(prompt))