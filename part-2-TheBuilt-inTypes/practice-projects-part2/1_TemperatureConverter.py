# P1 (Easy) — Temperature Converter
# Ask the user for a temperature in Celsius.
# Print it converted to Fahrenheit and Kelvin, both to 2 decimal places, using f-strings.

celsius = float(input("Write the temperature in celsius -> "))

fahr = (celsius * 1.8) + 32
kel = celsius + 273.15

print(f"The temperature in Fahrenheit is {fahr:.2f}")
print(f"The temperature in Kelvin is {kel:.2f}")