lst1 = [1, 5, 3, 8, 4, 5]
lst2 = [8, 4, 6, 5, 7, 9]

for i in range(0, len(lst2)):
    lst1.append(lst2[i])

for i in range(len(lst1) - 1):
    for j in range(len(lst1) - i - 1):
        if lst1[j] < lst1[j + 1]:
            lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]


print(lst1)
