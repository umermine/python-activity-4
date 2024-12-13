#Adding variables
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

Bmi = weight / (height/100)**2
#Writing code
print("Your BMI is ",Bmi)

if Bmi < 18.4:
    print("You're serverly underweight.")
elif Bmi <= 18.4:
    print("You're underweight.")
elif Bmi <= 24.9:
    print("You're healthy.")
elif Bmi <= 29.9:
    print("You're overweight.")
elif Bmi <= 34.9:
    print("You're serverly overweight.")
elif Bmi <= 39.9:
    print("You're obese.")
else:
    print("You're serverly obese.")