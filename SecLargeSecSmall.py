l = [21, 32, 2, 6, 65, 5, 3, 6]
i = 0
for i in range(len(l) - i - 1):
    for j in range(len(l) - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print("second smallest : ", l[1])
print("second largest : ", l[len(l) - 2])
