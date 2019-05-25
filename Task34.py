#Input a text and count the occurrences of vowels and consonant:
text=input("Write your text here: ")
vowels =0
consonants =0
for i in text:
    if (i=='a' or i=='o' or i=='e' or i=='u' or i=='i' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U') :
        vowels=vowels+1
    else:
        consonants=consonants+1
print("Vowels in sentence is: ",vowels)
print("Consonants in sentence is:",consonants)        


