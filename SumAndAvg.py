n = int(input("enter the range : "))
l = []
sum = 0
for i in range(0, n):
    x = int(input("enter number in list : "))
    l.append(x)
    sum += l[i]

avg = sum / n
print("sum : ", sum)
print("avg : ", avg)
