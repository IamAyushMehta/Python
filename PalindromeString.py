str = input("enter string : ")
str = str.replace(" ", "").lower()
# rev = ""

# for i in str:
#     rev = i + rev

rev = str[::-1]


if str == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
