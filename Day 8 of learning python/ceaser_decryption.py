alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decryrt:\n ")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  cipher_text = ""
  for latter in text:
    # the .index is for picking out the alphabet in the the list
    position =  alphabet.index(latter) 
    # now adding them up together
    new_position = position + shift 
    new_latter = alphabet[new_position]
    cipher_text += new_latter
  print(f"The encode text is {cipher_text}")
  
     
# note:  After you are done with your coding in a a function assignment always call out the 'parameter' and 'argument' for your code to function using the variable you use at first. 

# encrypt(text=text, shift=shift)     
      

# and what if we try to encode the word that is really close to the end of the alphabet 'z'
#  The that means it's going to show me index out of rnage that mean we will have to duplicte it agian from the last line for it to start again once


def decrypt(text, shift):
  shift_text = ""
  for latter in text:
    position = alphabet.index(latter)
    new_position = position - shift
    new_latter = alphabet[new_position]
    shift_text += new_latter
  print(f"The decode text is {shift_text}") 
    
if direction == "encode":
  encrypt(text=text, shift=shift)    
elif direction == "decode":
  decrypt(text=text, shift=shift)     














