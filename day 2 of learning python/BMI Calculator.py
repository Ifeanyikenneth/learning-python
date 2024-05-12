#on line 8 the purpose for using the float on (height) is cuz when inputing our value we input a flaoting number and not a integer and out weight value is a (int) 
# THe BMI is a kind of way in measuring somebody body composition.. that's is kind of independent of there hieght and weight...
# BMI is calculated in = weight / heigth**2

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height)**2
bmi1 = int(bmi)
print(bmi1)
