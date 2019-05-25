#Write a program to check whether given input is palindrome or not:
word=input("Enter any word:" )
rev=word[::-1]
if word == rev:
    print("word is palindrome ")
else:
    print("word is not palindrome")    