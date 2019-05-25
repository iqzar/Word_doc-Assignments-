# Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure:
num=input("Enter your number here: ")
rev=num[::-1]
sum= int(num)+ int(rev)
sum=str(sum)
print("Sum of your number and its reverse: ",sum)
if sum == sum[::-1]:
    print("Is palindrome")
else:
    print("Is not palidrome")    