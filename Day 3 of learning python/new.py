print('''

********________________

  ' ' ' ''
  ' ;''-;---
              *_*____*_***__*
":":""""

  _______
  
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input('you are at a cross road. where do you want to go? "left" or "right" \n')


road1 = road.lower()

if road1 == "left":
    road2 = input('you came to a lake there is an island in the middle of the lake. typr "wait" to wait for a boat. type "swim" to swim across \n').lower()

    if road2 == "wait":
        road3 = input("you arrive at the island. there is a house with 3 doors. one red, one yellow and one blue. which color do you choose? \n").lower()


        if road3 == "yellow":
            print("finally you found the treasure, you won")


        elif road3 == "red":
            print("you enter a room of fire, you failed.")

        elif road3 == "blue":
            print("you enter a room of beasts, you failed.")

        


    else :
        print("you were eaten by a shark, game over.")
        


else :
    print("you failed, game over.")







    
