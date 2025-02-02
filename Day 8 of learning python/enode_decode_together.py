alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decryrt:\n ")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text, shift, direction):
  end_text = ""
  for letter in text:
    position = alphabet.index(letter)
    if direction == "encode":
      position + shift 
    else:
      position - shift
  new_latter = alphabet[position]
  end_text += new_latter
  print(f"Here's the {direction} result: {end_text}")

ceaser(text=text, shift=shift, direction=direction)



    











