# print(2023 % 2)

# def days_in_month(year, month):
#   if year == 0 or month == 0:
#     return "is a leap year"
#   else: 
#     return "is not a leap year"
  
# print(days_in_month(input("")))
 
def is_leap(year):
  if year % 4 == 0:
    if year % 10 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year , month  ):
  # if month > 12 or month < 1 : 
  #   return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31,30, 31 ]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# at first we return true using the return function to know if it is a leap year or not
# then after that we create a function that is going to tell you how many days in the month that you specify
# the after that we specify each of them and pass in all the necessary input and tell the user to input the str to cal the days in a month











