#Simple interest: Ask for principal P,
# rate r (as a percent),
# time t in years.
# Compute interest I = P * (r/100) * t and
# amount A = P + I.

principal = float(input("Enter principal value: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the number of years: "))

interest = principal * (rate/100) * time
amount = principal + interest

print(f"Interest: {interest}")
print(f"amount: {amount}")