student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)


addition = 0 

for student in student_heights:
  if student > addition: 
    addition = student
print(f"The highest score in the class is: {addition}")
   
 
 


