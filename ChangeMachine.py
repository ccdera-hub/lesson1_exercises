#Change machine: Ask for an amount of pennies as an integer. Print how many pounds, pence, and leftover pennies that makes using UK currency breakdown:
#1 pound = 100 pence.
#Also break the remaining pence into 50p, 20p, 10p, 5p, 2p, 1p coins (use // and %).

pennies = int(input("Pennies: "))
pounds = pennies // 100 # how many pounds
remaining = pennies % 100 # how many pence
print(f"{pounds} pound(s), {remaining} pence(s)")

for coin in [50, 20, 10, 5, 2, 1]:
    count = remaining // coin
    remaining %= coin

    print(f"{coin}p x {count}")
