student_height = input("input a list of student heights ",).split()

for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
# print(student_height)

# 156 178 165 171 187

addition = 0

for height in student_height:
  addition += height
# print(addition)


adding = 0 
for student in student_height:
  adding += 1
# print(adding)


average = round(addition / adding)
print(average)






