#Tip calculator: Ask for bill amount (float) and tip percent (float). Print the tip and total.

Bill_Amount = float(input("Enter the bill amount: "))
Tip_Percent = float(input("Enter the tip percent: "))

Tip = Bill_Amount * (Tip_Percent / 100)
total = Bill_Amount + Tip

print(f"Print the tip is {Tip} and total {total}.")
