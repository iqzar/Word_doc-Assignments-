#Write a Python program to count the number occurrence of a specific character in a string:
a =str(input("Enter your statement here: " ))
test_str = a
b =input("Enter letter you want to count: ")
count = 0
for i in test_str:
    if i == b :
        count=count+1
print(count)        
