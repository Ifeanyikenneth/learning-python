print("Welcome to the tip calculator.")

bill = float(input("what is the total bill? $"))

percentage = int(input("what percentage tip would you like to give? 10, 12, 15? "))

people = int(input("how many people to split the bill? "))

bill_per = bill * percentage / 100 + bill

together = bill_per / people

final = round(together, 2)
final = "{:.2f}".format(together)

print(f"Each person should pay: ${final}")

