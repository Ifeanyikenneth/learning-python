# # Travel_log = {
# #   {"State": "Lagos", "Area_visited": ["Shibiri", "Ojo", "Etegbin"] "total_visit": 12},
# #   {"country": "France", "Cites_vistied"["Berlin", "hamburg", "Stuttguart"] "total_visit": 32} ,
# # }

# # {"country": "Nigeria", "State_visted"["Anambra", "Abia", "Kaduna"] "Total visit": 22}







# programming ={
#   "code": "As a programmer you have to write down your code correctly to perform a particular task",
#   "function": " A peice of code that you can easily call over and over agian",
# }
# # # calling out a item from the dictionary
# # print(programming ["code"])

# # programming ["loop"] = "The action of doing smth over and over again"
# # print(programming)

# # programming = {}
# # print(programming)

# # edit  an item in dict
# # programming["code"] = "for a program to occur you must have down your code"
# # print(programming)


# for key in programming:
#   print(key)
#   print(programming[key])


student_score = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}


# student_grade = {}
# for student in student_score:
#   score = student_score[student]
#   if score > 90:
#     student_grade[student] = "Outstanding"
#   elif score > 80:
#     student_grade[student] = "Exceeds Expectation"
#   elif score > 70:
#     student_grade[student] = "Acceptable"
#   else:
#     student_grade[student] = "Fail"


# print(student_grade)




def cal_student_grade(student_score):
  student_grade = {}
  for student in student_score:
   score = student_score[student]
   if score > 90:
    student_grade[student] = "Outstanding"
   elif score > 80:
    student_grade[student] = "Exceeds Expectation"
   elif score > 70:
    student_grade[student] = "Acceptable"
   else:
    student_grade[student] = "Fail"

  print(student_grade)
  
cal_student_grade(student_score= student_score)





# nesting
Travel_log = {
 "lagos": ["shibiri", "ojo", "etegbin", "alaba"],
 "France": ["berlin", "harmbutg"],
}












