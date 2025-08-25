#Temperature converter: Ask for Celsius; print Fahrenheit using F = C * 9/5 + 32.

Celsius = float(input("Enter the Celsius value: "))
Fahrenheit = Celsius * (9 / 5) + 32

print(f"Celsius {Celsius} into Fahrenheit is {Fahrenheit}.")