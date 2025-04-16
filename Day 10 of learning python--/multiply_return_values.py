def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return f"You typed in an invalid code."
 
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name(input("what is your first name?"), input("what is your second name?")))
  

# note you: the return function mark the end of that line of code 
# firstly i check if the l or f name result to empty str them it should return the set of str in inputed
# secondly at the finaly print statement from the last code, i allow the user to check the str by allowing them to write it out by using the input function on it.




# return in a function simply tell the computer that this is where the line of code end or end of the function














