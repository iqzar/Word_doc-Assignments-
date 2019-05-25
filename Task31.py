# Python program to compute the greatest common divisor (GCD) of two positive integers.
a=int(input("Enter first no :" ))
b=int(input("Enter second no. :" ))
while a%b !=0:
      rem=a%b
      a=b
      b=rem
print("HCF",b)
