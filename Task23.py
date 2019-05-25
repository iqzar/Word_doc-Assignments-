#Python program to convert temperatures to and from Celsius, Fahrenheit:
#Fahrenheit to Celsius formula:(°F - 32) x 5/9 = °C
#Celsius to Fahrenheit formula:(°C × 9/5) + 32 = °F
temp =float(input("Enter temperature here: "))
conversion =input("Type C to convert in celsius or F to convert in Fahrenheit: ")
if conversion == 'C' :
    celsius_temp =(temp-32)*5/9
    print("Temperature in Celsius= ",celsius_temp)
else:
    Fahrenheit_temp =(temp*9/5)+32
    print("Temperature in 'Fahrenheit'= ",Fahrenheit_temp)
