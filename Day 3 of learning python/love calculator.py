print("Welcome to the Love Calculator!")

name1 = input("what is your name? \n")
name2 = input("what is their name? \n")


combine = name1 + name2

add = combine.lower()


t = add.count("t")
r = add.count("r")
u = add.count("u")
e = add.count("e")

true = t + r + u + e


l = add.count("l")
o = add.count("o")
v = add.count("v")
e = add.count("e")

love = l + o + v + e


addition = int(str(true) + str(love))

if addition < 10 or addition > 90 :
    print(f"your score is {addition}, you go together like coke and mentos.")

elif addition >= 40 and addition <= 50 :
    print(f"your score is {addition}, you are alright together.")

else :
    print(f"your score {addition}")
 







