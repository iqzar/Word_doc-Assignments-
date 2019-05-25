#Write a Python program that accepts a string and calculate the number of digits and letters Sample Data : Python 3.2, Expected Output : Letters 6, Digits 2:
data=str(input("Enter your data here: "))
digits=0
letters=0
for i in data:
    if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
        digits=digits+1
    else:
        letters=letters+1
print("Digits:", digits)
print("Letters:",letters)             