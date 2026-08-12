lst = [1,4,2,87,26,6]

smallest = lst[0]
largest = lst[0]

for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        largest = lst[i+1]

    if lst[i] > lst[i+1]:
        smallest = lst[i+1]


print(smallest)
print(largest)
