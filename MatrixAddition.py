lst1 = []
n = int(input("enter the range : "))
for i in range(n):
    lst1.append(int((input("enter the number in list 1 : "))))

lst2 = []
for i in range(n):
    lst2.append(int((input("enter the number in list 2 : "))))

res = []
for i in range((len(lst1))):
    res.append(lst1[i] + lst2[i])

print(lst1)
print(lst2)
print(res)
