#Python program to create the multiplication table (from 1 to 10) of a number:
n=int(input("Enter any number: "))
for i in range(1,11):
    table=(n,'x',i,'=',n*i)
    print(table)
