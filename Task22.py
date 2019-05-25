#Python program to calculate body mass index:
weight=int(input("Enter your weight in kg: "))
height=float(input("Enter your height in : "))
h_foot=height*0.3048
#Formula for BMI =weight(in kg)/height(in meter^2)
BMI=round(weight/h_foot**2)
print("Your BMI is: ",BMI)
