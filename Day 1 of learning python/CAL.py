4# prompt for user input
a = int(input ("Enter the first number: "))
b = int(input ("Enter the second number: "))

# perform operations

print("sum: {} + {} = {}".format(a,b,a+b))
print("Difference: {} - {} = {}".format(a,b,a-b))


f = a
a = b
b = f

print("a: " + str(a))
print("a: " + str(b))
