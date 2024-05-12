age = input("what is your current age? ")

age1 = int(age)

years = 90 - age1

year = years * 365
month = years * 12
week = years * 52

result = f" you have {year} days, {week} weeks, and {month} months left"

print(result)
 
