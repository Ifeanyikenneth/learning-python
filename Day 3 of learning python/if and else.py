name = int(input("which number do you want to check: "))

name1 = name % 2


if name1 >0:
    print("This is an odd number")
else :
    print("This is an even number")

    
#or

name = int(input("which number do you want to check: "))

if name % 2 == 0:
    print("This is an even number")
else :
      print("This is an odd number")
