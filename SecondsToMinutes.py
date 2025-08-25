#Seconds to minutes: Ask the user for a number of seconds (integer). Print how many whole minutes and remaining seconds that is. Example: 125 → 2 minute(s) and 5 second(s).

seconds = int(input("Enter number of seconds:"))

minute = seconds // 60
second = seconds % 60

print(f"{minute} minute(s) and {second} second(s)")