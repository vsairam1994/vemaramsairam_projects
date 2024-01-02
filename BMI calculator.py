name = input("Enter you name: ")

weight = int(input("Enter your weight in Kilograms: "))

height = int(input("Enter your height in Centimeters: "))

BMI = (weight) / ((height/100) **2)

print(BMI)

if BMI>0:
    if(BMI<16):
        print(name +", your classification is Severe Thinness.")
    elif (BMI<=17):
        print(name +", your classification is Moderate Thinness.")
    elif (BMI<18.5):
        print(name +", your classification is Mild Thinness.")
    elif (BMI<25):
        print(name +", your classification is Normal.")
    elif (BMI<30):
        print(name +", your classification is Overweight.")
    elif (BMI<35):
        print(name +", your classification is Obese Class I.")
    elif (BMI<40):
        print(name +", your classification is Obese Class II.")
    else:
        print(name +", your classification is Obese Class III.")
else:
    print("Enter valid input")