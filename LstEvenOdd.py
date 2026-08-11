lst = [1, 2, 3, 4, 5, 6, 7, 0, -2, 10]

even = []
odd = []

for i in range(0, len(lst)):
    if lst[i] <= 0:
        continue
    if lst[i] % 2 == 0:
        even.append(lst[i])
    else:
        odd.append(lst[i])

print(lst)
print(even)
print(odd)
