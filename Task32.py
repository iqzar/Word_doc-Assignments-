#Python program to get the least common multiple (LCM) of two positive integers:
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
for m in range(1,a*b+1):
    if m%a == 0 and m%b == 0:
        print("LCM between two no. is: ",m)
        break 