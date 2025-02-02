# height = input("Height of wall: ")
# width = input("Width of wall: ")

# coverage = 5 

# def cal_cans(height, width, coverage):
#   numbs_of_cans = height * width 
#   roudd = int(round(numbs_of_cans))
# #   print(f"you'll need {roudd} cans of paint. ")
# import math

# def paint_calc(height, width, coverage):
#   numbers_of_cans = height * width
#   area = math.ceil(numbers_of_cans / coverage)
#   print(f"you'll need {area} cans of paint. ")

# test_h = int(input("height of walls: "))
# test_w = int(input("width of wall: "))
# test_coverage = 5
# paint_calc(height=test_h, width=test_w, coverage=test_coverage)   

import math

user_height_input = int(input("height of wall: "))
user_width_input = int(input("width of wall: "))
coverage = 5

def paint_cal(height, width, coverage):
  multiply = height * width
  division = multiply / coverage
  rounding_funt = math.ceil(division)
  print(f"you'll need {rounding_funt} cans of paint. ")

paint_cal(user_height_input, user_width_input, coverage)














