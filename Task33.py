#Python program which accepts the user's first and last name and print them in reverse order with a space between them :
f_name=str(input("Enter your first name: "))
l_name=str(input("Enter your last name: "))
f=f_name[::-1]
l=l_name[::-1]
print(f,"",l)