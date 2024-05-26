# print("Welcome to python pizza deliveires.")

# add = 0

# size = input("what size pizza do you want? S, M, or L ").lower()
# want = input("do you want pepperoni? Y or N ").lower()
# cheese = input("do you want extra cheese? Y or N ").lower()


# if size == "s":
#   print("small pizza is $15")
# if size == "m":
#   print("medium pizza is $20")
# if size == "l":
#   print("large pizza is $25")

# if want  == "y":
#   if size == "s":
#    add += 15
#    add += 2

# if want == "y":
#   if size == "m":
#     add += 20
#     add += 3


# if want == "y":
#   if size == "l":
#     add += 25
#     add +=3


# if cheese == "y":
#   add += 1

# print(f"your final bill is {add}")


import random 

name1 = input("give me everybody names, seperated by a comma.")

names = name1.split(",")  

combine = len(names)

exchange = random.randint(0, combine - 1)

final = names[exchange]

print(f"{final} is going to pay the meal today.")


import random 

name1 = input("give me everybody names, seperated by a comma.")

names = name1.split(",")  

combine = random.choice(names)

print(f"{combine} is going to but the meal today.")