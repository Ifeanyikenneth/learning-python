print("Welcome to the tip calculator.")

bill = float(input("what is you total bill? $"))

tip = int(input("what percentage tip would you lke to get? 10, 12, or 15? "))

split = int(input("how many people to split the bill? "))

tip_bill = tip * bill / 100 + bill

result = tip_bill / split

final = round(result,2)

print(f"Each person should pay: ${final}")


