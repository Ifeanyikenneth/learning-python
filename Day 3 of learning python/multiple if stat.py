print("Welcome to my rollercoaster")

tall = int(input("how tall are you? "))
bill = 0

if tall >= 120:
    print("you can ride")

    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("child tickets are $5.")

    elif age <= 18:
        bill = 7
        print("youth ticket are $7.")

    else :
        bill = 12
        print("adult ticket are $12.")

    name = input("Do you want a photo taken? Y or N. ")
    if name == "y":
        bill = bill + 3

        print(f"your final bill is ${bill}")

        


else :
    print("sorry you cant ride")
