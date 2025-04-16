
# Add 
def add(n1, n2):
  return n1 + n2

# subtract 
def subtract(n1, n2):
  return n1 - n2

# multiply
def multiply(n1, n2):
  return n1 * n2

# divide
def divide(n1, n2):
  return n1 / n2


"""now we are storing each of this function now inside a dictionary
whereby the keys are the symbol and the values are the name of the symbol or the function
"""
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,

}

num1 = int(input("What's the first number?: "))

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))


calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")





"""
docstring: this helps others and yourself understand the purpose of the function, class or module
 and it is typically the first statement in the function....
And it can also be used as a multi line comment """ 



  



























