str = input("enter string : ")
rev = ""
for i in str:
    rev = i + rev

if str == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
