s = input("enter string : ")
words = s.split()
countW = 0
countS = 0

for i in s:
    if i == " ":
        countW += 1
    elif i in ".!?":
        countS += 1

longW = ""
for i in words:
    if len(i) > len(longW):
        longW = i

print("words : ", countW)
print("sentences : ", countS)
print("longest Word : ", longW)
