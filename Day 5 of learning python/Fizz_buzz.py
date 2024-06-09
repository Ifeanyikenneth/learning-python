# student_height = input("input a list of student heights ",).split()

# for n in range(0, len(student_height)):
#   student_height[n] = int(student_height[n])

for student in range(1,101):
  if student % 3 == 0 and student % 5 == 0:
    print("FizzBuzz")
  elif student % 3 == 0:
    print("Fizz")
  elif student % 5 == 0:
    print("Buzz")
  else:
    print(student)

  



