s = input("enter string : ")
title = ""

for i in s:
    if i == 0:
        title = title + i.capitalize()
    elif i.isspace():
        title = s[i + 1].capitalize()

print(title)
 