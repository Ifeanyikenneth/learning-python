import random 

every_body = input("Give me everybody's names, seperated by comma. ")
names = every_body.split(",")


every_combine = len(names)
who_to_pay = random.randint(0, every_combine - 1)
final = names[who_to_pay]


print(f"{final}, is going to pay the bill today.")



