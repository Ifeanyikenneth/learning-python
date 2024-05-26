print("Welcome to Python PIzza Deliveries!")
add = 0

pizza = input("what size of pizza do you want? S, M, or L ")

if pizza == "s":
    print("Small pizza: $15")

if pizza == "m":
    print("Medium pizza: $20")

if pizza == "l":
    print("Large pizza: $25")



want = input("Do you want pepperoni? Y or N ")

if want == "y":
    if pizza == "s":
        add += 15
        add += 2

    elif pizza == "m":
        add += 20
        add += 3

    elif pizza == "l":
        add += 25
        add += 3
      
you = input("Do you wan extra cheese? Y or N ")
if you == "y":
    add += 1


print(f"Your final bill is: ${add}")




    

    
    
        
   
        
         
    


    
    
    
    

   

    
