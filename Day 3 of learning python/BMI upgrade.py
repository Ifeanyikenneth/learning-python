height = float(input("enter youe height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if  bmi < 18.5 :
    print(f"your BMI is {bmi}, your are underweight")

elif bmi < 25 :
    print(f"your BMI is {bmi}, your are normal weight")

elif bmi < 30 :
    print(f"your BMI is {bmi}, your are overweight")

elif bmi < 35 :
    print(f"your BMI is {bmi}, your are obese")

else :
    print(f"your BMI is {bmi}, your are clinically obese")
    


    
