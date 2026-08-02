l = [1, 2, 3, 4, 5]

for i in range(0, len(l) - 1):
    if i % 2 == 0:
        l[i], l[i + 1] = l[i + 1], l[i]

for i in l:
    print(i, end=" ")
