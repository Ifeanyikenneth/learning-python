print("Welcome to tip calculator.")
bill = float(input("what was the total bill? $"))
perc = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("how many people to split the bill? "))
             

bill_perc = bill * perc / 100 + bill

bill_add = bill_perc / split

final = round(bill_add, 2)
final = "{:.2f}".format(bill_add)

print(f"Each person should pay: ${final}")



 


