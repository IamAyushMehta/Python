str = input("enter string : ")
str = str.lower()

countVowel, countConsonant = 0, 0

for i in str:
    if i in "aeiou":
        countVowel += 1
    elif i.isalpha():
        countConsonant += 1

print(f"Vowel : {countVowel}")
print(f"Consonant : {countConsonant}")
