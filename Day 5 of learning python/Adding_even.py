student_height = input("input a list of student heights ",).split()

for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])


addition = 0

for student in range(1,101):
  if student % 2 == 0:
    addition += student

print(addition)
 
# or


adding = 0
for teacher in range(2, 101, 2):
  adding += teacher
print(adding)
  

