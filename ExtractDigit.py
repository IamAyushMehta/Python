s = input("enter alphanumerical string : ")
digit = ""
for i in s:
    if i.isdigit():
        digit += i

print("digit : ", digit)
