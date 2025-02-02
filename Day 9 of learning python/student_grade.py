# Student_grades = {
#   "Harry": "Exceeds Expectation.",
#   "Ron": "Acceptable",
#   "Hermione": "Oustanding",
#   "Draco": "Acceptable",
#   "Neville": "Fail", 
# }

# print(Student_grades)


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Oustanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectation"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"



print(student_grades)
    
    
    
















