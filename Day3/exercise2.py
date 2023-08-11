# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height**2);

if bmi > 35:
    bmi_value = "are clinically obese";
elif bmi > 30:
    bmi_value = "are obese";
elif bmi > 25:
    bmi_value = "are slightly overweight";
elif bmi > 18.5:
    bmi_value = "have a normal weight";
else:
    bmi_value = "are underweight";

print(f"Your BMI is {int(round(bmi,0))}, you {bmi_value}.");
