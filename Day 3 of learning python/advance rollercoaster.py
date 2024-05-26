print("Welcome to my rollercoaster")

tall = int(input("how tall are you? "))

if tall >= 120:
    print("you can ride")

    age = int(input("what is your age? "))
    if age < 12:
        print("please pay $5.")

    elif age <= 18:
            print("please pay $7.")

    else :
        print("please pay $12.")


else :
    print("sorry you cant ride")
